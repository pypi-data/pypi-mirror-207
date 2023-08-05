#!/usr/bin/env python3
from functools import lru_cache
import pymysql
from pymysql import InternalError
import os
import pandas as pd

class OdinPricing(object):
    @lru_cache
    def get_weekly_pricing(self, state: str) -> 'DataFrame':

        query: str = """
            SELECT 
                wpr.period, 
                wpr.value, 
                wpr.units 
    
            FROM pricing_%s wpr 
        """ % (state)
        try:
            conn: 'MySQL' = pymysql.connect(host=os.environ["MYSQL_HOST"],
                                            user=os.environ["MYSQL_USER"],
                                            password=os.environ["MYSQL_PASSWD"],
                                            database=os.environ["MYSQL_DB"])

            df: 'DataFrame' = pd.read_sql(query, con=conn)
            df['period'] = pd.to_datetime(df['period'])
            df['year'] = df['period'].apply(lambda row: row.year)
            df['quarter'] = df['period'].apply(lambda row: row.quarter)

            return df

        except InternalError as e:
            raise InternalError(
                "The server has encountered an internal error. Please check your query again!!!\n[QUERY]%s" % (
                    query)) from e


