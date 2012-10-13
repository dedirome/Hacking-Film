from cartodb import CartoDBAPIKey, CartoDBException

user =  'me@mail.com'
API_KEY ='YOUR_CARTODB_API_KEY'
cartodb_domain = 'YOUR_CARTODB_DOMAIN'
cl = CartoDBAPIKey(API_KEY, cartodb_domain)
try:
    print cl.sql('select * from mytable')
except CartoDBException as e:
    print ("some error ocurred", e)
