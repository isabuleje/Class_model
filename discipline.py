class Discipline():
    def __init__(self, name, hours, credits):
        self.name = name
        self.hours = hours
        self.credits = credits
        self.teachers = []
    
    def get_teachers(self):
        return self.teachers

    def add_teacher(self, teacher):
        '''It assigns a teacher to the discipline'''
        self.teachers.append(teacher)

    def remove_teacher(self, teacher):
        if teacher in self.teachers:
            self.teachers.remove(teacher)
    
    def change_hours(self, new_hours):
        '''Changes the hours of a discipline'''
        self.hours = new_hours

    def change_credits(self,new_credits):
        '''Changes the credits of a discipline'''
        self.credits = new_credits
    
    def __str__(self):
        return f"Disciplina = {self.name}"
    
    def __repr__(self):
        teachers = ""
        for teacher in self.teachers:
            teachers += str(teacher)+"\n"
        return f"\n    Disciplina = {self.name} \n Professor = \n {teachers} \n"