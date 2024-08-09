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
        with open("compra.json",encoding="utf-8") as openarchivo:#esto es para abrir el json de compra
            comprita=json.load( openarchivo)
        return comprita

def guardarcompra(compris):
    with open("compra.json", "w") as archivo:#esto es para guardar info en el json de compra
        json.dump(compris,archivo)

def medicamentos():
        medicamenticos=[]
        with open("Medicamentos.json",encoding="utf-8") as archivo:#esto es para abrir el json de compra
          medicamenticos=json.load(archivo)
        return   medicamenticos
def guardarcompra(medi):
    with open("Medicamentos.json", "w") as archivo1:#esto es para guardar info en el json de compra
        json.dump(medi,archivo1)

def menu():#Menú  principal
    print("==============FARMACIA=================\n"
      " ELIGE LA OPCIÖN A LA QUE QUIERES ACCEDER\n"
      "1. REGISTROS DE VENTAS\n"
      "2. REGISTROS DE COMPRAS\n"
      "3. SALIR\n"
      "========================================")
comprass=compras()#json compra
ventas=abrirArchivo()#json ventas
medicinas=medicamentos()
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
        print("")
        print("======lista de Medicamentos====")
        print("")
        for  r  in medicinas[0]["medicina"]:#mostrar medicamentos y precios
            print("-", r["nombre"],"precio:",r["precio"])
        print("======================================")
        nombreMedicamento=input("ingrese el nombre del medicamento :  ")
        cantidadVendida=int(input("ingrese la cantidad :  "))
        precio=int(input("ingrese el precio del medicamento : "))
        print("======================================")
 
        #recopila la información para guardarla en el json de ventas
        ventas[0]["ventas"].append({"fechaVenta":fechaVenta,"paciente":{"nombre":nombre1,"direccion":direccion},"empleado":{ "nombre":nombre2, "cargo":cargo},"medicamentosVendidos":[{
             "nombreMedicamento": nombreMedicamento, "cantidadVendida": cantidadVendida ,"Precio":precio}]})
        print("Su registro se ha hecho con exito!!")
        guardarArchivo(ventas)

       


    if opc==2:
        comprass=compras()

        #pide la info para crear los registros de compras
        print("============REGISTRO DE COMPRAS============\n")  
        fecha=input("ingrese la fecha de compra:  ")
        nombre1=input("ingrese el nombre del proveedor: ")
        contacto=input("ingrese el contacto del proveedor : ")
        nombre2=input("ingrese el nombre del encargado : ")
        cargo=input("ingrese el cargo : ")
        print("")
        print("======lista de Medicamentos====")
        print("")
        for  r  in medicinas[0]["medicina"]:#mostrar medicamentos,stock y precios
            print("-", r["nombre"],"precio:",r["precio"],"stock",r["stock"])
        print("======================================")
        nombreMedicamento=input("ingrese el nombre del medicamento :  ")
        cantidadcomprada=int(input("ingrese la cantidad :  "))
        precio=int(input("ingrese el precio de compra: "))
        print("======================================")
        
        #recopila la información para guardarla en el json de compra
        comprass[0]["compra"].append({"fechaCompra":fecha,"proveedor":{"nombre":nombre1,"contacto":contacto},"medicamentosVendidos":[{
             "medicamentosComprados": nombreMedicamento, "cantidadComprada":  cantidadcomprada ,"precioCompra":precio}]})
        print("Su registro se ha hecho con exito!!")
        guardarcompra(comprass)

    if opc==3:#finaliz el programa
        print("Saliendo del programa...")
        booleanito=False

        
    #desarrollado por Botello Garcia Yurley t.i: 1066085539
                                