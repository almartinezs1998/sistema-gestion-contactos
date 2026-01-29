import sys

class Contacto:
    """
    Clase que representa un contacto con sus atributos personales.
    Cumple con el requerimiento de Programación Orientada a Objetos.
    """
    def __init__(self, nombre, telefono, email, direccion):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.direccion = direccion

    def __str__(self):
        return f"Nombre: {self.nombre} | Tel: {self.telefono} | Email: {self.email} | Dir: {self.direccion}"

class GestorContactos:
    """
    Clase encargada de la lógica de negocio: agregar, buscar, editar y eliminar.
    Utiliza una lista para almacenar los objetos Contacto.
    """
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, nombre, telefono, email, direccion):
        nuevo_contacto = Contacto(nombre, telefono, email, direccion)
        self.contactos.append(nuevo_contacto)
        print(f"✅ Contacto '{nombre}' agregado correctamente.")
        return nuevo_contacto

    def buscar_contacto(self, dato):
        """Busca por nombre o teléfono."""
        for contacto in self.contactos:
            if dato.lower() in contacto.nombre.lower() or dato == contacto.telefono:
                return contacto
        return None

    def eliminar_contacto(self, nombre):
        contacto = self.buscar_contacto(nombre)
        if contacto:
            self.contactos.remove(contacto)
            print(f"🗑️ Contacto '{nombre}' eliminado.")
            return True
        else:
            print("❌ No se encontró el contacto.")
            return False

    def editar_contacto(self, nombre_buscar, nuevo_nombre, nuevo_telefono, nuevo_email, nueva_direccion):
        contacto = self.buscar_contacto(nombre_buscar)
        if contacto:
            if nuevo_nombre: contacto.nombre = nuevo_nombre
            if nuevo_telefono: contacto.telefono = nuevo_telefono
            if nuevo_email: contacto.email = nuevo_email
            if nueva_direccion: contacto.direccion = nueva_direccion
            print(f"✏️ Contacto actualizado.")
            return contacto
        return None

# Función para el menú (se ejecuta solo si corres este archivo directamente)
def menu():
    gestor = GestorContactos()
    while True:
        print("\n--- 📞 Sistema de Gestión de Contactos ---")
        print("1. Agregar Contacto")
        print("2. Buscar Contacto")
        print("3. Editar Contacto")
        print("4. Eliminar Contacto")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            n = input("Nombre: ")
            t = input("Teléfono: ")
            e = input("Email: ")
            d = input("Dirección: ")
            gestor.agregar_contacto(n, t, e, d)
        elif opcion == '2':
            d = input("Buscar por Nombre o Teléfono: ")
            res = gestor.buscar_contacto(d)
            print(res if res else "No encontrado.")
        elif opcion == '3':
            b = input("Nombre del contacto a editar: ")
            if gestor.buscar_contacto(b):
                nn = input("Nuevo Nombre (enter para omitir): ")
                nt = input("Nuevo Teléfono (enter para omitir): ")
                ne = input("Nuevo Email (enter para omitir): ")
                nd = input("Nueva Dirección (enter para omitir): ")
                gestor.editar_contacto(b, nn, nt, ne, nd)
            else:
                print("Contacto no existe.")
        elif opcion == '4':
            b = input("Nombre a eliminar: ")
            gestor.eliminar_contacto(b)
        elif opcion == '5':
            sys.exit()

if __name__ == "__main__":
    menu()