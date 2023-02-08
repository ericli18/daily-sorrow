import csv
x = 0
words = []
definitions = [] 
etyms = []
with open('words.txt', "r") as csvfile:
    reader = csv.reader(csvfile, delimiter='\n')
    for row in reader:
        if(len(row) < 2):
            words.append(row)
with open('definitions.txt', "r") as csvfile:
    reader = csv.reader(csvfile, delimiter='$')
    for row in reader:
        if(len(row) < 2):
            definitions.append(row)
with open('etymology.txt', "r") as csvfile:
    reader = csv.reader(csvfile, delimiter='$')
    for row in reader:
        if(len(row) < 2):
            etyms.append(row)
print(len(words), len(definitions), len(etyms))

with open('links.csv', "w") as f:
    writer = csv.writer(f)
    writer.writerow(['word', 'definition', 'etymology'])
    for i in range(len(words)):
        writer.writerow([words[i], definitions[i], etyms[i]])