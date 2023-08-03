# ECBC-Data-2023
Ethical Consumption Before Capitalism, Data+ 2023

Hello, we are the ECBC Data+ 2023 Cohort! In this repository, you will find all relevant code that was used to conduct our analysis this summer. 

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
* 
