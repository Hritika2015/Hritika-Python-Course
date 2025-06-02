import random
import time
def getRandomDate(startDate, endDate):
    print("Mrs. Sheha needs to go to work again, she needs to go to work at", endDate)
    dateFormat = '%m/%d/%Y

    startTime = time.mktime(time.strptime(startDate, dateFormat))
    endTime = time.mktime(time.strptime(endDate, dateFormat))
# Generate a random time between start and end
    randomTime = startTime + random.random() * (endTime - startTime)
# Convert timestamp back to a readable date
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate
# Call the function
print("Random Date = ", getRandomDate("1/1/2016", "12/12/2018"))