class Teacher():
    def __init__(self, first_name, last_name, date_of_birth, department):
        self.first_name = first_name
        self.last_name = last_name
        self.email = first_name + '.' + last_name + "@university.com"
        self.date_of_birth = date_of_birth
        self.department = department
        self.discipline_teaching = []
        
        
    def get_full_name(self):
        '''Gets the teacher full name'''
        return "{} {}".format(self.first_name, self.last_name)
    
    def assign_disciplines(self, discipline):
        '''Assings the teacher to a discipline'''
        self.discipline_teaching.append(discipline)
        
    
teacher_1 = Teacher('Laura', 'Pastel', '12022999')

print(Teacher.get_full_name(teacher_1))