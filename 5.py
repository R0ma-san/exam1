import csv
import random 
from faker import Faker
faker = Faker()

# with open("file.csv", 'w') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['name', 'age', 'job', 'phone_number', 'address'])
#     for i in range(11):
#         writer.writerow([faker.name(), random.randint(18, 50), faker.job(), faker.phone_number(), faker.address()])
#     csvfile.close()

class Csv:
        
    def sort():
        pass

    def row_writer(self, name, age, job, phone_number, address):
        with open("file.csv", 'r') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([name, age, job, phone_number, address])
        csvfile.close()

    def row(self):
       pass

    def row_updater(self):
        pass

    def searcher(self, a):
        with open("file.csv", 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                for i in row:
                    if i.startswith(a):
                        print(row)

        csvfile.close()

c = Csv()
c.searcher('Michelle ')
