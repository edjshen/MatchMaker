# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 17:36:31 2022

@author: ejs et al
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



"""
class Lover:
    #attributes
    emailTail = "@georgetown.edu"
    
    def __init__(self,name,email,q1,q2,q3):
        self.name = name
        self.email = email
        #self.gender = gender
        #self.orient = orient
        #self.match = match
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
"""

def loadCSV():
    file = os.path.join(os.path.dirname(__file__), "data","data - Form Responses 1.csv")    
    global people
    global lenP
    people = read_csv(file)
    people = people.to_dict('records')
    print("Data file Successfully Loaded")
    #print(products)
    #print(products_csv)
    #lenP = len(people)
    #print(people)
    return people

"""
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
                            trash = lovers.pop(suitorID[ii])
                            trash = lovers.pop(i-1)
                ii = ii + 1
                go = 0
            print("Pair " + str(i+1) + " = " + op.name + " & " + matchPerson)
            print("Your match score is " + str(matchScore))
            #del lovers[i]
            #del lovers[matchIndex]
            i = i - 1            
"""

def matchmake():
    i = 0
    isEmpty = 0
    matchingMatrix = []
    global people
    if(len(people) == 0):
        isEmpty = 1
    if(isEmpty == 1):
        print("Reached end of list")
    else:
        print("wait")
        
    
        
    

def sendEmail():
    load_dotenv()
    SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", default="OOPS, please set env var called 'SENDGRID_API_KEY'")
    SENDER_ADDRESS = os.getenv("SENDER_ADDRESS", default="OOPS, please set env var called 'SENDER_ADDRESS'")
    email = input("Enter your email to receive an email receipt or enter N\n\n")
    
    client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
    if(email == "n" or email == "N"):
        return 0
    else:
        subject = "Your Match from MatchMaker"
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

