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

def loadCSV(file):
    global people_length
    #file = os.path.join(os.path.dirname(__file__), "data","data - Form Responses 1.csv")
    #file = input("Enter File Name")
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

