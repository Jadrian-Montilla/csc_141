def describe_city(city, country="united kingdom"):
    print(city.title()+ " is in "+ country.title())

describe_city("\nbuenas aires")
describe_city("\nbirmingham")
describe_city("\nlondon")

mess= ["\nHello! how are you doing?",
       "Yo, do you like books?",
       "I love eating tacos!"]

def show_message(send):
    for message in send:
        print(message)

show_message(mess)

import printing_functions 


printing_functions.print_models(printing_functions.unprinted_designs, 
                                printing_functions.completed_models)
printing_functions.show_completed_models(printing_functions.completed_models)