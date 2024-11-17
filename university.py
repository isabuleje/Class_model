class University():
    def __init__(self, name):
        self.name = name
        self.departments = []
    
    def gets_name(self):
        '''Gets the name from the university'''
        return self.name

    def add_departments(self, department):
        '''Adds departments to the list'''
        self.departments.append(department)
        
    def remove_departments(self,department):
        '''Removes departments from the list'''
        if department in self.departments:
            self.departments.remove(department)
    
    def gets_full_discipline(self):
        '''Grabs a discipline with the department and teacher'''