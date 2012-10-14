from api.Rotten import *

rotten = Rotten(api_key=u'eskr4pjvnmsgg8ghwvg6pzkn')

# Returns a JSON result
print rotten.in_theaters()
