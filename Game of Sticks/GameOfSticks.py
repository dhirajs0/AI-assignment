import random

def game_over_decision(game_sticks):
    if game_sticks <= 0:
        return True
    else:
        return False


def continue_game(): 
    continue_game = ''
    continue_bool = False
    while True:
        continue_game = input("Play again? [Y/n]: ").lower()
        if continue_game == '' or continue_game == 'y':
            continue_bool = True
            break
        elif continue_game == 'n':
            continue_bool = False
            print('\nSee You....\n\n')
            break
        else:
            continue
    return continue_bool

def mode_selection():
    while True:
        game_mode = input("The game mode by number:"
                          "\n  (1) Human vs AI \n  (2) AI vs AI\n> ")
        try:
            game_mode = int(game_mode)
            if 1 <= game_mode <= 2:
                break
            else:
                print('Choose the game mode  (1 or 2)')
                continue
        except:
            print('Choose the game mode (1 or 2)')
            continue
    return game_mode

def num_of_sticks_allowed(player, min_stick_choice=1, max_stick_choice=3):
    player_move = ''
    while True:
        if max_stick_choice > 3:
            player_move = input('Number of sticks on the table initially ({}-{})?\n> '.format(min_stick_choice, max_stick_choice))
        else:
            player_move = input('{}: How many sticks will you take (1-3)? '.format(player))
        try:
            player_move = int(player_move)
            if min_stick_choice <= player_move <= max_stick_choice:
                break
            else:
                print('Enter a no. between {} and {}.'.format(min_stick_choice, max_stick_choice))
                continue
        except:
            print('Enter a no. between {} and {}.'.format(min_stick_choice, max_stick_choice))
            continue
    print('')
    return player_move


def initialize_ai(name):
    ret_dict = {}
    for n in list(range(1,101)):
        ret_dict[n] = {'hat': [1, 2, 3], 'beside': []}
    return ret_dict


def generate_ai_beside(ai_dict, game_sticks):
    ret = dict(ai_dict)
    ret[game_sticks]['beside'].append(random.choice(ret[game_sticks]['hat']))
    return ret[game_sticks]['beside'][0], ret

def ai_loses(ai_dict):
    temp_dict = dict(ai_dict)
    for num_sticks, stick_dict in temp_dict.items():
        if len(str(stick_dict['beside'])) > 0:
            if ai_dict[num_sticks]['beside'].count(ai_dict[num_sticks]['hat']) > 1:
                ai_dict[num_sticks]['hat'].remove(ai_dict[num_sticks]['beside'])
            ai_dict[num_sticks]['beside'] = []
    return ai_dict


def ai_wins(ai_dict):
    for num_sticks, stick_dict in ai_dict.items():
        if len(str(stick_dict['beside'])) > 0:
            stick_dict['hat'].extend(stick_dict['beside'])
            stick_dict['beside'] = []
    return ai_dict

def ai_ai_loop(players, ai_player_1, ai_player_2, game_mode, game_sticks):
    count = 0
    player_move = 0
    play_again = False

    while True:
        print('There are {} sticks on the board.'.format(game_sticks))

        if count % 2 == 1 and game_mode == 2:
            player_move, ai_player_1 = generate_ai_beside(ai_player_1, game_sticks)
            print(ai_player_1[game_sticks]['hat'])
            print('{}: How many sticks will you take (1-3)? {}'.format(players[count % 2], player_move))
        elif count % 2 == 0 and game_mode == 2:
            player_move, ai_player_2 = generate_ai_beside(ai_player_2, game_sticks)
            print(ai_player_2[game_sticks]['hat'])
            print('{}: How many sticks will you take (1-3)? {}'.format(players[count % 2], player_move))

        game_sticks = game_sticks - player_move

        if game_over_decision(game_sticks):
            if count % 2 == 1:
                print('AI-1 Loses....')
                ai_loses(ai_player_1)
            else:
                print('AI-1 Wins....')
                ai_wins(ai_player_1)
            if count % 2 == 0:
                print('AI-2 Loses....')
                ai_loses(ai_player_2)
            else:
                print('AI-2 Wins....')
                ai_wins(ai_player_2)
            break
        print('')
        count += 1

    play_again = continue_game()
    return play_again

def ai_human_loop(players, game_sticks, game_mode, ai_player_1):
    count = random.randint(1,1000)           
    player_move = None  
    play_again = False  

    while True:
        print('There are {} sticks on the board.'.format(game_sticks))

        if count % 2 == 1 and game_mode == 1:
            player_move, ai_player_1 = generate_ai_beside(ai_player_1, game_sticks)
            print(ai_player_1[game_sticks]['hat'])
            print('{}: How many sticks will you take (1-3)? {}'.format(players[count % 2], player_move))
        else:
            player_move = num_of_sticks_allowed(players[count % 2])

        game_sticks = game_sticks - player_move 

        if game_over_decision(game_sticks):
            print('\n{}, you lose.\n\n'.format(players[count % 2]))
            if game_mode >= 2:
                if count % 2 == 1:
                    ai_loses(ai_player_1)
                else:
                    ai_wins(ai_player_1)
            break
        print('')
        count += 1

    play_again = continue_game()
    return play_again

def main():
    players = []            
                            
    min_start_sticks = 10
    max_start_sticks = 100
    game_sticks = 0         
    game_mode = None        
    play_again = False
    ai_player_1 = {}
    ai_player_2 = {}

    print('Welcome to the Game of Sticks!')

    while True:
        if not play_again:
            game_mode = mode_selection()
            if game_mode == 1:
                players.append('Human')
                players.append('AI')
                ai_player_1 = initialize_ai('AI')
            if game_mode == 2:
                players.append('AI-1')
                players.append('AI-2')
                ai_player_1 = initialize_ai('AI-1')
                print('Your AI-1 is ready!!')
                ai_player_2 = initialize_ai('AI-2')
                print('Your AI-2 is ready!!')
                print('AI vs AI started....')

        game_sticks = num_of_sticks_allowed(players[0], min_start_sticks, max_start_sticks)
        if(game_mode == 2):
            play_again = ai_ai_loop(players, ai_player_1, ai_player_2, game_mode, game_sticks)
        else:
            play_again = ai_human_loop(players, game_sticks, game_mode, ai_player_1)

        if not play_again:
            break

if __name__ == '__main__':
    main()