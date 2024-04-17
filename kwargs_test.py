import unittest
from kwargs import buscar_datos, database


class TestKwargs(unittest.TestCase):

    def test_picasso(self):
        result = buscar_datos("Pablo", "Diego", "Ruiz", "Picasso", **database)
        self.assertEqual(result,{
            "persona1":{
                    "primer_nombre":"Pablo",
                    "segundo_nombre":"Diego",
                    "primer_apellido":"Ruiz",
                    "segundo_apellido":"Picasso"
                    }})

    def test_roman(self):
        result = buscar_datos("Jorge", "Roman", "Castro", "Sanchez", **database)
        self.assertEqual(result,{
            "persona2":{
                    "primer_nombre":"Jorge",
                    "segundo_nombre":"Roman",
                    "primer_apellido":"Castro",
                    "segundo_apellido":"Sanchez"
                    }})
        
    def test_none(self):
        result = buscar_datos("Alfonso", "Dario", "Martinez", "Aguirre", **database)
        self.assertEqual(result,None)

    def test_none2(self):
        result = buscar_datos("Jorge", "Roman", "Castro", "Gomez", **database)
        self.assertEqual(result,None)

    def test_osvaldo(self):
        result = buscar_datos("Osvaldo", "Cerro", **database)
        self.assertEqual(result,{
            "persona3":{
                    "primer_nombre":"Osvaldo",
                    "primer_apellido":"Cerro",
                    }})
        
    def test_rodolfo(self):
        result = buscar_datos("Luis", "Damian", "Rodolfo", "Lucero", "Perez", **database)
        self.assertEqual(result,{
            "persona4":{
                    "primer_nombre":"Luis",
                    "segundo_nombre":"Damian",
                    "tercer_nombre":"Rodolfo",
                    "primer_apellido":"Lucero",
                    "segundo_apellido":"Perez"
                    }})


if __name__ == "__main__":
    unittest.main()