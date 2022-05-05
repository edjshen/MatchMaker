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
import csv
people_length = 0

fileX = 0
fileY = 0
file = 0

def loadCSV():
    global file
    global people_length
    #file = os.path.join(os.path.dirname(__file__), "data","data - Form Responses 1.csv")  
    file = input("Enter CSV file\n")
    global people
    global lenP
    people = read_csv(file)
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

    
    holdNames = []
    heldName = ""
    
    notSame = 0
    bestMatchEmailList = []
    #automating question indexing
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

            #make special case for last two people
            if(lenPy <= 2):

                
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
     
                
                
                
                
                #print(peopleY)
                if(len(peopleY) > 1):
                    q1ScorePy = peopleY[1]["q1"]
                    q2ScorePy = peopleY[1]["q2"]
                    q3ScorePy = peopleY[1]["q3"]
                    q4ScorePy = peopleY[1]["q4"]
                    q5ScorePy = peopleY[1]["q5"]
                    q6ScorePy = peopleY[1]["q6"]
                    q7ScorePy = peopleY[1]["q3"]
                    q8ScorePy = peopleY[1]["q8"]
                    q9ScorePy = peopleY[1]["q9"]
                    q10ScorePy = peopleY[1]["q10"]
                    q11ScorePy = peopleY[1]["q11"]
                    q12ScorePy = peopleY[1]["q12"]
                    q13ScorePy = peopleY[1]["q13"]
                    q14ScorePy = peopleY[1]["q14"]
                    q15ScorePy = peopleY[1]["q15"]
                    q16ScorePy = peopleY[1]["q16"]
                    q17ScorePy = peopleY[1]["q17"]
                    q18ScorePy = peopleY[1]["q18"]
                    q19ScorePy = peopleY[1]["q19"]
                    q20ScorePy = peopleY[1]["q20"]
                    q21ScorePy = peopleY[1]["q21"]
                    q22ScorePy = peopleY[1]["q22"]
                    q23ScorePy = peopleY[1]["q23"]
                    q24ScorePy = peopleY[1]["q24"]
                    q25ScorePy = peopleY[1]["q25"]
                    q26ScorePy = peopleY[1]["q26"]
                    q27ScorePy = peopleY[1]["q27"]
                    q28ScorePy = peopleY[1]["q28"]
                    q29ScorePy = peopleY[1]["q29"]
                    q30ScorePy = peopleY[1]["q30"]
                    q31ScorePy = peopleY[1]["q31"]
                    q32ScorePy = peopleY[1]["q32"]
                    q33ScorePy = peopleY[1]["q33"]
                    q34ScorePy = peopleY[1]["q34"]
                elif(len(peopleY) == 1):
                    q1ScorePy = peopleY[0]["q1"]
                    q2ScorePy = peopleY[0]["q2"]
                    q3ScorePy = peopleY[0]["q3"]
                    q4ScorePy = peopleY[0]["q4"]
                    q5ScorePy = peopleY[0]["q5"]
                    q6ScorePy = peopleY[0]["q6"]
                    q7ScorePy = peopleY[0]["q3"]
                    q8ScorePy = peopleY[0]["q8"]
                    q9ScorePy = peopleY[0]["q9"]
                    q10ScorePy = peopleY[0]["q10"]
                    q11ScorePy = peopleY[0]["q11"]
                    q12ScorePy = peopleY[0]["q12"]
                    q13ScorePy = peopleY[0]["q13"]
                    q14ScorePy = peopleY[0]["q14"]
                    q15ScorePy = peopleY[0]["q15"]
                    q16ScorePy = peopleY[0]["q16"]
                    q17ScorePy = peopleY[0]["q17"]
                    q18ScorePy = peopleY[0]["q18"]
                    q19ScorePy = peopleY[0]["q19"]
                    q20ScorePy = peopleY[0]["q20"]
                    q21ScorePy = peopleY[0]["q21"]
                    q22ScorePy = peopleY[0]["q22"]
                    q23ScorePy = peopleY[0]["q23"]
                    q24ScorePy = peopleY[0]["q24"]
                    q25ScorePy = peopleY[0]["q25"]
                    q26ScorePy = peopleY[0]["q26"]
                    q27ScorePy = peopleY[0]["q27"]
                    q28ScorePy = peopleY[0]["q28"]
                    q29ScorePy = peopleY[0]["q29"]
                    q30ScorePy = peopleY[0]["q30"]
                    q31ScorePy = peopleY[0]["q31"]
                    q32ScorePy = peopleY[0]["q32"]
                    q33ScorePy = peopleY[0]["q33"]
                    q34ScorePy = peopleY[0]["q34"]
                else:
                    break
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
                
                matchScore = abs(totalPx - totalPy)
                matchScoreList.append(matchScore)
                
            
              
                bestMatchName = people[colCounter]["name"]
                bestMatchList.append(bestMatchName)
                bestMatchEmail = people[colCounter]["email"]
                bestMatchEmailList.append(bestMatchEmail)

                
                
            else:

                lenPx = len(peopleX)
                lenPy = len(peopleY)


                if(peopleX[0]["email"] == peopleY[colCounter]["email"]):
                    
                    notSame = 0

                else:

                    notSame = 1

                #sum up all question scores
                
                if(peopleX[0]["pref"] == 3 and peopleX[0]["gender"] == peopleY[colCounter]["pref"]):
                    goAheadM = 1
                if(peopleX[0]["pref"] == peopleY[colCounter]["gender"] and peopleX[0]["gender"] == peopleY[colCounter]["pref"]):
                   goAheadM = 1
                
                    
                if(notSame == 1): 
                    goAheadM = 1
                    if(goAheadM == 1):
                        #print(peopleY[colCounter]["name"]," is a potential match\n")
                        #print(colCounter)
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
                        pass
                        matchScore = 100000
                        matchScoreList.append(matchScore)
                        bestMatchName = "N/A"
                        bestMatchEmail = "N/A"
                        bestMatchList.append(bestMatchName)
                        bestMatchEmailList.append(bestMatchEmail)
                        
                        
                else:
                    pass
                    
                
            
            colCounter = colCounter + 1
        
        if(len(matchScoreList) == 0):
            break
        else:
            pass
        #print(bestMatchList)
        
        
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
        #delete match made, need to hammer this out, doesn't work for all cases
            trashY = peopleY.pop(bestMatchIndex+1)
            trashY = peopleY.pop(0) 
        if (len(peopleX) > bestMatchIndex+1):
        #need line below for friend matching
            trashX = peopleX.pop(bestMatchIndex+1) 
            trashX = peopleX.pop(0)
        #need line below for friend matching
        
        
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
        
      
    global people_length
    #calculating match percentage
    maxPerc = (people_length*10) - 3
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
    header = ["Name","Partner Name","Score","Match Percent", "Email", "Partner Email"]
    data = []
    while(counterV < len(outputMatchesList)):
        print("Match: ",counterV+1)
        print("Name: ", outputMatchesList[counterV]["name"])
        print("Partner Name: ", outputMatchesList[counterV]["partner"])
        print("Score: ", outputMatchesList[counterV]["score"])
        print("Match Percent: ", matchPercentList[counterV],"%")
        print("Email: ", outputMatchesList[counterV]["email"])
        print("Partner Email: ", outputMatchesList[counterV]["partner email"])
        print("--------------------------")
       
        counterV = counterV + 1 
    #write to csv
    counterV = 0
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
            counterV = counterV + 1
    counterV = 0     
    with open('didnotmatch.csv', 'a', encoding='UTF8') as f:
        writer = csv.writer(f)
        while(counterV < len(noMatchList)):
            data = [noMatchList[counterV],noMatchEmailList[counterV]]
            writer.writerow(data)
            counterV = counterV + 1
            
if __name__ == "__main__": 

    peopleX = loadCSV()
    fileX = file
    peopleY = loadCSV()
    fileY = file
    alg(peopleX,peopleY)
    


    