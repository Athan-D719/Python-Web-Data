import re
numlist = list()
sumatoria = 0
value = 0
hand = open('regex_sum_297273.txt') #go back to the main.
for line in hand:
    #line = line.rstrip()
    if re.findall('[0-9]+', line):
        data =  re.findall('[0-9]+', line)
        for i in range(len(data)):
            num = int(data[i])
            numlist.append(num)
#print(numlist)
for i in range(len(numlist)):
    suma = int(numlist[i]) 
    sumatoria += suma
print(sumatoria)