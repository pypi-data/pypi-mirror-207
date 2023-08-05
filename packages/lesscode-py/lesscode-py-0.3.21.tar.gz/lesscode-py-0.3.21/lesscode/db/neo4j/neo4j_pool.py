# -*- coding: utf-8 -*-
import importlib

from lesscode.db.base_connection_pool import BaseConnectionPool

try:
    neo4j = importlib.import_module("neo4j")
except ImportError as e:
    raise Exception(f"neo4j is not exist,run:pip install neo4j==5.0.0")


class Neo4jPool(BaseConnectionPool):
    """
    Neo4j 数据库链接创建类
    """

    async def create_pool(self):
        """
        创建Neo4j 连接池
        :return:
        """
        driver = neo4j.AsyncGraphDatabase.driver(f"bolt://{self.conn_info.host}:{self.conn_info.port}",
                                                 auth=(self.conn_info.user, self.conn_info.password))
        return driver

    def sync_create_pool(self):
        """
        创建Neo4j 连接池
        :return:
        """
        driver = neo4j.GraphDatabase.driver(f"bolt://{self.conn_info.host}:{self.conn_info.port}",
                                            auth=(self.conn_info.user, self.conn_info.password))
        return driver
