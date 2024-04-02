
class Personaje:
    
    
    # Constructor
    def __init__(self, nombre, vida, fuerza):
        self.nombre = nombre
        self.vida = vida
        self.fuerza = fuerza

    # Métodos
    def atacar(self, objetivo):
        if isinstance(objetivo, Personaje):
            print(f"{self.nombre} ataca a {objetivo.nombre}!")
            objetivo.recibir_danio(self.fuerza)
        else:
            print("El objetivo no es un personaje válido.")

    def recibir_danio(self, cantidad):
        self.vida -= cantidad
        print(f"{self.nombre} recibe {cantidad} de daño. Vida restante: {self.vida}")

    def __str__(self):
        return f"Nombre: {self.nombre}, Vida: {self.vida}, Fuerza: {self.fuerza}"
