#Write a Python program to read a file line by line and store it into a list

with open("p.txt") as f:
    #l=[a for a in f]
    #l=[a.strip() for a in f]
    l=f.readlines()
print(l)    

#remove new line char
l=[a.strip() for a in l]
print(l)


