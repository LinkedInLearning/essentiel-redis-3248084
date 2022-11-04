GRAPH.QUERY metro_paris "MATCH (s:Station { nom: 'Balard' }) RETURN s"
GRAPH.QUERY metro_paris "MATCH (s1:Station { nom: 'Lourmel' })-[:Ligne]-(s2:Station) RETURN s2"

GRAPH.QUERY metro_paris "MATCH (s1:Station { nom: 'Lourmel' }), (s2:Station { nom: 'Pyramides' }) WITH s1, s2 MATCH p=allShortestPaths((s1)-[:Ligne*]->(s2)) RETURN nodes(p) as stations"