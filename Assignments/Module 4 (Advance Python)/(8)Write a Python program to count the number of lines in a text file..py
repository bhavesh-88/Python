#Write a Python program to count the number of lines in a text file.

with open("p.txt","r") as f:
    count=0
    F=f.read()
    l=F.split("\n")
    print(F)
    print(l)
    for i in l:
        if i
            count=count+1
    print("Total number of lines in file :",count)
