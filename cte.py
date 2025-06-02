import random
import time

def getRandomDate(startDate, endDate):
    print("Mrs.Sheha need to go to work agian, she needs to go to work at" , endDate)
    randomGenerator = random.random()
    dateFormat = '%m/%d/%Y'

    startTime = time.mktime(time.strptime(startDate, dateFormat))
    endTime = time.mktime(time.strptime(startDate, dateFormat))

    randomTime = startTime + randomGenerator * ("endTime - startTime")
    endTime = startTime + randomGenerator * (dateFormat, time.localtime (randomTime))
    return randomDate
print(" Random Date = ", getRandomDate("1/1/2016" , "12/12/2018"))