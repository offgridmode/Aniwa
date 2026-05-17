import polars as pl

from aniwa.io.readers import read_dataset


def test_read_csv(tmp_path):
    file_path = tmp_path / "customers.csv"
    file_path.write_text("id,name\n1,Ama\n2,Kofi\n", encoding="utf-8")

    df = read_dataset(str(file_path))

    assert df.shape == (2, 2)
    assert df.columns == ["id", "name"]


def test_read_json(tmp_path):
    file_path = tmp_path / "customers.json"
    file_path.write_text(
        '[{"id": 1, "name": "Ama"}, {"id": 2, "name": "Kofi"}]',
        encoding="utf-8",
    )

    df = read_dataset(str(file_path))

    assert df.shape == (2, 2)
    assert df.columns == ["id", "name"]


def test_read_parquet(tmp_path):
    file_path = tmp_path / "customers.parquet"

    original_df = pl.DataFrame(
        {
            "id": [1, 2],
            "name": ["Ama", "Kofi"],
        }
    )
    original_df.write_parquet(file_path)

    df = read_dataset(str(file_path))

    assert df.shape == (2, 2)
    assert df.columns == ["id", "name"]


def test_read_excel(tmp_path):
    file_path = tmp_path / "customers.xlsx"

    original_df = pl.DataFrame(
        {
            "id": [1, 2],
            "name": ["Ama", "Kofi"],
        }
    )
    original_df.write_excel(file_path)

    df = read_dataset(str(file_path))

    assert df.shape == (2, 2)
    assert df.columns == ["id", "name"]


def test_read_xls_dispatches_to_excel_reader(tmp_path, monkeypatch):
    file_path = tmp_path / "customers.xls"
    file_path.write_text("fake excel content", encoding="utf-8")

    called = {"value": False}

    def fake_read_excel(path):
        called["value"] = True
        return pl.DataFrame({"id": [1], "name": ["Ama"]})

    monkeypatch.setattr(pl, "read_excel", fake_read_excel)

    df = read_dataset(str(file_path))

    assert called["value"] is True
    assert df.shape == (1, 2)
    assert df.columns == ["id", "name"]


def test_unsupported_file_type(tmp_path):
    file_path = tmp_path / "customers.txt"
    file_path.write_text("id,name\n1,Ama\n", encoding="utf-8")

    try:
        read_dataset(str(file_path))
    except ValueError as exc:
        assert "Unsupported file type" in str(exc)
    else:
        raise AssertionError("Expected ValueError for unsupported file type")