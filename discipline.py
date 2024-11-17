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
    
    def change_hours(self, new_hours):
        '''Changes the hours of a discipline'''
        self.hours = new_hours

    def change_credits(self,new_credits):
        '''Changes the credits of a discipline'''
        self.credits = new_credits
   