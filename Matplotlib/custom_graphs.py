import numpy as np
import matplotlib.pyplot as plt

#Dispersión (no une los puntos)
#Configurar el tamaño del gráfico
plt.figure(figsize=(8,6))

hours = [2,3,4,5,6,7,8]
exam_scores_student_1 = [55,60,65,70,75,80,85]
exam_scores_student_2 = [50,58,63,69,74,78,83]

plt.scatter(hours, exam_scores_student_1, marker='o', color='green',  label='Estudiante 1')
plt.scatter(hours, exam_scores_student_2, marker='s', color='red',  label='Estudiante 2')

plt.title('Relación entre horas estudiadas y el puntaje de dos estudiantes')
plt.xlabel('Horas')
plt.ylabel('Puntaje')

plt.show()

#--------------------------------------------------
#Puntos (une las líneas)
#Configurar el tamaño del gráfico
plt.figure(figsize=(8,6))

hours = [2,3,4,5,6,7,8]
exam_scores_student_1 = [55,60,65,70,75,80,85]
exam_scores_student_2 = [50,58,63,69,74,78,83]

plt.plot(hours, exam_scores_student_1, marker='o', color='green', linestyle='-', linewidth= 2, label='Estudiante 1')
plt.plot(hours, exam_scores_student_2, marker='s', color='red', linestyle='--', linewidth= 2, label='Estudiante 2')

plt.title('Relación entre horas estudiadas y el puntaje de dos estudiantes')
plt.xlabel('Horas')
plt.ylabel('Puntaje')

plt.show()