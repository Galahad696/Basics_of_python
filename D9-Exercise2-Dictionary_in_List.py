travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]


#A function that will allow new countries
#to be added to the travel_log.
def add_new_country(country_name, visits_number, cities_visited):
    new_dictionary = {
        "country": country_name,
        "visits": visits_number,
        "cities": cities_visited
    }
    travel_log.append(new_dictionary)





add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
