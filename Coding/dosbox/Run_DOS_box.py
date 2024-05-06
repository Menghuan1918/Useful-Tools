import time
import subprocess
import curses
import re

way_to_edit = "nano"
times_between_commands = 0.25


def setup_colors():
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_RED, -1)
    curses.init_pair(2, curses.COLOR_GREEN, -1)
    curses.init_pair(3, curses.COLOR_BLUE, -1)
    curses.init_pair(4, curses.COLOR_WHITE, -1)


def multiple_choice(stdscr, window_id):
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
                0, 0, "Please select the target window, press any key to launch a new DosBox window:", curses.color_pair(1)
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
            return window_id[selected_index]
        elif key == curses.KEY_UP and selected_index == 0:
            selected_index = len(window_id) - 1
        elif key == curses.KEY_DOWN and selected_index == len(window_id) - 1:
            selected_index = 0
        elif key == curses.KEY_LEFT:
            return None
        elif key == ord("q"):
            return None
        else:
            subprocess.Popen(["dosbox"])
            time.sleep(2)
            return -1


def get_window_id(stdscr):
    try:
        window_id = (
            subprocess.check_output(["xdotool", "search", "--name", "Dosbox"])
            .decode()
            .strip()
        )
    except:
        subprocess.Popen(["dosbox"])
        time.sleep(2)
        window_id = (
            subprocess.check_output(["xdotool", "search", "--name", "Dosbox"])
            .decode()
            .strip()
        )
    window_id = window_id.split("\n")
    window_id_select = multiple_choice(stdscr, window_id)
    if not window_id_select:
        exit("No window selected")
    if window_id_select == -1:
        window_id_select = get_window_id(stdscr)
    return window_id_select


def input_dialog(stdscr, prompt):
    stdscr.clear()
    stdscr.addstr(prompt, curses.color_pair(2))
    stdscr.refresh()
    curses.echo()
    user_input = stdscr.getstr(0, len(prompt))
    curses.noecho()
    return user_input.decode()


def main(stdscr):
    setup_colors()
    stdscr.refresh()
    window_id = get_window_id(stdscr)

    while True:
        stdscr.clear()
        stdscr.addstr("e/E - Edit the enter code\n", curses.color_pair(4))
        stdscr.addstr("w/W - Reselect the window\n", curses.color_pair(4))
        stdscr.addstr("q/Q - Quit the program\n", curses.color_pair(4))
        stdscr.addstr("Any Other Key - Run the code\n", curses.color_pair(4))
        stdscr.refresh()
        choose = chr(stdscr.getch())

        if choose in ["e", "E"]:
            try:
                subprocess.call([way_to_edit, "codes.txt"])
            except:
                stdscr.addstr(
                    f"Could not open the file, use the command: {way_to_edit} codes.txt", curses.color_pair(1)
                )
                stdscr.refresh()
                time.sleep(2)
        elif choose in ["w", "W"]:
            window_id = get_window_id(stdscr)
        elif choose in ["q", "Q"]:
            break
        else:
            with open("codes.txt") as f:
                commands = [line.strip() for line in f]
            variables = {}
            for command in commands:
                if re.search(r"%%\w+", command):
                    variable = re.search(r"%%\w+", command).group(0)
                    if variable not in variables:
                        variables[variable] = input_dialog(
                            stdscr, f"Please input the value of {variable}:"
                        )
            run_command = []
            for command in commands:
                for variable, value in variables.items():
                        command = command.replace(variable, value)
                run_command.append(command)
            stdscr.clear()
            stdscr.refresh()
            stdscr.addstr("Running the code...", curses.color_pair(2))
            for command in run_command:
                subprocess.call(["xdotool", "type", "--window", window_id, command])
                subprocess.call(["xdotool", "key", "--window", window_id, "Return"])
                time.sleep(times_between_commands)

    curses.endwin()


curses.wrapper(main)