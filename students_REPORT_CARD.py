class report_card:
    def __init__(self, teachers_name, teacher_password):
        self.teachers_name = teachers_name
        self.teacher_password = teacher_password

    def teacher(self):
        print(f"welcome {self.teachers_name} your password is {self.teacher_password}")
        teacher = int(input("please enter your password please: "))
        if teacher == self.teacher_password:
            print("ok that's you, thank you")
        else:
            print("sorry that's not you")
            exit()

    def input_grades(self):
        print("today you just can make report card for 3 students")

        
        student1 = []
        student2 = []
        student3 = []

 
        student1_average = 0
        student2_average = 0
        student3_average = 0
        
        input_student_name1 = input("please enter the student name: ")
        student1.append(input_student_name1)
        while True:
            input_student_grade = input("What lesson do you want to choose first? "
                                        "Math, Science, English, Computer. "
                                        "If you add all of the score press s: ").lower()
            if input_student_grade == "math":
                student1.append("math")
                math_score = int(input("please enter the score: "))
                student1_average += math_score
                student1.append(math_score)
            elif input_student_grade == "science":
                student1.append("science")
                science_score = int(input("please enter the score: "))
                student1_average += science_score
                student1.append(science_score)
            elif input_student_grade == "english":  
                student1.append("english")
                english_score = int(input("please enter the score: "))
                student1_average += english_score
                student1.append(english_score)
            elif input_student_grade == "computer":
                student1.append("computer")
                computer_score = int(input("please enter the score: "))
                student1_average += computer_score
                student1.append(computer_score)
            elif input_student_grade == "s":
                break
            else:
                print("sorry, we are out of subject")

        
        input_student_name2 = input("please enter the student name: ")
        student2.append(input_student_name2)
        while True:
            input_student_grade2 = input("What lesson do you want to choose first? "
                                         "Math, Science, English, Computer. "
                                         "If you add all of the score press s: ").lower()
            if input_student_grade2 == "math":
                student2.append("math")
                math_score2 = int(input("please enter the score: "))
                student2_average += math_score2
                student2.append(math_score2)
            elif input_student_grade2 == "science":
                student2.append("science")
                science_score2 = int(input("please enter the score: "))
                student2_average += science_score2
                student2.append(science_score2)
            elif input_student_grade2 == "english":  # Fix here: 'english' instead of 'engilish'
                student2.append("english")
                english_score2 = int(input("please enter the score: "))
                student2_average += english_score2
                student2.append(english_score2)
            elif input_student_grade2 == "computer":
                student2.append("computer")
                computer_score2 = int(input("please enter the score: "))
                student2_average += computer_score2
                student2.append(computer_score2)
            elif input_student_grade2 == "s":
                break
            else:
                print("sorry, we are out of subject")

        
        input_student_name3 = input("please enter the student name: ")
        student3.append(input_student_name3)
        while True:
            input_student_grade3 = input("What lesson do you want to choose first? "
                                         "Math, Science, English, Computer. "
                                         "If you add all of the score press s: ").lower()
            if input_student_grade3 == "math":
                student3.append("math")
                math_score3 = int(input("please enter the score: "))
                student3_average += math_score3
                student3.append(math_score3)
            elif input_student_grade3 == "science":
                student3.append("science")
                science_score3 = int(input("please enter the score: "))
                student3_average += science_score3
                student3.append(science_score3)
            elif input_student_grade3 == "english":  # Fix here: 'english' instead of 'engilish'
                student3.append("english")
                english_score3 = int(input("please enter the score: "))
                student3_average += english_score3
                student3.append(english_score3)
            elif input_student_grade3 == "computer":
                student3.append("computer")
                computer_score3 = int(input("please enter the score: "))
                student3_average += computer_score3
                student3.append(computer_score3)
            elif input_student_grade3 == "s":
                break
            else:
                print("sorry, we are out of subject")

        # Printing the results
        print(student1)
        print(student2)
        print(student3)
        print(f"{input_student_name1}'s average is {student1_average/4}")
        print(f"{input_student_name2}'s average is {student2_average/4}")
        print(f"{input_student_name3}'s average is {student3_average/4}")


# Main part of the code
class1 = report_card(input("please enter your teacher name: "), int(input("please enter your password to sign in: ")))
class1.teacher()
class1.input_grades()
