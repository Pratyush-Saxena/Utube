import requests
import time
import os
from threading import Thread

HOST=os.environ.get('HOST')
print("running HOST ",HOST)

#this function runs the main django server
def RunServer():
    os.system('python3 manage.py runserver '+HOST)


#this function calls the the loadvideo view function to load
# video in a database from youtube API after every 10 sec 
def APICaller():
    try:
        while(True):
            result=requests.get('http://'+HOST+'/loadvideo')
            time.sleep(10) #after every 10 sec API will be called
    except:
        print("error in calling api !!! , please check the server")

#Approch used here is multi threading to call the API
#asyncronously 
if __name__ == '__main__':
    Thread(target=RunServer).start()
    time.sleep(10) # waits for 10 sec in case server takes time for loading 
    Thread(target=APICaller).start()

    

