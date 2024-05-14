from pymongo import MongoClient

# change URL if using a different MongoDB server
client = MongoClient("mongodb+srv://vitst:P1q2w3e4r@cluster0.0uj64vn.mongodb.net/")
db = client.pets_database
collection = db["cats"]


def read_all_records():
    try:
        for record in collection.find():
            print(record)
    except Exception as e:
        print("Error reading records:", e)


def find_record_by_name(name):
    try:
        record = collection.find_one({"name": name})
        if record:
            print(record)
        else:
            print("Record not found")
    except Exception as e:
        print("Error finding record by name:", e)


def update_age_by_name(name, new_age):
    try:
        collection.update_one({"name": name}, {"$set": {"age": new_age}})
        print(f"Age {new_age} updated for", name)
    except Exception as e:
        print("Error updating age by name:", e)


def add_feature_to_cat(name, new_feature):
    try:
        collection.update_one({"name": name}, {"$push": {"features": new_feature}})
        print(f"Feature {new_feature} added for", name)
    except Exception as e:
        print("Error adding a new feature by name:", e)


def delete_cat_record(name):
    try:
        collection.delete_one({"name": name})
        print("Record deleted for", name)
    except Exception as e:
        print("Error deleting record by name:", e)


def delete_all_records():
    try:
        collection.delete_many({})
        print("All records deleted")
    except Exception as e:
        print("Error deleting all records:", e)


if __name__ == "__main__":

    print("All records:")
    read_all_records()


    print("Information about a cat by name:")
    find_record_by_name("Boris")


    update_age_by_name("Murzik", 6)


    add_feature_to_cat("barsik", "affectionate")


    delete_cat_record("Murzik")


    delete_all_records()
