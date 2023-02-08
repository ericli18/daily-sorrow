with open('temp.txt') as f1, open('words.txt') as f2:
    words1 = set(f1.read().split(", \n"))
    words2 = set(f2.read().split("\n"))
    unique_to_file1 = words1 - words2
    unique_to_file2 = words2 - words1
    print("Words unique to file1:", unique_to_file1)
    print("Words unique to file2:", unique_to_file2)
