from cartodb import CartoDBOAuth, CartoDBException

user =  'me@mail.com'
password =  'secret'
CONSUMER_KEY='YOUR_CARTODB_CONSUMER_KEY'
CONSUMER_SECRET='YOUR_CARTODB_CONSUMER_SECRET'
cartodb_domain = 'YOUR_CARTODB_DOMAIN'
cl = CartoDBOAuth(CONSUMER_KEY, CONSUMER_SECRET, user, password, cartodb_domain)
try:
    print cl.sql('select * from mytable')
except CartoDBException as e:
    print ("some error ocurred", e)
