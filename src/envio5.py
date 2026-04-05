def calcular_envio():
    precios = {
        "local": {"hasta1": 500, "hasta5": 1000, "mas5": 2000},
        "regional": {"hasta1": 1000, "hasta5": 2500, "mas5": 5000},
        "nacional": {"hasta1": 2000, "hasta5": 4500, "mas5": 8000}
    }
    
    peso = float(input("Ingrese el peso del paquete (kg): "))
    zona = input("Ingrese la zona de destino (local/regional/nacional): ")
    
    if zona not in precios:
        print(f"Zona no válida. Las zonas disponibles son: local, regional, nacional.")
        return
    
    if peso <= 1:
        costo = precios[zona]["hasta1"]
    elif peso <= 5:
        costo = precios[zona]["hasta5"]
    else:
        costo = precios[zona]["mas5"]
    
    print(f"Costo de envío: ${costo}")