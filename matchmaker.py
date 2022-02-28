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
people = []

def loadCSV():
    file = os.path.join(os.path.dirname(__file__), "data","input.csv")    
    global people
    people = read_csv(file)
    people = people.to_dict('records')
    print("Data file Successfully Loaded")
    #print(products)
    #print(products_csv)
    return people

def sort():
    qImportance = 0
    questionNum = 0

class Lover:
    #attributes
    emailTail = "@georgetown.edu"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

if __name__ == "__main__":
    print(people[1][1])
    
    