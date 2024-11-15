class Programa:
    def __init__(self, nombre, universidad, codigo_snies, nivel, campus):
        self.nombre = nombre
        self.universidad = universidad
        self.codigo_snies = codigo_snies
        self.nivel = nivel
        self.campus = campus

    def obtener_informacion(self):
        return (f"Programa: {self.nombre}\n"
                f"Universidad: {self.universidad}\n"
                f"Código SNIES: {self.codigo_snies}\n"
                f"Nivel: {self.nivel}\n"
                f"Campus: {self.campus}\n")

    def __repr__(self):
        return (f"Programa(nombre={self.nombre}, universidad={self.universidad}, "
                f"codigo_snies={self.codigo_snies}, nivel={self.nivel}, campus={self.campus})")
