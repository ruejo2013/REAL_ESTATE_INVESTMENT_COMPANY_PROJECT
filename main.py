#!/usr/bin/env python3

import numpy as np
import pandas as pd
import hvplot.pandas
from pathlib import Path
from dbutils import create_df, credit_score_checker
from dbutils.tableutils import create_tables, query_table
import questionary
from functools import reduce


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
    
    engine = create_tables(tbl_name, df)
    df_new = query_table(sql_query, tbl_name)
    

    print('-------------- \n' )
    credit_check, avg_income = credit_score_checker(df_new, 'credit_scores', first_name=first_name)

    if not credit_check:
        print(f"Sorry {first_name} we cannot offer you a loan, your credit score is too low")
        print(avg_income)
    else:
        print(f"Congrats {first_name} you qualify for a loan")
        questionary.text("How much loan you want").ask()

    # print(df_new)


if __name__ == '__main__':
    main()