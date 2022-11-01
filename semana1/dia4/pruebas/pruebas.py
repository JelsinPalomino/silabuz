class Humano:
    def __init__(self, edad):
        self.edad = edad

    def hablar(self, mensaje):
        print(f'{mensaje}')

pedro = Humano(20)
raul  = Humano(30)

pedro.hablar("Como estas?")

print(f"Soy Pedro y tengo, {pedro.edad}")

print(f"Soy Pedro y tengo, {raul.edad}")