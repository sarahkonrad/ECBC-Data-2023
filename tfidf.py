"""
this is an updated version of the gettexts function from data+ 2022. edited by sarah konrad, data+ 2023, 
easier to use.

this is an adapted and improved version of the vocab.ipynb created by the 2022 cohort. 
input a base text and use it to generate a TF-IDF table
"""
import os
from collections import Counter
import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer

def gettexts(folder):
    texts = []
    #list of lists of strings, each text broken up into individual token strings
    tokenized = []
    #list of texts as a continuous string
    textnames = []
    for file in os.listdir(folder):
        path = os.path.join(folder,file)
        name = os.path.basename(file)
        f = open(path,'r', encoding="utf-8")
        data = f.read()
        textnames.append(name)
        texts.append(data)
        f.close()
    for text in texts:
        #tokenize by white space
        words = text.strip().split(' ')
        tokenized.append(words)
    return [tokenized, texts, textnames]
    #i.e. index 0 gives list of tokens, 1 gives list of texts as one string, 2 gives list textnames

#input which texts you would like to analyze  
# put whatever file you want to analyze in here 
tfidfdata = gettexts(r"C:\Users\sarah\Downloads\1606-1612_texts")
tfidftokens = tfidfdata[0]
tfidftexts = tfidfdata[1]
tfidfnames = tfidfdata[2]

data = {'text names' : tfidfnames, 'tokens' : tfidftokens, 'texts' : tfidftexts}

#setting a text to sort by for TF-IDF analysis
#the basetexts list is a list of relevant sermons from giungni and hines
#the basetexts list is never used in this code
basetexts = ['A19313', 'A19590', 'A08541', 'A10057', 'A13290', 'A02059', 'A19548']
#swap out base text as you please
basetext = 'A12466.txt'

#load wordcounts onto dataframe
wordcounts = [Counter(t) for t in tfidftokens]
df = pd.DataFrame(wordcounts, index=[name for name in tfidfnames]).fillna(0)
# using transformer, generate table to compare tf-idfs across multiple texts

# normalization turned off
# sublinear term frequency scaling turned on (takes log of term frequencies and can help to de-emphasize function words like pronouns and articles)
tfidf = TfidfTransformer(norm=None, sublinear_tf=True)
results = tfidf.fit_transform(df)
table = pd.DataFrame(results.toarray(), index=df.index, columns=df.columns)

# columns are texts, using .head(25) to show top 25 terms
# sort using words with highest tfidf scores in specified basetext as an example
table = table.T.sort_values(by=[basetext], ascending=False).head(150)
table.to_csv('tfidf.csv', sep='\t', encoding='utf-8')
# transformer version, but outputting tf-idf values for a single text, easier viewing

#Use the following code to see the TF-IDF scores of a single text with words based off the tuning text!
transformer = TfidfTransformer(norm=None, sublinear_tf=True, use_idf=True)
cv = CountVectorizer()
wc = cv.fit_transform(tfidftexts)
wctrans = transformer.fit_transform(wc)

single = pd.DataFrame(wctrans[tfidfnames.index(basetext)].T.todense(), index=cv.get_feature_names_out(), columns=[basetext + " TF-IDF"])
single = single.sort_values(basetext + ' TF-IDF', ascending=False)

print(single.head(150))

"""
Some closing thoughts: to get a more accurate tuning set for TF-IDF should we use our base text as a VC company sermon, 
OR should we compile multiple of them into a document for tuning? Which would provide a better experience?
"""