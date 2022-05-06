# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 17:36:31 2022

@author: ejs et tz
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
import csv
from utility import *
people_length = 0

fileX = 0
fileY = 0
file = 0
            
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
                    
                    
                    totalPy = assignCol(peopleY,colCounter)
                    
                    totalPx = assignNot(peopleX)
                    
                    matchScore = abs(totalPx - totalPy)
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
        
        if(bestScore == 100000):
            noMatchList.append(peopleX[0]["name"])
            noMatchEmailList.append(peopleX[0]["email"])
        
        bestMatchIndex = matchScoreList.index(bestScore)
    
        bestMatchName = bestMatchList[bestMatchIndex]
        bestMatchEmail = bestMatchEmailList[bestMatchIndex]
      
        outputMatches = {"name" : peopleX[0]["name"], "score" : matchScoreList[bestMatchIndex],
                         "partner" : bestMatchName,"email":people[0]["email"], "partner email": bestMatchEmail}
        outputMatchesList.append(outputMatches)

        i = i + 1

        if (len(peopleY) > bestMatchIndex+1):
            trashY = peopleY.pop(bestMatchIndex+1)
            trashY = peopleY.pop(0) 
        if (len(peopleX) > bestMatchIndex+1):
            trashX = peopleX.pop(bestMatchIndex+1) 
            trashX = peopleX.pop(0)
        
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
    maxPerc = (lenP*10)
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
            
def test_always_passes():
    assert True

def test_always_fails():
    assert False
def testAlg():
    assert alg(peopleX,peopleY)
            
if __name__ == "__main__": 

    peopleX = loadCSV()
    fileX = file
    peopleY = loadCSV()
    fileY = file
    alg(peopleX,peopleY,peopleX)
    


    