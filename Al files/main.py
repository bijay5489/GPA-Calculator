"""GpaCalculator class is a class that calculates the GPA of a student."""
class GpaCalculator:
    # Class variable "quality_points" is a dictionary that maps grades to quality points
    quality_points = {"A+": 4.0, "A": 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0, "B-": 2.7, "C+": 2.3, "C": 2.0, "C-": 1.7, "D+": 1.3, "D": 1.0, "D-": 0.7, "F": 0.0}

    """Constructor for GpaCalculator class"""
    def __init__(self, grades, credit_hours):
        self.grades = grades
        self.credit_hours = credit_hours

    """Method that calculates the GPA of a student"""
    def calculate_gpa(self):
        gpa = 0
        # zip functions makes pairs of items from both lists.
        for grade, credit_hour in zip(self.grades, self.credit_hours):
            gpa += self.quality_points[grade] * credit_hour
        return round(gpa / sum(self.credit_hours), 2) # rounding the GPA to 2 decimal places


"""Reads the file and returns a list of subjects"""
def read_file(filename):
    subjects = []
    # reading file in read ("r") mode.
    with open(filename, 'r') as f:
        for line in f:
            subject = line.strip() # striping incase of spaces
            subjects.append(subject)

    return subjects

"""Calculates the grade of a student according to the marks"""
def calculate_grade(marks):
    if marks >= 97:
        return 'A+'
    elif marks >= 93:
        return 'A'
    elif marks >= 90:
        return 'A-'
    elif marks >= 87:
        return 'B+'
    elif marks >= 83:
        return 'B'
    elif marks >= 80:
        return 'B-'
    elif marks >= 77:
        return 'C+'
    elif marks >= 73:
        return 'C'
    elif marks >= 70:
        return 'C-'
    elif marks >= 67:
        return 'D+'
    elif marks >= 63:
        return 'D'
    elif marks >= 60:
        return 'D-'
    else:
        return 'F'

# Main function that has the driver code to take input from the user and calculate the GPA
def main():
    print("          GPA Calculator")
    print("------------------------------------------")
    # list of files in our directory with all the subjects
    list_of_files = ["1st Year 1st Semester.txt", "1st Year 2nd Semester.txt",
                        "2nd Year 2nd Semester.txt", "2nd Year 2nd Semester.txt",
                        "3rd Year 1st Semester.txt", "3rd Year 2nd Semester.txt",
                        "4th Year 1st Semester.txt", "4th Year 2nd Semester.txt"]
    
    # loading subjects from list of files using read_file function
    files = [read_file(file) for file in list_of_files]
    for i, file in enumerate(list_of_files): # enumerate function returns a tuple of index and value
        file_name = file.split('.')[0] # splitting the file name to get the subject name
        print(f'{i+1}.{file_name}')
    
    grades = []
    credit_hours = []
    print("Enter your final Exam Marks")
    semester = int(input("Choose your semester: "))
    semester = semester - 1
    
    # Loop to take input from the user for the marks and quality points of each subject
    for subject in files[semester]:
        marks = int(input(f"Enter marks for {subject}: "))
        grades.append(calculate_grade(marks))
        credit_hours.append(int(input(f"Enter credit hours for {subject}: ")))
    
    # Instantiating the GpaCalculator class
    gpa_calculator = GpaCalculator(grades, credit_hours)
    print(gpa_calculator.calculate_gpa())


if __name__ == '__main__':
    main()