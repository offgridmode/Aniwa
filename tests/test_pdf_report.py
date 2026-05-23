from aniwa.models.profile import (
    ColumnProfile,
    DatasetProfile,
    DatasetSummary,
    Insight,
    NumericStats,
    ProfileMetadata,
    QualityProfile,
)
from aniwa.reports.pdf_report import render_pdf_report


def build_profile() -> DatasetProfile:
    return DatasetProfile(
        summary=DatasetSummary(
            rows=1000,
            columns=4,
        ),
        quality=QualityProfile(
            duplicate_rows=120,
            duplicate_percent=12.0,
        ),
        columns=[
            ColumnProfile(
                name="customer_id",
                dtype="Int64",
                null_count=0,
                null_percent=0.0,
                unique_count=1000,
                numeric_stats=NumericStats(
                    min=1,
                    max=1000,
                    mean=500.5,
                    median=500.0,
                    std=288.67,
                ),
            ),
            ColumnProfile(
                name="email",
                dtype="String",
                null_count=45,
                null_percent=4.5,
                unique_count=955,
            ),
            ColumnProfile(
                name="country",
                dtype="String",
                null_count=120,
                null_percent=12.0,
                unique_count=18,
            ),
            ColumnProfile(
                name="revenue",
                dtype="Float64",
                null_count=5,
                null_percent=0.5,
                unique_count=980,
                numeric_stats=NumericStats(
                    min=100.0,
                    max=95000.0,
                    mean=14500.25,
                    median=12000.0,
                    std=8500.12,
                ),
            ),
        ],
        insights=[
            Insight(
                level="warning",
                message="Column 'country' has elevated null values.",
            ),
            Insight(
                level="critical",
                message="Duplicate row percentage exceeds recommended threshold.",
            ),
        ],
        metadata=ProfileMetadata(
            generated_at="2026-05-22 14:00:00 UTC",
            aniwa_version="0.1.2",
            python_version="3.12.10",
            operating_system="Windows",
            polars_version="1.30.0",
            dataset_path="examples/customers.csv",
            dataset_file_type="CSV",
            dataset_size="2.14 MB",
            profiling_mode="deep",
            report_format="pdf",
            report_template="enterprise",
            included_sections=[
                "summary",
                "schema",
                "quality",
                "statistics",
                "insights",
                "charts",
            ],
            excluded_sections=None,
            profiling_duration="1.42s",
            command_used=(
                "aniwa examples/customers.csv "
                "--report pdf "
                "--template enterprise"
            ),
        ),
    )


def assert_valid_pdf(output_path) -> None:
    assert output_path.exists()
    assert output_path.stat().st_size > 0


def test_render_pdf_report_default(tmp_path):
    profile = build_profile()
    output_path = tmp_path / "report_default.pdf"

    render_pdf_report(
        profile=profile,
        output=str(output_path),
        template="default",
    )

    assert_valid_pdf(output_path)


def test_render_pdf_report_clean(tmp_path):
    profile = build_profile()
    output_path = tmp_path / "report_clean.pdf"

    render_pdf_report(
        profile=profile,
        output=str(output_path),
        template="clean",
    )

    assert_valid_pdf(output_path)


def test_render_pdf_report_compact(tmp_path):
    profile = build_profile()
    output_path = tmp_path / "report_compact.pdf"

    render_pdf_report(
        profile=profile,
        output=str(output_path),
        template="compact",
    )

    assert_valid_pdf(output_path)


def test_render_pdf_report_enterprise(tmp_path):
    profile = build_profile()
    output_path = tmp_path / "report_enterprise.pdf"

    render_pdf_report(
        profile=profile,
        output=str(output_path),
        template="enterprise",
    )

    assert_valid_pdf(output_path)


def test_render_pdf_report_dark(tmp_path):
    profile = build_profile()
    output_path = tmp_path / "report_dark.pdf"

    render_pdf_report(
        profile=profile,
        output=str(output_path),
        template="dark",
    )

    assert_valid_pdf(output_path)


def test_render_pdf_report_creates_parent_directories(tmp_path):
    profile = build_profile()

    output_path = (
        tmp_path
        / "nested"
        / "reports"
        / "aniwa_report.pdf"
    )

    render_pdf_report(
        profile=profile,
        output=str(output_path),
        template="default",
    )

    assert_valid_pdf(output_path)
    assert output_path.parent.exists()


def test_render_pdf_report_without_metadata(tmp_path):
    profile = build_profile()
    profile.metadata = None

    output_path = tmp_path / "report_without_metadata.pdf"

    render_pdf_report(
        profile=profile,
        output=str(output_path),
        template="default",
    )

    assert_valid_pdf(output_path)


def test_render_pdf_report_without_insights(tmp_path):
    profile = build_profile()
    profile.insights = []

    output_path = tmp_path / "report_without_insights.pdf"

    render_pdf_report(
        profile=profile,
        output=str(output_path),
        template="default",
    )

    assert_valid_pdf(output_path)


def test_render_pdf_report_without_numeric_statistics(tmp_path):
    profile = build_profile()

    for column in profile.columns or []:
        column.numeric_stats = None

    output_path = tmp_path / "report_without_stats.pdf"

    render_pdf_report(
        profile=profile,
        output=str(output_path),
        template="default",
    )

    assert_valid_pdf(output_path)


def test_render_pdf_report_without_summary(tmp_path):
    profile = build_profile()
    profile.summary = None

    output_path = tmp_path / "report_without_summary.pdf"

    render_pdf_report(
        profile=profile,
        output=str(output_path),
        template="default",
    )

    assert_valid_pdf(output_path)


def test_render_pdf_report_without_quality(tmp_path):
    profile = build_profile()
    profile.quality = None

    output_path = tmp_path / "report_without_quality.pdf"

    render_pdf_report(
        profile=profile,
        output=str(output_path),
        template="default",
    )

    assert_valid_pdf(output_path)


def test_render_pdf_report_without_columns(tmp_path):
    profile = build_profile()
    profile.columns = None

    output_path = tmp_path / "report_without_columns.pdf"

    render_pdf_report(
        profile=profile,
        output=str(output_path),
        template="default",
    )

    assert_valid_pdf(output_path)


def test_render_pdf_report_with_empty_columns(tmp_path):
    profile = DatasetProfile(
        summary=DatasetSummary(
            rows=0,
            columns=0,
        ),
        quality=QualityProfile(
            duplicate_rows=0,
            duplicate_percent=0.0,
        ),
        columns=[],
        insights=[],
        metadata=ProfileMetadata(
            generated_at="2026-05-22 14:00:00 UTC",
            aniwa_version="0.1.2",
        ),
    )

    output_path = tmp_path / "empty_report.pdf"

    render_pdf_report(
        profile=profile,
        output=str(output_path),
        template="clean",
    )

    assert_valid_pdf(output_path)


def test_invalid_template_raises_value_error(tmp_path):
    profile = build_profile()
    output_path = tmp_path / "invalid_template.pdf"

    try:
        render_pdf_report(
            profile=profile,
            output=str(output_path),
            template="invalid-template",
        )
    except ValueError as exc:
        assert "Invalid PDF report template" in str(exc)
        return

    assert False, "Expected ValueError for invalid template"


def test_render_pdf_report_includes_charts(tmp_path):
    profile = build_profile()
    output_path = tmp_path / "report_with_charts.pdf"

    render_pdf_report(
        profile=profile,
        output=str(output_path),
        template="enterprise",
    )

    assert_valid_pdf(output_path)