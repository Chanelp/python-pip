import csv

def read_csv(path):
   with open(path, 'r') as csvfile:
       total = sum(int(row[1]) for row in csv.reader(csvfile))
       return total

if __name__ == "__main__":
    response = read_csv('./app/gastos.csv')
    print(response)