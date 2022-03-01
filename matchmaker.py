# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 17:36:31 2022

@author: edjsh
"""
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
lovers = {}
lenP = len(people)
lenL = len(lovers)
class Lover:
    #attributes
    emailTail = "@georgetown.edu"
    
    def __init__(self,name,email,q1,q2,q3):
        self.name = name
        self.email = email
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3

def loadCSV():
    file = os.path.join(os.path.dirname(__file__), "data","data - Form Responses 1.csv")    
    global people
    global lenP
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
        matchIndex = 0
        global lenL
        while(i<lenL):
            op = lovers[i]
            #print(lovers[suitorID[ii]].q1)
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
                    matchIndex = ii
                ii = ii + 1
            print("Pair " + i + "= " + op + " & " + matchPerson)
            del lovers[i]
            del lovers[matchIndex]
            i = i + 1            

def sendEmail():
    load_dotenv()
    SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", default="OOPS, please set env var called 'SENDGRID_API_KEY'")
    SENDER_ADDRESS = os.getenv("SENDER_ADDRESS", default="OOPS, please set env var called 'SENDER_ADDRESS'")
    email = input("Enter your email to receive an email receipt or enter N\n\n")
    
    client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
    if(email == "n" or email == "N"):
        return 0
    else:
    
        subject = "Your Match from AASA MatchMaker"
        html_content = ""
            
        # FYI: we'll need to use our verified SENDER_ADDRESS as the `from_email` param
        # ... but we can customize the `to_emails` param to send to other addresses
        message = Mail(from_email=SENDER_ADDRESS, to_emails=email, subject=subject, html_content=html_content)
        
        try:
            response = client.send(message)    
            #print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
            #print(response.status_code) #> 202 indicates SUCCESS
            #print(response.body)
            #print(response.headers)    
        except Exception as err:
            print(type(err))
            print(err)

def assign():
    i = 0
    global lenL
    dicty = {}
    global list
    global people
    global lovers
    while (i<lenP):
        dicty["Person%s" %i] = Lover(people[i]["Name"],
                                          people[i]["Georgetown Email Address"],
                                          people[i]['Do you believe in love at first sight?'],
                                          people[i]['how much do you love sea lions'],
                                          people[i]['will you marry me'])
        i = i+1
        
    #lovers = DataFrame.from_dict(dicty.values)
    lovers = list(dicty.values())
    lenL = len(lovers)
    #print(lovers)
    #lenL = len(lovers)


if __name__ == "__main__":
    loadCSV()   
    assign()
    compare()
    
    