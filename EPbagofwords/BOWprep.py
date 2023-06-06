"""author: sarah konrad, data+ 2023

bowprep.py cleans body texts extracted from EP (not EEBO) TCP files that have
already been VEP processed to remove variant accents on characters and ampersands.EP files
are also partially lemmatized and standardized.


bowprep.py lowercases all words, strips of punctuation, and removes all numbers.
carots are kept, as those inside words are necessary for further lemmatization.
"""
import re, os

def replaceNonsense(text):
    #removes structural garbage from files including *, (@), ., and numbers
    structural_garbage = ["(@)", "@", ".", "(...)", "*", "1", "2", "3",
    "4", "5", "6", "7", "8", "9", "0"]
    for trash in structural_garbage:
        text = text.replace(trash, "")
    return text

def readandConvert(file, outputFolder):
    # takes text.py cleaned (initially VEP processed) texts and returns them in BOW format
    name = os.path.basename(file)
    with open(file, encoding="utf-8") as EPextracted:
        with open(os.path.join(outputFolder, name + '.txt'), 'w+') as lowerFile:
            data = EPextracted.read()
            data = replaceNonsense(data)
            lowerFile.write(data.lower())
    return lowerFile

if __name__ == '__main__':
    inputFolder = input("Enter what folder of files need to be converted: ")
    outputFolder = input("Enter folder for converted files: ")
    for file in os.scandir(inputFolder):
        readandConvert(file, outputFolder)


