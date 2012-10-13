from cartodb import CartoDBAPIKey, CartoDBException

user =  'wmaio@gmail.com'
API_KEY ='ef51a53f44eff0538e1372e9cd955727c5afda38'
cartodb_domain = 'wmaiouiru'

cl = CartoDBAPIKey(API_KEY, cartodb_domain)

try:
    print cl.sql('SELECT * FROM uiru_test1')
except CartoDBException as e:
    print ("some error ocurred", e)
