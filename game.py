#! /usr/bin/python3
import curses
from dataclasses import dataclass, field
import random

from windows import *

COMMAND_WIN_HEIGHT = 3

@dataclass
class APP:
    output_win: int
    info_win: int
    command_win: int
    hand_win: int
    stdscr: int
    motors: int = 0
    sensors: int = 0
    device: int = 0

@dataclass
class Entity():

    def __init__(self, name, hp = 100, deck = [], draw_limit = 4):
        self.name = name
        self.hp = hp
        self.deck = deck
        random.shuffle(self.deck)
        self.hand = self.deck[0:draw_limit]
        self.deck = self.deck[draw_limit:]
        self.discard = []
        self.draw_limit = draw_limit

    def use_card(self, n, target):
        self.hand[n].act(target)
        self.discard.append(self.hand.pop(n))
        self.hand.append(self.deck.pop(0))

    def damage(self, val):
        self.hp -= val
        if self.hp < 0:
            self.hp = 0

    def __str__(self):
        s = f'{self.name}: [HP: {self.hp}] [Deck: {len(self.deck)}] [Dis: {len(self.discard)}]'
        for i, c in enumerate(self.hand):
            s += f'\n[{i+1}] {str(c)}'
        return s

@dataclass
class Card():

    def __init__(self, name = 'default', val = 0):
        self.name = name
        self.val = val

    def act(self, target):
        return 'No function implemented'

    def __str__(self):
        return f'{self.name}: {self.val}'

class Attack_Card(Card):

    def act(self, target):
        target.damage(self.val)
        return f'{target.name} hit for {self.val}'


app = APP(0,0,0,0,0)

# def init_curses(stdscr):
#     curses.use_default_colors()
#     curses.init_pair(1, curses.COLOR_RED, -1)
#     curses.init_pair(2, curses.COLOR_GREEN, -1)
#     curses.init_pair(3, curses.COLOR_BLUE, -1)
#     curses.init_pair(4, curses.COLOR_YELLOW, -1)
#     curses.init_pair(5, curses.COLOR_CYAN, -1)
#     curses.init_pair(8, curses.COLOR_BLACK, -1)
#     curses.init_pair(9, curses.COLOR_WHITE, -1)

#     app.output_win = Output_Window(stdscr = stdscr, p_height = curses.LINES + 100, p_width = curses.COLS + 100,
#         resize_y = lambda std: 0, 
#         resize_x = lambda std: 0,d
#         resize_height = lambda std: std.getmaxyx()[0] - COMMAND_WIN_HEIGHT, 
#         resize_width = lambda std: std.getmaxyx()[1],
#         color = 2, pad = True, name = 'Y', margin = 1)
#     app.output_win.init_out()
#     app.output_win.border()

#     app.command_win = Command_Window(stdscr = stdscr, 
#         resize_y = lambda std: std.getmaxyx()[0] - COMMAND_WIN_HEIGHT, 
#         resize_x = lambda std: 0,
#         resize_height = lambda std: COMMAND_WIN_HEIGHT, 
#         resize_width = lambda std: std.getmaxyx()[1],
#         color = 3, pad = False, name = 'Z')
#     app.command_win.init_command()
#     app.command_win.border()

# s, h, c, d
# ♠♥♣♦

def main():
    deck = []
    for x in range(20):
        deck.append(Attack_Card(name = 'Attack', val = random.randint(5,10)))
    player = Entity(name = 'Player', deck = deck)
    print(player)
    player.use_card(1, player)
    print(player)

if __name__ == '__main__':
    main()