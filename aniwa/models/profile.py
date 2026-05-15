from pydantic import BaseModel


class DatasetSummary(BaseModel):
    rows: int
    columns: int


class ColumnProfile(BaseModel):
    name: str
    dtype: str
    null_count: int
    null_percent: float
    unique_count: int


class QualityProfile(BaseModel):
    duplicate_rows: int
    duplicate_percent: float


class Insight(BaseModel):
    level: str
    message: str


class DatasetProfile(BaseModel):
    summary: DatasetSummary
    columns: list[ColumnProfile]
    quality: QualityProfile
    insights: list[Insight]