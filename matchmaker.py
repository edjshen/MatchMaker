# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 17:36:31 2022

@author: edjsh
"""

print("Hello")

from datetime import datetime
import os
from dotenv import load_dotenv
from pathlib import Path
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import pandas as pd
from pandas import read_csv
from pandas import DataFrame

def loadCSV():
    file = os.path.join(os.path.dirname(__file__), "data","input.csv")    
    global products
    products = read_csv(file)
    products = products.to_dict('records')
    print("Data file Successfully Loaded")
    #print(products)
    #print(products_csv)
    return products

if __name__ == "__main__":
    