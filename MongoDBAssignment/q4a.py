from pymongo import MongoClient

def task_i():
    pipeline1 = [
        {
            '$group': {
                '_id': '$name',
                'totalComments': {
                    '$sum': 1
                }
            }
        }, {
            '$sort': {
                'totalComments': -1
            }
        }, {
            '$limit': 10
        }
    ]

    results1 = collection.aggregate(pipeline1)
    for users in results1:
        print(f" User - {users['_id']};   Total Comments - {users['totalComments']}")


def task_ii():
    pipeline2 = [
        {
            '$group': {
                '_id': '$movie_id',
                'totalComments': {
                    '$sum': 1
                }
            }
        }, {
            '$sort': {
                'totalComments': -1
            }
        }, {
            '$limit': 10
        }, {
            '$lookup': {
                'from': 'movies',
                'localField': '_id',
                'foreignField': '_id',
                'as': 'movie'
            }
        }, {
            '$unwind': {
                'path': '$movie',
                'preserveNullAndEmptyArrays': False
            }
        }, {
            '$project': {
                'totalComments': 1,
                '_id': 0,
                'movie.title': 1
            }
        }
    ]

    results2 = collection.aggregate(pipeline2)
    for movie in results2:
        print(f"Movie - {movie['movie']['title']} ; Total comments - {movie['totalComments']}")

def task_iii():
    year = int(input("Enter the year in which you want to see the comment counts per month : "))
    pipeline3 = [
        {
            '$project': {
                'month': {
                    '$month': '$date'
                },
                'year': {
                    '$year': '$date'
                },
                'text': 1
            }
        }, {
            '$match': {
                'year': year
            }
        }, {
            '$group': {
                '_id': '$month',
                'totalComments': {
                    '$sum': 1
                }
            }
        }, {
            '$sort': {
                '_id': 1
            }
        }
    ]

    results3 = collection.aggregate(pipeline3)
    for result in results3:
        print(f"Month - {result['_id']}  ;  Total Comments - {result['totalComments']}")


if __name__ == "__main__":

    try:
        client = MongoClient("mongodb://127.0.0.1:27017")
        print("Connection successful")
        print(client.server_info())

        collection = client['moviesData']['comments']
        print("Q3) Create Python methods and MongoDB queries to support the below operations -")
        print('''Choices : 
        1. Find top 10 users who made the maximum number of comments.
        2. Find top 10 movies with most comments.
        3. Given a year find the total number of comments created each month in that year
            ''')
        choice = int(input("Enter your choice : "))
        if choice == 1:
            task_i()
        elif choice == 2:
            task_ii()
        elif choice == 3:
            task_iii()

    except:
        print("Could not establish connection")
