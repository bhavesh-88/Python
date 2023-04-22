#Write a Python program to write a list to a file.

l=["One","Two","Three","Four","Five","Six","Seven","Eigth","Nine","Ten"]

with open("p.txt","w") as file:
    for i in l:
        #file.write("%s\n" %i)
        file.write(f"{i}\n")
        #file.close()

f=open("p.txt")
print(f.read())
