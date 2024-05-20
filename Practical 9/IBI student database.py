# Keep a record of the students in IBI1 

# create a class 
class students:
    # initialise with the parameter mention in practical 9 guidance 
    def __init__ (self, name, majors, portfolio_score, project_score, exam_score):
       # provided value for the parameters
       self.name = name 
       self.majors = majors
       self.portfolio_score = portfolio_score
       self.project_score = project_score
       self.exam_score = exam_score
    
    # ensure the portfolio score marks are out of 100 
    def correct_portfolio_score (self, portfolio_score):
        if not 0 <= int (self.portfolio_score) <= 100:
            print ("Invalid portfolio score, enter score between 0 to 100")
        return portfolio_score
    
    # ensure the project score marks are out of 100 
    def correct_project_score (self, project_score):
        if not 0 <= int (self.project_score) <= 100:
            print ("Invalid project score, enter score between 0 to 100")
        return project_score
    
    # ensure the exam score marks are out of 100 
    def correct_exam_score (self, exam_score):
        if not 0 <= int (self.exam_score) <= 100:
            print ("Invalid exam score, enter score between 0 to 100")
        return exam_score
    
    def introducte_self (self):
        print ("My name is " + self.name)
        print ("My majors is " + self.majors)
        print ("My portfolio score is " + self.portfolio_score + " marks")
        print ("My group project score is " + self.project_score + " marks")
        print ("My exam score is " + self.exam_score + " marks")

# create a example of class with provided information 
student1 = students("Teo Li Xian", "IBI", "101","80","80" )

# call out the funciton 
student1.introducte_self()
student1.correct_portfolio_score (portfolio_score=101)
student1.correct_project_score (project_score=80)
student1.correct_exam_score (exam_score=80)
