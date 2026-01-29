import unittest
from main import GestorContactos  # Importamos la clase del archivo principal

class TestGestorContactos(unittest.TestCase):
    
    def setUp(self):
        """Se ejecuta antes de cada prueba para iniciar con una lista limpia."""
        self.gestor = GestorContactos()
        # Agregamos un contacto base para pruebas
        self.gestor.agregar_contacto("Juan Perez", "123456789", "juan@test.com", "Calle 1")

    def test_agregar_contacto(self):
        """Prueba que el contacto se agregue a la lista."""
        inicial = len(self.gestor.contactos)
        self.gestor.agregar_contacto("Ana Gomez", "987654321", "ana@test.com", "Calle 2")
        final = len(self.gestor.contactos)
        self.assertEqual(final, inicial + 1)

    def test_buscar_contacto_existente(self):
        """Prueba la búsqueda por nombre."""
        contacto = self.gestor.buscar_contacto("Juan Perez")
        self.assertIsNotNone(contacto)
        self.assertEqual(contacto.telefono, "123456789")

    def test_buscar_contacto_inexistente(self):
        """Prueba buscar alguien que no existe."""
        contacto = self.gestor.buscar_contacto("Fantasma")
        self.assertIsNone(contacto)

    def test_eliminar_contacto(self):
        """Prueba eliminar un contacto."""
        resultado = self.gestor.eliminar_contacto("Juan Perez")
        self.assertTrue(resultado)
        self.assertEqual(len(self.gestor.contactos), 0)

if __name__ == '__main__':
    unittest.main()