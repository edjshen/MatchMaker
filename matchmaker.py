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

fileX = 0
fileY = 0
file = 0

def loadCSV():
    global file
    #file = os.path.join(os.path.dirname(__file__), "data","data - Form Responses 1.csv")  
    file = input("Enter CSV file\n")
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
            
def isEmpty(lis1):
    if not lis1:
        return 0
    else:
        return 1

def alg(peopleX,peopleY):   
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
    #people = loadCSV() 
    #initial assignments to variables
    #peopleX = people
    #peopleY = people
    lenPx = len(peopleX)
    lenPy = len(peopleY)
    lenP = len(people)
    #print(people)
    #print(lenPx,lenPy,lenP)
    #print(peopleX)
    
    holdNames = []
    heldName = ""
    
    notSame = 0
    
    #automating question indexing
    couting = 0
    
    #while(counting < len(people[0].keys())-2):
        
    
    #Looping through Person X (rows)
    while(isEmpty(peopleX)):
        #print("This is i ", i)
        #print(peopleX)
        #print("I am finding the perfect match for",peopleX[0]["name"])
        #Looping through all Person Ys (Columns)
        while(colCounter < lenPy):
            #print("heyo")
            #print(lenPy) 
            #lenPy = len(peopleY)
            #print("this is lenPy",lenPy)
            #make special case for last two people
            if(lenPy <= 2):
                #print("We're on our last possible candidate!\n")
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
                """
                bestScore = max(matchScoreList)
                bestMatchIndex = matchScoreList.index(bestScore)
                bestMatchName = matchScoreList[bestMatchIndex]
                bestMatchList.append(bestMatchName)
                bestScoreList.append(bestScore)
                """
                
            
                
                #print(peopleX[0]["name"],"'s"," best match is " , bestMatchName)
                #print("My match score with", bestMatchName, " is ", matchScoreList[bestMatchIndex])
                bestMatchName = peopleX[colCounter]["name"]
                bestMatchList.append(bestMatchName)

                #peopleY.pop(matchScoreList[bestMatchIndex])
                #print("I AM RUNINGDKADLFJADLKFJAD;FJDA;KLJFKLADSF")
                
                
            else:
                #print("There is more than 1 person left to check\n")
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
                if(peopleX[0]["email"] == peopleY[colCounter]["email"]):
                    
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
                #sum up all question scores
                if(notSame == 1): 
                    #print(peopleY[colCounter]["name"]," is a potential match\n")
                    #print(colCounter)
                    q1ScorePx = peopleX[0]["q1"]
                    q2ScorePx = peopleX[0]["q2"]
                    q3ScorePx = peopleX[0]["q3"]
                    
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
                               
    # Finding who is best match, adding them to output list, and deleting matches from general population

                    #print("Length of PeopleX = ",len(peopleX))
                    #print("Length of PeopleY = ",len(peopleY))
                    #print("Length of i = ",i)
                    #print("Length of colCounter = ",colCounter)
            
                    #bestScore = max(matchScoreList)
                    #bestScoreList.append(bestScore)
                    #bestMatchIndex = matchScoreList.index(bestScore)
                    #print("i have ran" + str(colCounter) + " Y people")
                    #print(peopleX)
                    #print(colCounter)
                    bestMatchName = people[colCounter]["name"]
                    bestMatchList.append(bestMatchName)
                    
                    #print(peopleX)
                    #print()
                    #print("I am the best match", bestMatchName)
                    #print(bestScore)
                    #print(peopleY)
                    #holder = peopleY.pop(colCounter)
            
                    lenPx = len(peopleX)
                    lenPy = len(peopleY)
                else:
                    pass
                    #print(peopleX)
                    #print("You can't match with yourself\n")
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
                
            #print("This is column counter: ", str(colCounter),
            #      " and this is the match person being tested" ,peopleY[colCounter]["name"])
            colCounter = colCounter + 1
            #print("i have looped ",colCounter," times")
            #print("My name is ", peopleX[0]["name"], "my match score is "
            #     , matchScore, "and my current testing partner's name is",bestMatchName)
            #print(lenPy)
            #print(colCounter)
        #holder = peopleX.pop(i)
        #print(bestScoreList)
        bestScore = min(matchScoreList)
        bestMatchIndex = matchScoreList.index(bestScore)
        #print("i have ran" + str(colCounter) + " Y people")
        #print(peopleX)
        bestMatchName = bestMatchList[bestMatchIndex]
        #print(peopleX[0]["name"],"'s"," best match is " , bestMatchName)
        #print("My match score with", bestMatchName, " is ", matchScoreList[bestMatchIndex])
        outputMatches = {"name" : peopleX[0]["name"], "score" : matchScoreList[bestMatchIndex],
                         "partner" : bestMatchName}
        outputMatchesList.append(outputMatches)
        #print(peopleX[i])
        i = i + 1
        #Clear Variables for next iteration of PersonX
        #colCounter = 0
        
        #peopleX.pop(matchScoreList[bestMatchIndex])
        #print(peopleY)
        #print(bestMatchIndex)
        #print("hey")
        #print(peopleY)
        #print(bestMatchIndex)
        #print(len(peopleY))
        
        #delete match made, need to hammer this out, doesn't work for all cases
        trashY = peopleY.pop(bestMatchIndex+1)
        #need line below for friend matching
        trashX = peopleX.pop(bestMatchIndex+1) 
        trashX = peopleX.pop(0)
        #need line below for friend matching
        trashY = peopleY.pop(0) 
        
        #print(trashX)
        colCounter = 0
        matchScoreList = []
        matchScore = 0
        bestScore = 0
        bestMatchIndex = 0
        bestMatchName = 0
        holder = 0
        bestScoreList =[]
        bestMatchList=[]
        
      
        
    #calculating match percentage
    maxPerc = 30.00
    counterP = 0
    matchPercentList = []
    while(counterP < len(outputMatchesList)):     
        matchPercentage = round(1-(outputMatchesList[counterP]["score"]/maxPerc),4)*100
        matchPercentList.append(matchPercentage)
        counterP = counterP + 1
    
    #Output
    counterV = 0
    print("OUTPUTS")
    print("--------------------------")
    while(counterV < len(outputMatchesList)):
        print("Match: ",counterV+1)
        print("Name: ", outputMatchesList[counterV]["name"])
        print("Partner Name: ", outputMatchesList[counterV]["partner"])
        print("Score: ", matchPercentList[counterV],"%")
        print("--------------------------")
        counterV = counterV + 1 
 
