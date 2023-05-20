from DB import *

def quizmain():

    qz=Quizhelper()
    print("\t\t\t WELCOME MASTER\n")
    print("SHAKE YOUR BRAIN AND ADD SOME CHALLENGING QUESTIONS..")
    print()
    while True:
        print("press 1 for add questions")
        print("press 2 for view questions")
        print("press 3 for exit")
        print()
        try:
            choice=int(input("Which Operation you want to perform: "))
            if (choice==1):
                queno=int(input("Enter a question number: "))
                ques=input("Enter a question: ")
                opta=input("Enter Option A: ")
                optb=input("Enter Option B: ")
                ans=input("Enter Answer ? A | B => ")
                qz.insert_quiz(queno,ques,opta,optb,ans)
                
            elif (choice==2):
                print("Questions in quiz")
                print()
                qz.fetch_quiz()

            elif(choice==3):
                break

            else:
                print("Invalid Input ! Try again.")
                
        except Exception as e:
            print(e)
            print("Invalid Input ! Try again.")

def usermain():

    uq=User_Quiz()
    print("********WEL-COME QUIZ-CRACKER********")
    print()
    while True:
        print("Press 1 for play quiz")
        print("Press 2 for exit")
        print()
        ch=int(input("Enter your choice: "))
        if ch==1:
            print("Are you ready to play game? ")
            print("YES(y)/ NO(n)")
            s=input("Enter your choice: ")
            print()
            if s.lower()=='y' or s.lower()=='yes':
                uq.fetch_que()
        elif ch==2:
            break


#def allplaymain():
#    print()
#    print("--------Players and their scores-------")
#    print()
#    pq=ShowUserScore()




                
        
