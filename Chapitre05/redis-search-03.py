from redisearch import Client

client = Client("ArbresParis")

res = client.search("@genre:{Ulmus}")

print(res.total)
print(res.docs[0].arrondissement)