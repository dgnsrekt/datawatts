import sys
import os
import curses


def draw_menu(stdscr, dataname=None):
    k = 0
    cursor_x = 0
    cursor_y = 0

    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # Loop where k is the last character pressed
    while True:

        # Initialization
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        if k == curses.KEY_DOWN:
            cursor_y = cursor_y + 1
        elif k == ord('j'):
            cursor_y = cursor_y + 1

        elif k == curses.KEY_UP:
            cursor_y = cursor_y - 1
        elif k == ord('k'):
            cursor_y = cursor_y - 1

        elif k == curses.KEY_RIGHT:
            cursor_x = cursor_x + 1
        elif k == ord('l'):
            cursor_x = cursor_x + 1

        elif k == curses.KEY_LEFT:
            cursor_x = cursor_x - 1
        elif k == ord('h'):
            cursor_x = cursor_x - 1

        cursor_x = max(0, cursor_x)
        cursor_x = min(width-1, cursor_x)

        cursor_y = max(0, cursor_y)
        cursor_y = min(height-1, cursor_y)

        # Declaration of strings
        title = "Datawatts"[:width-1]
        if dataname == None:
            subtitle = "Datassette x Alan Watts"[:width-1]
        else:
            subtitle = f"{dataname} x Alan Watts"[:width-1]
        statusbarstr = "Press 'CTRL-C' to exit.| if zen != True, restart."

        # Centering calculations
        start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
        start_x_subtitle = int((width // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
        start_y = int((height // 2) - 2)

        # Render status bar
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(height-1, 0, statusbarstr)
        stdscr.addstr(height-1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))
        stdscr.attroff(curses.color_pair(3))

        # Turning on attributes for title
        stdscr.attron(curses.color_pair(2))
        stdscr.attron(curses.A_BOLD)

        # Rendering title
        stdscr.addstr(start_y, start_x_title, title)

        # Turning off attributes for title
        stdscr.attroff(curses.color_pair(2))
        stdscr.attroff(curses.A_BOLD)

        # Print rest of text
        stdscr.addstr(start_y + 1, start_x_subtitle, subtitle)
        # stdscr.addstr(start_y + 3, (width // 2) - 2, '-' * len(subtitle))
        stdscr.move(cursor_y, cursor_x)

        # Refresh the screen
        stdscr.refresh()

        # Wait for next input
        k = stdscr.getch()


def main_menu(dataname=None):
    curses.wrapper(draw_menu, dataname)


if __name__ == "__main__":
    main_menu()
