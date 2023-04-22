#Write a Python program to read an entire text file.

#f=open("p.txt","w")
#f.write("Hello, Welcome To My Profile,\n this is file management demo using python")
#f.close()


def read_file(file):
    f=open(file)
    print(f.read())
    f.close()
    
read_file("p.txt")    
