import statistics

# Create a dictionary
studentDict = {}

# Create a function to display menu 
def displayMenu():

  # This option will involve you adding a student and a collection for their grades to a dictionary!
  print("1. Add a Student")

  # This option will involve you removing a pair from a dictionary!
  print("2. Remove a Student")

  # This option will require you to grab a student from a dictionary and add a quiz grade to it's corresponding collection of grades!
  # You'll also need to use a pre-written function that ensures the user is entering a valid grade (a decimal number)
  print("3. Add Quiz Grade for Student")

  # This option will require you to use a loop to list all of the grades for an INDIVIDUAL student!
  print("4. List a Student's Quiz Grades")

  # This option will have you write a function that takes in a student's grade as a number and return the letter grade equivalent!
  print("5. Get Student's Letter Grade")

  print("6. Quit")

# Function to get grade from user
def getNumberGradeFromUser():

  val = None

  while(val == None):
    try:
      test = float(input("Enter a Grade: "))
      val = test
    except:
      val = None
  
  return val
# Create function for user input


  # Define user input
userInput = ""
  
  # Create While loop
while(userInput != "6"):
  print()
  displayMenu()
  userInput = input("Select an Option: ")
  
  if userInput == "1":
    
    question1 = input("Enter a student name: ")
    # Create list of students
    studentDict[question1] = []

  # create elif statment to connect the if statement before this one 
  elif userInput == "2":
    
    #
    question2 = input("Enter a student name: ")

    # if statement for question 2
    if question2 in studentDict:
      
      # remove name from dictionary 
      studentDict.pop(question2)

      #print name of student removed
      print(f"{question2} removed!")
  
  # user input question 3  
  if userInput == "3":

    # enter student name
    student = input("Enter student name: ")
    
    # student in dictionary ask for grade  
    if student in studentDict:
      
      # get grade for user
      question3 = getNumberGradeFromUser()
      
      #add the grade to the list 
      studentDict[student].append(question3)
  
  # if user inputs question 4 
  if userInput == "4":

    # question 4 for the user
    question4 = input("Enter student name: ")
    
    # if the name is in the dictionary
    if question4 in studentDict:
      
      # print quiz grades
      print(f"{question4}`s quiz grades:")
      
      # pick grade out of dictionary matching the name
      for grade in studentDict[question4]:

        # print grade
        print(grade)

  # if user inputs 5 
  if userInput == "5":

    # question 5 printed out
    question5 = input("Enter a student name: ")

    avgGrade = statistics.mean(studentDict[question5])
    
    ## if statement if student is listed
    if question5 in studentDict:
      
    # find grade correlating to the students name
      for grade in studentDict[question5]:

        # for an a 
        if(90 <= avgGrade <= 100):
          letterGrade = "A"        
        
        # for a b
        if(80 <= avgGrade < 90):
          letterGrade = "B"
        
        # for a c
        if(70 <= avgGrade < 80):
          letterGrade = "C"
        
        # for a d
        if(60 <= avgGrade < 70):
          letterGrade = "D"
        
        # for a e
        if(50 <= avgGrade < 60):
          letterGrade = "E"
        
        # for a f
        if(avgGrade < 50):
          letterGrade = "F"
      
      # print the value which is grade
      print(f"{question5}`s current grade is a {letterGrade}")
  
  # if user inputs 6
  if userInput == "6":

    # print that its over
    print("Program over")