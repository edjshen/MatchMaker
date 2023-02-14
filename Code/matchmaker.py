# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 17:36:31 2022

@author: ejs et tz
"""
import streamlit as st
from datetime import datetime
import os
import pandas as pd
from dotenv import load_dotenv
from pathlib import Path
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from pandas import read_csv
from pandas import DataFrame
import csv
from pandas import read_csv


def loadCSV(f):
    global people_length
    #file = os.path.join(os.path.dirname(__file__), "data","data - Form Responses 1.csv")
    #file = input("Enter File Name")
    global people
    global lenP
    people = read_csv(f, encoding='cp1252')
    people_length = len(people.columns)
    people = people.to_dict('records')  
    print("Data file Successfully Loaded")
    #print(products)
    #print(products_csv)
    #lenP = len(people)
    #print(people)
    return people

# Import the library
from tkinter import *
from tkinter import filedialog



# Function to open a file in the system
def open_file():
    # Create an instance of window
    win=Tk()

    # Set the geometry of the window
    win.geometry("700x300")

    # Create a label
    Label(win, text="Click the button to open a dialog", font='Arial 16 bold').pack(pady=15)
    filepath = filedialog.askopenfilename(title="Open a CSV File", filetypes=(("csv    files","*.csv"), ("all files","*.*")))
    #file = open(filepath,'r')
    #print(file.read())
    #file.close()
    
    # Create a button to trigger the dialog
    button = Button(win, text="Open", command=open_file)
    button.pack()

    win.mainloop()
    return filepath



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
people_length = 0

fileX = 0
fileY = 0
file = 0
numbers = []
nQuestions = 34
            
def alg(peopleX,peopleY,people):   
    #declare variables
    #peopleX = []
    #peopleY = []
    lenPX = 0
    lenPY = 0
    i = 0
    q1ScorePx = 0
    q1ScorePy = 0
    q2ScorePx = 0
    q2ScorePy = 0
    q3ScorePx = 0
    q3ScorePy = 0
    totalPx = 0
    totalPy = 0
    matchScore = 0
    matchScoreList = []
    bestScore = 0
    bestMatchIndex = 0
    bestMatchName = ""
    bestMatchList = []
    bestScoreList = []
    colCounter = 0
    outputMatches = {}
    outputMatchesList =[]
    
    #load in data file
    #initial assignments to variables
    
    lenPx = len(peopleX)
    lenPy = len(peopleY)
    lenP = len(people)
    
    holdNames = []
    heldName = ""
    
    notSame = 0
    bestMatchEmailList = []
    couting = 0
    goAhead = 0
    goAheadT = 0
    goAheadM = 0
    noMatchList = []
    noMatchEmailList = []

    #Looping through Person X (rows)
    while(len(peopleX) > 0):

        while(colCounter < lenPy):
            goAhead = 0
            goAheadT = 0
            goAheadM = 0

            lenPx = len(peopleX)
            lenPy = len(peopleY)
            if(peopleX[0]["email"] == peopleY[colCounter]["email"]): 
                notSame = 0
            else:
                notSame = 1

            #sum up all question scores                
                
            if(notSame == 1): 
                goAheadM = 1
                if(goAheadM == 1):
                    
                    
                    matchScore = assign(peopleX,peopleY,colCounter)
                    matchScoreList.append(matchScore)
                               
    # Finding who is best match, adding them to output list, and deleting matches from general population

                    bestMatchName = people[colCounter]["name"]
                    bestMatchEmail = people[colCounter]["email"]
                    bestMatchList.append(bestMatchName)
                    bestMatchEmailList.append(bestMatchEmail)

                    lenPx = len(peopleX)
                    lenPy = len(peopleY)
                else:               
                    matchScore = 100000
                    matchScoreList.append(matchScore)
                    bestMatchName = "N/A"
                    bestMatchEmail = "N/A"
                    bestMatchList.append(bestMatchName)
                    bestMatchEmailList.append(bestMatchEmail)           
            colCounter = colCounter + 1
        
        if(len(matchScoreList) == 0):
            break
        else:
            pass 
        bestScore = min(matchScoreList)
        
        if(bestScore > 5000):
            noMatchList.append(peopleY[colCounter]["name"])
            noMatchEmailList.append(peopleY[colCounter]["email"])
        
        bestMatchIndex = matchScoreList.index(bestScore)
        bestMatchName = bestMatchList[bestMatchIndex]
        bestMatchEmail = bestMatchEmailList[bestMatchIndex]

        outputMatches = {"name" : peopleX[0]["name"], "score" : matchScoreList[bestMatchIndex],
                         "partner" : bestMatchName,"email":peopleX[0]["email"], "partner email": bestMatchEmail}
        outputMatchesList.append(outputMatches)

        i = i + 1
        
        trashX = peopleX.pop(0)
        #print(bestMatchIndex+1)
        trashY = peopleY.pop(bestMatchIndex)
        #if (len(peopleY) > bestMatchIndex+1):
            #trashY = peopleY.pop(bestMatchIndex+1)
            #trashY = peopleY.pop(0) 
        #if (len(peopleX) > bestMatchIndex+1):
            #trashX = peopleX.pop(bestMatchIndex+1) 
            #trashX = peopleX.pop(0)
        
        #print(trashX)
        colCounter = 0
        matchScoreList = []
        matchScore = 0
        bestScore = 0
        #bestMatchIndex = 0
        bestMatchName = 0
        holder = 0
        bestScoreList =[]
        bestMatchList=[]
        bestMatchEmailList = []
        
    #calculating match percentage
    maxPerc = (nQuestions*100)
    counterP = 0
    matchPercentList = []
    while(counterP < len(outputMatchesList)):     
        matchPercentage = round(1-(outputMatchesList[counterP]["score"]/maxPerc),4)*100
        matchPercentList.append(matchPercentage)
        counterP = counterP + 1
    
    #Output
    #write to csv

    counterV = 0
    print("OUTPUTS")
    print("--------------------------")
    header = ["Name","Partner Name","Score","Match Percent", "Email", "Partner Email"]
    data = []
    with open('output.csv', 'a', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        while(counterV < len(outputMatchesList)):
            data = [outputMatchesList[counterV]["name"],
                            outputMatchesList[counterV]["partner"],
                            outputMatchesList[counterV]["score"],
                            matchPercentList[counterV],
                            outputMatchesList[counterV]["email"],
                            outputMatchesList[counterV]["partner email"]]
            writer.writerow(data)
            print("Match: ",counterV+1)
            print("Name: ", outputMatchesList[counterV]["name"])
            print("Partner Name: ", outputMatchesList[counterV]["partner"])
            print("Score: ", outputMatchesList[counterV]["score"])
            print("Match Percent: ", matchPercentList[counterV],"%")
            print("Email: ", outputMatchesList[counterV]["email"])
            print("Partner Email: ", outputMatchesList[counterV]["partner email"])
            print("--------------------------")
            counterV = counterV + 1
    counterV = 0     
    with open('didnotmatch.csv', 'a', encoding='UTF8') as f:
        writer = csv.writer(f)
        while(counterV < len(noMatchList)):
            data = [noMatchList[counterV],noMatchEmailList[counterV]]
            writer.writerow(data)
            counterV = counterV + 1
    counterV = 0
    with open('nomatch.csv', 'a', encoding='UTF8') as f:
        writer = csv.writer(f)
        while(counterV < len(peopleY)):
            data = [peopleY[counterV]["name"],peopleY[counterV]["email"]]
            writer.writerow(data)
            counterV = counterV + 1
            

            
def assign(peopleX,peopleY,colCounter):
    squareScoreTotal = 0
    sqrDif = 0
    xList = []
    yList = []
    for x in range(1,34):
        numbers.append(x)
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
    #q35ScorePx = peopleX[0]["q35"]
    
    xList.append(q1ScorePx)
    xList.append(q2ScorePx)
    xList.append(q3ScorePx)
    xList.append(q4ScorePx)
    xList.append(q5ScorePx)
    xList.append(q6ScorePx)
    xList.append(q7ScorePx)
    xList.append(q8ScorePx)
    xList.append(q9ScorePx)
    xList.append(q10ScorePx)
    xList.append(q11ScorePx)
    xList.append(q12ScorePx)
    xList.append(q13ScorePx)
    xList.append(q14ScorePx)
    xList.append(q15ScorePx)
    xList.append(q16ScorePx)
    xList.append(q17ScorePx)
    xList.append(q18ScorePx)
    xList.append(q19ScorePx)
    xList.append(q20ScorePx)
    xList.append(q21ScorePx)
    xList.append(q22ScorePx)
    xList.append(q23ScorePx)
    xList.append(q24ScorePx)
    xList.append(q25ScorePx)
    xList.append(q26ScorePx)
    xList.append(q27ScorePx)
    xList.append(q28ScorePx)
    xList.append(q29ScorePx)
    xList.append(q30ScorePx)
    xList.append(q31ScorePx)
    xList.append(q32ScorePx)
    xList.append(q33ScorePx)
    xList.append(q34ScorePx)
    #xList.append(q35ScorePx)
    
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
    #q35ScorePy = peopleY[colCounter]["q35"]
    
    yList.append(q1ScorePy)
    yList.append(q2ScorePy)
    yList.append(q3ScorePy)
    yList.append(q4ScorePy)
    yList.append(q5ScorePy)
    yList.append(q6ScorePy)
    yList.append(q7ScorePy)
    yList.append(q8ScorePy)
    yList.append(q9ScorePy)
    yList.append(q10ScorePy)
    yList.append(q11ScorePy)
    yList.append(q12ScorePy)
    yList.append(q13ScorePy)
    yList.append(q14ScorePy)
    yList.append(q15ScorePy)
    yList.append(q16ScorePy)
    yList.append(q17ScorePy)
    yList.append(q18ScorePy)
    yList.append(q19ScorePy)
    yList.append(q20ScorePy)
    yList.append(q21ScorePy)
    yList.append(q22ScorePy)
    yList.append(q23ScorePy)
    yList.append(q24ScorePy)
    yList.append(q25ScorePy)
    yList.append(q26ScorePy)
    yList.append(q27ScorePy)
    yList.append(q28ScorePy)
    yList.append(q29ScorePy)
    yList.append(q30ScorePy)
    yList.append(q31ScorePy)
    yList.append(q32ScorePy)
    yList.append(q33ScorePy)
    yList.append(q34ScorePy)
    #yList.append(q35ScorePy)
    
    scoreslist = []
    i = 0
    while(i<nQuestions):
        sqrDif = (xList[i] - yList[i])**2
        scoreslist.append(sqrDif)
        i = i+1
    i = 0
    squareScoreTotal = 0
    while(i<len(scoreslist)):
        squareScoreTotal = scoreslist[i]+squareScoreTotal
        i = i + 1
    
    xList = []
    yList = []
    scoreslist = [] 
    return squareScoreTotal
        
    
            
if __name__ == "__main__": 

    
    filex = open_file()
    filex = str(filex)
    peopleX = loadCSV(filex)
    #file = "C:/Users/edjsh/OneDrive - Georgetown University/Documents/GitHub/MatchMaker/Code/testdata.csv"
    #fileX = file
    
    file1 = open_file()
    file1 = str(file1)
    peopleY = loadCSV(file1)
    #fileY = file
    alg(peopleX,peopleY,people)
    
    
