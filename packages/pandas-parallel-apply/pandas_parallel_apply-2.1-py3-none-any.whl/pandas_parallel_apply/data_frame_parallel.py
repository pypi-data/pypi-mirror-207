"""
Wrapper on top of pd.DataFrame with some parallel operations
Apply on column
Usage:
    standard => df[col_name].apply(f)
    parallel => DataFrameParallel(df, n_cores)[col_name].apply(f)

Apply on row
Usage:
    standard => df.apply(f, axis=1)
    parallel => DataFrameParallel(df, n_cores).apply(f, axis=1)
"""
from functools import partial
from typing import Callable
import pandas as pd

from .series_parallel import SeriesParallel
from .groupby_parallel import GroupByParallel
from .utils import parallelize_dataframe


def _apply_on_df(df: pd.DataFrame, f: Callable, pbar: bool = True) -> pd.Series:
    """Apply a function on each row (all possible columns), returning a series"""
    if pbar:
        return df.progress_apply(f, axis=1)
    return df.apply(f, axis=1)

class DataFrameParallel:
    """DataFrameParallel implementation"""
    def __init__(self, df: pd.DataFrame, n_cores: int, pbar: bool = True):
        self.df = df
        self.n_cores = n_cores
        self.pbar = pbar

    # pylint: disable=unused-argument
    def apply(self, func, axis, raw: bool = False, result_type = None, args=(), **kwargs):
        """Wrapper on top of regular df.apply(fn)"""
        assert axis == 1, "Only axis=1 is supported in parallel df apply"
        return parallelize_dataframe(self.df, partial(_apply_on_df, f=func, pbar=self.pbar), self.n_cores)

    def groupby(self, *args, **kwargs):
        """Wrapper on top of regular df.groupby(col)"""
        return GroupByParallel(self.df.groupby(*args, **kwargs), self.n_cores, self.pbar)

    def __getitem__(self, x):
        return SeriesParallel(self.df[x], self.n_cores, self.pbar)

    def __str__(self) -> str:
        f_str = f"[Parallel DataFrame - {self.n_cores} crores]\n" + self.df.__str__()
        return f_str
