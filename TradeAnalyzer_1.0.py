import os
#This program filter a *.csv file with a specific keyword
Version = 1.0

#User enter here a path to the file
while True:
    print('Enter a path to the file:')
    file_read = input()
    if file_read == 'exit':
        exit()
    elif os.path.exists(file_read) == False: #Program checking if the file exist.
        print('Enter a correct path. Try again, or type "exit" to exit program.')
    else:
        break


file = os.path.basename(file_read) #Program saving a path to this file

namefile = file.split('.') #Program saving a name of file

file_write = os.path.dirname(file_read) + '\\' + namefile[0] +"_new.csv" #Program saving a new file with same name of
                                                                # input file form user
data = [] #Temporary data of whole contet of file
filter = [] #Variable for lins with keyword
count = 0 # program will count how many lines have a keyword

print('Enter a looking keyword:') #User define a looking keyword
find = input()

#Program opening a file and reading it
with open (file_read, 'r', encoding="utf8") as file:
    for line in file:
        data.append(line) #Program input all data to variable 'data'
        smallLetrers = line.lower() #Program chaning all letters to lower to easer find a keyword
        if smallLetrers.find(find.lower()) > 0: #Program find a looking keayword and saving it
            filter.append(line) #Program input looking line with keyword to variable 'line'
            count+=1 #program count line with keyword


#Program write all what it find to new file
fw = open(file_write, 'w')
fw.write(data[0]) # Program alawyas input a first line which one is a base
for line in filter:
    if line != data[0]: #If keyword is the same like in base it skip it
        fw.write(line) #Else it writhe to new file
fw.close()

print('Program found %d line/s with keyword "%s".\n' %(count, find))
print('New data saved in %s' % (file_write))
