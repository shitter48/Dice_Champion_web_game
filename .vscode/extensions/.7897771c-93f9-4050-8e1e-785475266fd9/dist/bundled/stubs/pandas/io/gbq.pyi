from typing import (
    Any,
    Dict,
    List,
    Optional,
)

from pandas.core.frame import DataFrame

def read_gbq(
    query: str,
    project_id: Optional[str] = ...,
    index_col: Optional[str] = ...,
    col_order: Optional[List[str]] = ...,
    reauth: bool = ...,
    auth_local_webserver: bool = ...,
    dialect: Optional[str] = ...,
    location: Optional[str] = ...,
    configuration: Optional[Dict[str, Any]] = ...,
    credentials=...,
    use_bqstorage_api: Optional[bool] = ...,
    private_key=...,
    verbose=...,
    progress_bar_type: Optional[str] = ...,
) -> DataFrame: ...
def to_gbq(
    dataframe: DataFrame,
    destination_table: str,
    project_id: Optional[str] = ...,
    chunksize: Optional[int] = ...,
    reauth: bool = ...,
    if_exists: str = ...,
    auth_local_webserver: bool = ...,
    table_schema: Optional[List[Dict[str, str]]] = ...,
    location: Optional[str] = ...,
    progress_bar: bool = ...,
    credentials=...,
    verbose=...,
    private_key=...,
) -> None: ...
