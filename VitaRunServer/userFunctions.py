import json
import os
import errno
import datetime
import csv
import numpy as np
import pandas as pd


now = datetime.datetime.now()

post_data = {

    'StartDateTime': '08011997:1345',
    'P1': 1,
    'P2': 14,
    'P3': 25,
    'P4': 1,
    'P5': 1,
    'P6': 25,
}
details = {

    'Name': 'Mila',
    'Username': "Mila123",
    'Password': 789,
    'Age': 89,
}

username = "Mila" #put username into there
filename = now.strftime("%Y-%m-%d %H:%M:%S") + ".csv"
file_path = "/Users/mila/Bioengineering_Year_4/MHML/pronation_classification/VitaRunServer/userProfiles/"
directory = os.path.dirname(file_path)


def createFiles(Username, Password, Name, Age, Weight):
    
    # if this username already exists, return 0
    if not os.path.isdir(directory+ '/'+ Username):
        os.makedirs(directory + '/'+ Username + '/' )
        os.makedirs(directory + '/'+ Username + '/' + 'temp/')

        with open(directory+ '/' + Username + '/'+ 'info.csv', 'wt', newline ='') as file:
            header = ['Name', 'Username', 'Password', 'Weight', 'Age']
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
            newLogin = [Name, Username, Password, Weight, Age]
            writer = csv.writer(file)
            writer.writerow(newLogin)

        with open(directory+ '/' + Username + '/History.csv', 'wt', newline ='') as file:
            header = ['DateTime_Start', 'DateTime_End', 'Number_Of_Steps','Count_NP','Count_OP','Count_UP','Average_Frequency']
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()

        with open(directory+ '/' + Username + '/'+ 'temp/frequencyRunData.csv', 'wt', newline ='') as file:
            file.close()

        with open(directory+ '/' + Username + '/'+ 'temp/pronationRunData.csv', 'wt', newline ='') as file:
            file.close()

        with open(directory+ '/'+ 'Login.csv', 'a', newline ='') as file:
            newLogin = [Username, Password]
            writer = csv.writer(file)
            file.write('\n')
            writer.writerow(newLogin)
            
        return True
    return False


def getPassword():
    with open(directory+ '/' + username + '/'+ 'info.csv') as fin:
        df = pd.read_csv(fin)
        fin.close()


def addFreq(username, num):
    with open(directory+ '/' + username + '/'+ 'temp/frequencyRunData.csv', 'a', newline ='') as outputFile:
        writer = csv.writer(outputFile)
        writer.writerow([num])


def addPronation(username, num):
    print(type(num[1]))
    with open(directory+ '/' + username + '/'+ 'temp/pronationRunData.csv', 'a', newline ='') as outputFile:
        writer = csv.writer(outputFile)
        for i in range(0,len(num)):
            y = num[i]
            writer.writerow(y)


def averageFreq(username):
    with open(directory+ '/' + username + '/temp/frequencyRunData.csv') as fin:
        # fin.next()
        total = sum(int(r[0]) for r in csv.reader(fin))
        return total


def totalSteps():
    with open(directory+ '/' + username + '/'+ 'History.csv') as fin:
        df = pd.read_csv(fin)
        totalSteps = sum(df['Number_Of_Steps'])
        print(totalSteps)


def count_NP_last5(username):
    with open(directory+ '/' + username + '/'+ 'History.csv') as fin:
        df = pd.read_csv(fin)
        length=len(df)
        # for x in range(length-5, length):
        count_NP_last5 = df['Count_NP']
        test = count_NP_last5[length-5:length]
        sum1 = sum(test)
        return sum1

def count_OP_last5(username):
    with open(directory+ '/' + username + '/'+ 'History.csv') as fin:
        df = pd.read_csv(fin)
        length=len(df)
        # for x in range(length-5, length):
        count_NP_last5 = df['Count_OP']
        test = count_NP_last5[length-5:length]
        sum1 = sum(test)
        return sum1

def count_UP_last5(username):
    with open(directory+ '/' + username + '/'+ 'History.csv') as fin:
        df = pd.read_csv(fin)
        length=len(df)
        # for x in range(length-5, length):
        count_NP_last5 = df['Count_UP']
        test = count_NP_last5[length-5:length]
        sum1 = sum(test)
        return sum1

def pronation(Username):
    NP = count_NP_last5(Username)
    OP = count_OP_last5(Username)
    UP = count_UP_last5(Username)
    if NP>OP:
        if NP>UP:
            return 'NP'
        else:
            return 'UP'
    else:
        if OP>UP:
            return 'OP'
        else:
            return 'UP'




