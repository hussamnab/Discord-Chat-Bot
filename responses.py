import random

def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hey!'
    
    if p_message == 'roll dice':
        return str(random.randint(1,6))
    
    if p_message == '!help':
        return "`This is a help message`"
    
    # return "I'm sorry, I didn't get that."