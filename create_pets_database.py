from pymongo import MongoClient
from bson import ObjectId

client = MongoClient(
    "mongodb+srv://vitst:P1q2w3e4r@cluster0.0uj64vn.mongodb.net/"
    )
db = client.pets_database

collection = db["cats"]

cats_data = [
    {
        "name": 'Lama',
        "age": 2,
        "features": ['ходить в лоток', 'не дає себе гладити', 'сірий'],
    },
    {
        "name": 'Liza',
        "age": 4,
        "features": ['ходить в лоток', 'дає себе гладити', 'білий'],
    },
    {
        "name": 'Boris',
        "age": 12,
        "features": ['ходить в лоток', 'не дає себе гладити', 'сірий'],
    },
    {
        "name": 'Murzik',
        "age": 1,
        "features": ['ходить в лоток', 'дає себе гладити', 'чорний'],
    },
    {
        "name": 'barsik',
        "age": 3,
        "features": ['ходить в капці','дає себе гладити','рудий'],
    },

]

collection.insert_many(cats_data)

print("Database created successfully!")
