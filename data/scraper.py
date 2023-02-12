from bs4 import BeautifulSoup
import os

path = "./xhtml"
dir_list = os.listdir(path)
# print(dir_list)
wordFile = open('words.txt', 'w')
definitionFile = open('definitions.txt', 'w')
etymologyFile = open('etymology.txt', 'w')
l = 0
x = 0
z = 0
for file in dir_list:
    print(file)
    with open('./xhtml/' + file) as f:
        soup = BeautifulSoup(f, 'html.parser')
        words = soup.select('.dfhead, .dfheadx')
        definition = soup.select('.dftxt')
        etymology = soup.find_all(class_="dfsoot")
        titles = soup.find_all(class_="h2")
        for wordList in words:
            wordFile.write(wordList.text)
            wordFile.write('\n')
        for definitionList in definition:
            definitionFile.write(definitionList.text)
            definitionFile.write('\n')
            definitionFile.write('$')
            definitionFile.write('\n')
            l+=1
        for etymologyList in etymology:
            etymologyFile.write(str(etymologyList))
            etymologyFile.write('\n')
            etymologyFile.write('$')
            etymologyFile.write('\n')
            x+=1
        for titleList in titles:
            z+=1
            print(z, titleList.text)

    print('-----------------')
print(l, x)