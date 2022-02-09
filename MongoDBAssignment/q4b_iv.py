from pymongo import MongoClient

def task():
    n = int(input("Enter a number : "))
    pipeline = [
        {
            '$unwind': {
                'path': '$genres',
                'preserveNullAndEmptyArrays': False
            }
        }, {
            '$project': {
                'title': 1,
                'rating': '$imdb.rating',
                'genres': 1
            }
        }, {
            '$sort': {
                'rating': -1
            }
        }, {
            '$match': {
                'rating': {
                    '$ne': ''
                }
            }
        }, {
            '$group': {
                '_id': '$genres',
                'movies': {
                    '$push': {
                        'movie': '$title',
                        'rating': '$rating'
                    }
                }
            }
        }, {
            '$project': {
                'movies': {
                    '$slice': [
                        '$movies', 0, n
                    ]
                }
            }
        }
    ]

    results = collection.aggregate(pipeline)
    for result in results:
        print()
        print(f"Genre : {result['_id']}")
        print("------------------------")
        for i in range(len(result['movies'])):
            print(f"Movie : {result['movies'][i]['movie']} ;  Rating : {result['movies'][i]['rating']}")
        print()
        print("========================")


if __name__ == "__main__":

    try:
        client = MongoClient("mongodb://127.0.0.1:27017")
        print("Connection successful")
        print(client.server_info())

        collection = client['moviesData']['movies']
        print("Q4) Create Python methods and MongoDB queries to support the below operations -")
        print("Find top `N` movies for each genre with the highest IMDB rating.")
        task()
    except:
        print("Could not establish connection")