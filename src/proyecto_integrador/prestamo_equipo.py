import datetime

class SistemaPrestamos:
    def __init__(self):
        self.equipos = {
            "PC-01": {"disponible": True, "prestamos": []},
            "Laptop-02": {"disponible": True, "prestamos": []}
        }

    def mostrar_equipos(self):
        for nombre, datos in self.equipos.items():
            estado = "Disponible" if datos["disponible"] else "❌ Prestado"
            print(f"- {nombre}: {estado}")

    def registrar_prestamo(self):
        self.mostrar_equipos()
        nombre = input("\nNombre del equipo para préstamo: ")
        
        if nombre in self.equipos:
            if self.equipos[nombre]["disponible"]:
                usuario = input("Nombre del solicitante: ")
                fecha = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
                

                prestamo = (usuario, fecha)
                self.equipos[nombre]["prestamos"].append(prestamo)
                self.equipos[nombre]["disponible"] = False
                
                print(f"LISTO PA! {nombre} entregado a {usuario}.")
            else:
                print("El equipo ya se encuentra prestado.")
        else:
            print("El equipo no existe en el sistema.")

    def devolver_equipo(self):
        nombre = input("\nNombre del equipo por devolver: ")
        if nombre in self.equipos:
            if not self.equipos[nombre]["disponible"]:
                self.equipos[nombre]["disponible"] = True
                print(f"Equipo {nombre} devuelto correctamente.")
            else:
                print("El equipo ya estaba en el almacen.")
        else:
            print("Equipo no encontrado :(.")

    def ver_historial(self):
        for nombre, datos in self.equipos.items():
            print(f"\nEquipo: {nombre}")
            if not datos["prestamos"]:
                print("   Sin préstamos registrados.")
            else:
                for p in datos["prestamos"]:

                    print(f"   Usuario: {p[0]} | Fecha: {p[1]}")

    def agregar_equipo(self):
        nombre = input("\nNombre del nuevo equipo: ")
        if nombre not in self.equipos:
            self.equipos[nombre] = {"disponible": True, "prestamos": []}
            print(f"Equipo {nombre} gurdado en el sistema.")
        else:
            print("Ese equipo ya está en el sistema.")

def menu():
    sistema = SistemaPrestamos()
    
    while True:
        print("1. Ver equipos")
        print("2. Registrar préstamo")
        print("3. Devolver equipo")
        print("4. Ver historial")
        print("5. Agregar nuevo equipo")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            sistema.mostrar_equipos()
        elif opcion == "2":
            sistema.registrar_prestamo()
        elif opcion == "3":
            sistema.devolver_equipo()
        elif opcion == "4":
            sistema.ver_historial()
        elif opcion == "5":
            sistema.agregar_equipo()
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()