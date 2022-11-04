from redisearch import Client, IndexDefinition, TextField, NumericField, GeoField, TagField

client = Client("ArbresParis")

definition = IndexDefinition(prefix=['arbre:'])

client.create_index((TextField("nom", weight=5.0), TagField("espece"), TagField("genre"), 
    NumericField("hauteur"), TextField("adresse"), TextField("arrondissement"), GeoField("coordonnees")), 
    definition=definition)