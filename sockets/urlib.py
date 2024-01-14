import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt') #makesthe request and opens it

counts = dict()
for line in fhand: #for every line...
    print(line.decode().strip()) #decodes the line and represents it eith the strip() method gives it 'enters'
#This time theres no metacode.(no headers)

#But soft what light through yonder window breaks
#It is the east and Juliet is the sun
#Arise fair sun and kill the envious moon
#Who is already sick and pale with grief

##################################################################################################################
##################################################################################################################
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt') #makesthe request and opens it

counts = dict()
for line in fhand: #for every line...
    words = (line.decode().split()) #spliting the lines per word
                                    #with the strip() it separates the letters.
    for word in words:
        counts[word] = counts.get(word, 0) + 1 #here after the words are splited we just asign with the get() method of the dictionary
                                               #the number of times in this case a word repeated.
                                               #the +1 sums to the keyword value.
print(counts)
#split():{'But': 1, 'soft': 1, 'what': 1, 'light': 1, 'through': 1, 'yonder': 1, 'window': 1, 'breaks': 1, 'It': 1, 'is': 3, 'the': 3, 'east': 1, 'and': 3, 'Juliet': 1, 'sun': 2, 'Arise': 
#1, 'fair': 1, 'kill': 1, 'envious': 1, 'moon': 1, 'Who': 1, 'already': 1, 'sick': 1, 'pale': 1, 'with': 1, 'grief': 1}

#strip():{'B': 1, 'u': 6, 't': 12, ' ': 29, 's': 11, 'o': 8, 'f': 3, 'w': 4, 'h': 9, 'a': 10, 'l': 6, 'i': 13, 'g': 3, 'r': 7, 
#'y': 2, 'n': 9, 'd': 6, 'e': 12, 'b': 1, 'k': 3, 'I': 1, 'J': 1, 'A': 1, 'v': 1, 'm': 1, 'W': 1, 'c': 1, 'p': 1}
#############################################################################################################################################

