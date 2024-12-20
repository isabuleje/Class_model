from department import Department

class University():
    def __init__(self, name, departments):

        if not departments or len(departments) < 1:
            raise ValueError("A universidade deve ter pelo menos 1 departmaneto para funcionar")
        
        self.name = name
        self.departments = []
        for department in departments:
            self.departments.append(Department(department))
    
    def gets_name(self):
        '''Gets the name of the university'''
        return self.name
    
    def get_departments(self):
        '''Gets the name of the university'''
        return self.departments

    def add_departments(self, department):
        '''Adds departments to the list'''
        self.departments.append(Department(department))
        
    def remove_departments(self,department):
        '''Removes departments from the list'''
        if department in self.departments:
            self.departments.remove(department)

    def __repr__(self):
        dept_names = ", ".join([dept.name for dept in self.departments])
        return f"\n Universidade = {self.name} \n Departmentos = {dept_names} \n"