import os

def get_population(country_dict):
    population_dict = {
    '2022': int(country_dict['2022 Population']),
    '2020': int(country_dict['2020 Population']),
    '2015': int(country_dict['2015 Population']),
    '2010': int(country_dict['2010 Population']),
    '2000': int(country_dict['2000 Population']),
    '1990': int(country_dict['1990 Population']),
    '1980': int(country_dict['1980 Population']),
    '1970': int(country_dict['1970 Population'])}
     
    labels = population_dict.keys()
    values = population_dict.values()
    return labels, values

def get_world_population_percentage(data):
  wpp = {country['Country/Territory']:country['World Population Percentage'] for country in data}
  names = wpp.keys()
  values = wpp.values()
  return names, values

def population_by_country(data, country):
    result = list(filter(lambda key:key['Country/Territory'] == country, data))
    return result

def create_folder(path, name_folder="logs"):
  path_to_create = os.path.join(path, name_folder)

  try:
   os.mkdir(path_to_create)
   print("Created successfully!!")
  except Exception as error:
     print(f"It has ocurred an unexpected error, details -- {error}")