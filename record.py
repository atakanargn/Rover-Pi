from time import sleep
from motor import *
import csv
from os import system

def kaydet(komut,hiz):
    with open('kayit.csv', 'a+') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow([komut,hiz])

def sonSil():
    system("rm -rf kayit.csv")

def oynat():
    with open('kayit.csv', 'r') as f:
        reader = csv.reader(f)
        adimlar=[]
        for row in reader:
            adimlar.append(row)
        
        for adim in adimlar:
            setSpeed(float(adim[1]))
            if(adim[0]=="duz"):
                goForward()
                sleep(1.5)
                engineWait()
            elif(adim[0]=="sol"):
                turnLeft()
                engineWait()
            elif(adim[0]=="sag"):
                turnRight()
                engineWait()