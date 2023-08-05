#!/usr/bin/env python3
from functools import lru_cache
import pymysql
from pymysql import InternalError
import os
import pandas as pd

class OdinDB(object):

    @lru_cache
    def get_dashboard_data(self, tbl_name: str, limit: int = None) -> 'DataFrame':
        # period,area_name,product_name,process_name,value,units

        query: str = """
            SELECT 
                t.period, 
                t.area_name,
                t.product_name, 
                t.process_name, 
                t.value,
                t.units
    
            FROM %s t 
        """ % (tbl_name)

        if limit:
            query += f" LIMIT {limit}"

        try:
            conn: 'MySQL' = pymysql.connect(host=os.environ["MYSQL_HOST"],
                                            user=os.environ["MYSQL_USER"],
                                            password=os.environ["MYSQL_PASSWD"],
                                            database=os.environ["MYSQL_DB"])

            df: 'DataFrame' = pd.read_sql(query, con=conn)
            df['period'] = pd.to_datetime(df['period'])
            df['year'] = df['period'].apply(lambda row: row.year)
            df['quarter'] = df['period'].apply(lambda row: row.quarter)
            df['month'] = df['period'].apply(lambda row: row.month_name())

            conn.close()
            return df

        except InternalError as e:
            raise InternalError(
                "The server has encountered an internal error. Please check your query again!!!\n[QUERY]%s" % (
                    query)) from e

    @lru_cache
    def get_crude_oil_imports(self, **kwargs) -> 'DataFrame':

        try:
            query: str = f"""
                SELECT 
                    c.period,
                    c.originId,
                    c.originType, 
                    c.originTypeName, 
                    c.destinationId, 
                    c.destinationName, 
                    c.destinationType, 
                    c.destinationTypeName, 
                    c.gradeId, 
                    c.gradeName, 
                    c.quantity, 
                    c.quantity_units,
                    c.start_date, 
                    c.end_date

                FROM crude_oil_imports c 
                
                {kwargs.get('where', '')}
                {kwargs.get('order_by', '')}
                {kwargs.get('limit', '')}
            """.replace("'", "")

            conn: 'MySQL' = pymysql.connect(host=os.environ["MYSQL_HOST"],
                                            user=os.environ["MYSQL_USER"],
                                            password=os.environ["MYSQL_PASSWD"],
                                            database=os.environ["MYSQL_DB"])

            return pd.read_sql(query, con=conn)

        except InternalError as e:
            raise InternalError(
                "The server has encountered an internal error. Please check your query again!!!\n[QUERY]%s" % (
                    query)) from e

