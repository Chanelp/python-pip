import csv

def read_csv(path):
    with open(path, 'r') as csvfile:

        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data = []

        for row in reader:
            iterable = zip(header, row)
            country_dict = dict(iterable)
            data.append(country_dict)
        
        return data
    
def get_country(countrySearched, data):
    country = list(filter(lambda c: c['Country/Territory']== countrySearched, data))
    return country

def get_dict(country):
    countryDict = {k:v for k,v in country[0].items()}
    return countryDict

def get_population(dict):
    population = {}
    for key, value in dict.items():
        if key[-5:] == 'ation':
            population[key[0:4]] = value
    return population



if __name__ == "__main__":
    data = read_csv('./app/data.csv')
    pais = get_country("Argentina", data)
    paisDict = get_dict(pais)
    print(get_population(paisDict))
