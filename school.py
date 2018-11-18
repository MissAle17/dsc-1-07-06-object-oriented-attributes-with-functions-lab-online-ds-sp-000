class School():
    def __init__(self, name):
        self.name=name
        self._roster={}
    
    def roster(self):
        return self._roster

    def add_student(self, student_name, grade_level):
        if grade_level in self._roster:
            self._roster[grade_level].append(student_name)
        else: 
            self._roster[grade_level] = [student_name]
        return self._roster
    
    def grade(self,grade_level):
        return self._roster[grade_level]
    
    def sort_roster(self):
        alpha = {}
        for grade_level in self._roster:
            alpha[grade_level] = self._roster[grade_level]
            alpha[grade_level].sort()
        return alpha
                
 