from email import message
#from colorama import Fore, Back, Style
from selenium import webdriver
from mailtm import Email
from win10toast import ToastNotifier
import subprocess
import socket
import time
import os

subprocess.call('cls', shell=True)

print("""
    ____        __           _         
   / __ \____  / /___ ______(_)____    
  / /_/ / __ \/ / __ `/ ___/ / ___/ version 1.1
 /_/    \____/_/\__,_/_/  /_/____/  Dev by xxxx

 [*] Create unlimited shodan free accounts :)
""")

def polaris_registration():
    
    username_registration_username = input(" username : ")
    username_registration_password = input(" password : ")
    #username_registration_password_verif = input(" retype password : ")
    
    logins_informations = open("logins.txt", "w+")
    logins_informations.write(f'Username : {username_registration_username} Password : {username_registration_password}')
    logins_informations.close()

    listener = message
    
    def account_creation_choice():
    
        selection=int (input(" --> "))
        
        if selection==1:
            listener(message)
        else:
            print("")
            print("\n[!] Account has not been created.")

    def listener(message):
        print("")
        print("---------------------- INFOS ----------------------")
        print("[+] [Subject] " + message['subject'])
        print("[+] [Content] " + message['text'] if message['text'] else message['html'])
        print("---------------------------------------------------")
        print("")

    test = Email()

    test.register()
    print("\n[+] Email Adress: " + str(test.address))

    test.start(listener, interval=1)
    print("\n[%] Waiting for verification mail...")
    print("")

    driver_shodan_registration = webdriver.Chrome(executable_path="chromedriver.exe")
    driver_shodan_registration.get("https://account.shodan.io/register")

    shodan_registration_username = driver_shodan_registration.find_element_by_id("username")
    shodan_registration_username.send_keys(username_registration_username) 

    shodan_registration_password = driver_shodan_registration.find_element_by_id("password")
    shodan_registration_password.send_keys(username_registration_password) 

    shodan_registration_password_confirm = driver_shodan_registration.find_element_by_id("password_confirm")
    #shodan_registration_password_confirm.send_keys(username_registration_password_verif)
    shodan_registration_password_confirm.send_keys(username_registration_password)

    shodan_registration_password_confirm2 = driver_shodan_registration.find_element_by_id("email")
    shodan_registration_password_confirm2.send_keys(test.address)

    shodan_registration_button = driver_shodan_registration.find_element_by_class_name("button-primary")
    shodan_registration_button.click()

    driver_shodan_registration.get("https://account.shodan.io/login")

    shodan_registration_username2 = driver_shodan_registration.find_element_by_id("username")
    shodan_registration_username2.send_keys(username_registration_username)

    shodan_registration_password2 = driver_shodan_registration.find_element_by_id("password")
    shodan_registration_password2.send_keys(username_registration_password)

    toaster = ToastNotifier()
    toaster.show_toast("Polaris",
                   "Don't forget to activate your account before trying to login !",
                   duration=10)

    time.sleep(999999999999)
    
polaris_registration()
    

    
