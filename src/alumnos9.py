def normalizar_alumnos(students):
    alumnos_limpios = {}
    
    for alumno in students:
        if alumno["name"] is None or alumno["name"].strip() == "":
            continue
        if alumno["grade"] is None or alumno["grade"].strip() == "":
            continue
        try:
            nota = int(alumno["grade"])
        except ValueError:
            continue
        nombre = alumno["name"].strip().title()
        estado = alumno["status"].strip().title()
        if nombre not in alumnos_limpios:
            alumnos_limpios[nombre] = {"grade": nota, "status": estado}
        else:
            if nota > alumnos_limpios[nombre]["grade"]:
                alumnos_limpios[nombre] = {"grade": nota, "status": estado}
    
    alumnos_ordenados = sorted(alumnos_limpios.items())
    
    print("Registros limpios de alumnos:")
    print(f"{'Nombre':<20} {'Nota':<6} {'Estado'}")
    print("-" * 42)
    for nombre, datos in alumnos_ordenados:
        print(f"{nombre:<20} {datos['grade']:<6} {datos['status']}")
    
    print(f"\nTotal de alumnos válidos: {len(alumnos_ordenados)}")