# -*- coding: utf-8 -*-
"""
Created on Thu May  5 19:00:20 2022

@author: edjsh
"""

from pandas import read_csv
import csv
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os

def loadCSV():
    global file
    global people_length
    #file = os.path.join(os.path.dirname(__file__), "data","data - Form Responses 1.csv")  
    file = input("Enter CSV file\n")
    global people
    global lenP
    people = read_csv(file, encoding='cp1252')
    people_length = len(people.columns)
    people = people.to_dict('records')  
    print("Data file Successfully Loaded")
    #print(products)
    #print(products_csv)
    #lenP = len(people)
    #print(people)
    return people

def isEmpty(lis1):
    if not lis1:
        return 0
    else:
        return 1
    
def sendEmail(name, matchName, email, matchEmail):
    load_dotenv()
    SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", default="OOPS, please set env var called 'SENDGRID_API_KEY'")
    SENDER_ADDRESS = os.getenv("SENDER_ADDRESS", default="OOPS, please set env var called 'SENDER_ADDRESS'")
    email = input("Enter your email to receive an email receipt or enter N\n\n")
    
    client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
    if(email == "n" or email == "N"):
        return 0
    else:
    
        subject = "Dear " + name + ", We've found your match"
        html_content = "Your Match is: " + matchName + " and their contact is " + matchEmail
            
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

def assignNot(peopleX):
    q1ScorePx = peopleX[0]["q1"]
    q2ScorePx = peopleX[0]["q2"]
    q3ScorePx = peopleX[0]["q3"]
    q4ScorePx = peopleX[0]["q4"]
    q5ScorePx = peopleX[0]["q5"]
    q6ScorePx = peopleX[0]["q6"]
    q7ScorePx = peopleX[0]["q3"]
    q8ScorePx = peopleX[0]["q8"]
    q9ScorePx = peopleX[0]["q9"]
    q10ScorePx = peopleX[0]["q10"]
    q11ScorePx = peopleX[0]["q11"]
    q12ScorePx = peopleX[0]["q12"]
    q13ScorePx = peopleX[0]["q13"]
    q14ScorePx = peopleX[0]["q14"]
    q15ScorePx = peopleX[0]["q15"]
    q16ScorePx = peopleX[0]["q16"]
    q17ScorePx = peopleX[0]["q17"]
    q18ScorePx = peopleX[0]["q18"]
    q19ScorePx = peopleX[0]["q19"]
    q20ScorePx = peopleX[0]["q20"]
    q21ScorePx = peopleX[0]["q21"]
    q22ScorePx = peopleX[0]["q22"]
    q23ScorePx = peopleX[0]["q23"]
    q24ScorePx = peopleX[0]["q24"]
    q25ScorePx = peopleX[0]["q25"]
    q26ScorePx = peopleX[0]["q26"]
    q27ScorePx = peopleX[0]["q27"]
    q28ScorePx = peopleX[0]["q28"]
    q29ScorePx = peopleX[0]["q29"]
    q30ScorePx = peopleX[0]["q30"]
    q31ScorePx = peopleX[0]["q31"]
    q32ScorePx = peopleX[0]["q32"]
    q33ScorePx = peopleX[0]["q33"]
    q34ScorePx = peopleX[0]["q34"]
    
    totalPx = (q1ScorePx+
    q2ScorePx+
    q3ScorePx+
    q4ScorePx+
    q5ScorePx+
    q6ScorePx+
    q7ScorePx+
    q8ScorePx+
    q9ScorePx+
    q10ScorePx+
    q11ScorePx+
    q12ScorePx+
    q13ScorePx+
    q14ScorePx+
    q15ScorePx+
    q16ScorePx+
    q17ScorePx+
    q18ScorePx+
    q19ScorePx+
    q20ScorePx+
    q21ScorePx+
    q22ScorePx+
    q23ScorePx+
    q24ScorePx+
    q25ScorePx+
    q26ScorePx+
    q27ScorePx+
    q28ScorePx+
    q29ScorePx+
    q30ScorePx+
    q31ScorePx+
    q32ScorePx+
    q33ScorePx+
    q34ScorePx
    )
    
    return totalPx

def assignCol(peopleY,colCounter):
    q1ScorePy = peopleY[colCounter]["q1"]
    q2ScorePy = peopleY[colCounter]["q2"]
    q3ScorePy = peopleY[colCounter]["q3"]
    q4ScorePy = peopleY[colCounter]["q4"]
    q5ScorePy = peopleY[colCounter]["q5"]
    q6ScorePy = peopleY[colCounter]["q6"]
    q7ScorePy = peopleY[colCounter]["q3"]
    q8ScorePy = peopleY[colCounter]["q8"]
    q9ScorePy = peopleY[colCounter]["q9"]
    q10ScorePy = peopleY[colCounter]["q10"]
    q11ScorePy = peopleY[colCounter]["q11"]
    q12ScorePy = peopleY[colCounter]["q12"]
    q13ScorePy = peopleY[colCounter]["q13"]
    q14ScorePy = peopleY[colCounter]["q14"]
    q15ScorePy = peopleY[colCounter]["q15"]
    q16ScorePy = peopleY[colCounter]["q16"]
    q17ScorePy = peopleY[colCounter]["q17"]
    q18ScorePy = peopleY[colCounter]["q18"]
    q19ScorePy = peopleY[colCounter]["q19"]
    q20ScorePy = peopleY[colCounter]["q20"]
    q21ScorePy = peopleY[colCounter]["q21"]
    q22ScorePy = peopleY[colCounter]["q22"]
    q23ScorePy = peopleY[colCounter]["q23"]
    q24ScorePy = peopleY[colCounter]["q24"]
    q25ScorePy = peopleY[colCounter]["q25"]
    q26ScorePy = peopleY[colCounter]["q26"]
    q27ScorePy = peopleY[colCounter]["q27"]
    q28ScorePy = peopleY[colCounter]["q28"]
    q29ScorePy = peopleY[colCounter]["q29"]
    q30ScorePy = peopleY[colCounter]["q30"]
    q31ScorePy = peopleY[colCounter]["q31"]
    q32ScorePy = peopleY[colCounter]["q32"]
    q33ScorePy = peopleY[colCounter]["q33"]
    q34ScorePy = peopleY[colCounter]["q34"]
    
    totalPy = (q1ScorePy+
    q2ScorePy+
    q3ScorePy+
    q4ScorePy+
    q5ScorePy+
    q6ScorePy+
    q7ScorePy+
    q8ScorePy+
    q9ScorePy+
    q10ScorePy+
    q11ScorePy+
    q12ScorePy+
    q13ScorePy+
    q14ScorePy+
    q15ScorePy+
    q16ScorePy+
    q17ScorePy+
    q18ScorePy+
    q19ScorePy+
    q20ScorePy+
    q21ScorePy+
    q22ScorePy+
    q23ScorePy+
    q24ScorePy+
    q25ScorePy+
    q26ScorePy+
    q27ScorePy+
    q28ScorePy+
    q29ScorePy+
    q30ScorePy+
    q31ScorePy+
    q32ScorePy+
    q33ScorePy+
    q34ScorePy
    )
    
    return totalPy