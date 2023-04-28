def menu_output():
    """Outputs main menu text, returns user's choice as str"""
    menu_title = 'Wassup!! You are in FunChat! Make a choice and have fun!'
    menu_list = (
        ('1', 'What to watch?'),
        ('2', 'What to listen?'),
        ('3', 'What to play?'),
        ('4', 'Want a joke? :)'),
        ('5', 'Let\'s play some games!'),
        ('0', 'Exit')
        )
    print(menu_title)
    for i in range(len(menu_list)):
        print(menu_list[i][0] + '.', menu_list[i][1])
    menu_choice = input('So what? ')
    while menu_choice not in list('012345'):
        menu_choice = input('Try again: ')
    return menu_choice

def continue_request():
    request = input('Do you want some more? (Y/n) ')
    if request == 'n':
        exit(0)

