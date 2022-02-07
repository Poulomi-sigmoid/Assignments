from pymongo import MongoClient

def task_1():
    n1 = int(input("Enter a number : "))
    pipeline1 = [
        {
            '$unwind': {
                'path': '$directors',
                'preserveNullAndEmptyArrays': False
            }
        }, {
            '$group': {
                '_id': '$directors',
                'totalMovies': {
                    '$sum': 1
                }
            }
        }, {
            '$sort': {
                'totalMovies': -1
            }
        }, {
            '$limit': n1
        }
    ]

    results1 = collection.aggregate(pipeline1)
    for result in results1:
        print(f"Director - {result['_id']} ; No of movies - {result['totalMovies']}")


def task_2():
    n2 = int(input("Enter a number : "))
    year = int(input("Enter the year : "))
    pipeline2 = [
        {
            '$unwind': {
                'path': '$directors',
                'preserveNullAndEmptyArrays': False
            }
        }, {
            '$match': {
                'year': year
            }
        }, {
            '$group': {
                '_id': '$directors',
                'totalMovies': {
                    '$sum': 1
                }
            }
        }, {
            '$sort': {
                'totalMovies': -1
            }
        }, {
            '$limit': n2
        }
    ]

    results2 = collection.aggregate(pipeline2)
    for result in results2:
        print(f"Director - {result['_id']} ; No of movies - {result['totalMovies']}")


def task_3():
    genre = input("Enter a genre : ")
    n3 = int(input("Enter a number : "))

    pipeline3 = [
        {
            '$unwind': {
                'path': '$directors',
                'preserveNullAndEmptyArrays': False
            }
        }, {
            '$match': {
                'genres': genre
            }
        }, {
            '$group': {
                '_id': '$directors',
                'totalMovies': {
                    '$sum': 1
                }
            }
        }, {
            '$sort': {
                'totalMovies': -1
            }
        }, {
            '$limit': n3
        }
    ]

    results3 = collection.aggregate(pipeline3)
    for result in results3:
        print(f"Director - {result['_id']} ; No of movies - {result['totalMovies']}")


if __name__ == "__main__":

    try:
        client = MongoClient("mongodb://127.0.0.1:27017")
        print("Connection successful")
        print(client.server_info())

        collection = client['moviesData']['movies']
        print("Q4) Create Python methods and MongoDB queries to support the below operations -")
        print('''Choices : 
        Find top `N` directors 
        1. who created the maximum number of movies.
        2. who created the maximum number of movies in a given year.
        3. who created the maximum number of movies for a given genre
            ''')
        choice = int(input("Enter your choice : "))
        if choice == 1:
            task_1()
        elif choice == 2:
            task_2()
        elif choice == 3:
            task_3()

    except:
        print("Could not establish connection")