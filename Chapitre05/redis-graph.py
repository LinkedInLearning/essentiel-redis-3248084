import redis
import os

chemin = os.path.abspath(os.path.dirname(__file__))

r = redis.StrictRedis('localhost', 6379, charset="utf-8", decode_responses=True)

# https://github.com/julio24048/neo4j-metro-parisien
f = open(f"{chemin}\\metro.cypher", mode='r', encoding='utf-8')

# commandes = f.read().split('CREATE')
commandes = f.readlines()

for c in commandes:
    # print(c)
    # r.graph('metro_paris').
    if(len(c.strip())) and not c.startswith('//') :
        r.execute_command('GRAPH.QUERY', 'metro_paris', c)
    # print (reponse)

f.close()