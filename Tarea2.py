def funcion(A,B): #se debe ingresar los strings con las comillas sino tira el error
    if type(A)!=int or type(B)!=int:
        return -15 #comprobar si la entrada es un numero
    if  (A<B):
        return -25
    else:
        resta = A-B
        suma = A+B
        multiplicacion = A*B
        return(resta,suma,multiplicacion)

