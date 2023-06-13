"""data+ 2022
MUST BE USED ON VEP PRE-PROCESSED TEXTS (avoids the pesky dots and gives
ASCII carets instead) 

this is an adapted version of the file text.py from the 2022 data+
github. the functions are unchanged, but the order of their calls
has been manipulated for our purposes.

It aims to clean TCP XML files and render them into a more readable
format, extracting both the dedication and body of texts.

The 2023 ECBC Data+ group intends to use/will use this code to
clean raw XML files in order to create BOW models on relevant texts."""

from bs4 import BeautifulSoup
import re, os, time

'''
STAGE I TEXT PROCESSING for both body text and dedications. 
'''


def text(soup):
    '''
    Gets the body of the text file into string format.
    -----------------------------------
    Does not grab any text in the tag <front> which contains div tags such as ['title_page', 'dedication',
    'to_the_reader', 'list'...] that are not part of the main text.

    Does not grab any text in the tag <back> which contains div tags such as ['errata', 'index',
    'supplied_by_editor', ...] that are not part of the main text.

    Does not grab any text under the <table> or <foreign> tags

    Does not grab any text under div type 'coat_of_arms' or attribute 'lat'

    '''
    text_list = []
    for sibling in soup.find_all('w'):
        parent_name = [parent.name for parent in sibling.parents]
        parent_attrs = [parent.attrs for parent in sibling.parents]
        divType = [ats['type'] for ats in parent_attrs if 'type' in ats.keys() and ats['type'] == 'coat_of_arms']
        divLat = [ats['xml:lang'] for ats in parent_attrs if 'xml:lang' in ats.keys() and ats['xml:lang'] == 'lat']
        if not any(x in parent_name for x in ['front', 'table', 'back',
                                              'foreign']) and 'coat_of_arms' not in divType and 'lat' not in divLat and re.search(
                'lemma', str(sibling)) and str(sibling['lemma']) != 'n/a':
            text_list.append(sibling['lemma'])
    return ' '.join(text_list)


def dedication(soup):
    text_list = []
    for sibling in soup.find_all('w'):
        parent_attrs = [parent.attrs for parent in sibling.parents]
        parent_title = [ats['type'] for ats in parent_attrs if 'type' in ats.keys() and ats['type'] == 'dedication']
        if 'dedication' in parent_title and re.search('lemma', str(sibling)) and str(sibling['lemma']) != 'n/a':
            text_list.append(sibling['lemma'])
    return ' '.join(text_list)


def convert(folder, file, textfolder, typeText, typeText2):
    '''
    Master function for converting each XML file into a dataframe
    '''
    fileName = os.path.join(folder, file)
    name = file.split('.')[0]
    data = open(fileName, 'r', encoding='utf-8')
    data = data.read()
    soup = BeautifulSoup(data, 'html.parser')
    # call text function to output the body text as a plain text file
    with open(os.path.join(textfolder, name + '.txt'), 'w+', encoding='utf-8') as file:
        if typeText == 'text':
            toFile = text(soup)
        if typeText2 == 'dedication':
            toFile2 = dedication(soup)
        file.write(toFile2)
        file.write(toFile)


if __name__ == '__main__':
    print("Extracts dedication and body texts from XML files.")
    folder = input('Enter folder path: ')
    textfolder = input('Enter the folder path for your output text files: ')
    typeText = input('Enter text: ')
    typeText2 = input('Enter dedication: ')

    start = time.time()
    count = 0
    for file in os.listdir(folder):
        count += 1
        if count % 10 == 0 and count != 0:
            print("Processed " + str(count) + " files so far")
        convert(folder, file, textfolder, typeText, typeText2)
    print('The number of total files is ' + str(count))
    end = time.time()
    print("The time of execution is :", end - start, ' seconds')
