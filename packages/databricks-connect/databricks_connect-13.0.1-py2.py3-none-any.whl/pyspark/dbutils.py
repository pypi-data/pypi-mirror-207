#
# DATABRICKS CONFIDENTIAL & PROPRIETARY
# __________________
#
# Copyright 2019 Databricks, Inc.
# All Rights Reserved.
#
# NOTICE:  All information contained herein is, and remains the property of Databricks, Inc.
# and its suppliers, if any.  The intellectual and technical concepts contained herein are
# proprietary to Databricks, Inc. and its suppliers and may be covered by U.S. and foreign Patents,
# patents in process, and are protected by trade secret and/or copyright law. Dissemination, use,
# or reproduction of this information is strictly forbidden unless prior written permission is
# obtained from Databricks, Inc.
#
# If you view or obtain a copy of this information and believe Databricks, Inc. may not have
# intended it to be made available, please promptly report it to Databricks Legal Department
# @ legal@databricks.com.
#
from pyspark.sql import SparkSession
from pyspark.sql.connect.session import SparkSession as RemoteSession, SparkConnectClient
from typing import cast, Optional


class DBUtils:
    """
    This class exists to satisfy API backwards compatibility with applications using DB Connect v1.

    .. deprecated:: 13.0
        Switch to DBUtils in the Databricks Python SDK.
    """

    def __init__(self, spark: Optional[SparkSession] = None):
        if spark is None:
            spark = SparkSession.builder.getOrCreate()

        if hasattr(spark, "_sc"):
            # Running in a Databricks notebook
            import IPython

            self._utils = IPython.get_ipython().user_ns["dbutils"]
        else:
            # Running locally
            from databricks.sdk.dbutils import Config, RemoteDbUtils

            if not isinstance(spark, RemoteSession):
                raise TypeError(
                    "DBUtils can be initialized only with a remote spark session."
                    + "See Databricks Connect on how to setup a remote spark session."
                )

            client: SparkConnectClient = cast(RemoteSession, spark).client
            url = client._builder.url

            splits = url.params.split(";")
            params = {}

            for split in splits:
                inner_split = split.split("=")
                if len(inner_split) != 2:
                    raise RuntimeError(f"Invalid connection string: {url}")

                params[inner_split[0]] = inner_split[1]

            if (
                client.host is None
                or client.token is None
                or "x-databricks-cluster-id" not in params
            ):
                raise RuntimeError(f"Invalid connection string: {url}")

            config = Config(
                host=client.host,
                token=client.token,
                cluster_id=params["x-databricks-cluster-id"],
            )
            self._utils = RemoteDbUtils(config)

        self.fs = self._utils.fs
        self.secrets = self._utils.secrets
