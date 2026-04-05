import random

def sorteo_amigo_invisible():
    nombres = input("Ingrese los participantes (separados por coma): ")
    participantes = [nombre.strip() for nombre in nombres.split(",")]
    
    if len(participantes) < 3:
        print("Debe haber al menos 3 participantes.")
        return
    
    participantes_lower = [nombre.lower() for nombre in participantes]
    if len(participantes_lower) != len(set(participantes_lower)):
        print("No puede haber nombres duplicados.")
        return
    
    asignaciones = participantes.copy()
    while True:
        random.shuffle(asignaciones)
        if all(participantes[i] != asignaciones[i] for i in range(len(participantes))):
            break
    
    print("\nSorteo de amigo invisible:")
    for i in range(len(participantes)):
        print(f" {participantes[i]} → {asignaciones[i]}")