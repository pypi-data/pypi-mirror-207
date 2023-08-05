from typing import List
from pathlib import Path
from csv import reader


def _read_from_csv(csv_path: str) -> List[str]:
    """
    Reads the data from a CSV file.

    Args:
        csv_path: The path of the CSV file.

    Returns:
        A list of rows from the CSV file.
    """
    with open(csv_path, encoding="utf-8") as file:
        csv_reader = reader(file)
        next(csv_reader)  # skip header
        rows = [r[0] for r in csv_reader]
    return rows


data_dir = Path(__file__).parent / 'data'

MALE_NAMES = _read_from_csv(Path(data_dir, 'male_names.csv').as_posix())
FEMALE_NAMES = _read_from_csv(Path(data_dir, 'female_names.csv').as_posix())
MALE_SURNAMES = _read_from_csv(Path(data_dir, 'male_surnames.csv').as_posix())
FEMALE_SURNAMES = _read_from_csv(Path(data_dir, 'female_surnames.csv').as_posix())
