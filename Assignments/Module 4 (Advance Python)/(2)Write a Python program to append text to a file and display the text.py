#Write a Python program to append text to a file and display the text

def append_file(file):
    with open(file,"a") as f:
        f.write("\n This is now append ")
        f.close()
    F=open(file)
    print(F.read())
    F.close()


append_file("p.txt")    
