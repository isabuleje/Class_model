class Teacher():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.email = first_name + '.' + last_name + "@university.com"
        self.department_name = None
        self.disciplines_teaching = []
        
    def get_full_name(self):
        '''Gets the teacher full name'''
        return f"{self.first_name} {self.last_name}"
        
    def assign_disciplines(self, discipline):
        '''Assings the teacher to a discipline'''
        self.disciplines_teaching.append(discipline)

    def remove_disciplines_teaching(self, discipline):
        '''Removes the teacher from a discipline'''
        if discipline in self.disciplines_teaching:
            self.disciplines_teaching.remove(discipline)


    def __repr__(self):
        
        return f"\n Nome = {self.first_name} \n Departmento = {self.department_name if self.department_name else 'None'} \n Disciplinas responsavel = {self.disciplines_teaching} \n"