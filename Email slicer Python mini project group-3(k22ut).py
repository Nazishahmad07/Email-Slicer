#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      hp
#
# Created:     25/11/2022
# Copyright:   (c) hp 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def email_splitter(email):
    username = email.split('@')[0]
    domain = email.split('@')[1]

    print('Username : ', username)
    print('Domain   : ', domain)
email_splitter(input("Enter your email address:"))
