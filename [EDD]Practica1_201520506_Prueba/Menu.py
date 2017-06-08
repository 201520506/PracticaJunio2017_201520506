import os
import lista
import Pila_Cola

usuario = lista.Lista()
Cola = Pila_Cola.Cola()
Pila = Pila_Cola.Pila()
newmatriz = []
transpuesta =[]


#LEER ARCHIVO
def leer():

    archivo1 = open("entrada.xml", 'r')
    linea = archivo1.readline()
    cox = None
    coy = None
    while linea != "":
        if linea == "<operacion>\n":
            linea = archivo1.readline()
            per = linea.strip('\n\t\r')
            Cola.add(per)
        if cox == None:
            if linea == "<matriz>\n":
                linea = archivo1.readline()
                array = linea.split(">")
                x = array[1].split("<")
                cox = x[0]
                linea = archivo1.readline()
                array = linea.split(">")
                y = array[1].split("<")
                coy = y[0]
        linea = archivo1.readline()
    valor = str(cox) + "," + str(coy)
    archivo1.close()

    return valor
def operar():
    dato = Cola.sacar()
    opere = dato.split(" ")
    for x in range(len(opere)):
        Pila.push(opere[x])
        if opere[x] is "+":
            Pila.pop()
            numero1 = Pila.pop()
            numero2 = Pila.pop()
            resultado = int(numero2) + int(numero1)
            Pila.push(resultado)
            print (str(numero2) + "+" + str(numero1) + "=" + str(resultado))
        if opere[x] is "*":
            Pila.pop()
            numero1 = Pila.pop()
            numero2 = Pila.pop()
            resultado = int(numero1) * int (numero2)
            Pila.push(resultado)
            print (str(numero2) + "*" + str(numero1) + "=" + str(resultado))
        if opere[x] is "-":
            Pila.pop()
            numero1 = Pila.pop()
            numero2 = Pila.pop()
            resultado = int(numero2) - int (numero1)
            Pila.push(resultado)
            print (str(numero2) + "-" + str(numero1) + "=" + str(resultado))

def menu():
    print("""\n--------- MENU PRINCIPAL --------    
    1. Crear Usuario
    2. Ingresar al Sistema
    3. Salir del Programa    
    """)

def sistema():
    print ("""\n--------- SISTEMA ----------
    1. Leer Archivo
    2. Resolver Operaciones
    3. Operar la Matriz
    4. Mostrar Usuarios
    5. Mostrar Cola
    6. Cerrar Sesion
     """)

def resolverop():
    print ("""\n--------- OPERACIONES ----------
       1. Operar Siguiente
       2. Regresar      
        """)

def matriz():
        print ("""\n--------- MATRIZ ----------
    1. Ingresar dato
    2. Operar transpuesta
    3. Mostrar matriz original
    4. Mostrar matriz transpuesta
    5. Regresar
    """)
while True:
#MENU
    menu()
    menu1 = raw_input("Ingrese Una Opcion \n")
    if menu1 == '1':
        user = raw_input("User Name:")
        password = raw_input("Password:")
        usuario.InsertarPrimero(str(user),str(password))
#INGRESAR AL SISTEMA
    elif menu1 == '2':
        nombre = raw_input("Ingrese su User Name:")
        con = raw_input("Ingrese su Password:")
        if usuario.login(nombre, con) == True:
#SISTEMA
            while True:
                sistema()
                sis1 = raw_input("Ingrese Una Opcion \n")
#LEER ARCHIVO
                if sis1 == '1':
                    cordenadas = leer().split(",")
                    for i in range(int(cordenadas[0])):
                        newmatriz.append([0] * (int(cordenadas[1])))
                    for j in range(int(cordenadas[1])):
                        transpuesta.append([0]*(int(cordenadas[0])))

#OPERACIONES
                elif sis1 == '2':
                    while True:
                        resolverop()
                        op = raw_input("Ingrese Una Opcion \n")#OPERAR
                        if op == '1':
                            operar()
#SALIR
                        elif op == '2':
                            break
                        else:
                            print ("DEBE DE SELECCIONAR ALGUNA OPCION")

                elif sis1 == '3':
                    while True:
                        matriz()
                        ma = raw_input("Ingrese Una Opcion \n")
                        if ma == '1':
                            ejex = raw_input("Ingrese Coordenada en X:  ")
                            ejey = raw_input("Ingrese Coordenada en Y:  ")
                            valor = raw_input("Ingrese valor:  ")
                            newmatriz[int(ejex)][int(ejey)] = valor
                        elif ma == '2':
                            for l in range((int(cordenadas[1]))):
                                for t in range((int(cordenadas[0]))):
                                   transpuesta[l][t] = newmatriz[t][l]
                        elif ma == '3':
                            val = ""
                            for l in range((int(cordenadas[1]))):
                                for t in range((int(cordenadas[0]))):
                                    val = val + newmatriz[t][l] + ","
                                    val = val.strip(',')
                                print "|" + str(val) + "|"
                                val = ""
                        elif ma == '4':
                            val2 = ""
                            for l in range((int(cordenadas[0]))):
                                for t in range((int(cordenadas[1]))):
                                    val2 = val2 + transpuesta[t][l] + ","
                                    val2 = val2.strip(',')
                                print "|" + str(val2) + "|"
                                val2 = ""
                        elif ma == '5':
                           break
                        else:
                           print ("DEBE DE SELECCIONAR ALGUNA OPCION")
#MOSTRAR USUARIO
                elif sis1 == '4':
                    usuario.Listar()
                    usuario.listarCola()
#MOSTRAR COLA DE OPERACIONES
                elif sis1 == '5':
                    Cola.mostrar()
#SALIR
                elif sis1 == '6':
                    break
                else:
                    print ("DEBE DE SELECCIONAR ALGUNA OPCION")
        else:
            print ("NO SE ENCONTRO NINGUN USUARIO")
    elif menu1 == '3':
        print("CHAO...")
        break
    else:
        print ("DEBE DE SELECCIONAR ALGUNA OPCION")

