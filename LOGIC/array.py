#questions asked me in interview 

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
        



































