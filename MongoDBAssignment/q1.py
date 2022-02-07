from pymongo import MongoClient

if __name__ == "__main__":

    print("Q1) Python application to connect to MongoDB.")
    try:
        client = MongoClient("mongodb://127.0.0.1:27017")
        print("Connection successful")
        print(client.server_info())
    except:
        print("Could not establish connection")
