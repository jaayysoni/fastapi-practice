#questions asked me in interview 

# we need to get all the common words in a and b , words not letters and get it in c and print
a = "my name is jay"
b = "my name is akshey"
c = []

for i in a.split():
    if i in b.split():
        c.append(i)
print(c)










































