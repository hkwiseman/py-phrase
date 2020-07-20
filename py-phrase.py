__author__ = "H. Kyle Wiseman"
__copyright__ = "Copyright 2020"
__credits__ = ["H. Kyle Wiseman"]
__license__ = "GPLv3"
__version__ = "0.1.0"
__maintainer__ = "H. Kyle Wiseman"
__email__ = "kwiseman@highpoint.edu"
import sys
import secrets

# Generate random number to build number corresponding to word list
def rollDice():
    rollNum = ""
    for i in range(5):
        rollNum += str(secrets.randbelow(5)+1)
    return rollNum

passPhrase = []
builtPassword = ""
randomWord = ""
wordList = {}
count = 2
with open('eff_large_wordlist.txt', 'r') as f:
    for line in f:
        for word in line.strip().split("\t"):
            if(count % 2 == 0):
                wordList[word] = " "
                key = word
            else:
                wordList[key] = word
            count += 1

print("-----------------------------------------------------------------------")
print("|         WELCOME TO THE PY-PHRASE PASSPHRASE GENERATOR!              |")
print("| All passphrases are randomly made up of some number of English      |")
print("| words based on the Electronic Frontier Foundation's word list.      |")
print("-----------------------------------------------------------------------")
print()

passnum = int(input("Enter the number of passphrases you would like generated: "))
for i in range(passnum):
    print()
    print("Choose the number of words you would like in your passphrase.")
    print("Reccomendations: 4 - For unimportant accounts, 5 - For good level of security,")
    print("and 7 or more - For very strong security.")
    print()
    length = int(input("Enter here for passphrase " + str(i+1) + ": "))
    for j in range(length):
        randomWord = ""
        randomWord = wordList[rollDice()]
        builtPassword += randomWord
        print("Word " + str(j+1) + " in password " + str(i+1) + ": " + randomWord)

    passPhrase.append(builtPassword)
    print("Password " + str(i+1) + ":" + builtPassword)
    builtPassword = ""
print()
print("Final passwords: ")
print("-----------------------------")
for i in range(passnum):
    print("Password[" + str(i+1) + "] = " + passPhrase[i])

print()
print("WARNING: No history of passphrases generated is kept.")
print("Please write them down or save passphrases in a password manager to have a backup.")
