import redis

lignes = """Rions, chantons, ô mes amis,
Occupons-nous à ne rien faire,
Laissons murmurer le vulgaire,
Le plaisir est toujours permis.
Que notre existence légère
S'évanouisse dans les jeux.
Vivons pour nous, soyons heureux,
N'importe de quelle manière.
Un jour il faudra nous courber
Sous la main du temps qui nous presse ;
Mais jouissons dans la jeunesse,
Et dérobons à la vieillesse
Tout ce qu'on peut lui dérober.""".splitlines()

r = redis.StrictRedis('localhost', 6379, charset="utf-8", decode_responses=True)

for l in lignes:
    r.publish('poeme', l)