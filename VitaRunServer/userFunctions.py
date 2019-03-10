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


filename = now.strftime("%Y-%m-%d %h:%m:%s") + ".csv"

file_path = "/Users/mila/Bioengineering_Year_4/MHML/pronation_classification/VitaRunServer/"
directory = os.path.dirname(file_path)
def createFiles(Username, Password):
    # print(Username)
    # print(Password)

# create a file name and file and put the json into the file
    # file_path = "/Users/jonathanmidgen/Documents/GitHub/MHML_old/VitaRunServer/"
    # directory = os.path.dirname(file_path)
    if not os.path.isdir(directory+ '/'+ Username):
        os.makedirs(directory + '/'+ Username + '/' )
        os.makedirs(directory + '/'+ Username + '/' + 'temp/')

        # f = csv.writer(open(directory+ '/' + username + '/'+ 'info' , "w"))

        with open(directory+ '/' + Username + '/'+ 'info.csv', 'wt', newline ='') as file:
            header = ['Name', 'Username', 'Password', 'Age']
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
        with open(directory+ '/' + Username + '/History.csv', 'wt', newline ='') as file:
            header = ['DateTime_Start', 'DateTime_End', 'Number_Of_Steps','Count_NP','Count_OP','Count_UP','Average_Frequency']
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()


        with open(directory+ '/' + Username + '/'+ 'temp/frequecyRunData.csv', 'wt', newline ='') as file:
            header = ['DateTime Start', 'DateTime End', 'Number Of Steps','Count NP','Count OP','Count UP','Average Frequency']
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()


        with open(directory+ '/'+ 'Login.csv', 'a', newline ='') as file:
            newLogin = [Username, Password]
            print(newLogin)
            writer = csv.writer(file)
            file.write('\n')
            writer.writerow(newLogin)
            print(newLogin[0])
                # fd.write(myCsvRow)
        #     header = ['Username', 'Password']
        #     writer = csv.DictWriter(file, fieldnames=header)
        #
        #     newLogin = [Username, Password]
        #     writer.writeheader()
        #     print(type(newLogin))
        #     print('hello')

        # with open(directory + '/'+'Login.csv', 'a',newline ='') as outputFile:#load csv file
        #     writer = csv.writer(outputFile)
        #     writer.writerow(newLogin)
        #     print(newLogin[0])
        #     # fd.write(myCsvRow)





        # fh = open('./'+ username + '/'+ filename,'w')

        # f = csv.writer(open(directory+ '/' + Username + '/History.csv' , "w"))
        # header = ['DateTime_Start', 'DateTime_End', 'Number_Of_Steps','Count_NP','Count_OP','Count_UP','Average_Frequency']





    #
    # f = csv.writer(open(directory+ '/' + username + '/'+ filename , "w"))
    # header = ['DateTime Start', 'DateTime End', 'Number Of Steps','Count NP','Count OP','Count UP','Average Frequency']
    # some_list = [1, 2, 3, 4, 5, 6]
    # with open(directory+ '/' + username + '/'+ filename, 'wt', newline ='') as file:
    #     writer = csv.writer(file, delimiter=',')
    #     writer.writerow(i for i in header)
    #     for '0' in file:
    #         writer.writerow(4)


def getPassword():
    with open(directory+ '/' + username + '/'+ 'info.csv') as fin:
        df = pd.read_csv(fin)


def addFreq(num):
    num
    with open(directory+ '/' + username + '/'+ 'temp/frequecyRunData.csv', 'a', newline ='') as outputFile:
        writer = csv.writer(outputFile)
        writer.writerow([num])


def averageFreq():
    with open(directory+ '/' + username + '/'+ 'temp/frequecyRunData.csv') as fin:
        # fin.next()
        total = sum(int(r[0]) for r in csv.reader(fin))
        print(total)




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







def login(Username, Password):
    with open(directory + '/' + 'Login.csv') as fin:
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
                if str(password_of_interest[x]) in Password:
                    return 1
                else:
                    return 0












def checkUsername(Username):
    with open(directory+ '/' + 'info.csv') as fin:
        df = pd.read_csv(fin)
        print(df)
        length=len(df)
        print(Username)
        column_of_interest = df["Username"]
        for x in range(1, length):
            if column_of_interest[x] == Username:
                print("good")





def setUserDetails():
    inputFile= list(details.values())
    print(inputFile)

    with open(directory + '/'+ username + '/' + 'info.csv','a') as fin:
        writer = csv.writer(fin)
        writer.writerow(inputFile)
        print(inputFile[0])




def getUserDetails():

    with open(directory + '/'+ username + '/' + 'info.csv') as fin:
         print (''.format(fin.readline().split()))
         line = fin.readline()
         print(line)
         for x in fin:
                x=x.split()
                # print ('{0}'.format(x[0],sum(map(int,x[1:]))))
                line = fin.readline()





def writeJsonToFile():

    inputFile= list(post_data.values())
    print(inputFile)

    # inputFile =  json.dumps(post_data.values())#open json file
    with open(directory + '/' + username + '/History.csv', 'a') as outputFile:#load csv file
        writer = csv.writer(outputFile)
        writer.writerow(inputFile)
        print(inputFile[0])











#createFiles('jacob', 'hi4')

# writeJsonToFile()

# array()

# addFreq(1)

# averageFreq()

# totalSteps()

# count_NP_last5()

# getPassword()
#User = 'jacob'
#p = 'hi4'
#test = login(User,p)
#print(test)
# # checkUsername('Mila')

# setUserDetails()

# getUserDetails()









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