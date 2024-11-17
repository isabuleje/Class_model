from university import University
from discipline import Discipline
from department import Department
from teacher import Teacher

university = University("Uea")

#Creating departments
fisioterapy_department = Department("Fisioterapia", "Rue", "001")
water_department = Department("agua", "Fernande", "002")

#Adding the departments to university
university.add_departments(fisioterapy_department)
university.add_departments(water_department)

#Creating teachers
teacher_1 = Teacher("Ronalde", "Ultimo", "23120023", "Fisioterapia")
teacher_2 = Teacher("Luize", "Jk", "2783283", 'agua')

#Adding the teachers to departments
fisioterapy_department.add_teacher(teacher_1)
water_department.add_teacher(teacher_2)

#Creating disciplines
matematica_aff = Discipline("mat", "30", "30", "100")

#Adding discipline to a department
fisioterapy_department.add_discipline(matematica_aff)

#Adding teacher to a discipline
matematica_aff.assign_teacher(teacher_1)
