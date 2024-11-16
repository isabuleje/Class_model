from department import Department

class University(Department):
    def __init__(self):
        self.disciplines = []
        self.teachers = []
        self.departments = []
        
    def add_discipline(self, discipline):
        self.disciplines.append(discipline)
        
    def add_teacher(self, teacher):
        self.teachers.append(teacher)
        
    def get_discipline(self):
        pass
        