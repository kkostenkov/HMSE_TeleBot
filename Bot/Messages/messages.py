import json

class MessageParser():
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
            if chat_info is None:
                return
            self.id = chat_info["id"]
            self.username = chat_info.get("username", "None")
            self.first_name = chat_info.get("first_name", "")
            self.last_name = chat_info.get("last_name", "")
            self.type = chat_info.get("type", "")
    
    class FromInfo():
        def __init__(self, from_info):
            self.id = from_info["id"]
            self.username = from_info.get("username", "None")
            self.first_name = from_info.get("first_name", "")
            self.last_name = from_info.get("last_name", "")

    def __init__(self, message):
        self.origin = message
        print("_______parsing message_______")
        print(message)
        print("_______done parsing message_______")
        self.id = message.get('message_id', "")
        self.date = message.get('date', "")
        self.text = message.get('text', "")
        self.chat_info = self.ChatInfo(message.get("chat", None))
        self.from_info = self.FromInfo(message.get("from", None))
        if "game_short_name" in message:
           self.text = "/game"
           self.game_request = message["game_short_name"]
           self.chat_instance = message["chat_instance"]
        
    def __str__(self):
        return str(self.origin)
 

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
