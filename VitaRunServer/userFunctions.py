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
        return totalSteps
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
<<<<<<< HEAD
    with open(directory+ '/' + username + '/'+ 'History.csv') as fin:
        df = pd.read_csv(fin)
        length=len(df)
        # for x in range(length-5, length):
        count_NP_last5 = df['Count_OP']
        test = count_NP_last5[length-5:length]
        sum1 = sum(test)
        return sum1

def count_UP_last5(username):
=======
>>>>>>> f891300811a1954b8edd7e69a7bab03d8cee834d
    with open(directory+ '/' + username + '/'+ 'History.csv') as fin:
        df = pd.read_csv(fin)
        length=len(df)
        # for x in range(length-5, length):
<<<<<<< HEAD
=======
        count_NP_last5 = df['Count_OP']
        test = count_NP_last5[length-5:length]
        sum1 = sum(test)
        return sum1

def count_UP_last5(username):
    with open(directory+ '/' + username + '/'+ 'History.csv') as fin:
        df = pd.read_csv(fin)
        length=len(df)
        # for x in range(length-5, length):
>>>>>>> f891300811a1954b8edd7e69a7bab03d8cee834d
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
#        return True


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
<<<<<<< HEAD
                if str(password_of_interest[x]) in Password:
                    return True
=======

                print('test1')
                if str(password_of_interest[x]) in Password:
                    return 1
>>>>>>> f891300811a1954b8edd7e69a7bab03d8cee834d
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

<<<<<<< HEAD

=======
def writeJsonToFile():
>>>>>>> f891300811a1954b8edd7e69a7bab03d8cee834d

def getUserDetails(username):
    with open(directory+ '/' + username + '/'+ 'info.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            elif line_count == 1:
                historyDict = {'name': row[0], 'username': row[1], 'password': row[2], 'weight': row[3], 'age': row[4]}
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
<<<<<<< HEAD
=======





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
# x = ['2', '2','2','1','1']
# addPronation('Jonny1', x)

# count_NP_last5('Jonny1')

test = pronation('Jonny1')
print(test)
# getPassword()

# User = 'jacob'
# p = 'hhi4'
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
# Number_Of_Steps = '6'
# Count_NP = '5'
# Count_OP = '2'
# Count_UP = '7'
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
>>>>>>> f891300811a1954b8edd7e69a7bab03d8cee834d
