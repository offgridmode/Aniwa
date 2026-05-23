from io import BytesIO

from aniwa.charts.pdf_charts import (
    generate_cardinality_chart,
    generate_duplicate_chart,
    generate_null_chart,
)
from aniwa.models.profile import (
    ColumnProfile,
    DatasetProfile,
    DatasetSummary,
    QualityProfile,
)


def build_profile() -> DatasetProfile:
    return DatasetProfile(
        summary=DatasetSummary(
            rows=1000,
            columns=3,
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
        ],
    )


def assert_valid_chart_buffer(buffer: BytesIO) -> None:
    assert isinstance(buffer, BytesIO)
    assert buffer.getbuffer().nbytes > 0


def test_generate_null_chart():
    buffer = generate_null_chart(build_profile())

    assert_valid_chart_buffer(buffer)


def test_generate_cardinality_chart():
    buffer = generate_cardinality_chart(build_profile())

    assert_valid_chart_buffer(buffer)


def test_generate_duplicate_chart():
    buffer = generate_duplicate_chart(build_profile())

    assert_valid_chart_buffer(buffer)


def test_duplicate_chart_handles_zero_duplicates():
    profile = build_profile()
    profile.quality = QualityProfile(
        duplicate_rows=0,
        duplicate_percent=0.0,
    )

    buffer = generate_duplicate_chart(profile)

    assert_valid_chart_buffer(buffer)


def test_duplicate_chart_handles_missing_quality():
    profile = build_profile()
    profile.quality = None

    buffer = generate_duplicate_chart(profile)

    assert_valid_chart_buffer(buffer)


def test_duplicate_chart_handles_missing_summary():
    profile = build_profile()
    profile.summary = None

    buffer = generate_duplicate_chart(profile)

    assert_valid_chart_buffer(buffer)


def test_null_chart_handles_empty_columns():
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
    )

    buffer = generate_null_chart(profile)

    assert_valid_chart_buffer(buffer)


def test_null_chart_handles_missing_columns():
    profile = DatasetProfile(
        summary=DatasetSummary(
            rows=0,
            columns=0,
        ),
        quality=QualityProfile(
            duplicate_rows=0,
            duplicate_percent=0.0,
        ),
        columns=None,
    )

    buffer = generate_null_chart(profile)

    assert_valid_chart_buffer(buffer)


def test_cardinality_chart_handles_empty_columns():
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
    )

    buffer = generate_cardinality_chart(profile)

    assert_valid_chart_buffer(buffer)


def test_cardinality_chart_handles_missing_columns():
    profile = DatasetProfile(
        summary=DatasetSummary(
            rows=0,
            columns=0,
        ),
        quality=QualityProfile(
            duplicate_rows=0,
            duplicate_percent=0.0,
        ),
        columns=None,
    )

    buffer = generate_cardinality_chart(profile)

    assert_valid_chart_buffer(buffer)