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
lovers = []
lenP = len(people)
lenL = len(lovers)
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
    lenP = len(people)
    
    return people


def compare():
        op = lovers[1]
        i = 0
        ii = 0
        quality = 0
        suitorID = []
        count = 0
        counter = 0
        q1Compat = 0
        q2Compat = 0
        q3Compat = 0
        matchScore = 0
        q1Check = 100
        q2Check = 100
        q3Check = 100
        matchPerson = 0
        while(i<lenL):
            op = lovers[i]
            while(ii<lenL):
                if(i != ii):
                    suitorID.append(ii)
                if(abs(op.q1 - lovers[suitorID[ii]].q1)<q1Compat):
                    q1Check = 1                    
                if(abs(op.q2 - lovers[suitorID[ii]].q2)<q2Compat):
                    q2Check = 1   
                if(abs(op.q3 - lovers[suitorID[ii]].q3)<q3Compat):
                    q3Check = 1
                if (q1Check & q2Check & q3Check):
                    q1Compat = abs(op.q1 - lovers[suitorID[ii]].q1)
                    q2Compat = abs(op.q2 - lovers[suitorID[ii]].q2)
                    q3Compat = abs(op.q3 - lovers[suitorID[ii]].q3)
                    matchScore = q1Compat + q2Compat + q3Compat
                    matchPerson = suitorID[ii].name
                ii = ii + 1
            i = i + 1            

def assign():
    i = 0
    dicty = {}
    global list
    for number in range(1,lenP):
        dicty["Person%s" %number] = Lover(people[1][1],people[1][2],people[1][3],people[1][4],people[1][5])
        lovers = list(dicty.values)
    lenL = len(lovers)


if __name__ == "__main__":
    loadCSV()   
    assign()
    compare()
    
    