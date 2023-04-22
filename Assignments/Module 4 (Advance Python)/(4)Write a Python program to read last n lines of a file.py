#Write a Python program to read last n lines of a file

def lastNline(file,n):
    with open(file) as f:
        print("Last",n," Lines from file : ",file)
        for i in (f.readlines()[-n:]):
            print(i,end='')
file=input("Enter file Name :")
n=int(input("Enter no of lines to read :"))
try:
    lastNline(file,n)
except:
    print("file does not found.......")
        
    
