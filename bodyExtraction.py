"""author: sarah konrad, data+ 2023. bodyExtraction.py takes VEP pre-processed XML EEBO TCP files
and extracts the body text from the body tags. To process VEP processed XML files,
bodyExtraction.py asks for an input folder pathway (XML files) and an output pathway (folder
for extracted body texts)."""

from bs4 import BeautifulSoup
import os, time


# uses BeautifulSoup get_text() to extract the body text from XML files
def bodyExtract(file, outputFolder):
    #strip whatever comes after the TCP ID
    uglyname = os.path.basename(file)
    name = uglyname.split(".")[0]

    #XML file must be read to get its contents into a text form that BeautifulSoup can digest
    xmlFile = open(file)
    xmlContent = xmlFile.read()

    #despite these being XML files we opted for the html.parser given the ECBC 2022 cohort's rec
    soup = BeautifulSoup(xmlContent, 'html.parser')

    # identifies all body text via xml/html tags
    result = soup.find("body")
    bodyText = result.get_text()
    with open(os.path.join(outputFolder, name + '.txt'), 'w+') as file:
        file.write(bodyText)

if __name__ == '__main__':
    inputFolder = input("Enter the path of the folder containing the files to be processed: ")
    outputFolder = input("Enter the folder of ouput for the extracted body texts: ")

    start = time.time()
    count = 0
    for file in os.scandir(inputFolder):
        count += 1
        if count % 100 == 0 and count != 0:
            print("Extracted " + str(count) + " body texts so far")
        bodyExtract(file, outputFolder)
    end = time.time()
    print("The time of execution was ", end-start, "seconds")







