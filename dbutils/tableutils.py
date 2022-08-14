#!/usr/bin/env python3

# Importing the required libraries and dependencies
import numpy as np
import pandas as pd
import sqlalchemy




database_connection_string = 'sqlite:///banking.db'
engine = sqlalchemy.create_engine(database_connection_string)



def create_tables(tbl_name, df, engine=engine):
        
    """
    Function to create sql tables.  
    
    """
    

    df.to_sql(tbl_name, engine, index=False, if_exists='replace')
    print(f'{tbl_name} table created')
    return engine


def query_table(query, engine=engine):
    """
    Execute sql query to create an sqlite table
    input:
    tbl: table name
    engine: sql engine   
    output:
    sql engine (with sql db and table)
    """
    dataframe = pd.read_sql_query(query, con=engine)
    return dataframe