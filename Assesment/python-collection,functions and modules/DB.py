import mysql.connector as connector


# Class for Quiz Master
class Quizhelper():
    
    def __init__(self):
        self.con=connector.connect(host='localhost',user='root',password='',database='quiz')
        
    
    #insert questions
    def insert_quiz(self,queno,ques,opta,optb,ans):
        query="INSERT INTO mcqquiz VALUES({},'{}','{}','{}','{}')".format(queno,ques,opta,optb,ans)
        cur = self.con.cursor()
        cur.execute(query)
        #Commit means changing in database physically or really.
        #if we dont use commit() then it will only show output in cmd but the real db did not get changed. Thats why we have to use commit
        self.con.commit()
        print('Question Saved To Database')

        
    # quiz master can view questions
    def fetch_quiz(self):
        query='SELECT * FROM mcqquiz'
        cur=self.con.cursor()
        cur.execute(query)
        for row in  cur:  
            print('Question No:',row[0])
            print('Question:',row[1])         
            print('Option 1:',row[2])
            print('Option 2:',row[3])
            print('Answer:',row[4])
            print()
            print()

# Class for Quiz cracker
class User_Quiz():
    def __init__(self):
        self.con=connector.connect(host='localhost',user='root',password='',database='quiz')

    def fetch_que(self):
        que='select * from mcqquiz'    # Query to see all qustions from table
        cur=self.con.cursor()
        cur.execute(que)

        for row in cur:  
            print('Que No:',row[0],'>','Question:',row[1])
            print('Option 1:',row[2])
            print('Option 2:',row[3])
            print()
            num=input('Enter Your Answer(A | B): ')
            if num==row[4]:
                print("Correct Answer")
            else:
                print("Wrong Answer")
        
