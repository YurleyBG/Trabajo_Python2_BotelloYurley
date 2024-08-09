import json #libreria json

def abrirArchivo():
    datos=[]
    with open("Ventas.json", encoding="utf-8") as openfile:#esto es para abrir el json de ventas
        datos=json.load(openfile)
    return datos

def guardarArchivo(dato):
    with open("Ventas.json", "w") as file:#esto es para guardar info en el json de ventas
        json.dump(dato,file)

def compras():
        comprita=[]
        with open("compra.json",encoding="utf-8") as openarchivo:
            comprita=json.load( openarchivo)
        return comprita

def guardarcompra(compris):
    with open("compra.json", "w") as archivo:
        json.dump(compris,archivo)

def menu():#primer menú o principal
    print("==============FARMACIA=================\n"
      " ELIGE LA OPCIÖN A LA QUE QUIERES ACCEDER\n"
      "1. REGISTROS DE VENTAS\n"
      "2. REGISTROS DE COMPRAS\n"
      "3. SALIR\n"
      "========================================")
comprass=compras()
ventas=abrirArchivo()
booleanito=True
while booleanito==True:
    menu()#abre el primer menú
    print("Elige una opción por favor")
    opc=int(input())
    
    if opc==1:
       
        ventas=abrirArchivo()
        #pide info para agregar cada registro de venta
        print("============REGISTRO DE VENTAS============\n")  
        fechaVenta=input("ingrese la fecha de venta :  ")
        nombre1=input("ingrese el nombre del paciente : ")
        direccion=input("ingrese la dirección : ")
        nombre2=input("ingrese el nombre del encargado : ")
        cargo=input("ingrese el cargo : ")
        nombreMedicamento=input("ingrese el nombre del medicamento :  ")
        cantidadVendida=int(input("ingrese la cantidad :  "))
        precio=int(input("ingrese el precio del medicamento : "))
        print("======================================")

        ventas[0]["ventas"].append({"fechaVenta":fechaVenta,"paciente":{"nombre":nombre1,"direccion":direccion},"empleado":{ "nombre":nombre2, "cargo":cargo},"medicamentosVendidos":[{
             "nombreMedicamento": nombreMedicamento, "cantidadVendida": cantidadVendida ,"Precio":precio}]})
        print("Su registro se ha hecho con exito!!")
        guardarArchivo(ventas)
    if opc==2:
        comprass=compras()
        #pide la info para crear los registrod de compras
        print("============REGISTRO DE COMPRAS============\n")  
        fecha=input("ingrese la fecha de compra:  ")
        nombre1=input("ingrese el nombre del proveedor: ")
        contacto=input("ingrese el contacto del proveedor : ")
        nombre2=input("ingrese el nombre del encargado : ")
        cargo=input("ingrese el cargo : ")
        nombreMedicamento=input("ingrese el nombre del medicamento :  ")
        cantidadVendida=int(input("ingrese la cantidad :  "))
        precio=int(input("ingrese el precio de compra: "))
        print("======================================")

        comprass[0]["compra"].append({"fechaCompra":fecha,"proveedor":{"nombre":nombre1,"contacto":contacto},"medicamentosVendidos":[{
             "medicamentosComprados": nombreMedicamento, "cantidadComprada": cantidadVendida ,"precioCompra":precio}]})
        print("Su registro se ha hecho con exito!!")
        guardarcompra(comprass)
    if opc==3:
        print("Saliendo del programa...")
        booleanito=False