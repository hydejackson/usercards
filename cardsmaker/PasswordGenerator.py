#Create random passwords from list of words and 3-digit numbers, ain't need to be too fancy it's just temp for new hires. currently 284,000 combinations I think
#in:  string filename, int length (of list)
#out: list[string]

import random
import csv

def passwordGenerator(filename, length):
    random.seed()
    file = open(filename, "r")
    data = list(csv.reader(file, delimiter=","))
    file.close()

    passwords = []
    partTwo = ''
    for i in range(length):
        partOne = random.choice(data)[0]
        partTwo = random.choice(data)[0][:3]
        randomSplit = random.randint(1, len(partOne)-1)
        partOneSplit = partOne[:randomSplit] + random.choice(['-', '!', '?', '@', '$']) + partOne[randomSplit:]
        parts = partOneSplit + partTwo
        passwords.append(parts + str(random.randint(100, 999)))

        partTwo = ''

    return passwords