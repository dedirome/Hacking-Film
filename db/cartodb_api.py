from cartodb import CartoDBAPIKey, CartoDBException

user =  'mik3cap@gmail.com'
API_KEY ='a593f743aebe095ab7c75d230c71e2fd13e5bc24'
cartodb_domain = 'mik3cap'

cl = CartoDBAPIKey(API_KEY, cartodb_domain)

try:
    print cl.sql('SELECT * FROM user_info')
except CartoDBException as e:
    print ("some error ocurred", e)

try:
    print cl.sql('SELECT * FROM movie')
except CartoDBException as e:
    print ("some error ocurred", e)

try:
    print cl.sql('SELECT * FROM venue')
except CartoDBException as e:
    print ("some error ocurred", e)

try:
    print cl.sql('SELECT * FROM plan')
except CartoDBException as e:
    print ("some error ocurred", e)



# INSERT INTO user_info (email, fb_user_id, full_name) VALUES (%s, %s, %s)

# INSERT INTO movie (genre, movie_name, movie_time, rating, running_time, theatre_name, ticket_url) VALUES (%s, %s, %s, %s, %s, %s, %s)

# INSERT INTO venue (atmosphere, hours_of_operation, venue_cuisine, venue_name, venue_type) 
# VALUES (%s, %s, %s, %s, %s)

# INSERT INTO plan (movie_appeal, movie_name, movie_time, theater_id, user_id, user_organizer, venue_appeal, venue_id, venue_time) 
# VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)

