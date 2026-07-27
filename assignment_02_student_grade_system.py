def get_grade(score):
   if score < 0 or score > 100:
       return "Invalid score"
   elif score >= 80:
       return "A"
   elif score >= 70:
       return "B"
   elif score >= 60:
       return "C"
   elif score >= 50: 
       return "D"                  
   else:
         return "F"

  if __name__ == "__main__":
      score = int(input("Enter the student's score (0-100): "))
      grade = get_grade(score)
      if grade == "Invalid score":
          print( "Error: The score must be between 0 and 100.")
        else:
          print(f"The student's grade is: {grade}")