class Discipline():
    def __init__(self, name, hours, credits, id):
        self.name = name
        self.hours = hours
        self.credits = credits
        self.id = id
        self.teacher = None
        self.department = None
    
    def assign_teacher(self, teacher):
        '''It assigns a teacher to the discipline'''
        self.teacher = teacher
        
        
    
    
        