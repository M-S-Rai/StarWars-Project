import pymongo

client = pymongo.MongoClient()
db = client['starwars']

# Use find() to get _id and name
characters = db.characters.find({}, {"_id": 1, "name": 1})

# Print the _id and name for each character
for character in characters:
    print(character)