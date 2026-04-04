def analizar_playlist(playlist):
    total_segundos = 0
    duraciones = []
    
    for cancion in playlist:
        partes = cancion['duration'].split(':')
        segundos = int(partes[0]) * 60 + int(partes[1])
        total_segundos += segundos
        duraciones.append((cancion['title'], segundos, cancion['duration']))
    
    minutos_total = total_segundos // 60
    segundos_total = total_segundos % 60
    
    mas_larga = max(duraciones, key=lambda x: x[1])
    mas_corta = min(duraciones, key=lambda x: x[1])
    
    return f'{minutos_total}m {segundos_total}s', mas_larga, mas_corta 