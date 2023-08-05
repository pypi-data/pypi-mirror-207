from pathlib import Path
from typing import Optional, Union

import pandas as pd

read_func_map = {
    ".feather": pd.read_feather,
    ".pickle": pd.read_pickle,
    ".pkl": pd.read_pickle,
    ".parquet": pd.read_parquet,
    ".hdf": pd.read_hdf,
    ".json": pd.read_json,
    ".csv": pd.read_csv,
    ".tsv": pd.read_csv,
    ".h5": pd.read_hdf,
    ".xlsx": pd.read_excel,
}


class HeadTail:
    def __init__(
        self,
        file_path: Union[str, Path],
        num_lines: int = 10,
        num_bytes: Optional[int] = None,
        quiet: bool = False,
        verbose: bool = False,
        zero_terminated: bool = False,
    ) -> None:
        self.file_path: Path = Path(file_path)
        self.num_lines: int = num_lines - 1
        self.num_bytes: Optional[int] = num_bytes
        self.quiet: bool = quiet
        self.verbose: bool = verbose
        self.zero_terminated: bool = zero_terminated
        self._validate_arguments()

    def _validate_arguments(self) -> None:
        if not self.file_path.exists():
            raise FileNotFoundError(f"File not found: {self.file_path}")

        if self.num_lines <= 0:
            raise ValueError("Number of lines must be greater than 0.")

        if self.num_bytes is not None and self.num_bytes <= 0:
            raise ValueError("Number of bytes must be greater than 0.")

    def _read_dataframe(self) -> pd.DataFrame:
        file_extension = self.file_path.suffix
        if file_extension in read_func_map:
            return read_func_map[file_extension](self.file_path)
        else:
            raise ValueError(f"Unsupported file extension: {file_extension}")

    def head(self) -> str:
        if self.verbose and not self.quiet:
            print(f"==> {self.file_path} <==")

        df = self._read_dataframe()
        return df.head(self.num_lines).to_string(index=False)

    def tail(self) -> str:
        if self.verbose and not self.quiet:
            print(f"==> {self.file_path} <==")

        df = self._read_dataframe()
        return df.tail(self.num_lines).to_string(index=False)
