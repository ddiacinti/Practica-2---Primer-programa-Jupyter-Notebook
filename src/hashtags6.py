def analizar_hashtags(posts):
    conteo = {}
    
    for post in posts:
        for palabra in post.split():
            if palabra.startswith("#"):
                if palabra in conteo:
                    conteo[palabra] += 1
                else:
                    conteo[palabra] = 1
    
    trending = {hashtag: cantidad for hashtag, cantidad in conteo.items() if cantidad > 1}
    
    print("Hashtags trending (más de una aparición):")
    for hashtag, cantidad in trending.items():
        print(f" {hashtag}: {cantidad}")
    
    print(f"\nTotal de hashtags únicos: {len(conteo)}")