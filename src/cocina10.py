def calcular_puntaje_ronda(scores):
    return {participante: sum(jueces.values())
            for participante, jueces in scores.items()}


def obtener_ganador_ronda(puntajes_ronda):
    ganador = max(puntajes_ronda, key=lambda p: puntajes_ronda[p])
    return ganador, puntajes_ronda[ganador]


def actualizar_totales(totales, puntajes_ronda, ganador):
    for participante, puntaje in puntajes_ronda.items():
        totales[participante]['total'] += puntaje
        totales[participante]['rondas_ganadas'] += (1 if participante == ganador else 0)
        if puntaje > totales[participante]['mejor_ronda']:
            totales[participante]['mejor_ronda'] = puntaje
    return totales


def mostrar_tabla(totales, num_rondas):
    print(f"{'Cocinero':<12} {'Puntaje':>8} {'Rondas ganadas':>15} {'Mejor ronda':>12} {'Promedio':>10}")
    print("-" * 60)

    ranking = sorted(totales.items(), key=lambda x: x[1]['total'], reverse=True)

    for participante, datos in ranking:
        promedio = datos['total'] / num_rondas
        print(f"{participante:<12} {datos['total']:>8} {datos['rondas_ganadas']:>15} {datos['mejor_ronda']:>12} {promedio:>10.1f}")

    print("-" * 60)


def inicializar_totales(participantes):
    return {participante: {'total': 0, 'rondas_ganadas': 0, 'mejor_ronda': 0}
            for participante in participantes}

def simular_competencia(rounds):
    participantes = list(rounds[0]['scores'].keys())
    totales = inicializar_totales(participantes)
    
    for i, ronda in enumerate(rounds):
        puntajes_ronda = calcular_puntaje_ronda(ronda['scores'])
        ganador, puntaje_ganador = obtener_ganador_ronda(puntajes_ronda)
        totales = actualizar_totales(totales, puntajes_ronda, ganador)
        
        print(f"\nRonda {i+1} - {ronda['theme']}:")
        print(f" Ganador: {ganador} ({puntaje_ganador} pts)")
        mostrar_tabla(totales, i+1)
    
    print("\nTabla de posiciones final:")
    mostrar_tabla(totales, len(rounds))