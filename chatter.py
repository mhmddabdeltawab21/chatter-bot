import random

class Botchat():

    def __init__(self):
        self.response_dict = {}

    def add_responses(self ,keys ,values):
        key = tuple(keys)
        value = tuple(values)
        self.response_dict[key] = value

    def add_response(self ,key ,value):
        self.response_dict[key] = value

    def get_response(self , key):

        for keys ,value in self.response_dict.items():
            if key in keys:
                return random.choice(value)

    def print_dict(self):
        print(self.response_dict)

def main():
    new_bot = Botchat()

    new_bot.add_response('hi' , 'hi sir')
    new_bot.add_responses(['how are you' , 'how are you?'] , ['fine ,thanks , how about you' , 'fine and you' , 'doing well'] )

    user_text = input('say something .\n')

    print(new_bot.get_response(user_text))

    again = input('want to try again ?\n').lower()

    if again == 'y':
        main()


main()
