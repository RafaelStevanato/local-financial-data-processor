from pathlib import Path


def validate_file_exists(file_path: Path) -> None:
    if not file_path.exists():
        raise FileNotFoundError(f"Input file not found: {file_path}")