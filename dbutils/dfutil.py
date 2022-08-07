#!/usr/bin/env python3

import numpy as np
import pandas as pd
import hvplot.pandas
import questionary




def create_df(file_path):
    """
    
    
    """
    df = pd.read_csv(file_path)

    return df


def credit_score_checker(df, col, first_name):
    credit_score = df[col]

    if int(credit_score) < 700:
        print(f"Sorry {first_name} we cannot offer you a loan, your credit score is too low")
    else:
        print(f"Congrats {first_name} you qualify for a loan")
        questionary.text("How much loan you want").ask()