def analizar_texto(texto):
    #separo las lineas para contarlas
    lineas = texto.split("\n")
    total_lineas = len(lineas)

    # cuento las palabras
    total_palabras = 0
    for linea in lineas:
        total_palabras += len(linea.split()) #separa , cuenta y acumula el total de palabras

    # calculo promedio
    promedio_palabras = total_palabras/ total_lineas

    # obtiene las lineas superiores al promedio
    lineas_superiores = []
    for linea in lineas:
        if len(linea.split()) > promedio_palabras:
            lineas_superiores.append(linea)

    return total_lineas,total_palabras, promedio_palabras, lineas_superiores

    