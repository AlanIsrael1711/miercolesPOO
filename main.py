from cosas import Alumno, Perro

def main():
    al1 = Alumno("Alan", 18, "ICO")
    print(vars(al1))
    al1.__nombre = "Diego"
    print(vars(al1))
    al1.set_nombre("David")
    print(vars(al1))
    print("-----To String-----")
    print(al1)
    al1.set_edad(99)
    print(al1)
    al1.estudiar(4)
    print("-----PERRO-----")
    perro1 = Perro("Poodle", 2, 0.35)
    print(vars(perro1))
    perro1.__raza = "De la calle" #Set en noacion Pythonic
    print(vars(perro1))
    perro1.__raza = "Otra"
    print(vars(perro1))
    perro1.edad = 12
    perro1.estatura = 0.43
    print(perro1)
    cachorro = Perro.es_cachorro(perro1.edad)
    print(cachorro)
    Perro.dormir()
    danes = Perro.perro_grande(0.8)
    print(danes)

main()