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
    file = open_file()
    file = str(file)
    #file = "C:/Users/edjsh/OneDrive - Georgetown University/Documents/GitHub/MatchMaker/Code/testdata.csv"
    peopleX = loadCSV(file)
    fileX = file
    peopleY = loadCSV(file)
    fileY = file
    alg(peopleX,peopleY,peopleX)
    
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
    