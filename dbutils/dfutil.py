#!/usr/bin/env python3

import numpy as np
import pandas as pd
import hvplot.pandas
import questionary
from functools import reduce



def dbt_income_ratio(df):
    """
    function to calculate current debt to income ratio
    input:
    df: pandas df
    col1; year 1 earning
    col2: year 2 earning
    col3: year 3 earning
    col4: 
    """
    customer_info = list(df.values)
    lst = (customer_info[0][5], customer_info[0][6], customer_info[0][7])
    avg_income = round(reduce(lambda a, b: a + b, lst) / len(lst), 2)
    monthly_gross_income = avg_income/12
    monthly_debt_payment = customer_info[0][10]/12
    dti = round((monthly_debt_payment / monthly_gross_income) * 100, 2)
    return avg_income, dti


def create_df(file_path):
    """
    Function to read file to pandas dataframe
    input file: file path
    output: pandas df    
    """
    df = pd.read_csv(file_path)

    return df


def credit_score_checker(df, col, first_name):
    """
    loan qualifier function
    input: 
    pandas df
    col: column name
    first name: customers name
     
    """
    credit_score = df[col]
    avg_income, debt_to_income = dbt_income_ratio(df)
    pass_credit_check = None
    

    if int(credit_score) < 700:
        pass_credit_check = False

    elif int(credit_score) > 690 and int(debt_to_income) > 15:
        pass_credit_check = False
              
    
    else:
        pass_credit_check = True


    return pass_credit_check, avg_income


def amount_qualified(avg_income, period, request_amount):
    """
    Function to determine the amount the applicant qualify for.
    Input:
    
    
    """
    qualified_amount = avg_income * 0.35 * period

    if qualified_amount > request_amount:
        return_msg = f"Congratulations! you are qualified for the amount you requested ${request_amount:,}"
        return_amount = request_amount
    else:
        return_msg = f"Congratulations! you are qualified for  ${qualified_amount:,}"
        return_amount = qualified_amount
    return return_msg, return_amount