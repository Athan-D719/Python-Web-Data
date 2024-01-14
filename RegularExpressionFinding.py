#JUST COMMENT TO SEE THE DIFERENCE

import re

###########################################################################################################################################
#Basically these prints the whole lines where the word to find is in
hand = open('sample(From).txt')
for line in hand:
    line = line.rstrip() #method returns a copy of the string with trailing characters removed (based on the string argument passed). If no argument is passed, it removes trailing spaces.
    if line.find('From:') >= 0: #method returns the lowest index of the substring if it is found in given string. If its is not found then it returns -1.
        print(line)

#using the regular expression library
hand = open('sample(From).txt')
for line in hand:
    line = line.rstrip() #basically the position
    if re.search('From:', line): 
        print(line)

###########################################################################################################################################
#These will only print the lines where the key_word is 'startingwith' the line.
hand = open('sample(From).txt')
for line in hand:
    line = line.rstrip() 
    if line.startswith('From:'): #can be inversed with endswith()
        print(line)

#using the regular expression library
hand = open('sample(From).txt')
for line in hand:
    line = line.rstrip() 
    if re.search('^From:', line): #can be modfied so it works with the end '$'
        print(line)

###########################################################################################################################################
#These let you extract numbers from a string or a file
x = 'My 2 favorite numbers are 19 and 42'
#when we actually want to find data inside a string we use findall()
y = re.findall('[0-9]+', x) #[0-9] refers to a single number btwn those two and the '+' is for findinf more digits
print(y) #returns it in a list of the findings 

##########################################################################################################################################
#GREEDY MATCHING
#streches in both directions(BE CAREFUL)
x = 'From: Using the : character'
y = re.findall('^F.+:', x) #starts with F (^),one or more characters (.+), ends in ':' so...
print(y)
#['From: Using the :']
y = re.findall('^F.+?:', x) #the '?' stops when it find the last character ':' NOT GREEDY
print(y)
#['From:']

#########################################################################################################################################
#Fine-Tuning String Extraction
#using re.findall() to separate substrings finding using a character as index
x = 'From stephen.marquard@uct.ac.za    jonathan.marquard@uct.ac.za Sat jan 5 09:14:16 2008'
y = re.findall('\S+@\S+', x) #\S is s non-whitespacing characters so it will separate the word from spacing after and befor it
                             #the + makes it to be one or more of them
#with the ? it would just print the @s
print(y)
#['stephen.marquard@uct.ac.za', 'jonathan.marquard@uct.ac.za']
y = re.findall('^From (\S+?@\S+?)', x) #just extracts the first word after the 'From ' 
print(y)
#['stephen.marquard@uct.ac.za']

#########################################################################################################################################
#Finding positions and limist with...
data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16'
atpos = data.find('@')
print(atpos)
#21, the '@' is in this position on the string
sppos = data.find(' ', atpos)
print(sppos)
#31, the ' ' position in the string after the '@'
host = data[atpos+1 : sppos]
print(host)
#uct.ac.za, prints from the atpos+1 position until the space(sppos)

##########################################################################################################################################
#The Double split Pattern
line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16'
words = line.split()
email = words[1] #we take the second word and declare it as a variable
pieces = email.split('@') #split the word from the '@' sign 
print(pieces[1]) #take the second word as printed
#uct.ac.za

#RE
line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16'
y = re.findall('@([^ ]*)', line) #looking through the string until it finds an '@', extract after it until it finds a space
                            #* followed by any number of characters.
                            #[^ ] Match non-blanck character EVERYTHING BUT 
y = re.findall('^From .*@([^ ]*)', line) #extracts from 'From ' (.*) any number of characters up to an '@'...
print(y)
#uct.ac.za
#$$ y is a LIST()
#########################################################################################################################################
#EXERCISE
import re
hand = open('sample(From).txt') #method open to open the .txt file
numlist = list() #clisify this variable as a list
for line in hand:
    line = line.rstrip() #for that line
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line) #extracts every number and  .
    if len(stuff) != 1: continue #asuring that theres just one element in that stuff list
    num = float(stuff[0]) #we take the first element of the list as a float for the num variable
    numlist.append(num) #we add that cloat to the numlist list()
    print('Maximum: ', max(numlist)) #prints it.




