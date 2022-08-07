#!/usr/bin/env python3

import numpy as np
import pandas as pd
import hvplot.pandas
from pathlib import Path
from dbutils import create_df, credit_score_checker
from dbutils.tableutils import create_tables, query_table
import questionary


file_tbl = Path('Resources/customer_data.csv')
tbl_name = 'customers'
first_name = questionary.text("What's your first name").ask()
ssn = questionary.text("What's your ssn").ask()

sql_query = f"""
SELECT * 
FROM {tbl_name}
where first_name = '{first_name}'
and ssn = '{ssn}'
"""
# sql2 = f"""
# SELECT address 
# FROM {tbl_name}
# where first_name = '{first_name}'

# """


def main():
    df = create_df(file_tbl)
    # print(df.head(2))
    engine = create_tables(tbl_name, df)
    df_new = query_table(sql_query, tbl_name)
    print('-------------- \n' )
    print(credit_score_checker(df_new, 'credit_scores', first_name=first_name))
    # print(df_new)


if __name__ == '__main__':
    main()