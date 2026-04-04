def filtrar_spoilers(texto):
    palabras = input("Ingrese las palabras spoiler (separadas por coma): ")
    palabras_spoiler = palabras.split(",")
    
    for palabra in palabras_spoiler:
        palabra = palabra.strip()
        asteriscos = "*" * len(palabra)
        texto = texto.replace(palabra, asteriscos)
        texto = texto.replace(palabra.lower(), asteriscos)
        texto = texto.replace(palabra.upper(), asteriscos)
        texto = texto.replace(palabra.capitalize(), asteriscos)
    return texto