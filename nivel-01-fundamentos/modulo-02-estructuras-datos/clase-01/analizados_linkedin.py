# Últimos 10 posts de LinkedIn — datos reales de ejemplo
posts = [
    "Prospección B2B en 2026",
    "Cómo audito Meta Ads en 15 min",
    "Errores caros de traffickers junior",
    "Mi setup de trabajo",
    "Reel de trafficker: caso real",
    "Automatizar reportes con IA",
    "Coaching + Marketing = ventaja",
    "Análisis de campaña Coolsmart",
    "Newsletter semanal #12",
    "Mi ritual de lunes"
]

likes    = [45, 128,  87,  23,  210,  62,  91,  34,  78, 156]
comments = [ 3,  27,  12,   2,   45,   9,  15,   4,  11,  38]

# panorama general de post y likes
 
print("el total de posts es")
print(len(posts))
print("el total de likes es")
print(sum(likes))
print("el total de comentarios es")
print(sum(comments))
print("el promedio de likes por post es")
promedio=(sum(likes)/len(posts))
print(promedio)
print("el promedio de comentarios por post es")
promedio1=(sum(comments)/len(posts))
print(promedio1)
print("________________________")

# extremos maximos y minimos

print("el maximo de likes en la lista")
print(max(likes))
print("el minimo de likes en la lista")
print(min(likes))
print("el post que mas likes tuvo es")
indice=likes.index(max(likes))
print(posts[indice])
print("el post que menos likes tuvo es")
indice1=likes.index(min(likes))
print(posts[indice1])
print("_______________________")


# clasificación por performance


viral = 0
bueno = 0
bajo = 0

for i, x in enumerate(likes):
    if x >= 150:
        categoria = "Viral"
        viral += 1
    elif 50 <= x < 150:
        categoria = "Buen post"
        bueno += 1
    else:
        categoria = "Bajo"
        bajo += 1

    print(f'{categoria} — {x:3} likes — "{posts[i]}"')

print()
print(f"Total virales: {viral}")
print(f"Total buenos:  {bueno}")
print(f"Total bajos:   {bajo}")
print("__________________-")

# Engagement rate 

engagement_rates = []

for i in range(len(posts)):
    rate = round(comments[i] / likes[i] * 100, 1)
    engagement_rates.append(rate)

print(engagement_rates)


max_rate = max(engagement_rates)
i_max = engagement_rates.index(max_rate)

print(f'Post más conversacional: "{posts[i_max]}"')
print(f'  Likes: {likes[i_max]}')
print(f'  Comments: {comments[i_max]}')
print(f'  Engagement: {max_rate}%')
print("________________________")

# top 3 mejores post

top3_likes = sorted(likes, reverse=True)[:3]
medallas = ["primero", "segundo", "tercero"]

for j, likes_top in enumerate(top3_likes):
    i = likes.index(likes_top)   # ← posición en la lista ORIGINAL
    print(f"{medallas[j]} {likes_top} likes — \"{posts[i]}\"")
