#Write a Python program to copy the contents of a file to another file

with open("p.txt","r") as firstfile,open("s.txt","a") as secondfile:
    for i in firstfile:
        secondfile.write(i)

'''        
import shutil

#use copyfile
shutil.copyfile("p.txt","s.txt")
'''
