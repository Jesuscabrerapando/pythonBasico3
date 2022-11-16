def notaexamen():
    correctas=int(input('dime cuantas preguntas has acertado'))
    incorrectas=int(input('dime cuantas preguntas has fallado'))
    sinresponder=int(input('dime cuantas preguntas hay sin responder'))
    notaexamen=(correctas*0.5)-(incorrectas*0.25)+(sinresponder*0)
    print(notaexamen)
notaexamen()