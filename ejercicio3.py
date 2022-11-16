#Se pide calcular la nota de tu examen tipo test.
#Serán 20 preguntas
#Las preguntas correctas sumarán 0,5
#Las preguntas incorrectas restarán 0,25
#Las preguntas sin contestar tendrán 0

def notaexamen():
    correctas=int(input('dime cuantas preguntas has acertado'))
    incorrectas=int(input('dime cuantas preguntas has fallado'))
    sinresponder=int(input('dime cuantas preguntas hay sin responder'))
    notaexamen=(correctas*0.5)-(incorrectas*0.25)+(sinresponder*0)
    print(f'Has sacado un {round(notaexamen)} ')
notaexamen()