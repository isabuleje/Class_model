from university import University
from discipline import Discipline
from department import Department
from teacher import Teacher

#Creating teachers
teacher_1 = Teacher("Ronalde", "Ultimo")
teacher_2 = Teacher("Luize", "Jk")
teacher_3 = Teacher("Gero", "Nimo")

#Creating disciplines
matematica_aff = Discipline("mat", 30, 20)
lp1 = Discipline("lp1", 40, 10)
lp2 = Discipline("lp2", 50, 10)
fisica = Discipline("fisica", 45, 15)

departamento_tecnologia = Department("Departamento de Tecnologia")
departamento_basico = Department("Ciclo Basico")

university = University("UEA", [departamento_tecnologia, departamento_basico])


teacher_1.assign_disciplines(matematica_aff)
teacher_1.assign_disciplines(fisica)
teacher_2.assign_disciplines(lp1)
teacher_2.assign_disciplines(lp2)
teacher_3.assign_disciplines(lp1)

departamento_basico.add_teacher(teacher_1)
departamento_tecnologia.add_teacher(teacher_2)
departamento_tecnologia.add_teacher(teacher_3)

print("Informações da universidade: ")
print(university)
print("Informacoes do departamento")
print(departamento_tecnologia)
print(departamento_basico)
print("Informacoes das disciplinas: ")
print(matematica_aff)
print(lp1)
print(lp2)
print(fisica)
print("Informacoes dos professores:")
print(teacher_1)
print(teacher_2)
print(teacher_3)