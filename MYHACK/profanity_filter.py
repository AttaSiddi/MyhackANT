def giveCleanString(filename):
    with open('profanitydataset.txt', 'r') as f:
        listl = []
        for line in f:
            string = line.strip()
            listl.append(string)

    bad_list_censor = open(filename, 'r')

    bad_word_sent = bad_list_censor.read()

    string1 = bad_word_sent.lower()

    for bad_word in listl:
        string2 = ""
        if bad_word in string1 and len(bad_word) > 0:
            string2 = bad_word[0]
            for j in range(len(bad_word)-1):
                string2 += "*"
            string1 = string1.replace(bad_word, string2)

    bad_list_censor.close()
    return string1


def createACleanFile(string1, filename = insertTextHere):
    file1 = open(filename, 'w')
    file1.write(string1)
    file1.close()


def readAFile(filename):
    file1 = open(filename, 'r')
    print(file1.read())
    file1.close()


clean = giveCleanString(insertTextHere)
createACleanFile(clean)
readAFile(insertTextHere)