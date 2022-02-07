from pymongo import MongoClient

def insert_documents(collection_name, document):
    collection = db[collection_name]
    record = collection.insert_one(document)
    print(f"Successfully inserted document into {collection_name} collection with id {record}")

movie_document = {
    "plot": "Three men hammer on an anvil and pass a bottle of beer around.",
    "genres": ["Short"],
    "runtime": 1,
    "cast": ["Charles Kayser", "John Ott"],
    "num_mflix_comments": 1,
    "title": "Blacksmith Scene",
    "fullplot": "A stationary camera looks at a large anvil with a blacksmith behind it and one on either side. The smith in the middle draws a heated metal rod from the fire, places it on the anvil, and all three begin a rhythmic hammering. After several blows, the metal goes back in the fire. One smith pulls out a bottle of beer, and they each take a swig. Then, out comes the glowing metal and the hammering resumes.",
    "countries": ["USA"],
    "released": {
        "$date": "1893-05-09T00:00:00.000Z"
    },
    "directors": ["William K.L. Dickson"],
    "rated": "UNRATED",
    "awards": {
        "wins": 1,
        "nominations": 0,
        "text": "1 win."
    },
    "lastupdated": "2015-08-26 00:03:50.133000000",
    "year": 1893,
    "imdb": {
        "rating": 6.2,
        "votes": 1189,
        "id": 5
    },
    "type": "movie",
    "tomatoes": {
        "viewer": {
            "rating": 3,
            "numReviews": 184,
            "meter": 32
        },
        "lastUpdated": {
            "$date": "2015-06-28T18:34:09.000Z"
        }
    }
}
comment_document = {
    "name": "Mercedes Tyler",
    "email": "mercedes_tyler@fakegmail.com",
    "movie_id": {
        "$oid": "573a1390f29313caabcd4323"
    },
    "text": "Eius veritatis vero facilis quaerat fuga temporibus. Praesentium expedita sequi repellat id. Corporis minima enim ex. Provident fugit nisi dignissimos nulla nam ipsum aliquam.",
    "date": {
        "$date": "2002-08-18T04:56:07.000Z"
    }
}
sessions_document = {
    "user_id": "t3qulfeem@kwiv5.6ur",
    "jwt": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1MTk5MDkzMjEsIm5iZiI6MTUxOTkwOTMyMSwianRpIjoiNmJlZDAwMWYtNTFiYi00NzVhLTgxZDAtMDcwNGE5Mjk0MWZlIiwiZXhwIjoxNTE5OTEwMjIxLCJpZGVudGl0eSI6eyJlbWFpbCI6InQzcXVsZmVlbUBrd2l2NS42dXIiLCJuYW1lIjoiM2lveHJtZnF4IiwicGFzc3dvcmQiOm51bGx9LCJmcmVzaCI6ZmFsc2UsInR5cGUiOiJhY2Nlc3MiLCJ1c2VyX2NsYWltcyI6eyJ1c2VyIjp7ImVtYWlsIjoidDNxdWxmZWVtQGt3aXY1LjZ1ciIsIm5hbWUiOiIzaW94cm1mcXgiLCJwYXNzd29yZCI6bnVsbH19fQ.ejtr_NyZyBronWMKuE0RFTjWej--T0zGrdc_iymGtVs"
}
theater_document = {
    "theaterId": 1012,
    "location": {
        "address": {
            "street1": "1207 W Century Ave",
            "city": "Bismarck",
            "state": "ND",
            "zipcode": "58503"
        },
        "geo": {
            "type": "Point",
            "coordinates": [-100.81213, 46.829876]
        }
    }
}
user_document = {
    "name": "Petyr Baelish",
    "email": "aidan_gillen@gameofthron.es",
    "password": "$2b$12$qM.YvmiekyYYY7p7phpK3OicbRCDkN7ESwYAnG/o9YnfHC0Mhkmbi"
}

if __name__ == "__main__":

    try:
        client = MongoClient("mongodb://127.0.0.1:27017")
        print("Connection successful")
        print(client.server_info())

        db = client['moviesData']
        print("Q3) Python methods and MongoDB queries to insert new comments, movies, theatres, and users into respective MongoDB collections.")
        print('''Choices : 
                1. Insert into movies collection.
                2. Insert into comments collection.
                3. Insert into sessions collection.
                4. Insert into theaters collection.
                5. Insert into users collection.
            ''')
        choice = int(input("Enter your choice : "))
        if choice == 1:
            insert_documents("movies", movie_document),
        elif choice == 2:
            insert_documents("comments", comment_document),
        elif choice == 3:
            insert_documents("sessions", sessions_document),
        elif choice == 4:
            insert_documents("theaters", theater_document),
        elif choice == 5:
            insert_documents("users", user_document)

    except:
        print("Could not establish connection")
