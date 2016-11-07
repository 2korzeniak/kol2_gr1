#
# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.

#!/usr/bin/python

from stud import Students
from sub import Subjects
from school_diary import SchoolDiary

student1 = Students("Andrzej", "Duda")
student2 = Students("Johnny", "Bravo")
subject1 = Subjects("Religia", "prof. Wojtyla")
subject2 = Subjects("Chemia", "dr Oetker")
subject3 = Subjects("ZTI", "dr inz. Antonio")
student1.add_subject_to_stud([subject1,subject2])
student2.add_subject_to_stud([subject2,subject3])
student1.add_grade("Religia", [2.0, 3.0, 4.0])
student1.add_grade("Chemia", [4.0, 5.0, 5.0])
student2.add_grade("Chemia", [3.0, 3.0, 4.0])
student2.add_grade("ZTI", [4.0, 4.0, 5.0])

d = SchoolDiary("2016")
d.add_students([student1,student2])
d.print_studs()

std = d.get_student("Andrzej", "Duda").average().sub_average("Religia").add_attendance("Religia", 5)
std.print_attend()