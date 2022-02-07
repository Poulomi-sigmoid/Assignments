from pymongo import MongoClient

def task_i():
    pipeline1 = [
        {
            '$project': {
                'theaterId': 1,
                '_id': 0,
                'city': '$location.address.city'
            }
        }, {
            '$group': {
                '_id': '$city',
                'totalTheaters': {
                    '$sum': 1
                }
            }
        }, {
            '$sort': {
                'totalTheaters': -1
            }
        }, {
            '$limit': 10
        }
    ]

    results1 = collection.aggregate(pipeline1)
    for result in results1:
        print(f"City - {result['_id']} ; No of theaters - {result['totalTheaters']}")


def task_ii():
    pipeline2 = [
        {
            '$geoNear': {
                'near': {
                    'type': 'Point',
                    'coordinates': [
                        -118.11414, 37.667957
                    ]
                },
                'maxDistance': 1000000,
                'distanceField': 'dist.calculated',
                'includeLocs': 'dist.location',
                'distanceMultiplier': 0.001,
                'spherical': True
            }
        }, {
            '$project': {
                'theaterId': 1,
                '_id': 0,
                'city': '$location.address.city',
                'distance': '$dist.calculated'
            }
        }, {
            '$limit': 10
        }
    ]

    results2 = collection.aggregate(pipeline2)
    for result in results2:
        print(f"City - {result['city']} ; TheaterId - {result['theaterId']} ; Distance - {result['distance']}")


if __name__ == "__main__":

    try:
        client = MongoClient("mongodb://127.0.0.1:27017")
        print("Connection successful")
        print(client.server_info())

        collection = client['moviesData']['theaters']
        print("Q4) Create Python methods and MongoDB queries to support the below operations -")
        print('''Choices : 
        1. Top 10 cities with the maximum number of theatres.
        2. Top 10 theatres nearby given coordinates
            ''')
        choice = int(input("Enter your choice : "))
        if choice == 1:
            task_i()
        elif choice == 2:
            task_ii()

    except:
        print("Could not establish connection")