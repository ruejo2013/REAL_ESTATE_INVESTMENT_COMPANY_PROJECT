#!/usr/bin/env python3

import numpy as np
import pandas as pd
import matplotlib as plt
from pathlib import Path
from dbutils import create_df, credit_score_checker, amount_qualified
from dbutils.tableutils import create_tables, query_table
import questionary
from functools import reduce


# declaring and assigning values to variables

file_tbl = Path("Resources/customer_data.csv")
file_tbl2 = Path("Resources/cleaned_nyc_housing_data.csv")
tbl_name = "customers"
tbl_two = "housing"
first_name = questionary.text("What's your first name").ask()
ssn = questionary.text("What's your ssn").ask()


# sql query to read the applicants information 
sql_query = f"""
SELECT * 
FROM {tbl_name}
where first_name = '{first_name}'
and ssn = '{ssn}'
"""
# sql query to read housing data from the users selected boroughs

sql_query2 = """
SELECT *
FROM {tbl_2}
where BOROUGH IN {borough_name}
order by PRICE desc 
limit 50

"""


def main():
    """
    Main function to run the app
    input: None
    Output: pandas df to plot geomap of selected houses or a message saying the applicant 
    do not qualify for a loan    
    """
    df = create_df(file_tbl)
    df_housing = create_df(file_tbl2)

    engine = create_tables(tbl_name, df)
    print("-------------- ------------ \n")
    df_new = query_table(sql_query, engine=engine)

    print("-------------- --------------  \n")
    credit_check, avg_income = credit_score_checker(
        df_new, "credit_scores", first_name=first_name
    )

    if credit_check:
        
        print(f"Congrats {first_name} you qualify for a loan")
        request_amount = int(questionary.text("How much loan do you want").ask())
        print("--------------------------- \n")
        period_list = int(
            questionary.rawselect("Loan term", choices=["15", "30"]).ask()
        )
        return_msg, qualified_amount = amount_qualified(
            period_list, avg_income, request_amount
        )
        print("-------------- ----------- \n")
        accept_offer = questionary.confirm(
            f"Congrats!, you qualify for ${qualified_amount:,}. Do you like to accept this loan amount?"
        ).ask()
        
        print(return_msg)
        print("-------------- ----------- \n")

        if accept_offer:
            borough_name = questionary.checkbox(
                "What Boroughs would you like:",
                choices=["MANHATTAN", "BRONX", "BROOKLYN", "QUEENS", "STATEN ISLAND"],
            ).ask()
            print("-------------- ----------- \n")
            engine = create_tables(tbl_two, df_housing)
            
            df_housing_selected = query_table(
                sql_query2.format(tbl_2=tbl_two, borough_name=tuple(borough_name)),
                engine=engine,
            )
            df_housing_selected.to_csv('Resources/housing_selected.csv', index=False)
            
            
            

    else:
        print(
            f"Sorry {first_name} we cannot offer you a loan, your credit score is too low"
        )




if __name__ == "__main__":
    main()
