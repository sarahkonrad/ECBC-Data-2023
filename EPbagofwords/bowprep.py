"""author: sarah konrad, data+ 2023

bowprep.py cleans body texts extracted from EP (not EEBO) TCP files that have
already been VEP processed to remove variant accents on characters and ampersands.EP files
are also partially lemmatized and standardized.

bowprep.py lowercases all words, strips of punctuation, and removes all numbers.
carots are kept, as those inside words are necessary for further lemmatization.
stop words are also removed, as well as all words 2 letters or smaller. the list
of stop words was generated by data+ 2022

update, 6/7: bowprep.py now lemmatizes texts using a text file as a dictionary!

this code is not perfect and cannot handle all standardization/lemmatization issues, but
it can return a relatively clean and lemmatized file for BOW modeling
"""
import ast, os, time

def replaceNonsense(text):
    #removes structural garbage from files including *, (@), ., and numbers
    structural_garbage = ["(@)", "@", ".", "(...)", "*", "1", "2", "3",
    "4", "5", "6", "7", "8", "9", "0", "()"]
    for trash in structural_garbage:
        text = text.replace(trash, "")
    return text

def removeToosmall(text):
    #perhaps unneeded? we will see
    text = text.split(" ")
    #removes words 2 letters or smaller, used after removeStopwords to catch
    for word in text:
        if len(word) <= 2:
            text.remove(word)
    text = " ".join(text)
    return text

def removeStopwords(text):
    #removes stop words from the text
    #thank you data+ 2022 for the stopwords!!
    stopwords = ['i', 'me', 'in', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you',
                "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves',
                'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it',
                "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves',
                'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those',
                'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had',
                'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'or',
                'as', 'until', 'while', 'at', 'by', 'for', 'with', 'about', 'between', 'into',
                'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up',
                'down', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here',
                'there', 'when', 'whence','where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more',
                'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so',
                'than', 'too', 'very', 's', 't', 'can', 'will', 'don', "don't", "should've", 'now',
                'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't",
                'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven',
                "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn',
                "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren',
                "weren't", 'won', "won't", 'wouldn', "wouldn't", 'neve', 'earlier', 'may',
                'unto', 'whereof', 'began', 'inasmuch', 'shall', 'de', 'we', 'sir', 'later', 'until',
                'could', 'two', 'years', 'mr', 'long', 'till', 'thereof', 'indeed', 'ie', 'himself',
                'neither', 'doth', 'thence', 'seem', 'part', 'old', 'definite', 'would', 'iq',
                'aforesaid', 'ever', 'might', 'upon', 'how', 'therein', 'through', 'done', 'begin',
                'little', 'last', 'also', 'ew', 'etc', 'full', 'second', 'though', 'more', 'his',
                'whereas', 'thy', 'thee', 'themselves', 'he', 'why', 'seldom', 'hear', 'what',
                'think', 'matter', 'et cetera', 'present', 'do', 'before', 'made', 'there',
                'thereforeunto', 'when', 'whilst', 'herself', 'definitely', 'her', 'arrived',
                'per', 'afterward', 'far', 'dr', 'saying', 'char', 'whereby', 'or', 'third',
                'seems', 'mentioned', 'go', 'esq', 'year', 'likewise', 'must', 'know', 'pag',
                'conerning', 'earliest', 'ditto', 'hath', 'without', 'self', 'lib', 'three',
                'and', 'itself', 'suchtwo', 'otherwise', 'seeing', 'him', 'latest', 'often',
                'cannot', 'et', 'thou', 'est', 'it', 'which', 'can', 'most', 'let', 'almost',
                'say', 'late', 'hereby', 'every', 'wherein', 'either', 'much', 'come', 'said',
                'else', 'near', 'cap', 'esq', 'viz', 'heard', 'fol', 'like',
                'within', 'have', 'thus', 'certainly', 'one', 'make', 'rather', 'she',
                'eg', 'where', 'ne', 'since', 'four', 'fourth', 'includes', 'even', 'us',
                'gone', 'five', 'anno', 'went', 'thing','according','hove','set',
                'ettling', 'hee', 'bee', 'wee', 'mat', 'gen','rom',
                'if','of','because','since','part','yet','whether',
                'many','day','great','qua','out','man','time',
                'first','one','two','second','well','see','call',
                'against','never','word','place','therefore',
                'way','still']
    #following two lines = attempt to rid of random stray letters, is partially successful
    #most end up removed but not all
    text = text.split(" ")
    text = [word.strip() for word in text]
    #.lower() is vital to catch uppercased words! EP lemmatization isn't everything
    tokens = [word for word in text if word.lower() not in stopwords]
    tokens = " ".join(tokens)
    return tokens

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
def readandConvert(file, outputFolder):
    # takes text.py cleaned (initially VEP processed) texts and returns them in BOW format
    lemmaDict = getLemmaDict(r"C:\Users\sarah\Downloads\lemmas.txt")
    name = os.path.basename(file)
    with open(file, encoding="utf-8") as EPextracted:
        with open(os.path.join(outputFolder, name + '.txt'), 'w+') as lowerFile:
            data = EPextracted.read()
            data = replaceNonsense(data)
            data = removeStopwords(data)
            data = removeToosmall(data)
            data = lemmatize(lemmaDict, data)
            lowerFile.write(data.lower())
    return lowerFile

if __name__ == '__main__':
    count = 0
    inputFolder = input("Enter what folder of files need to be converted: ")
    outputFolder = input("Enter folder for converted files: ")
    start = time.time()
    for file in os.scandir(inputFolder):
        count += 1
        if count % 100 == 0 and count != 0:
            print(count, " files prepared for BOW so far")
        readandConvert(file, outputFolder)
    end = time.time()
    print ("Time of execution was ", end-start, " seconds.")



