import time
import getpass
import urllib2
import os
import os.path
import socket
import platform
import json
import base64

def login():
    #print("this is a process")
    name = raw_input("Name: ")
    password = getpass.getpass("password: ")
    with open("D://test.txt") as file:
        data = json.load(file)
        for user in data["user"]:
            getPassword = base64.b64decode(user["password"])
            if name == user["name"] and password == getPassword:
                print "this was nice"
                process()
            else:
                print "not so nice"
                print
                login()

def changePassword():
    print "Before Name or Password can be changed"
    print "Your current identity has to be confirmed"
    name = raw_input("Name: ")
    password = getpass.getpass("password: ")
    with open("D://test.txt") as file:
        data = json.load(file)
        for user in data["user"]:
            getPassword = base64.b64decode(user["password"])
            if name == user["name"] and password == getPassword:
                newName = raw_input("new Name: ")
                newPassword = getpass.getpass("new password: ")
                newPassword = base64.b64encode(newPassword)
                data.append({
                    "name" : newName,
                    "password" : newPassword
                })
    with open("D://test.txt", "w+") as file:
        json.dump(data, file)


    #    login()
def GetSystemInformation():
    print("Your OS is " + platform.system()+" "+ platform.release())
    print("Your machine name is " + platform.machine())
    print("The version is " + platform.version())
    print(platform.processor())
    print("The platform is " + platform.platform())


def CheckInternetConnection():
    for timeout in [1,5,10,15]:
        try:
            #print("checking internet.....")
            socket.setdefaulttimeout(timeout)
            host = socket.gethostbyname("www.google.com")
            s = socket.create_connection((host, 80), 2)
            s.close()
            print "I know you are connected to the internet"
            print
            return True
        except Exception,e:
            print "I know you are not connected to the intenet"
            print
            return False
def opening():
#remove("D://test.txt")
    print("=====================================================================================================")
    print("=====================================================================================================")
    #time.sleep(2)
    print("                                          Yourfriend                                                 ")
    print("                                              by                                                     ")
    print("                                         Jason Millsom                                               ")
    #time.sleep(2)
    print("=====================================================================================================")
    print("=====================================================================================================")
    print
    print
    print
    time.sleep(1)

def Introduction():
    data = {}
    data["user"] = []
    print
    print("Hello")
    time.sleep(2)
    print("I am your friend")

    name = raw_input("What is your name? ")
    print("Hi " + name)
    print
    time.sleep(3)
    print(name + ", you will also need to set a password")
    password = getpass.getpass("Set password: ")
    password = base64.b64encode(password)

    data["user"].append({
        "name": name,
        "password": password
    })

    with open("D://test.txt", "w+") as file:
        json.dump(data, file)

    print

    time.sleep(3)
    print("This is a system which is designed to be someone you can talk to")
    time.sleep(1)
    print("I can also analyze your Computer and some more dank shit")
    print("for example")
    print
    time.sleep(1)

    CheckInternetConnection()

    print("I also know you are using " + platform.system()+" "+ platform.release())
    print

    file = open("D://Introduction.txt", "w+")
    file.write("Introduction Process has been complete")
    file.close()

def process():
    commands = {

    }

    for command in commands:
        print command
    print
    input = raw_input("Command: ")

    if input == "GetSystemInformation":
        print
        GetSystemInformation()


opening()

if os.path.isfile("D://Introduction.txt"):
    login()
    process()
else:
    Introduction()
    process()
