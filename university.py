class University():
    def __init__(self, location, name):
        self.name = name
        self.location = location
        self.departments = []
        
    def add_departments(self, department):
        '''Adds departments'''
        self.departments.append(department)
        
    def gets_departments(self):
        pass
    
    def gets_full_discipline(self):
        '''Grabs a discipline with the department and teacher'''