import pyjokes
from art import text2art
from menu import menu_output, continue_request
from recomendations import what_to_watch, what_to_listen, what_to_play
from games import crosses

Logo = text2art("FunChat",font='block',chr_ignore=True)
print(Logo)

while True:
    match menu_output():
        case '1':
            what_to_watch()
            continue_request()
        case '2':
            what_to_listen()
            continue_request()
        case '3':
            what_to_play()
            continue_request()
        case '4':
            print(pyjokes.get_joke())
            continue_request()
        case '5':
            crosses()
            continue_request()
        case '0':
            exit(0)
