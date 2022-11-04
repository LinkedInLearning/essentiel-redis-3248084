import json 
import urllib.request
from redisearch import Client

url = "https://opendata.paris.fr/api/records/1.0/search/?dataset=les-arbres&q=&rows=300"

page = urllib.request.urlopen(url)
if(page.getcode()==200):
    data = page.read()
else:
    print("Error receiving data", page.getcode())

arbres = json.loads(data) 

client = Client("ArbresParis")

for a in arbres["records"]:
        doc = {
            'nom': a["fields"]["libellefrancais"] if "libelleFrancais" in a["fields"] else '',
            'espece': a["fields"]["espece"] if "espece" in a["fields"] else '',
            'genre': a["fields"]["genre"],
            'hauteur': a["fields"]["hauteurenm"],
            'adresse': a["fields"]["adresse"],
            'arrondissement': a["fields"]["arrondissement"],
            'coordonnees': str(a["fields"]["geo_point_2d"])[1:-1]
        } 

        cle = f"arbre:{a['recordid']}"

        client.redis.hset(cle, mapping = doc)