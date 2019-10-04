#!/usr/bin/python
#
# Nikki Benoit
# Wed Aug 7 13:47 MDT 2017
#
# Send a message to the stdout every N seconds where N < 10 for
# a period of time <= 1hr
# Accept no. of seconds as well as the period.

import time

#Get Period of Time to transmit message from user
# Must not exceed 60 minutes
def getTimePeriod():

   period = int(input("Enter period of minutes to send message <= 60: "))

   if period > 60:
       print ("Too many minutes. Keep it under an hour!")
       getTimePeriod()
   else:
      return period

#Get Message Delay in Seconds from user
#Must not exceed 10 seconds
def getSeconds():

    delay = float(input("Enter second delay < 10: "))

    if delay >= 10:
        print ("Delay too long. Keep it under 10!")
        getSeconds()
    else:
        return delay

def main():

    periodOfTime = getTimePeriod() * 60     #Convert minutes to seconds
    periodOfDelay = getSeconds()

    while (periodOfTime > 0):               #Transmit up until Period
        time.sleep(periodOfDelay)           #Delay
        print "This message prints once per " + str(periodOfDelay) + " seconds"
        periodOfTime -= periodOfDelay - 1

if __name__ == '__main__':
  main()
