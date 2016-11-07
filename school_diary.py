from stud import Students
from sub import Subjects


class SchoolDiary(object):
    """School diary"""
    def __init__(self, year, students = []):
        self.year = year
        self.students = students
        
    def add_students(self, students):
        for i in students:
            if not isinstance(i, Students):				
				return
        self.students.extend(students)
        
    def get_student(self, fname, lname):
        for stud in self.students:
            #if stud.fname == fname and stud.lname == lname :
            print "\nStudent:"
            print(stud)
            return stud
        return
        
    def print_studs(self):
        print("Students:")
        print("\n".join(str(s) for s in self.students)) 
    
    @property
    def year(self):
        return self.__year
    
    @year.setter
    def year(self, year):
        self.__year = year



