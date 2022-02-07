from pymongo import MongoClient

def task_1():
    n1 = int(input("Enter a number : "))
    pipeline1 = [
        {
            '$match': {
                'imdb.rating': {
                    '$ne': ''
                }
            }
        }, {
            '$sort': {
                'imdb.rating': -1
            }
        }, {
            '$project': {
                'movie': '$title',
                'rating': '$imdb.rating'
            }
        }, {
            '$limit': n1
        }
    ]

    result1 = collection.aggregate(pipeline1)
    for movie in result1:
        print(f"Movie - {movie['movie']} ; IMDB Rating - {movie['rating']}")

def task_2():
    year = int(input("Enter the year in which you want to see the highest rated movie : "))
    n2 = int(input("Enter a number : "))
    pipeline2 = [
        {
            '$project': {
                'movie': '$title',
                'rating': '$imdb.rating',
                'year': {
                    '$year': '$released'
                }
            }
        }, {
            '$match': {
                'imdb.rating': {
                    '$ne': ''
                },
                'year': year
            }
        }, {
            '$sort': {
                'rating': -1
            }
        }, {
            '$limit': n2
        }
    ]

    result2 = collection.aggregate(pipeline2)
    for movie in result2:
        print(f"Movie - {movie['movie']} ; IMDB Rating - {movie['rating']}")

def task_3():
    n3 = int(input("Enter a number : "))
    pipeline3 = [
        {
            '$project': {
                'movie': '$title',
                'rating': '$imdb.rating',
                'votes': '$imdb.votes'
            }
        }, {
            '$match': {
                'imdb.rating': {
                    '$ne': ''
                },
                'votes': {
                    '$gt': 1000
                }
            }
        }, {
            '$sort': {
                'rating': -1
            }
        }, {
            '$limit': n3
        }
    ]

    result3 = collection.aggregate(pipeline3)
    for movie in result3:
        print(f"Movie - {movie['movie']} ; IMDB Rating - {movie['rating']} ; Votes - {movie['votes']}")

def task_4():

    n4 = int(input("Enter a number : "))
    string = input("Enter a string to be matched : ")
    pipeline4 = [
        {
            '$match': {
                'title': {
                    '$regex': string
                }
            }
        }, {
            '$project': {
                'title': 1,
                'rating': '$tomatoes.viewer.rating'
            }
        }, {
            '$sort': {
                'rating': -1
            }
        }, {
            '$limit': n4
        }
    ]

    result4 = collection.aggregate(pipeline4)
    for movie in result4:
        print(f"Movie - {movie['title']} ; IMDB Rating - {movie['rating']}")


if __name__ == "__main__":

    try:
        client = MongoClient("mongodb://127.0.0.1:27017")
        print("Connection successful")
        print(client.server_info())

        collection = client['moviesData']['movies']
        print("Q4) Create Python methods and MongoDB queries to support the below operations -")
        print('''Choices : 
        Find top `N` movies 
        1. with the highest IMDB rating.
        2. with the highest IMDB rating in a given year.
        3. with highest IMDB rating with number of votes > 1000
        4. with title matching a given pattern sorted by highest tomatoes ratings
            ''')
        choice = int(input("Enter your choice : "))
        if choice == 1:
            task_1()
        elif choice == 2:
            task_2()
        elif choice == 3:
            task_3()
        elif choice == 4:
            task_4()

    except:
        print("Could not establish connection")