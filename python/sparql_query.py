#pip install sparqlwrapper
#https://rdflib.github.io/sparqlwrapper/

from SPARQLWrapper import SPARQLWrapper, JSON
sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
sparql.setQuery("""SELECT ?book ?bookLabel
WHERE 
{
  ?book wdt:P136 wd:Q8261.
  ?book wdt:P50 wd:Q228889.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "zh". }
}

ORDER BY DESC (?bookLabel)""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

for result in results["results"]["bindings"]:
    print(result)

