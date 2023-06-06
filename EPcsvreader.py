""" authors: sarah konrad, jingyun liu data+ 2023.
EPcsvreader.py takes the EP metadata CSV spreadsheet and identifies
relevant texts for processing based off the keywords inputted.
The spreadsheet this was read off of was EP_availabletexts_1590-1639"""

import csv

def stringSearch(inputString, keyword):
    if keyword in inputString.lower():
        return True
    return False
def readEPcsv(inputFile, inputWords):
    relevantIDs = []
    #for some reason the code would not work without the following line
    #we suspect it is due to the fact keywords was read as a string from the terminal
    #and not a list
    keywords = inputWords.split(',')
    with open(inputFile, encoding = "utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        lineCount = 0
        for row in csv_reader:
            if lineCount == 0:
                lineCount += 1
            elif lineCount != 0:
                for word in keywords:
                    if stringSearch(str(','.join(row)), word) == True:
                        relevantIDs.append(row[0])
            lineCount += 1
    IDset = set(relevantIDs)
    return keywords, len(IDset), IDset

if __name__ == '__main__':
    inputFile = input("Enter the name of the CSV to be searched: ")
    inputWords = input("Enter the list of keywords to be searched (all lowercase): ")
    print(readEPcsv(inputFile, inputWords))