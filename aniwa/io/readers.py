from pathlib import Path

import polars as pl


def read_dataset(path: str) -> pl.DataFrame:
    file_path = Path(path)
    suffix = file_path.suffix.lower()

    if suffix == ".csv":
        return pl.read_csv(file_path)

    if suffix in [".xlsx", ".xls"]:
        return pl.read_excel(file_path)

    if suffix == ".json":
        return pl.read_json(file_path)

    if suffix in [".parquet", ".pq"]:
        return pl.read_parquet(file_path)

    raise ValueError(f"Unsupported file type: {suffix}")