if __name__ == "__main__":    
    #declare variables
    peopleX = []
    peopleY = []
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
    
    #load in data file
    people = loadCSV() 
    
    #initial assignments to variables
    peopleX = people
    peopleY = people
    lenPx = len(peopleX)
    lenPy = len(peopleY)
    lenP = len(people)
    
    
    holdNames = []
    heldName = ""
    
    notSame = 0
    
    #Looping through Person X (rows)
    while(i<lenPx):
        print("I am finding the perfect match for",peopleX[i]["name"])
        #Looping through all Person Ys (Columns)
        while(colCounter < len(peopleY)):
            #print("heyo")
            #print(lenPy) 
            lenPy = len(peopleY)
            #print("this is lenPy",lenPy)
            #make special case for last two people
            if(lenPy < 2):
                print("We're on our last possible candidate!\n")
                #print(peopleX)
                
                q1ScorePx = peopleX[0]["q1"]
                q2ScorePx = peopleX[0]["q2"]
                q3ScorePx = peopleX[0]["q3"]
                
                #print(peopleY)
                
                q1ScorePy = peopleY[1]["q1"]
                q2ScorePy = peopleY[1]["q2"]
                q3ScorePy = peopleY[1]["q3"]
                
                totalPx = q1ScorePx + q2ScorePx + q3ScorePx
                totalPy = q1ScorePy + q2ScorePy + q3ScorePy
                
                matchScore = abs(totalPx - totalPy)
                matchScoreList.append(matchScore)
                
                bestScore = max(matchScoreList)
                bestMatchIndex = matchScoreList.index(bestScore)
                bestMatchName = matchScoreList[bestMatchIndex]
                bestMatchList.append(bestMatchName)
                bestScoreList.append(bestScore)

                peopleY.pop(matchScoreList[bestMatchIndex])
                
                
            else:
                print("There is more than 1 person left to check\n")
                #print(peopleX)
                #print("i am running")
                lenPx = len(peopleX)
                lenPy = len(peopleY)
                #print(lenPy)
                #print(lenPx)
                #print(lenPy)
                #print(str(colCounter)+"]")
                #print(people)
                #print("PeopleX")
                #print(peopleX)
                #print("PeopleY")
                #print(peopleY)
                
                #Check if people are the same, if they are, skip it, if not, search
                #(colCounter >= lenPy):
                #    colCounter  = min(colCounter,lenPy) - 1
                #print(peopleY)
                #print("Length of PeopleX = ",len(peopleX))
                #print("Length of PeopleY = ",len(peopleY))
                #print("Length of i = ",i)
                #print("Length of colCounter = ",colCounter)
                if(peopleX[i]["email"] == peopleY[colCounter]["email"]):
                    
                    notSame = 0
                    #print("Person X Name ",peopleX[i]["name"])
                    #print(peopleY)
                    #print(colCounter)
                    #print("Person Y Name ", peopleY[colCounter]["name"])
                else:
                    #print(peopleX[i]["email"])
                    #print(peopleY[colCounter]["email"])
                    notSame = 1
                    #print("this is i ",i)
                    #print(peopleX)
                    #print("Person X Name ",peopleX[i]["name"])
                    #print(peopleY)
                    #print(colCounter)
                    #print("Person Y Name ", peopleY[colCounter]["name"])
                
                if(notSame == 1): 
                    print(peopleY[colCounter]["name"]," is a potential match\n")
                    print(colCounter)
                    q1ScorePx = peopleX[i]["q1"]
                    q2ScorePx = peopleX[i]["q2"]
                    q3ScorePx = peopleX[i]["q3"]
                    
                    q1ScorePy = peopleY[colCounter]["q1"]
                    q2ScorePy = peopleY[colCounter]["q2"]
                    q3ScorePy = peopleY[colCounter]["q3"]
                    
                    totalPx = q1ScorePx + q2ScorePx + q3ScorePx
                    totalPy = q1ScorePy + q2ScorePy + q3ScorePy
                    #print(peopleX[i])
                    #print(peopleY[colCounter])
                    #print(totalPx)
                    #print(totalPy)
                    
                    matchScore = abs(totalPx - totalPy)
                    matchScoreList.append(matchScore)
                    #print(matchScore)
                    
                        
            
    # Finding who is best match, adding them to output list, and deleting matches from general population

                    #print("Length of PeopleX = ",len(peopleX))
                    #print("Length of PeopleY = ",len(peopleY))
                    #print("Length of i = ",i)
                    #print("Length of colCounter = ",colCounter)
            
                    bestScore = max(matchScoreList)
                    bestScoreList.append(bestScore)
                    bestMatchIndex = matchScoreList.index(bestScore)
                    #print("i have ran" + str(colCounter) + " Y people")
                    #print(peopleX)
                    bestMatchName = peopleX[bestMatchIndex]
                    bestMatchList.append(bestMatchName)
                    
                    #print(peopleX)
                    #print()
                    #print("I am the best match", bestMatchName)
                    #print(bestScore)
                    #print(peopleY)
                    holder = peopleY.pop(colCounter)
            
                    lenPx = len(peopleX)
                    lenPy = len(peopleY)
                else:
                    #print(peopleX)
                    print("You can't match with yourself\n")
                    #print("i am people",people)
                    #holder = peopleY[colCounter]
                    #print(holder)
                    #print(peopleX)
                    #print("i am people x AFTER POP",people)
                    #print(people)
                    #peopleX = people
                    #print(holder)
                    #print(peopleX)
                    #print(peopleX[i]["name"])
                    #print(peopleY[colCounter]["name"])
                
            colCounter = colCounter + 1
            #print(lenPy)
        print("I IS ITERATING AHHHHHHHHHHHHHHHHHHHHHHHH")
        i = i + 1
        #Clear Variables for next iteration of PersonX
        #colCounter = 0
        #peopleX.pop(matchScoreList[bestMatchIndex])
        matchScoreList = []
        matchScore = 0
        bestScore = 0
        bestMatchIndex = 0
        bestMatchName = 0
        holder = 0

        
    
    #Output
    #print(bestMatchList)
    #print(bestScoreList)
            
    
    
    

    