if __name__ == "__main__": 
    """
    IMPORTANT NOTE! THIS ALGORITHM IS GENDER AND SEXUAL ORIENTATION AGNOSTIC,
    It is important to clean and sort the data before processing using this algorithm
    PLUG IN FIRST POPULATION AS PEOPLEX, IE STRAIGHT MEN, THEN THEIR PREFERENCE POOL, STRAIGHT/BI WOMEN
    """
    peopleX = loadCSV()
    fileX = file
    peopleY = loadCSV()
    fileY = file
    alg(peopleX,peopleY)
    
    """
    i = 0
    
    #alg()
    romantic = []
    platonic = []
    straightM = []
    straightF = []
    gayM = []
    gayF = []
    BiM = []
    BiF = []
    nonBin = []
    people = loadCSV()
    
    #loading different pools for different gender/sexual orientation
    while(i<len(people)):
        #split into romantic and platonic
        #print(people[i]["pref"])
        if(people[i]["pref"] == "R"):   
            romantic.append(people[i])
        else:
            platonic.append(people[i])
        i = i+1
                     
    i = 0
    while(i<len(romantic)):
        #different sexual orientation sorting
        #print(romantic)
        print(i)
        if(romantic[i]["gender"] == "M" and romantic[i]["orientation"] == "S"):
            #Straight Men
            print("added")
            straightM.append(romantic[i])

        elif(romantic[i]["gender"] == "M" and romantic[i]["orientation"] == "G"):
            #Gay Men
            gayM.append(romantic[i])

        elif(romantic[i]["gender"] == "F" and romantic[i]["orientation"] == "S"):
            #Straight Women
            straightF.append(romantic[i])

        elif(romantic[i]["gender"] == "F" and romantic[i]["orientation"] == "G"):
            #Gay Women
            gayF.append(romantic[i])
       
        elif(romantic[i]["gender"] == "M" and romantic[i]["orientation"] == "B"):
            #Bi Men
            BiM.append(romantic[i])

        elif(romantic[i]["gender"] == "F" and romantic[i]["orientation"] == "B"):
            #Bi Women
            BiF.append(romantic[i])

        elif(romantic[i]["gender"] == "X" and romantic[i]["orientation"] == "X"):
            #Non-binary
            nonBin.append(romantic[i])
        
        i = i+1
    print(straightM)
    #alg(straightM,straightF)
    #alg(gayM,gayM)
    #alg(gayF,gayF)
    #alg(BiM,gayM)
    #alg(platonic,platonic)

    """
            
    
    
    
    

    