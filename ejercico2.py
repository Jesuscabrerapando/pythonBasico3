def notas():
    nota=int(input('dime la nota del hito individual'))
    nota2=int(input('dime la nota del hito grupal'))
    nota3=int(input('dime la nota del examen'))
    mediafinal=(nota*0.3)+(nota2*0.2)+(nota3*0.5)
    print(mediafinal)
notas()