class Teacher():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.email = first_name + '.' + last_name + "@university.com"
        self.disciplines_teaching = []
        
    def get_full_name(self):
        '''Gets the teacher full name'''
        return f"{self.first_name} {self.last_name}"
        
    def assign_disciplines(self, discipline):
        '''Assings the teacher to a discipline'''
        self.disciplines_teaching.append(discipline)
        discipline.add_teacher(self)

    def remove_disciplines_teaching(self, discipline):
        '''Removes the teacher from a discipline'''
        if discipline in self.disciplines_teaching:
            self.disciplines_teaching.remove(discipline)
            discipline.remove_teacher(self)

    def __str__(self):
        return f"Nome = {self.first_name}"

    def __repr__(self):
        disciplines = ""
        for disc in self.disciplines_teaching:
            disciplines += str(disc)+"\n"
        return f"\n Nome = {self.first_name} \n Disciplinas responsavel = \n{disciplines}\n"
        