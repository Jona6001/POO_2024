#Formas de concatenacion en Python

nombre='Jonathan Rios'
especialidad='Tecnico Superior Universitario'
carrerra='Desarrollo de software'

#1ra forma
print("Mi nombre es "+nombre+" Estoy en la especialidad de "+especialidad+ " En la carrera de "+carrerra)

#2da forma
print("Mi nombre es ",nombre, " Estoy en la especialidad de ",especialidad, " En la carrera de ",carrerra)


#3ra forma
print(f"Mi nombre es {nombre} Estoy en la especialidad de {especialidad} En la carrera de {carrerra}")


#4ta forma
print("Mi nombre es {} Estoy en la especialidad de {} En la carrera de {}".format(nombre,especialidad,carrerra))

#5ta forma
print('Mi nombre es '+nombre+' Estoy en la especialidad de '+especialidad+ ' En la carrera de '+carrerra)
