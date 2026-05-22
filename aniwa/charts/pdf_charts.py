from io import BytesIO

import matplotlib.pyplot as plt
from matplotlib.figure import Figure

from aniwa.models.profile import DatasetProfile


def generate_null_chart(profile: DatasetProfile) -> BytesIO:
    columns = [col.name for col in profile.columns or []]
    null_percents = [col.null_percent for col in profile.columns or []]

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.bar(columns, null_percents)

    ax.set_title("Null Percentage by Column")
    ax.set_ylabel("Null %")
    ax.set_xlabel("Columns")

    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    return _figure_to_buffer(fig)


def generate_cardinality_chart(profile: DatasetProfile) -> BytesIO:
    columns = [col.name for col in profile.columns or []]
    unique_counts = [col.unique_count for col in profile.columns or []]

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.bar(columns, unique_counts)

    ax.set_title("Unique Values by Column")
    ax.set_ylabel("Unique Values")
    ax.set_xlabel("Columns")

    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    return _figure_to_buffer(fig)


def generate_duplicate_chart(profile: DatasetProfile) -> BytesIO:
    duplicate_rows = profile.quality.duplicate_rows if profile.quality else 0
    total_rows = profile.summary.rows if profile.summary else 0
    unique_rows = total_rows - duplicate_rows

    fig, ax = plt.subplots(figsize=(6, 6))

    ax.pie(
        [duplicate_rows, unique_rows],
        labels=["Duplicate Rows", "Unique Rows"],
        autopct="%1.1f%%",
    )

    ax.set_title("Duplicate Overview")

    plt.tight_layout()

    return _figure_to_buffer(fig)


def _figure_to_buffer(fig: Figure) -> BytesIO:
    buffer = BytesIO()

    fig.savefig(
        buffer,
        format="png",
        bbox_inches="tight",
    )

    buffer.seek(0)

    plt.close(fig)

    return buffer