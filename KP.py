####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

import random

team_name = 'KellyUtah'
strategy_name = 'Tit for Tat'
strategy_description = 'random start, then copy opponent\'s last move'

    
def move(my_history, their_history, my_score, their_score):
    if len(my_history) == 0:
        return random.choice(['c', 'b'])
    else:
        return their_history[-1]
