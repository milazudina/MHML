import json
import os
import errno
import datetime
import csv
import numpy as np


now = datetime.datetime.now()

post_data = {

    'StartDateTime': '08011997:1345',
    'P1': 1,
    'P2': 1,
    'P3': 25,
    'P4': 1,
    'P5': 1,
    'P6': 25,
}
print(type(post_data))
print(now.strftime("%Y-%m-%d"))






username = "test" #put username into there


filename = now.strftime("%Y-%m-%d") + ".csv"

file_path = "/Users/jonathanmidgen/Documents/GitHub/MHML_old/VitaRunServer/"
directory = os.path.dirname(file_path)
def createFiles():
# create a file name and file and put the json into the file
    # file_path = "/Users/jonathanmidgen/Documents/GitHub/MHML_old/VitaRunServer/"
    # directory = os.path.dirname(file_path)
    if not os.path.isdir(directory+ '/'+ username):
        os.makedirs(directory+ '/'+ username + '/' )

        # f = csv.writer(open(directory+ '/' + username + '/'+ 'info' , "w"))

        with open(directory+ '/' + username + '/'+ 'info.csv', 'wt', newline ='') as file:
            header = ['Name', 'Password', 'age']
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
        os.makedirs(directory+ '/'+ username + '/' + 'temp/')

        with open(directory+ '/' + username + '/'+ 'temp/frequecyRunData.csv', 'wt', newline ='') as file:
            # header = ['DateTime Start', 'DateTime End', 'Number Of Steps','Count NP','Count OP','Count UP','Average Frequency']
            writer = csv.DictWriter(file, fieldnames=header)
            # writer.writeheader()



        # fh = open('./'+ username + '/'+ filename,'w')

    f = csv.writer(open(directory+ '/' + username + '/'+ filename , "w"))
    header = ['DateTime Start', 'DateTime End', 'Number Of Steps','Count NP','Count OP','Count UP','Average Frequency']

    with open(directory+ '/' + username + '/'+ filename, 'wt', newline ='') as file:
        header = ['DateTime Start', 'DateTime End', 'Number Of Steps','Count NP','Count OP','Count UP','Average Frequency']
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()




    #
    # f = csv.writer(open(directory+ '/' + username + '/'+ filename , "w"))
    # header = ['DateTime Start', 'DateTime End', 'Number Of Steps','Count NP','Count OP','Count UP','Average Frequency']
    # some_list = [1, 2, 3, 4, 5, 6]
    # with open(directory+ '/' + username + '/'+ filename, 'wt', newline ='') as file:
    #     writer = csv.writer(file, delimiter=',')
    #     writer.writerow(i for i in header)
    #     for '0' in file:
    #         writer.writerow(4)




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








def writeJsonToFile():

    inputFile= list(post_data.values())
    print(inputFile)

    # inputFile =  json.dumps(post_data.values())#open json file
    with open(directory + '/' + username + '/' + filename, 'a') as outputFile:#load csv file
        writer = csv.writer(outputFile)
        writer.writerow(inputFile)
        print(inputFile[0])

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



# def array():
#     print(a)
#     np.savetxt('array.txt', a, fmt='%s')

    # inputFile = list(post_data.values())
    # a[3]=a[2]
    # a[2]=a[1]
    # a[1]=a[0]
    # a[0] = inputFile[1], inputFile[2], inputFile[3], inputFile[4], inputFile[4], inputFile[6]
    # print(a)

















# createFiles()

# writeJsonToFile()

# array()

# addFreq(15)

averageFreq()






















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
