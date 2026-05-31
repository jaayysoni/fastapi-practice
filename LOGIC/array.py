#questions asked me in interview 

#------------------------------------------ List ----------------------------------------------------------

# we need to get all the common words in a and b , words not letters and get it in c and print
a = "my name is jay"
b = "my name is akshey"
c = []
for i in a.split():
    if i in b.split():
        c.append(i)
print(c)



# given two strings, find word that are in a but not in b
a = "my name is jay"
b = "my name is akshey"
c = []
for i in a.split():
    if i not in b.split():
        c.append(i)
print(c)



# given a sentence remove all duplicate words and print the result
sentence = "jay is a good developer and jay loves to code and is happy"
result = []
for i in sentence.split():
    if i not in result:
        result.append(i)
print(result)



# given a words count how many times a word appears
sentence = "jay is a good developer and jay loves to code and jay is happy"
word = "jay"
count = 0
for i in sentence.split():
    if i == word:
        count += 1
print(count)



# given an sentence reverse the order of words not letters
sentence = "jay is a good developer and jay loves to code and jay is happy"
new = sentence.split()
print(new[::-1])



# given a sentence find the longest word in it or can say word with most no of letters in it 
sentence = "jay is a good developer and jay loves to code and jay is happy"
new_sentence = sentence.split()
final = 0
for i in new_sentence:
    if len(i) > final:
        final = len(i)
print(final)


# given two sentence, find all unique words across both ( no dulicate )
a = "jay is a good developer and loves to code"
b = "priya is a great designer and loves to travel"
seen = []
for i in a.split() + b.split():
    if i not in seen:
        seen.append(i)
print(seen)


# given a sentence, return only words that have more than three letters
sentence = "jay is a good developer and he loves to code every single day"
seen = []
for i in sentence.split():
    if len(i) > 3:
        seen.append(i)
print(seen)
        


# given a sentence check if there is any speficic word in it 
sentence = "jay is a passionate backend developer who loves building apis and working with databases every single day"
word = "apis"
if word in sentence.split():
    print(True)
else:
    print(False)



# given a sentence sort word alphabetically 
sentence = "jay is a passionate backend developer who loves building apis every day"
new = sorted(sentence.split())
print(new)


# given a sentence return the most repeated word
sentence = "jay loves to code and jay loves backend development and jay always says code every day because code is life and coding is what jay loves most"
seen = {}
for i in sentence.split():
    if i not in seen:
        seen[i] = 1
    else:
        seen[i] += 1
print(max(seen, key=seen.get))

print("List Over here, Hashmap below")
#--------------------------------------- Hashmap ---------------------------------------------------------


# create a list of students and their marks, print all names
hashmap = {
    "jay" : 100,
    "soni": 200,
    "B"   : 150,
    "Tech": 80,
    "SDE" : 250,
}
print(list(hashmap.keys()))


# add a new student to dict
hashmap["work"] = 5000
print(list(hashmap.keys()))


# update an existing marks 
hashmap["SDE"] = 200
print(hashmap)


# Delete Student from dict 
del hashmap["jay"]
hashmap.pop("soni")
print(hashmap)


# Check if student exists in dict 
print("SDE" in hashmap)


# Print all keys, value and key value pairs 
print(hashmap.keys(), hashmap.values(),hashmap)



# Given a list of words count how many times that words appears
words = ["jay", "code", "jay", "python", "code", "jay", "backend", "code", "python", "jay"]
seen = {}
for word in words:
    if word not in seen:
        seen[word] = 1
    else:
        seen[word] += 1
print(seen)



# Given two dict merge them into one
d1 = {"jay": 90, "priya": 85, "ram": 70}
d2 = {"soni": 95, "neha": 75, "amit": 60}
d1.update(d2)
print(d1)
d3 = {**d1 ,**d2}
print(d3)
d4 = d1 | d2
print(d4)



# given a dict give the key with highest value 
d = {"jay": 90, "priya": 85, "ram": 70, "soni": 95, "neha": 75}
print(max(d, key=d.get))



# Given a sentence count frequency of each word
sentence = "jay loves to code and jay loves backend development and jay always says code every day because code is life and coding is what jay loves most"
seen = {}
for i in sentence.split():
    if i not in seen:
        seen[i] = 1
    else:
        seen[i] += 1
print(seen)



# Given a list of numbers list them as even or odd
numbers = [1,2,3,4,5,6,7,8,9,10]
num = {"Even": [],"Odd": []}
for i in numbers:
    if i % 2 == 0:
        num["Even"].append(i)
    else:
        num["Odd"].append(i)
print(num)



# Given a dict reverse it, keys become value and value become keys
d = {"jay": 90, "priya": 85, "ram": 70}
reversed_dict = {}
for key,value in d.items():
    reversed_dict[value] = key
print(reversed_dict)



# given a dict return only words that appears more than twice
sentence = "jay loves to code and jay loves backend and jay always code every day code is life"
seen = {}
for i in sentence.split():
    if i not in seen:
        seen[i] = 1
    else:
        seen[i] += 1

winner = []
for key,values in seen.items():
    if value > 2:
        winner.append(key)
print(winner)



# Given two dict, find common key in both
d1 = {"jay": 90, "priya": 85, "ram": 70, "soni": 95}
d2 = {"jay": 80, "neha": 75, "ram": 60, "amit": 55}
seen = []
for key in d1:
    if key in d2:
        seen.append(key)
print(seen)



# Given a list of studensts and marks, find all students who passed (marks > 40)
students = {"jay": 90, "priya": 35, "ram": 70, "soni": 20, "neha": 75, "amit": 38}
passed = []
for key, value in students.items():
    if value > 40:
        passed.append(key)
print(passed)









