def validar_email(email):
    if email.count("@") != 1:
        return False
    
    partes = email.split("@")
    parte_local = partes[0]
    dominio = partes[1]
    
    if len(parte_local) == 0:
        return False
    
    if email.startswith("@") or email.startswith("."):
        return False
    if email.endswith("@") or email.endswith("."):
        return False

    if "." not in dominio:
        return False

    ultima_parte = dominio.split(".")[-1]
    if len(ultima_parte) < 2:
        return False
    
    return True