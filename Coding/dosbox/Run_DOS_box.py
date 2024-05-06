import time
import subprocess
import curses
import re

way_to_edit = "nano"
times_between_commands = 0.25


def multiple_choice(window_id):
    stdscr = curses.initscr()
    curses.start_color()
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.curs_set(0)
    stdscr.clear()
    stdscr.refresh()
    selected_index = 0
    window_name = []
    for i in window_id:
        window_name.append(
            subprocess.check_output(["xdotool", "getwindowname", i]).decode().strip()
        )
    while True:
        try:
            stdscr.addstr(
                0, 0, "Please select the target window,press any key to lauch a new DosBox window:", curses.color_pair(1)
            )
            for i, name in enumerate(window_name):
                if i == selected_index:
                    stdscr.addstr(i + 4, 0, f"> {name}", curses.color_pair(3))
                else:
                    stdscr.addstr(i + 4, 0, f"  {name}", curses.color_pair(4))
        except Exception:
            curses.endwin()
            input(
                "The terminal window is too small. Please resize it, then press Enter to exit"
            )
            exit()
        stdscr.refresh()
        stdscr.keypad(1)
        key = stdscr.getch()
        if key == curses.KEY_UP and selected_index > 0:
            selected_index -= 1
        elif key == curses.KEY_DOWN and selected_index < len(window_id) - 1:
            selected_index += 1
        elif key == ord("\n") or key == curses.KEY_RIGHT:
            curses.endwin()
            return window_id[selected_index]
        elif key == curses.KEY_UP and selected_index == 0:
            selected_index = len(window_id) - 1
        elif key == curses.KEY_DOWN and selected_index == len(window_id) - 1:
            selected_index = 0
        elif key == curses.KEY_LEFT:
            curses.endwin()
            return None
        elif key == ord("q"):
            curses.endwin()
            return None
        else:
            curses.endwin()
            subprocess.run(["dosbox"])
            time.sleep(2)
            return -1


def get_window_id():
    try:
        window_id = (
            subprocess.check_output(["xdotool", "search", "--name", "Dosbox"])
            .decode()
            .strip()
        )
    except:
        p = subprocess.run(["dosbox"])
        time.sleep(2)
        window_id = (
            subprocess.check_output(["xdotool", "search", "--name", "Dosbox"])
            .decode()
            .strip()
        )
    window_id = window_id.split("\n")
    window_id_select = multiple_choice(window_id)
    if not window_id_select:
        exit("No window selected")
    if window_id_select == -1:
        window_id_select = get_window_id()
    return window_id_select


def main():
    print("Select the window to interact with:")
    window_id = get_window_id()

    while True:
        choose = input(
"""
e/E - Edit the enter code\n
w/W - Reslect the window\n
q/Q - Quit the program\n
Any Other Key - Run the code\n
"""
        )
        if choose in ["e", "E"]:
            try:
                subprocess.call([way_to_edit, "codes.txt"])
            except:
                print(
                    f"Could not open the file, use the command: {way_to_edit} codes.txt"
                )
        elif choose in ["w", "W"]:
            window_id = get_window_id()
        elif choose in ["q", "Q"]:
            exit("Exiting the program")
        else:
            with open("codes.txt") as f:
                commands = f.readlines()
            variables = {}
            for command in commands:
                if re.match(r"%%[\w+]",command):
                    variable = re.match(r"%%([\w+])",command).group(1)
                    if variable not in variables:
                        variables[variable] = input(f"Please input the value of {variable}:")
            commands = [re.sub(r"%%[\w+]",variables[variable],command) for command in commands]
            for command in commands:
                subprocess.call(["xdotool", "type", "--window", window_id, command])
                subprocess.call(["xdotool", "key", "--window", window_id, "Return"])
                time.sleep(times_between_commands)

main()