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

print(type(post_data))

# print(now.strftime("%Y-%m-%d %H:%M:%S"))






username = "Jonny" #put username into there


filename = now.strftime("%Y-%m-%d %H:%M:%S") + ".csv"

file_path = "/Users/jonathanmidgen/Documents/GitHub/MHML_old/VitaRunServer/"
directory = os.path.dirname(file_path)

def createFiles(Username, Password, Name, Age, Weight):

    if not os.path.isdir(directory+ '/'+ Username):
        os.makedirs(directory + '/'+ Username + '/' )
        os.makedirs(directory + '/'+ Username + '/' + 'temp/')

        with open(directory+ '/' + Username + '/'+ 'info.csv', 'wt', newline ='') as file:
            header = ['Name', 'Username', 'Password', 'Weight', 'Age']
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
            newLogin = [Name, Username, Password, Weight, Age]
            print(newLogin)
            writer = csv.writer(file)
            file.write('\n')
            writer.writerow(newLogin)
            print(newLogin[0])

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
            print(newLogin)
            writer = csv.writer(file)
            file.write('\n')
            writer.writerow(newLogin)
            print(newLogin[0])
        return 1
    return 0


def getPassword():
    with open(directory+ '/' + username + '/'+ 'info.csv') as fin:
        df = pd.read_csv(fin)
        fin.close()


def addFreq(username, num):
    with open(directory+ '/' + username + '/'+ 'temp/frequencyRunData.csv', 'a', newline ='') as outputFile:
        writer = csv.writer(outputFile)
        writer.writerow([num])

def addPronation(username, num1, num2, num3, num4, num5, num6):
    with open(directory+ '/' + username + '/'+ 'temp/pronationRunData.csv', 'a', newline ='') as outputFile:
        writer = csv.writer(outputFile)
        writer.writerow([num1])
        writer.writerow([num2])
        writer.writerow([num3])
        writer.writerow([num4])
        writer.writerow([num5])
        writer.writerow([num6])

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


def count_NP_last5():
    with open(directory+ '/' + username + '/'+ 'History.csv') as fin:
        df = pd.read_csv(fin)
        length=len(df)
        for x in range(length-5, length):
            count_NP_last5 = df[1:7]
            print(count_NP_last5)


def writeHistory(Username,DateTime_Start, DateTime_End, Number_Of_Steps,Count_NP,Count_OP,Count_UP):
    averageFreqency = averageFreq(Username)
    with open(directory+ '/' + Username + '/'+ 'History.csv','a') as fin:
        newEntry = [DateTime_Start, DateTime_End, Number_Of_Steps,Count_NP,Count_OP,Count_UP,averageFreqency]
        writer = csv.writer(fin)
        writer.writerow(newEntry)
        return 1


def login(Username, Password):
    with open(directory+ '/' + 'Login.csv') as fin:
        print(Username)
        print(Password)
        df = pd.read_csv(fin)
        length=len(df)
        # print(df)
        column_of_interest = df["Username"]
        password_of_interest = df["Password"]
        # print(column_of_interest)
        for x in range(0, length):
            if column_of_interest[x] in Username:
                print('test1')
                if str(password_of_interest[x]) in Password:
                    print('test2')
                    return 1
                else:
                    return 0


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
    os.remove(directory + '/'+ username + '/' + 'info.csv')

    with open(directory + '/'+ username + '/' + 'info.csv','a') as fin:
        header = ['Name', 'Username', 'Password', 'Weight', 'Age']
        writer = csv.DictWriter(fin, fieldnames=header)
        writer.writeheader()
        newLogin = [Name, Username, Password, Weight, Age]
        print(newLogin)
        writer = csv.writer(fin)
        fin.write('\n')
        writer.writerow(newLogin)
        print(newLogin[0])


def getUserDetails(username):
    with open(directory + '/'+ username + '/' + 'info.csv') as fin:
        df = pd.read_csv(fin, skiprows=0)
        return df



def writeJsonToFile():

    inputFile= list(post_data.values())
    print(inputFile)

    # inputFile =  json.dumps(post_data.values())#open json file
    with open(directory + '/' + username + '/History.csv', 'a') as outputFile:#load csv file
        writer = csv.writer(outputFile)
        writer.writerow(inputFile)
        print(inputFile[0])


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
                historyDict = {'History': [{'DateTime_Start': row[0], 'DateTime_End': row[1], 'Number_Of_Steps': row[2],'Count_NP': row[3],'Count_OP': row[4],'Count_UP': row[5],'averageFreqency': row[6]}]}
                line_count += 1
            else:
                historyDict['History'].append(({'DateTime_Start': row[0], 'DateTime_End': row[1], 'Number_Of_Steps': row[2],'Count_NP': row[3],'Count_OP': row[4],'Count_UP': row[5],'averageFreqency': row[6]}))
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





                # print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                # data['DateTime_Start'] = row[0]
                # data['DateTime_End'] = row[1]
                # data['Number_Of_Steps'] = row[2]
                # data['Count_NP'] = row[3]
                # data['Count_OP'] = row[4]
                # data['Count_UP'] = row[5]
                # data['averageFreqency'] = row[6]
                # json_data = json.dumps(data)

        # print(f'Processed {line_count} lines.')



    # f = open( directory+ '/' + Username + '/'+ 'History.csv' , 'rU' )
    # reader = csv.DictReader( f, fieldnames = ("DateTime_Start","DateTime_End","Number_Of_Steps", "Count_NP","Count_OP","Count_UP","averageFreqency"))
    # store = []
    # framenames = []





    # with open(directory + '/'+ username + '/' + 'info.csv') as fin:
    #     reader = csv.reader(fin)
    #     field_names_list = next(reader)
    #     print(field_names_list)
    #      # print ('{0}'.format(fin.readline().split()))
    #      # line = fin.readline()
    #      # print(line)
    #      # print('test')
    #      # for x in fin:
    #      #        x=x.split()
    #      #        # print ('{0}'.format(x[0],sum(map(int,x[1:]))))
    #      #        line = fin.readline()

















