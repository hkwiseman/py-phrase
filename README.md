# py-phrase
Passphrase generator based on the DiceWare concept and the Electronic Frontier Foundation word list.

Each word in the word list corresponds to a 5 digit number that would normally be established through rolling dice.
This program instead creates random numbers to generate that value and builds a passphrase based on these random words
and the user defined length.

The word list can be altered to include different words or symbols instead of words as long as the total number of words or symbols does not change.

Disclaimer: The length of the passphrases reccomended is solely based off of my own research into experts' reccomendations and the passphrases are limited by what words exist in the word list.

Warning: No history is kept of the passphrases generated. Please write them down or save them if you are going to use them so you have a way of recovering the phrase if forgotten. 

To run the program just download the repository and run: python3 py-phrase.py.

After that the program will prompt for the values needed to create passphrases.

If the word list file is renamed then that name will need to be updated in the program to allow for it to read in that data.

The repository will be updated in the future to include different word lists and an option in the program to generate larger values that can relate to more possible words or symbols to increase randomness.
