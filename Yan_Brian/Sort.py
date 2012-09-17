import random
period6 = list()
period7 = list()
#Sort the classes
for text in open("ml7-student-names","r").readlines():
    firstname = " "
    lastname = " "
    text=text.strip()
    lastname = text[:text.index(",")]
    firstname = text[text.index(",")+1:text.rindex(",")]
    if text[text.rindex(",")+1:] == "6":
        period6.append(firstname + " " + lastname)
    else:
        period7.append(firstname + " " + lastname)
#Randomize Classes
random.shuffle(period6)
random.shuffle(period7)

#Print them out
group6 = ""
group7 = ""
index6 = 0
index7 = 0
print "Period 6"
while len(period6) > index6:
    if index6 % 4 == 0:
        group6 = group6 + "\n"
    group6 = group6+"\n"+period6[index6]
    index6 = index6 + 1
print "Period 7"
while len(period7) > index7:
    if index7 % 4 == 0:
        group7 = group7 + "\n"
    group7 = group7+"\n"+period7[index7]
    index7 = index7 + 1
print group6
print group7
