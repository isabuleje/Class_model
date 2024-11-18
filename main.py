from university import University
from discipline import Discipline
from department import Department
from teacher import Teacher

#Creating teachers
teacher_1 = Teacher("Ronalde", "Ultimo")
teacher_2 = Teacher("Luize", "Jk")

#Creating disciplines
matematica_aff = Discipline("B232", "mat", 30, 20)

departamento_tecnologia = Department("Departamento de Tecnologia", [teacher_1], [matematica_aff])

university = University("UEA", [departamento_tecnologia])

print("Informações da universidade: ")
print(university)
print("Informacoes do departamento")
print(departamento_tecnologia)
print("Informacoes das disciplinas: ")
print(matematica_aff)
print("Informacoes dos professores:")
print(teacher_1)