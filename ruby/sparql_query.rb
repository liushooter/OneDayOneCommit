#gem install sparql
#http://www.rubydoc.info/github/ruby-rdf/sparql/frames

require 'sparql'

endpoint = "https://query.wikidata.org/sparql"
sparql = <<'SPARQL'.chop
SELECT ?person ?personLabel 
WHERE 
{
  ?person wdt:P39 wd:Q268218.
  ?person wdt:P27 wd:Q9683.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "zh". }
}
SPARQL

client = SPARQL::Client.new(endpoint, :method => :get)
rows = client.query(sparql)

puts "Number of rows: #{rows.size}"
for row in rows
  for key,val in row do
    print "#{key}: #{val}\t"
  end
  print "\n"
end

