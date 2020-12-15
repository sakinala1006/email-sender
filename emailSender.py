#!/usr/bin/env python
# coding: utf-8
# Author: Sai Srinija Sakinala


import smtplib as smtp
import re


#email validation using regex
def validate_email(email):
    regex = '^[a-zA-Z]+[\._]?[a-zA-Z1-9]+[@]\w+[.]\w{2,3}$'
    
    if re.search(regex,email):
        return True
    else:
        print("Incorrect format, check again!")
    return False



def send_email(email, message):
    sender = 'saisrinija.sakinala@gmail.com'
    receivers = [email]
    
    #extract name of the receiver
    sep1 = email.index('@')
    name = email[0:sep1]
    
    #extract domain name
    domainCom = email[sep1+1:] 
    sep2 = domainCom.index('.')
    domain = domainCom[0:sep2]
    
    if domain == 'gmail' or domain == 'outlook':
        #general case
        message = "Hello " + name + "\n" + message
        
    else:
        #specific organization
        message = "Hello "+ name + " from " + domain + "\n" + message
    
    try:
        #run local server using the command : python -m smtpd -n -c DebuggingServer localhost:1025
        smtpObject = smtp.SMTP('localhost', 1025)
        smtpObject.sendmail(sender, receivers, message)
        print("SENT!")
        
    except Exception:
        print(e)
    
    

def main():
    email = raw_input("Enter the email to whom the message must be sent: ")

    if(validate_email(email)):
        message = raw_input("Message to be sent:")
        send_email(email, message)
    else:
        #if incorrectly entered, ask again
        main()



if __name__ == "__main__":
    main()
