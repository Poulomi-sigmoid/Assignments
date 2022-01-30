class Logger:

    def __init__(self):
        self.incoming_messages = {}

    def should_print_message(self, timestamp=None, message=None):
        if timestamp is None or message is None:
            return
        if message in self.incoming_messages.keys():
            if timestamp < self.incoming_messages[message]:
                return False
            else:
                self.incoming_messages[message] = timestamp + 10
                return True
        else:
            self.incoming_messages[message] = timestamp + 10
            return True


logger = Logger()
result = []

print("Type 'quit' anytime to exit.")

try:
    while True:
        timestamp = input("Enter the timestamp : ")
        if timestamp.lower() == 'quit':
            break
        elif timestamp != '':
            timestamp = int(timestamp)
        message = input("Enter the message : ")
        if message.lower() == 'quit':
            break
        print()
        if timestamp == '' and message == '':
            result.append(logger.should_print_message())
        else:
            result.append(logger.should_print_message(timestamp, message))

    print()
    print("Output logs :- ")
    for log in result:
        print(log)

except ValueError:
    print("Please enter timestamp in number format only")

except:
    print("Please enter a valid input")
