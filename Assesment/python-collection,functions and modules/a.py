from b import *

def main1():
    print("\t\t\t WELCOME TO TOPS QUIZ GAME CHALLENGE\n")
    '''print("\n")'''
    print("\t\t\t\tSelect your role: ")
    print("Quiz Master (press 1)")
    print("Quiz cracker (press 2)")
    n=int(input("Select your role: "))
    if n==1:
        quizmain()
    elif n==2:
        usermain()
main1()
