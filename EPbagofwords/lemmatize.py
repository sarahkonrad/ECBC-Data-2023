"""author: sarah konrad, data+ 2023

lemmatize.py takes already standardized texts (run through standardizer.py) and lemmatizes them
using a dictionary of lemmas provided by the user.

it is recommended to run lemmatize.py on files that already have stop words removed.
"""
import ast, os, time
def lemmatize(lemmaDict, text):
    #replaces words with their lemmatized versions, if available
    text = text.split(" ")
    lemmaText = []
    for word in text:
        if word in lemmaDict:
            lemmaText.append(lemmaDict.get(word))
        elif word not in lemmaDict:
            lemmaText.append(word)
    return " ".join(lemmaText)

def getLemmaDict(path):
    #getLemmaDict function from replace.ipynb written by data+ 2022! thank you!
    with open(path) as f:
        data = f.read()
    lemmaDict = ast.literal_eval(data)
    print(type(lemmaDict))
    return lemmaDict

def readandLemmatize(file, outputFolder):
    # takes standardized texts and returns them as lemmatized
    #supply your own lemmas dict here
    lemmaDict = getLemmaDict(r"C:\Users\sarah\Downloads\lemmas.txt")
    name = os.path.basename(file)
    with open(file, encoding="utf-8") as Standardextracted:
        with open(os.path.join(outputFolder, name), 'w+') as lowerFile:
            data = Standardextracted.read()
            data = lemmatize(lemmaDict, data)
            lowerFile.write(data)
    return lowerFile

if __name__ == '__main__':
    count = 0
    inputFolder = input("Enter what folder of files need to be converted: ")
    outputFolder = input("Enter folder for converted files: ")
    start = time.time()
    for file in os.scandir(inputFolder):
        count += 1
        if count % 100 == 0 and count != 0:
            print(count, " files lemmatized so far")
        readandLemmatize(file, outputFolder)
    end = time.time()
    print ("Time of execution was ", end-start, " seconds.")
