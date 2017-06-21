#########################################################################
#    USAGE: python3 main.py                                             #
#                                                                       #
#    MAKE SURE YOU USE PYTHON3 OTHERWISE YOU'RE GOING TO GET ERRORS!	#
#                                                                       #
#########################################################################

# from keypad import *
from on_off import *
from rpiCardScan import *
import sql
import time
import signal
import sys
import pymysql
import datetime
import os

if __name__ == '__main__':
    # initialize the keypad and important variables
    ID = None
    powerIsOn = False
    db = sql.SQL()

    # While the same card is still being read then do the following:
    # ask for PIN and search the SQL database to find the user
    while True:
        holdID = ID = RPICardScan()
        while (ID == holdID and holdID != None and holdID[0:5] == "02350"):
            if(db.isUserAuthorized(ID) == True and not powerIsOn):
                TurnPowerOn(ID)
                powerIsOn = True

            ID = RPICardScan()

        if(powerIsOn):
            TurnPowerOff(ID)
            powerIsON = False
