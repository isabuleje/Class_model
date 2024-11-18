class Department():
    def __init__(self, name):
        self.name = name
        self.email = name + '.' + '@university.com'
        self.teachers = []

    def add_teacher(self, teacher):
        '''Adds a teacher to the teacher list'''
        self.teachers.append(teacher)
        teacher.department = self

    def remove_teacher(self, teacher):
        '''Removes teacher from the teachers list'''
        if teacher in self.teachers:
            self.teachers.remove(teacher)
            
    def __str__(self):
        teacher_names = ", ".join(teacher.get_full_name() for teacher in self.teachers)
        return f"\n Departmento = {self.name} \n Professores = {teacher_names} \n"