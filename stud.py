from sub import Subjects


class Students(object):
    def __init__(self,fname,lname):
        self.__fname = fname
        self.__lname = lname
        self.attend = {}
        self.grade = {}
        self.subjects = []
        
    def __str__(self):
        return self.__fname + " " + self.__lname
        
    def add_subject_to_stud(self, subjects):
        for s in subjects:
            if not isinstance(s,Subjects):
                return
        self.subjects.extend(subjects)
    
    def add_grade(self, subject, grade):
        if subject in self.grade.keys():
            self.grade[subject].extend(grade)
        else:
            self.grade[subject] = grade
            
    def add_attendance(self, subject, count):
        if subject in self.attend.keys():
            self.attend[subject] += count
        else:
            self.attend[subject] = count
            
    def average(self):
        avg, count = 0, 0
        for i in self.grade:
            for j in self.grade[i]:
                avg += j
                count += 1
        if count!= 0:
            print("Total average is: " + str(avg/count))	
        return self
        
    def sub_average(self, subject):
        avg, count = 0, 0
        for j in self.grade[subject]:
            avg += j
            count += 1
            print(subject + " avarage is: " + str(avg/count))        
        return self
    
    def print_subjects(self):
        print "Student's subjects:"
        print "\n".join(str(s) for s in self.subjects)
        return self 

    def print_grade(self):
        print "\nGrades of:"
        print self
        for i in self.grade:
			print i + ": "
        for y in self.grade[i]:
            print(y)
        return self
	
    def print_attend(self):
        print("\nAttendance:")
        for i in self.attend:
            print(i + ": " + str(self.attend[i]))
        return self
	
    @property
    def fname(self):
        return self.__fname

	@fname.setter
	def fname(self, fname):
		self.__fname = fname

	@property
	def lname(self):
		return self.__lname

	@lname.setter
	def lname(self, lname):
		self.__lname = lname



    
        
    