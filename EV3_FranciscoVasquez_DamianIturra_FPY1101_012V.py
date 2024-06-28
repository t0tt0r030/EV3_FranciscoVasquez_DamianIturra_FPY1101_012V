import csv
import random

def certificado (afiliado):
    valor_certificado = random.randint (1000.1500)
    nombre_certificado = f"certificado de afiliacion de {afiliado['nombre']} {afiliado ['apellido_parterno']}"
    print (f"nombre del certificado: {'nombre_certificdo'}")
    print(f"rut: {afiliado['rut']}")
    print(f"nombre:{afiliado['nombre']}")
    print(f"apellido: {afiliado['apellido']}")
    print(f"edad: {afiliado['edad']}")
    print(f"estado civil: {afiliado['estado_civil']}")
    print(f"genero: {afiliado ['genero']}")
    print(f"fecha afiliacion:  {afiliado['fecha_afiliacion']}")
    print(f"valor de certificado: {afiliado[valor_certificado]}")

    with open(f"{afiliado['nombre']}{afiliado['apellido']}certificado.csv", newline = '') as file:
        writer = csv.writer(file)
        writer.writerow("nombre del certificado", "nombre del afiliado", "rut", "nombre", "apellido", "edad", "estado civil", "genero", "fecha afiliacion", "valor certificado")
        writer.writerow([nombre_certificado, f"{afiliado['nombre']} {afiliado['apellido']}", {afiliado['rut']}, {afiliado['nombre']}, {afiliado['apellido']}, {afiliado['edad']}, {afiliado['estado_civil']}, {afiliado['genero']}, {afiliado['fecha_afiliacion']}, valor_certificado]) 
def menu ():
    afiliados:[]
    while True:
        print("\nMenú:")
        print("1.-Grabar datos de afiliado")
        print("2.-Buscar datos de afiliado por su rut")
        print("3.-Imprimir certificado")
        print("4.-Salir")

        opcion=input("Selccione una opción: ")
        if opcion == "1":
            rut=input("Ingrese rut: ")
            nombre=input("Ingrese Nombre: ")
            apellido=input("Ingrese Apellido: ")
            edad=input("Ingrese edad: ")
            if int(edad)<=18:
                print("Debe ser mayor de edad")
            estado_civil=input("Ingrese estado civil (C=Casado, S=soltero, V=Viudo)")
            if estado_civil.lower() not in ['C','S','V']:
                print("Estado civil invalido. Intente nuevamente")
                
            genero=input("ngrese Genero (F= Femenino, M=Masculino)")
            if genero.lower() not in ['F','M']:
                print("Genero invalido")

            afiliado={
                'rut': rut,
                'nombre':nombre,
                'apellido': apellido,
                'edad':edad,
                'estado_civil':estado_civil,
                'genero':genero,
                'fecha_afiliacion':input("Ingrese fecha de afiliacion (dd-mm-aa)")
            }
            afiliado.append(afiliado)
            print("afiliado registado correctamente.")
            
        elif opcion =="2":
            rut_buscar = input("Ingrese el rut: ")
            for afiliado in afiliados:
                if afiliado['rut']==rut_buscar:
                    print("informacion del afiliado")
                    print(f"Rut: {afiliado['rut']}")
                    print(f"nombre{afiliado['nombre']}")
                    print(f"apellido{afiliado['apellido']}")
                    print(f"edad{afiliado['edad']}")
                    print(f"estado civil{afiliado['estado_civil']}")
                    print(f"genero{afiliado['genro']}")
                    print(f"fecha de afiliacion{afiliado['fecha_afiliacion']}")
                    encontrado = True
                    break
            if not encontrado:
                print("El rut no aparece")
        elif opcion =="3":
            if not afiliados:
                print("no hay afiliado registrado")
            for afiliado in afiliados:
                certificado(afiliado)
                print("certificado impreso")
        elif opcion == "4":
            print("Ha salido del programa")
            print("este programa fue creado por: Damian_Iturra en Colaborcion de Francisco_Vasquez ")
            print("Version: 6.6.6")
menu()                    