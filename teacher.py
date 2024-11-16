class Teacher():
    def __init__(self, first_name, last_name, date_of_birth, department):
        self.first_name = first_name
        self.last_name = last_name
        self.email = first_name + '.' + last_name + "@university.com"
        self.date_of_birth = date_of_birth
        self.department = department
        self.discipline_teaching = []
        
        
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)
    
    def get_disciplines(self):
        pass
        
    def assign_disciplines(self, discipline):
        pass
    
teacher_1 = Teacher('Laura', 'Pastel', '12022999')

print(Teacher.full_name(teacher_1))