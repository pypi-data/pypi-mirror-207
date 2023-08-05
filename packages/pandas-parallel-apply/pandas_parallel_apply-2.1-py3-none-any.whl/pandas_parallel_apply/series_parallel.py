"""
Apply on series
Usage:
    standard => series.apply(f)
    parallel => SeriesParallel(series, n_cores).apply(f)
             => SeriesParallel(df[col], n_cores).apply(f)
"""
from typing import Callable
from functools import partial
import pandas as pd

from .utils import parallelize_dataframe


def _apply_on_series(series: pd.Series, f: Callable, pbar: bool = True) -> pd.Series:
    """Returns progress_apply or simple apply based on pbar"""
    if pbar:
        return series.progress_apply(f)
    return series.apply(f)


class SeriesParallel:
    """SeriesParallel implementation"""
    def __init__(self, series: pd.Series, n_cores: int, pbar: bool = True):
        self.series = series
        self.n_cores = n_cores
        self.pbar = pbar

    def apply(self, func: Callable) -> pd.Series:
        """Wrapper on top of regular ser.apply(fn)"""
        return parallelize_dataframe(self.series, partial(_apply_on_series, f=func, pbar=self.pbar), self.n_cores)