# createFiles('Jonny1', 'let me in', 'Midge','22','1333')

# writeJsonToFile()

# array()

# addFreq('Jonny1', 199)

# totalAV = averageFreq()
# print(totalAV)

# totalSteps()

# addPronation('Jonny1', 2, 2, 2, 1, 1, 1)

# count_NP_last5()

# getPassword()

# User = 'jacob'
# p = 'hi4'
# test = login(User,p)
# print(test)

# checkUsername('Jonny1')

# setUserDetails('Jonny123', 'test', 'hello', '23', '12')

# test = getUserDetails('Jonny1')
# print(test)

# time =now.strftime("%Y-%m-%d %h:%m:%s")



# Username = 'Jonny1'
# DateTime_Start = '28'
# DateTime_End = '29'
# Number_Of_Steps = '30394'
# Count_NP = '655'
# Count_OP = '2948'
# Count_UP = '4444'
# writeHistory(Username,DateTime_Start, DateTime_End, Number_Of_Steps,Count_NP,Count_OP,Count_UP)
# print(now.strftime("%Y-%m-%d %H:%M:%S"))

#
# df,length = readHistoryFile('Jonny1')
# print(df)
# print(length)

# startRun('Jonny1')

# test = readPronation('Jonny1')
# print(test)

# test = readFrequency('Jonny1')
# print(test)

# #
#
#
# new login
# login
# start run
# end run
#
#
#























# def array():
#     print(a)
#     np.savetxt('array.txt', a, fmt='%s')

    # inputFile = list(post_data.values())
    # a[3]=a[2]
    # a[2]=a[1]
    # a[1]=a[0]
    # a[0] = inputFile[1], inputFile[2], inputFile[3], inputFile[4], inputFile[4], inputFile[6]
    # print(a)







#with open('newpath','w') as f: #open the new path file as f

#    json.dump(post_data, f) #then dump the data into the file

#print('done')





    # f.close()
    # f.writerow(["datetime", "P1", "P2", "P3"])
    #
    # for x in x:
    #     f.writerow([x["datetime"],
    #                 x["P1"],
    #                 x["P2"],
    #                 x["P3"],
    #                 ])
    # with open('./' + username + '/'+ filename, 'wb') as outcsv:
    #     f = csv.writer(outcsv)
    #     f.writerow(["Date", "P1", "P2", "P3"])
    #
    #     with open('t1.csv', 'rb') as incsv:
    #         reader = csv.reader(incsv)
    #         writer.writerows(row + [0.0] for row in reader)
    #
    #     with open('t2.csv', 'rb') as incsv:
    #         reader = csv.reader(incsv)
    #         writer.writerows(row[:1] + [0.0] + row[1:] for row in reader)
    #     # f.write(json.dumps(post_data, indent=2))


        # for j in some_list:
        #     writer.writerow(j)
    # f.close()




# open the file and read the json packages within the file

    # fh = open('./' + username + '/'+ filename, 'r')
    #
    #
    # json_str = fh.read()
    #
    # json_value = json.loads(json_str)
    #
    # print(json_value['runNumber'])
    #
    # with open(r'./' + username + '/'+ filename,'a') as csvfile:
    #     newfile = csv.write(csvfile)
    #     newfile.writerow([])



    #print(json_value([runNumber]))


    #newpath = os.path.expanduser('~/Users/jonathanmidgen/Documents/MHML/newpath')

    #if not os.path.exists(newpath): #see if the file exists

    #os.makedirs("newpath") # if it doesnt then create it

    #filename = "newpath"

    #if not os.path.exists(os.path.dirname(filename)):

    #    try:
    #        os.makedirs(filename)

    #    except OSError as exc:
    #        if exc.errno != errno.EEXIST:

    #            raise


    #with open(filename,"w") as f:

    #    f.write("Hello")


    # data = jso(inputFile) #load json content

    # inputFile.close() #close the input file

    # output = csv.writer(outputFile) #create a csv.write
    #
    # # output.writerow(inputFile[0].keys())  # header row
    #
    #
    # outputFile.writerow([inputFile["datetime"],
    #             inputFile["P1"],
    #             inputFile["P2"],
    #             inputFile["P3"],
    #             inputFile["P4"],
    #             inputFile["P5"],
    #             inputFile["P6"]])
    #
    # fh.close()




# def readJsons():

    # fh = open('./' + username + '/'+ filename, 'r')
    #
    # f = csv.writer(open('./' + username + '/'+ filename , "wb+"))
    # f.writerow(["datetime", "P1", "P2", "P3"])
    #
    # for x in x:
    # f.writerow([x["pk"],
    #             x["model"],
    #             x["fields"]["codename"],
    #             x["fields"]["name"],
    #             x["fields"]["content_type"]])
