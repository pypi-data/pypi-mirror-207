"""General module for parallelizing a dataframe apply function on a column (series) or entire row"""

from typing import Callable, Union
import numpy as np
import pandas as pd
from tqdm import tqdm
from pathos.multiprocessing import ProcessingPool as Pool, cpu_count

from .logger import logger

tqdm.pandas()

def get_n_cores(n_cores: int, df: Union[pd.DataFrame, pd.Series]) -> int:
    """
    Returns the actual n_cores used for the parallel operation. cpu_count() represents the total amount of phyisical
    cores. Possible cases:
    - n_cores < -1: will throw an AssertionError
    - n_cores = -1: will return cpu_count() - 1
    - n_cores in [0, cpu_count()]: will return the number as is
    - n_cores > cpu_count(): will return the number as is, but will throw a warning
    """
    assert n_cores >= -1, f"n_cores cannot be negative, except -1. Got {n_cores}"
    if n_cores == -1:
        n_cores = cpu_count() - 1
        logger.debug(f"n_cores -1 was provided. Using total number of physical cores - 1: {n_cores}")
    if n_cores > cpu_count():
        logger.warning(f"n_cores is greater than the number of physical cores: {n_cores} vs {cpu_count()}")
    if n_cores > len(df):
        logger.warning(f"n_cores is greater than the length of the df, return that: {n_cores} vs {len(df)}")
        n_cores = len(df)
    return n_cores

def parallelize_dataframe(df: Union[pd.DataFrame, pd.Series], func: Callable, n_cores: int) -> pd.DataFrame:
    """Function used to split a dataframe in n sub dataframes, based on the number of cores we want to use."""
    n_cores = get_n_cores(n_cores, df)
    if n_cores == 0:
        logger.debug("n_cores is set to 0, returning serial function")
        return func(df)
    logger.debug(f"Parallelizing apply on df (rows: {len(df)}) with {n_cores} cores")

    df_split = np.array_split(df, n_cores)
    pool = Pool(n_cores)
    pool_res = pool.map(func, df_split)

    # This should use less memory than pd.concat(pool_res)
    final_df = pool_res[0]
    for res_df in pool_res[1: ]:
        final_df = pd.concat([final_df, res_df], copy=False)
        del res_df
    return final_df
