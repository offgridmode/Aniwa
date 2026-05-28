import polars as pl
from typing import Callable, Optional

from aniwa.models.enums import ReportSection
from aniwa.models.profile import (
    ColumnProfile,
    DatasetProfile,
    DatasetSummary,
    Insight,
    NumericStats,
    QualityProfile,
)
from aniwa.utils.progress import ProgressTracker


NUMERIC_DTYPES = {
    pl.Int8,
    pl.Int16,
    pl.Int32,
    pl.Int64,
    pl.UInt8,
    pl.UInt16,
    pl.UInt32,
    pl.UInt64,
    pl.Float32,
    pl.Float64,
}


def profile_dataframe(
    df: pl.DataFrame,
    mode: str = "deep",
    sections: set[ReportSection] | None = None,
    verbose: bool = False,
) -> DatasetProfile:
    """Profile a DataFrame with optional progress tracking.
    
    Args:
        df: Polars DataFrame to profile
        mode: Profiling mode ("fast" or "deep")
        sections: Report sections to include
        verbose: Enable detailed progress output
    
    Returns:
        DatasetProfile containing all profiling results
    """
    if sections is None:
        sections = set(ReportSection)

    rows = df.height
    column_count = df.width
    
    # Initialize progress tracker
    tracker = ProgressTracker(verbose=verbose)

    summary = None
    if ReportSection.summary in sections:
        with tracker.stage("Generating dataset summary"):
            summary = DatasetSummary(
                rows=rows,
                columns=column_count,
            )

    analysis_columns = None
    if _needs_column_analysis(sections):
        with tracker.stage(
            "Analyzing columns", 
            total_steps=len(df.columns) if verbose else None
        ) as progress_callback:
            analysis_columns = _profile_columns(
                df=df,
                rows=rows,
                mode=mode,
                include_statistics=ReportSection.statistics in sections,
                progress_callback=progress_callback,
            )

    displayed_columns = None
    if _should_display_columns(sections):
        displayed_columns = analysis_columns or _profile_columns(
            df=df,
            rows=rows,
            mode=mode,
            include_statistics=ReportSection.statistics in sections,
        )

    duplicate_rows = 0
    duplicate_percent = 0.0

    if _needs_duplicate_analysis(sections):
        with tracker.stage("Detecting duplicate rows"):
            duplicate_rows = rows - df.unique().height
            duplicate_percent = round((duplicate_rows / rows) * 100, 2) if rows else 0.0

    quality = None
    if ReportSection.quality in sections:
        with tracker.stage("Building quality profile"):
            quality = QualityProfile(
                duplicate_rows=duplicate_rows,
                duplicate_percent=duplicate_percent,
            )

    insights = None
    if ReportSection.insights in sections:
        with tracker.stage("Generating insights"):
            insights = generate_insights(
                columns=analysis_columns or [],
                duplicate_rows=duplicate_rows,
                total_rows=rows,
            )

    # Show timing summary if verbose
    if verbose:
        tracker.show_timing_summary()

    return DatasetProfile(
        summary=summary,
        columns=displayed_columns,
        quality=quality,
        insights=insights,
    )


def _needs_column_analysis(sections: set[ReportSection]) -> bool:
    return any(
        section in sections
        for section in {
            ReportSection.schema,
            ReportSection.statistics,
            ReportSection.insights,
            ReportSection.charts,
        }
    )


def _should_display_columns(sections: set[ReportSection]) -> bool:
    return any(
        section in sections
        for section in {
            ReportSection.schema,
            ReportSection.statistics,
            ReportSection.charts,
        }
    )


def _needs_duplicate_analysis(sections: set[ReportSection]) -> bool:
    return any(
        section in sections
        for section in {
            ReportSection.quality,
            ReportSection.insights,
            ReportSection.charts,
        }
    )


