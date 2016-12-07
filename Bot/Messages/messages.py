import json

class MessagePasrser():
    def parse (self, messages):
        # Detect type of incoming data
        if type(messages) == type(dict()): # Single message
            return [Message(messages)]
        # Multi message string
        parsed_messages = []
        for message in messages:
            parsed_messages.append(Message(message["message"]))    
        return parsed_messages
    

 
class Message():
    class ChatInfo():
        def __init__(self, chat_info):
            self.id = chat_info["id"]
            self.username = chat_info["username"]
            self.first_name = chat_info["first_name"]
            self.last_name = chat_info["last_name"]
            self.type = chat_info["type"]  
    
    class FromInfo():
        def __init__(self, from_info):
            self.id = from_info["id"]
            self.username = from_info["username"]
            self.first_name = from_info["first_name"]
            self.last_name = from_info["last_name"]

    def __init__(self, message):
        self.origin = message
        #print("_______parsing message_______")
        #print(message)
        #print("_______done parsing message_______")
        self.id = message['message_id']
        self.date = message['date']
        self.text = message['text']
        self.chat_info = self.ChatInfo(message["chat"])
        self.from_info = self.FromInfo(message["from"])
        
    def to_string():
        print (self.origin)
 

text_message_example = """{"message_id": 77, 
                        "date": 1481125773, 
                        "text": "asdas", 
                        "from": {"first_name": "Kirill", 
                                 "id": 75498542, 
                                 "username": "kiparis87", 
                                 "last_name": "Kostenkov"
                                }, 
                        "chat": {"first_name": "Kirill", 
                                 "type": "private", 
                                 "id": 75498542, 
                                 "username": "kiparis87", 
                                 "last_name": "Kostenkov"
                                }
                        }"""
                        
dict_message_example = {'message_id': 77, 
                        'date': 1481125773, 
                        'text': 'asdas', 
                        'from': {'first_name': 'Kirill', 
                                 'id': 75498542, 
                                 'username': 'kiparis87', 
                                 'last_name': 'Kostenkov'
                                }, 
                        'chat': {'first_name': 'Kirill', 
                                 'type': 'private', 
                                 'id': 75498542, 
                                 'username': 'kiparis87', 
                                 'last_name': 'Kostenkov'
                                }
                        }
                        
if __name__ == "__main__":                       
    print("processing example")
    message = Message(text_message_example);
    print("done")
    print(message.id)
    print("chat id " + str(message.chat_info.id))
    #print(message.origin)