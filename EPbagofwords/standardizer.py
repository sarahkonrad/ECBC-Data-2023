"""author: sarah konrad, data+ 2023

standardizer.py cleans body + dedication texts extracted from EP (not EEBO) TCP files that had
already undergone VEP pre-processing before their extraction. 
EP files are also partially lemmatized and standardized. 

the cleaning process involves removing strange structural garbage like "(@)" and "(...)" etc., 
removing numbers and punctuation, unnecessary free-floating single letters, and lowercasing every word
in the file to eliminate case sensitivity. 

notes to add: potential to steal getLemmaDict function and add a standardization dictionary, 
though that seems redundant given the level of standardization offered by EP and the fact
that the lemmas dictionary already in existence catches a lot of the words of interest???

possibility to import stopwords as a text file so you don't have to edit the module every time??
"""
import ast, os, time

def replaceNonsense(text):
    #removes structural garbage from files including *, (@), ., and numbers
    structural_garbage = ["(@)", "@", ".", "(...)", "*", "1", "2", "3",
    "4", "5", "6", "7", "8", "9", "0", "()", "..."]
    for trash in structural_garbage:
        text = text.replace(trash, "")
    return text

def removeToosmall(text):
    #removes all free floating single letters other than a and i
    acceptableWords = ['i', 'a', 'A', 'I']
    text = text.split(" ")
    text = [word for word in text if word in acceptableWords or len(word) > 1]
    text = " ".join(text)
    return text

def removeStopwords(text):
    #removes stop words from the text
    #thank you data+ 2022 for the stopwords!! #this list is also editable and under review
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
    text = text.split(' ')
    text = [word.strip() for word in text]
    #attempt to remove random spaces
    #.lower() is vital to catch uppercased words! EP lemmatization isn't everything
    tokens = [word for word in text if word.lower() not in stopwords]
    tokens = " ".join(tokens)
    return tokens

def tryStrip(text):
    #removes random spaces from the text
    text = text.split(' ')
    badspace = ['']
    text = [word for word in text if word not in badspace]
    text = ' '.join(text)
    return text

def readandStandardize(file, outputFolder, tostopWordsornotostopWords):
    # reads extracted body and dedications (after textcleaner.py and VEP)
    name = os.path.basename(file)
    with open(file, encoding="utf-8") as EPextracted:
        with open(os.path.join(outputFolder, name), 'w+') as lowerFile:
            data = EPextracted.read()
            data = replaceNonsense(data)
            if tostopWordsornotostopWords == 'N':
                data = removeStopwords(data)
            data = removeToosmall(data)
            data = tryStrip(data)
            lowerFile.write(data.lower())
    return lowerFile

if __name__ == '__main__':
    count = 0
    inputFolder = input("Enter what folder of files need to be converted: ")
    outputFolder = input("Enter folder for converted files: ")
    tostopWordsornotostopWords = input("Stop words included? Y or N: ")
    start = time.time()
    for file in os.scandir(inputFolder):
        count += 1
        if count % 100 == 0 and count != 0 and tostopWordsornotostopWords == 'N':
            print(count, " files standardized without stop words included so far")
        elif count % 100 == 0 and count != 0 and tostopWordsornotostopWords == 'Y':
            print(count, " files standardized with stop words included so far")
        readandStandardize(file, outputFolder, tostopWordsornotostopWords)
    end = time.time()
    print ("Time of execution was ", end-start, " seconds.")