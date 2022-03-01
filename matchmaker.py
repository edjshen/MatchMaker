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
    
    def __init__(self,name,email,match,q1,q2,q3):
        self.name = name
        self.email = email
        self.match = match
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
        global lenL
        op = lovers[1]
        i = lenL - 1
        ii = 0
        quality = 0
        suitorID = []
        count = 0
        counter = 0
        q1Compat = 100
        q2Compat = 100
        q3Compat = 100
        matchScore = 100
        q1Check = 100
        q2Check = 100
        q3Check = 100
        matchPerson = ""
        matchIndex = 0
        go = 0
        empty = 1
        temp1 = 0
        temp2 = 0
        temp3 = 0        
        while(i>0):
            if(lovers):
                print("---")
            else:
                empty = 0
            if empty == 1:
                #print(lovers)
                op = lovers[lenL-i]
            while(ii<lenL):
                lenL = len(lovers)
                if(i != ii):
                    suitorID.append(ii)
                    go = 1
                if(go == 1):
                    #print(op.q1 - lovers[suitorID[ii-1]].q1)
                   # print(q1Compat)
                    if(abs(op.q1 - lovers[suitorID[ii-1]].q1)<q1Compat):
                        temp1 = op.q1 - lovers[suitorID[ii-1]].q1
                        q1Check = 1           
                        #print("yuh")
                    if(abs(op.q2 - lovers[suitorID[ii-1]].q2)<q2Compat):
                        temp2 = op.q2 - lovers[suitorID[ii-1]].q2
                        q2Check = 1   
                    if(abs(op.q3 - lovers[suitorID[ii-1]].q3)<q3Compat):
                        temp3 = op.q3 - lovers[suitorID[ii-1]].q3
                        q3Check = 1
                    if (q1Check or q2Check or q3Check):
                        tempTot = temp1+ temp2+ temp3
                        #print("YAAAA")
                        #print(tempTot)
                        #print(matchScore)
                        #print(temp1)
                        #print(temp2)
                        #print(temp3)
                        if(tempTot<matchScore):
                            #print("heyo")
                            #q1Compat = abs(op.q1 - lovers[suitorID[ii-1]].q1)
                            #q2Compat = abs(op.q2 - lovers[suitorID[ii-1]].q2)
                            #q3Compat = abs(op.q3 - lovers[suitorID[ii-1]].q3)
                            #matchScore = q1Compat + q2Compat + q3Compat
                            matchScore = tempTot
                            matchPerson = lovers[suitorID[ii]].name
                            matchIndex = ii                           
                            lovers.pop(suitorID[ii])
                            lovers.pop(i-1)
                ii = ii + 1
                go = 0
            print("Pair " + str(i+1) + " = " + op.name + " & " + matchPerson)
            print("Your match score is " + str(matchScore))
            #del lovers[i]
            #del lovers[matchIndex]
            i = i - 1            

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
    
    