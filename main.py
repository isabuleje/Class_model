from university import University
from discipline import Discipline
from teacher import Teacher


#Creating departments
departamento_tecnologia ="Departamento de Tecnologia"
departamento_basico = "Ciclo Basico"

#Creating teachers
teacher_1 = Teacher("Ronalde", "Pereira")
teacher_2 = Teacher("Joana", "Pedra")
teacher_3 = Teacher("Gero", "Nimo")

#Creating disciplines
mat = Discipline("mat", 30, 20)
lp1 = Discipline("lp1", 40, 10)
lp2 = Discipline("lp2", 50, 10)
fisica = Discipline("fisica", 45, 15)

#Creating the university
university = University("UEA", [departamento_tecnologia, departamento_basico])


teacher_1.assign_disciplines(mat)
teacher_1.assign_disciplines(fisica)
teacher_2.assign_disciplines(lp1)
teacher_2.assign_disciplines(lp2)
teacher_3.assign_disciplines(lp1)

departamento_basico.add_teacher(teacher_1)
departamento_tecnologia.add_teacher(teacher_2)
departamento_tecnologia.add_teacher(teacher_3)



print("-----------------------------------------------------------")
print("Informações da universidade: ")
print(university)
print("-----------------------------------------------------------")
print("Informacoes do departamento: ")
print(departamento_tecnologia)
print(departamento_basico)
print("-----------------------------------------------------------")
print("Informacoes das disciplinas: ")
print(mat)
print(lp1)
print(lp2)
print(fisica)
print(" ")
print("-----------------------------------------------------------")
print("Informacoes dos professores:")
print(teacher_1)
print(teacher_2)
print(teacher_3)
