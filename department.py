
class Department():
    def __init__(self, name, director, id):
        self.name = name
        self.email = name + '.' + '@university.com'
        self.director = director
        self.teachers = []
        self.disciplines = []
        self.id = id
        
    def add_discipline(self, discipline):
        '''Adds the discipline to the discipline list'''
        self.disciplines.append(discipline)
        discipline.department = self
        
    def add_teacher(self, teacher):
        '''Adds a teacher to the teacher list'''
        self.teachers.append(teacher)
        teacher.department = self
        
    def assign_teacher_to_discipline(self, teacher, discipline):
        '''Assigns a teacher to a discipline and a discipline to a teacher'''
        discipline.assign_teacher(teacher)
        teacher.add_discipline(discipline)
                
        