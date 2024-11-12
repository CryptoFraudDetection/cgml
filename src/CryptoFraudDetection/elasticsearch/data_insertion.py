"""
File: data_insertion.py

Description:
- This file is used to insert data into Elasticsearch.
"""

from typing import Any, Dict, List, Tuple
import logging
import pandas as pd
from elasticsearch.helpers import bulk, BulkIndexError

from CryptoFraudDetection.utils.logger import Logger
from CryptoFraudDetection.elasticsearch.elastic_client import get_elasticsearch_client

es = get_elasticsearch_client()


def insert_dataframe(
    logger: Logger, index: str, df: pd.DataFrame
) -> Tuple[int, int | List[Dict[str, list]]]:
    """
    Insert a pandas DataFrame into Elasticsearch.

    Args:
    - index (str): The Elasticsearch index to insert the data into.
    - df (pd.DataFrame): The DataFrame to insert.

    Returns:
    - dict: Elasticsearch bulk insert response.
    """
    if "id" in df.columns:
        data = [
            {
                "_index": index,
                "_id": record["id"],
                "_op_type": "create",
                "_source": record,
            }
            for record in df.to_dict(orient="records")
        ]
    else:
        data = [
            {
                "_index": index,
                "_source": record,
            }
            for record in df.to_dict(orient="records")
        ]

    try:
        success_fail = bulk(client=es, actions=data, raise_on_error=False)
    except BulkIndexError as e:
        logger.handle_exception(BulkIndexError, f"Skipped some documents:\n{e}")
    return success_fail


def insert_dict(
    logger: Logger, index: str, data_dict: Dict[str, list[str]]
) -> Tuple[int, int | List[Dict[str, Any]]]:
    """
    Insert a list of dictionaries into Elasticsearch.

    Args:
    - index (str): The Elasticsearch index to insert the data into.
    - data_dict (List[Dict[str, Any]]): The list of dictionaries to insert.

    Returns:
    - Tuple[int, int | List[Dict[str, Any]]]: Elasticsearch bulk insert response.
    """
    df = pd.DataFrame(data_dict)
    return insert_dataframe(logger, index, df)
