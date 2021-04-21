import csv
import json


with open('books.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    books = [{'title': line['Title'], "author": line['Author'], "height": line['Height']} for line in reader]

with open("users.json", "r") as f:
    reader = json.load(f)
    users = [{"name": data['name'], "gender": data["gender"], "address": data["address"], "books": []} for data in reader]

for i in users:
    for j in books:
        i["books"].append(j)
        books.remove(j)
        break

with open("users_with_books.json", "w") as f:
    f.write(json.dumps(users, indent=4))
