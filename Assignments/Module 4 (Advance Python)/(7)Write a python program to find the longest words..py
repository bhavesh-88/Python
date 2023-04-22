#Write a python program to find the longest words.

f=open("p.txt","r")
s=f.read()
l=s.split()
print(s)
print(l)
#print(max(l,key=len))
n=int(input("Enter the value :"))
for i in l:
    if len(i)>n:
        print((i))


    
    
