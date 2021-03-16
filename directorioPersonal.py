import os
import json

class directorio:
    directorioPersonal = {}
    
    def __init__ (self, duenoNombre, duenoApellido, duenoEdad, duenoCorreo, duenoTelefono, duenoCedula, contactos):
        self.directorioPersonal["duenoNombre"] = duenoNombre
        self.directorioPersonal["duenoApellido"] = duenoApellido
        self.directorioPersonal["duenoEdad"] = duenoEdad
        self.directorioPersonal["duenoCorreo"] = duenoCorreo
        self.directorioPersonal["duenoTelefono"] = duenoTelefono
        self.directorioPersonal["duenoCedula"] = duenoCedula
        self.directorioPersonal["contactos"]= contactos

    def mostrarDueno (self):
        print("\n1 - Mostrar información del dueño de este directorio personal\n")
        print("   Nombre: "+self.directorioPersonal["duenoNombre"])
        print("   Apellido: "+self.directorioPersonal["duenoApellido"])
        print("   Edad: "+self.directorioPersonal["duenoEdad"])
        print("   Correo: "+self.directorioPersonal["duenoCorreo"])
        print("   Teléfono: "+self.directorioPersonal["duenoTelefono"])
        print("   Cédula: "+self.directorioPersonal["duenoCedula"]+"\n")
    
    def addContacto (self):
        contactoNuevo=contacto()
        self.directorioPersonal["contactos"].append(contactoNuevo.dirContacto)
        print(type(self.directorioPersonal["contactos"][0]))
    
    def buscarContacto (self):
        nombreBuscado=input("\n Por favor digite el nombre, cualquier apellido del contacto: ")
        numEnc = 1

        for contactoDeseado in self.directorioPersonal["contactos"]:
            if (contactoDeseado["nombre"] == nombreBuscado):
                print("\nContacto encontrado:")
                print("   Nombre: "+contactoDeseado["nombre"])
                print("   Primer apellido: "+contactoDeseado["primerApellido"])
                print("   Segundo apellido: "+contactoDeseado["segundoApellido"])
                print("   Edad: "+contactoDeseado["edad"])
                print("   Correo: "+contactoDeseado["correo"])
                print("   Teléfono: "+contactoDeseado["telefono"])
                print("   Cédula: "+contactoDeseado["cedula"]+"\n")               
            
            elif (contactoDeseado["primerApellido"] == nombreBuscado):
                print("\nContacto encontrado:")
                print("   Nombre: "+contactoDeseado["nombre"])
                print("   Primer apellido: "+contactoDeseado["primerApellido"])
                print("   Segundo apellido: "+contactoDeseado["segundoApellido"])
                print("   Edad: "+contactoDeseado["edad"])
                print("   Correo: "+contactoDeseado["correo"])
                print("   Teléfono: "+contactoDeseado["telefono"])
                print("   Cédula: "+contactoDeseado["cedula"]+"\n")
                numEnc += 1

            elif (contactoDeseado["segundoApellido"] == nombreBuscado):
                print("\nContacto encontrado:")
                print("   Nombre: "+contactoDeseado["nombre"])
                print("   Primer apellido: "+contactoDeseado["primerApellido"])
                print("   Segundo apellido: "+contactoDeseado["segundoApellido"])
                print("   Edad: "+contactoDeseado["edad"])
                print("   Correo: "+contactoDeseado["correo"])
                print("   Teléfono: "+contactoDeseado["telefono"])
                print("   Cédula: "+contactoDeseado["cedula"]+"\n")

            elif (numEnc == len(self.directorioPersonal["contactos"]) ):
                print("\nContacto no encontrado\n")
            
            numEnc += 1

    def retornarDir (self):
        return self.directorioPersonal

class contacto:    
    
    def __init__ (self):
        print ("Aggregar nuevo contacto\n")
        self.cedula=input("Cédula: ")
        self.nombre=input("Nombre: ")
        self.primerApellido=input("Primer apellido: ")
        self.segundoApellido=input("Segundo apellido: ")
        self.edad=input("Edad: ")
        self.correo=input("Correo electrónico: ")
        self.telefono=input("Número de teléfono: ")

        self.dirContacto={"cedula":self.cedula,"nombre":self.nombre,"primerApellido":self.primerApellido,"segundoApellido":self.segundoApellido,"edad":self.edad,"correo":self.correo,"telefono":self.telefono}

def menu(dirActual):
    loop = "true"
    while loop == "true":
        accion=int(input(
    """ Seleccione una acción:
        1 - Mostrar información del dueño de este directorio personal
        2 - Ingresar un contacto a mi lista
        3 - Buscar un contacto de mi lista (Pueder usar: nombre, primer apellido o segundo apellido)
        4 - Eliminar un contacto de mi lista
        5 - Salir del directorio (cambios se salvarán al salir)

        Opcion: """))

        if accion == 1:            
            dirActual.mostrarDueno()
        elif accion == 2:
            dirActual.addContacto()
        elif accion == 3:
            dirActual.buscarContacto()
        elif accion == 4:
            pass
        elif accion == 5:
            loop = "false"



def main():
    cedula=input("\n\n**************************************\n Bienvenido a su Directorio Personal.\n         Por favor digite su cédula: ")
    directorioArchivo=cedula+"_contactos.json"

    if os.path.exists(directorioArchivo):
        f = open(directorioArchivo, "r+")
        data = json.load(f)        
        print ("\n\nEcontrado directorio personal para: "+data["duenoNombre"]+" "+data["duenoApellido"]+"")
        dirActual=directorio(data["duenoNombre"], data["duenoApellido"], data["duenoEdad"], data["duenoCorreo"], data["duenoTelefono"], data["duenoCedula"], data["contactos"])
    else:
        print ("Nuevo usuario, creando nuevo directorio\n")
        duenoNombre=input("¿Cuál es su nombre? ")
        duenoApellido=input("¿Cuál es su apellido? ")
        duenoEdad=input("¿Qué edad tiene? ")
        duenoCorreo=input("¿Cuál es su correo electrónico? ")
        duenoTelefono=input("¿Cuál es su teléfono? ")
        contactos=[]

        print("\n Creando su nuevo directorio personal\n")
       
        dirActual=directorio(duenoNombre, duenoApellido, duenoEdad, duenoCorreo, duenoTelefono, cedula, contactos)
        
        f = open(directorioArchivo, "w")
    
    menu(dirActual)

    f.seek(0)
    json.dump(dirActual.retornarDir(), f , indent=2)    
    f.close()



if __name__ == "__main__":
    main()

    
