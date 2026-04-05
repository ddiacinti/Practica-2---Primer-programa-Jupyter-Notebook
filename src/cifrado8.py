def cifrado_cesar():
    mensaje = input("Ingrese un mensaje: ")
    desplazamiento = int(input("Ingrese el desplazamiento: "))
    
    cifrado = ""
    for letra in mensaje:
        if letra.isalpha():
            if letra.isupper():
                cifrado += chr((ord(letra) - ord('A') + desplazamiento) % 26 + ord('A'))
            else:
                cifrado += chr((ord(letra) - ord('a') + desplazamiento) % 26 + ord('a'))
        else:
            cifrado += letra
    
    descifrado = ""
    for letra in cifrado:
        if letra.isalpha():
            if letra.isupper():
                descifrado += chr((ord(letra) - ord('A') - desplazamiento) % 26 + ord('A'))
            else:
                descifrado += chr((ord(letra) - ord('a') - desplazamiento) % 26 + ord('a'))
        else:
            descifrado += letra
    
    print(f"Mensaje cifrado: {cifrado}")
    print(f"Mensaje descifrado: {descifrado}")