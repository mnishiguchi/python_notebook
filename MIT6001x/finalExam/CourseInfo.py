class courseInfo(object):
    
    # constructor
    def __init__(self, courseName):
        # initialize attributes
        self.courseName = courseName
        self.psetsDone = []    # a list of tuples (p, score)
        self.grade = "No Grade"
        
    def setPset(self, pset, score):
        self.psetsDone.append( (pset, score) )
        
    def getPset(self, pset):
        for (p, score) in self.psetsDone:
            if p == pset:
                return score

    def setGrade(self, grade):
        if self.grade == "No Grade":
            self.grade = grade

    def getGrade(self):
        return self.grade


class edx(object):
    # constructor
    def __init__(self, courses):
        """
        courses: a list of strings(course names)
        """
        # a dict to store key-value pairs of courseName string => courseInfo object
        self.myCourses = {}
        
         #  create key-value pairs and store them in myCourses dict
        for course in courses:
            self.myCourses[course] =  courseInfo(course) 
    
    # **** TODO ****
    # Fill in the code for setGrade, getGrade, setPset, and getPset, using the courseInfo class
    
    def setGrade(self, grade, course="6.01x"):
        """
        grade: integer greater than or equal to 0 and less than or equal to 100
        course: string 

        This method sets the grade in the courseInfo object named by `course`.   

        If `course` was not part of the initialization, then no grade is set, and no
        error is thrown.

        The method does not return a value.
        """
        assert grade <=0 or grade <= 100
        
        # If `course` was not part of the initialization,
        # then no grade is set, and no error is thrown.
        if course in self.myCourses.keys():
            self.myCourses[course].setGrade(grade)            

    def getGrade(self, course="6.02x"):
        """
        course: string 

        This method gets the grade in the the courseInfo object named by `course`.

        returns: the integer grade for `course`.  
        If `course` was not part of the initialization, returns -1.
        """
        # If `course` was not part of the initialization, returns -1
        if course in self.myCourses.keys():
            return self.myCourses[course].getGrade()
        else:
            return -1

    def setPset(self, pset, score, course="6.00x"):
        """
        pset: a string or a number
        score: an integer between 0 and 100
        course: string

        The `score` of the specified `pset` is set for the
        given `course` using the courseInfo object.

        If `course` is not part of the initialization, then no pset score is set,
        and no error is thrown.
        """
        if course in self.myCourses.keys():
            self.myCourses[course].setPset(pset, score)

    def getPset(self, pset, course="6.00x"):
        """
        pset: a string or a number
        course: string        

        returns: The score of the specified `pset` of the given
        `course` using the courseInfo object.
        If `course` was not part of the initialization, returns -1.
        """
        if course in self.myCourses.keys():
            return self.myCourses[course].getPset(pset)
        else:
            return -1


edX = edx( ["6.00x","6.01x","6.02x"] )
edX.setPset(1, 100)
edX.setPset(2, 100,"6.00x")
edX.setPset(2, 90, "6.00x")

edX.setGrade(100)

for c in ["6.00x", "6.01x", "6.02x"]:
    edX.setGrade(90, c)

for c in ["6.00x", "6.01x", "6.02x"]:
    print c, ":",
    print edX.getGrade(c)
