
import csv
import pymongo

'''functions .. begin'''
def read(dbname,colname,client):
    mydb=client[dbname]
    cols=mydb[colname]
    mydoc=cols.find({})
    for x in mydoc:
        print(x)


def delete_all(dbname,colname,client):
    mydb=client[dbname]
    cols=mydb[colname]
    cols.delete_many({})
def csv_file(csv_name):
    with open (csv_name) as csvfile:
        reader = csv.reader(csvfile)

        skip_header = True
        header = []
        for i in reader:
            if skip_header:
                skip_header = False

                for value in i:
                    header.append(value)

            else:

                record = dict()
                index = 0
                while index < len(i):
                    record[header[index]] = i[index]
                    index += 1

                mycol.insert_one(record)

'''functions...end'''


'''Main'''
myclient=pymongo.MongoClient("mongodb://localhost:27017/")
delete_all("Mongodb_2","ninteen",myclient)
db=myclient.Mongodb_2
mycol=db.ninteen

csv_file("local.csv")
read("Mongodb_2","ninteen",myclient)

