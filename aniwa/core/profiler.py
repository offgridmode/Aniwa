import polars as pl

from aniwa.models.profile import (
    DatasetProfile,
    DatasetSummary,
    ColumnProfile,
    QualityProfile,
    Insight,
)


def profile_dataframe(df: pl.DataFrame) -> DatasetProfile:
    rows = df.height
    columns = df.width

    column_profiles: list[ColumnProfile] = []

    for col in df.columns:
        null_count = df[col].null_count()
        null_percent = round((null_count / rows) * 100, 2) if rows else 0
        unique_count = df[col].n_unique()

        column_profiles.append(
            ColumnProfile(
                name=col,
                dtype=str(df[col].dtype),
                null_count=null_count,
                null_percent=null_percent,
                unique_count=unique_count,
            )
        )

    duplicate_rows = rows - df.unique().height
    duplicate_percent = round((duplicate_rows / rows) * 100, 2) if rows else 0

    insights = generate_insights(column_profiles, duplicate_rows, rows)

    return DatasetProfile(
        summary=DatasetSummary(rows=rows, columns=columns),
        columns=column_profiles,
        quality=QualityProfile(
            duplicate_rows=duplicate_rows,
            duplicate_percent=duplicate_percent,
        ),
        insights=insights,
    )


def generate_insights(
    columns: list[ColumnProfile],
    duplicate_rows: int,
    total_rows: int,
) -> list[Insight]:
    insights: list[Insight] = []

    if duplicate_rows > 0:
        insights.append(
            Insight(
                level="warning",
                message=f"{duplicate_rows} duplicate rows detected.",
            )
        )

    for col in columns:
        if col.null_percent > 50:
            insights.append(
                Insight(
                    level="critical",
                    message=f"Column '{col.name}' is highly sparse with {col.null_percent}% nulls.",
                )
            )

        if col.unique_count == total_rows and total_rows > 0:
            insights.append(
                Insight(
                    level="info",
                    message=f"Column '{col.name}' may be a unique identifier.",
                )
            )

        if col.unique_count == 1:
            insights.append(
                Insight(
                    level="warning",
                    message=f"Column '{col.name}' has only one unique value.",
                )
            )

    return insights