def _profile_columns(
    df: pl.DataFrame,
    rows: int,
    mode: str,
    include_statistics: bool,
    progress_callback: Optional[Callable[[int], None]] = None,
) -> list[ColumnProfile]:
    """Profile all columns with optional progress callback.
    
    Args:
        df: Polars DataFrame
        rows: Total row count
        mode: Profiling mode
        include_statistics: Whether to compute numeric statistics
        progress_callback: Optional callback to advance progress bar
    
    Returns:
        List of ColumnProfile objects
    """
    column_profiles: list[ColumnProfile] = []
    total_columns = len(df.columns)

    for idx, col in enumerate(df.columns):
        series = df[col]

        null_count = series.null_count()
        null_percent = round((null_count / rows) * 100, 2) if rows else 0.0
        unique_count = series.n_unique()

        numeric_stats = None

        if include_statistics and mode == "deep" and series.dtype in NUMERIC_DTYPES:
            with tracker.stage(f"Computing statistics for {col}"):
                numeric_stats = NumericStats(
                    min=_safe_float(series.min()),
                    max=_safe_float(series.max()),
                    mean=_safe_float(series.mean()),
                    median=_safe_float(series.median()),
                    std=_safe_float(series.std()),
                )

        column_profiles.append(
            ColumnProfile(
                name=col,
                dtype=str(series.dtype),
                null_count=null_count,
                null_percent=null_percent,
                unique_count=unique_count,
                numeric_stats=numeric_stats,
            )
        )
        
        # Advance progress bar if callback provided
        if progress_callback:
            progress_callback(1)

    return column_profiles


def _safe_float(value: object) -> float | None:
    if value is None:
        return None

    try:
        return round(float(value), 4)
    except (TypeError, ValueError):
        return None


def generate_insights(
    columns: list[ColumnProfile],
    duplicate_rows: int,
    total_rows: int,
) -> list[Insight]:
    """Generate insights from profiling data."""
    insights: list[Insight] = []

    if duplicate_rows > 0:
        insights.append(
            Insight(
                level="warning",
                message=f"{duplicate_rows} duplicate rows detected.",
            )
        )

    for col in columns:
        column_name = col.name.lower()

        if col.null_percent >= 75:
            insights.append(
                Insight(
                    level="critical",
                    message=(
                        f"Column '{col.name}' is extremely sparse "
                        f"with {col.null_percent}% null values."
                    ),
                )
            )

        elif col.null_percent >= 40:
            insights.append(
                Insight(
                    level="warning",
                    message=(
                        f"Column '{col.name}' contains "
                        f"{col.null_percent}% null values."
                    ),
                )
            )

        if col.unique_count == 1:
            insights.append(
                Insight(
                    level="warning",
                    message=f"Column '{col.name}' contains only one unique value.",
                )
            )

        if (
            col.unique_count == total_rows
            and total_rows > 0
            and "name" not in column_name
        ):
            insights.append(
                Insight(
                    level="info",
                    message=f"Column '{col.name}' may be a unique identifier.",
                )
            )

        if total_rows > 0:
            cardinality_ratio = col.unique_count / total_rows

            if cardinality_ratio >= 0.9 and total_rows > 20:
                insights.append(
                    Insight(
                        level="info",
                        message=f"Column '{col.name}' has very high cardinality.",
                    )
                )

        pii_keywords = [
            "email",
            "phone",
            "mobile",
            "ssn",
            "passport",
            "card",
            "credit",
            "address",
        ]

        if any(keyword in column_name for keyword in pii_keywords):
            insights.append(
                Insight(
                    level="warning",
                    message=f"Column '{col.name}' may contain sensitive information.",
                )
            )

        if col.numeric_stats:
            stats = col.numeric_stats

            if stats.min is not None and stats.min < 0:
                insights.append(
                    Insight(
                        level="info",
                        message=f"Column '{col.name}' contains negative values.",
                    )
                )

            if (
                stats.mean is not None
                and stats.std is not None
                and stats.mean != 0
            ):
                variability_ratio = abs(stats.std / stats.mean)

                if variability_ratio > 2:
                    insights.append(
                        Insight(
                            level="info",
                            message=f"Column '{col.name}' shows high variability.",
                        )
                    )

    return insights