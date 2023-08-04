# Ethical Cosumption Before Capitalism Data+ 2023
Hello, we are the ECBC Data+ 2023 Cohort! In this repository, you will find all relevant code that was used to conduct our analysis this summer. 

We combine the power of computational linguistics and close-reading techniques to evaluate the discourse surrounding 17th century English colonization and how it viewed different groups of people—its colonial rivals, the Indigenous nations it invaded, the Irish it subjugated, and the indentured children and enslaved Africans it shipped to the New World—in terms of profit, both economic and spiritual. With a specific focus on the Virginia Company, we analyze how the company focused on turning a "profit of souls" when it continuously failed to turn a commercial profit by preying on anxieties surrounding the spread of Catholicism, and how the larger umbrella of English colonization viewed the people it exploited in the years 1590-1639. Our work is built on prior years of Data+ and Bass Connections cohorts at Duke.

# 2022 relevant files (folder) 
* *replace.ipynb* standardizes and lemmatizes files using provided .txt file dictionaries. We ended up not using all of this code, though it provided some useful functionality for our lemmatization code
* *text.py* extracts texts from XML files provided by EP that are already partially standardized and lemmatized, deals with the "lemma" specifications put in by EP
# EPBagofWords (folder) 
* *EPcsvreader.py* takes the EP metadata CSV spreadsheet and identifies relevant texts for processing based off the keywords inputted
* *bowprep.py* non-used code that lowercases all text and removes punctuation
* *keywordsIDs.txt* selected outputted results from EPcsvreader.py
* *lemmas.txt* dictionary of all standardizations and lemmatizations used on our texts
* *lemmatize.py* lemmatizes inputted texts and outputs their cleaned versions using lemmas.txt
* *standardizedwords* a text file version of all variant spellings that were standardized for the purposes of our project, including those with ASCII carets
* *standardizer.py* standardizes all variant spellings, adapted version of bowprep.py
* *textcleaner.py* same as text.py from 2022 relevant files
# HTMLFolder (folder) 
* includes all CSS, Javascript, and HTML code necessary to create the graph visualization on the R Shiny web app

# PNGFolder (folder)
* contains all PNGs used on the R Shiny web app created by our POS code and Word2Vec models

# POS Visualizations (folder) 
* contains POS_Visualizations, a folder full of all of the PNGs for our part of speech tagging results

# Text Classification (folder)
* *kmeans.ipynb* code to do kmeans clustering on cleaned texts, visualize PCA clusters
* *lda_topics.ipynb* lda topic modeling code for cleaned texts given specified n number of topics, TF-IDF vectorization or plain BOW processed texts
* *supervised.ipynb* supervised text clustering based off of metadata tags taken from the EP spreadsheet to specify region
* *counting text entries.qmd* used to filter TF-IDF results by # of relevant words hit inside a text for a given subject

# Text Date Ranges (folder) 
* .txt files labeled by the date ranges they cover, includes all TCP ids in the relevant range

# VEP-Pipeline (folder)
 *All of the code in this folder was written by the Visualizing English Print (VEP) Project that is a collaboration between the University of Wisconsin-Madison, the Folger Shakespeare Library, and the University of Strathclyde. We have appended the necessary licenses for use.*
* *charactercleaner.py* pre-processes the raw XML files, removing structural garbage and some special characters from texts and inputting ASCII carets into transcription omissions, MUST BE RUN FROM THE COMMAND LINE
* *conversiondict.py* necessary companion to charactercleaner.py that is used to remove and replace structural garbage & special characters
# General Code 
* *bodyExtraction.py* removes all <body> tagged text from XML files, did not end up being used in our project after we switched to EP instead of EEBO files, though useful for understanding BeautifulSoup
* *list_csv.py* turns a given list into a CSV
* *move.ipynb* used to copy over and move specified files around the Duke Compute Cluster

# Heatmaps 
* *enslaved african heatmaps* contains all PNGs of heatmaps for vocab related to enslaved Africans overtime and in their focused subcorpus
* *indentured heatmaps* contains all PNGs of heatmaps for vocab related to indentured child labor/indentured labor overtime and in their focused subcorpus
* *irish heatmaps* contains all PNGs of heatmaps for vocab related to the Irish overtime and in their focused subcorpus
* *powhatan heatmaps* contains all PNGs of heatmaps for vocab related to the Powhatan overtime and in their focused subcorpus
* *spanish heatmaps* contains all PNGs of heatmaps for vocab related to the Spanish overtime and in their focused subcorpus
* *spiritual profit heatmaps* contains all PNGs of heatmaps for the vocabulary of spiritual profit overtime and its its focused (Virginia subcorpus)
* *virginia heatmaps* contains all PNGs of heatmaps vocab related to Virginia overtime in its focused subcorpus

# ngrams & tfidf (folder)
* *ngrams.ipynb* generates and extracts bigrams and trigrams from specified texts
* *tf-idf.py* generates a table of TF-IDF scores using vocab from given base text

# parts of speech (folder) 
 *All of this code was adapted from the 2022 ECBC cohort for our purposes. Primary authorship belongs to them, not us* 
* *cleanTextPOS.ipynb* parses XML files and extracts the word and its POS tag, cleans text by lemmatizing, standardizing, and removing stop words
* *getData.ipynb* extracts 10 words surrounding given key words in all instances in the text, gives json file with the top 10 of each specified part of speech surrounding the keyword

# word2vec (folder) 
* *overtime.ipynb* tracks cosine similarity overtime, tracks euclidean distance overtime, functionality for checking instances of a word in all texts over time
* *regionalword2vec.ipynb* groups given TCP ids in subcorpora into their date ranges to create word2vec models, generates cosine similarity overtime for regional corpora
* *wordembed.ipynb* generates heatmaps given a specified lexicon







