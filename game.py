#! /usr/bin/python3
import curses
from dataclasses import dataclass, field

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

app = APP(0,0,0,0,0)

def init_curses(stdscr):
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_RED, -1)
    curses.init_pair(2, curses.COLOR_GREEN, -1)
    curses.init_pair(3, curses.COLOR_BLUE, -1)
    curses.init_pair(4, curses.COLOR_YELLOW, -1)
    curses.init_pair(5, curses.COLOR_CYAN, -1)
    curses.init_pair(8, curses.COLOR_BLACK, -1)
    curses.init_pair(9, curses.COLOR_WHITE, -1)

    app.output_win = Output_Window(stdscr = stdscr, p_height = curses.LINES + 100, p_width = curses.COLS + 100,
        resize_y = lambda std: 0, 
        resize_x = lambda std: 0,
        resize_height = lambda std: std.getmaxyx()[0] - COMMAND_WIN_HEIGHT, 
        resize_width = lambda std: std.getmaxyx()[1],
        color = 2, pad = True, name = 'Y', margin = 1)
    app.output_win.init_out()
    app.output_win.border()

    app.command_win = Command_Window(stdscr = stdscr, 
        resize_y = lambda std: std.getmaxyx()[0] - COMMAND_WIN_HEIGHT, 
        resize_x = lambda std: 0,
        resize_height = lambda std: COMMAND_WIN_HEIGHT, 
        resize_width = lambda std: std.getmaxyx()[1],
        color = 3, pad = False, name = 'Z')
    app.command_win.init_command()
    app.command_win.border()

# s, h, c, d
# ♠♥♣♦

def main(stdscr):
    init_curses(stdscr)
    while True:
        if app.command_win.handle_user():
            x = app.command_win.get_command()
            if 'exit' in x:
                exit(0)
            elif 'c' in x:
                build_card()
            else:
                app.output_win.print_out(x)
        curses.doupdate()

if __name__ == '__main__':
    c = Card(3, 'h')
    c.draw_card()
    exit(0)
    curses.wrapper(main)
    print('Done Exec')