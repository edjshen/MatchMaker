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
lenP = len(people)

class Lover:
    #attributes
    emailTail = "@georgetown.edu"
    
    def __init__(self, name, age, q1,q2,q3):
        self.name = name
        self.age = age

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

def assign():
    i = 0
    dicty = {}
    for number in range(1,lenP):
        dicty["Person%s" %number] = Lover(people[1][1],people[1][2],people[1][3],people[1][4],people[1][5])
        listy = list(dicty.values)'
        
    print(listy)

if __name__ == "__main__":
    #loadCSV()
    #person = Lover("name")
    #print(people[1][1])
    assign()
    
    