#!/usr/bin/env python3

# Importing the required libraries and dependencies
import numpy as np
import pandas as pd
import hvplot.pandas
import sqlalchemy




database_connection_string = 'sqlite:///banking.db'
engine = sqlalchemy.create_engine(database_connection_string)



def create_tables(tbl_name, df, engine=engine):
        
    """
    
    
    
    """
    

    df.to_sql(tbl_name, engine, index=False, if_exists='replace')
    print(f'{tbl_name} table created')
    return engine


def query_table(query, tbl, engine=engine):
    """
    
    
    
    """
    dataframe = pd.read_sql_query(query, con=engine)
    return dataframe