def writeHistory(Username,DateTime_Start, DateTime_End, Number_Of_Steps,Count_NP,Count_OP,Count_UP):
    averageFreqency = averageFreq(Username)
    with open(directory+ '/' + Username + '/'+ 'History.csv','a') as fin:
        newEntry = [DateTime_Start, DateTime_End, Number_Of_Steps,Count_NP,Count_OP,Count_UP,averageFreqency]
        writer = csv.writer(fin)
        writer.writerow(newEntry)
        return True


def login(Username, Password):
    with open(directory+ '/' + 'Login.csv') as fin:

        df = pd.read_csv(fin)
        length=len(df)
        # print(df)
        column_of_interest = df["Username"]
        password_of_interest = df["Password"]
        # print(column_of_interest)
        for x in range(0, length):
            if column_of_interest[x] in Username:
                if str(password_of_interest[x]) in Password:
                    return True
                else:
                    return False


def checkUsername(Username):
    with open(directory+ '/' + 'Login.csv') as fin:
        df = pd.read_csv(fin)
        # print(df)
        length=len(df)
        # print(Username)
        column_of_interest = df["Username"]
        for x in range(1, length):
            if column_of_interest[x] == Username:
                print("good")


def setUserDetails(Username, Password, Name, Age, Weight):
    os.remove(directory + '/'+ Username + '/' + 'info.csv')

    with open(directory + '/'+ Username + '/' + 'info.csv','a') as fin:
        header = ['Name', 'Username', 'Password', 'Weight', 'Age']
        writer = csv.DictWriter(fin, fieldnames=header)
        writer.writeheader()
        newLogin = [Name, Username, Password, Weight, Age]
        writer = csv.writer(fin)
        writer.writerow(newLogin)



def getUserDetails(username):
    with open(directory+ '/' + username + '/'+ 'info.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            elif line_count == 1:
                historyDict = {'Name': row[0], 'Username': row[1], 'Password': row[2], 'weight': row[3], 'Age': row[4]}
                return historyDict


def startRun(Username):
        os.remove(directory + '/'+ Username + '/' + 'temp/frequencyRunData.csv')
        with open(directory+ '/' + Username + '/'+ 'temp/frequencyRunData.csv', 'wt', newline ='') as file:
            file.close()
        os.remove(directory + '/'+ Username + '/' + 'temp/pronationRunData.csv')
        with open(directory+ '/' + Username + '/'+ 'temp/pronationRunData.csv', 'wt', newline ='') as file:
            file.close()


def readHistoryFile(Username):

    with open(directory+ '/' + Username + '/'+ 'History.csv') as csv_file:
        df = pd.read_csv(csv_file)
        length=len(df)
        csv_file.close()
    with open(directory+ '/' + Username + '/'+ 'History.csv') as csv_file:

        csv_reader = csv.reader(csv_file, delimiter=',')

        line_count = 0

        for row in csv_reader:

            if line_count == 0:

                line_count += 1
            elif line_count == 1:
                historyDict = {'DateTime_Start': row[0], 'DateTime_End': row[1], 'Number_Of_Steps': row[2],'Count_NP': row[3],'Count_OP': row[4],'Count_UP': row[5],'averageFreqency': row[6]}
                line_count += 1
            else:
                historyDict.append({'DateTime_Start': row[0], 'DateTime_End': row[1], 'Number_Of_Steps': row[2],'Count_NP': row[3],'Count_OP': row[4],'Count_UP': row[5],'averageFreqency': row[6]})
                test = json.dumps(myDict)

        return historyDict, length


def readPronation(Username):
    with open(directory+ '/' + Username + '/'+ 'temp/pronationRunData.csv') as csv_file:

        csv_reader = csv.reader(csv_file, delimiter=',')

        line_count = 0

        for row in csv_reader:

            if line_count == 0:
                dictPronation = {'Pronation': [{'Pronation':row[0]}]}
                line_count += 1

            else:
                dictPronation['Pronation'].append(({'Pronation':row[0]}))
                test = json.dumps(dictPronation)

        return dictPronation


def readFrequency(Username):
    with open(directory+ '/' + Username + '/'+ 'temp/frequencyRunData.csv') as csv_file:

        csv_reader = csv.reader(csv_file, delimiter=',')

        line_count = 0

        for row in csv_reader:

            if line_count == 0:

                line_count += 1
            elif line_count == 1:

                dictPronation = {'Frequency': [{'Frequecy':row[0]}]}

                line_count += 1
            else:
                dictPronation['Frequency'].append(({'Frequecy':row[0]}))
                test = json.dumps(dictPronation)

        return dictPronation
