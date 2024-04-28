import os
import subprocess
import curses

def get_files_and_directories(path):
    entries = os.listdir(path)
    files = [entry for entry in entries if entry.endswith('.l')]
    directories = [entry for entry in entries if os.path.isdir(os.path.join(path, entry))]
    return files, directories

def display_menu(stdscr, current_path, files, directories):
    stdscr.clear()
    stdscr.addstr(0, 0, f"Current directory: {current_path}", curses.color_pair(1))
    stdscr.addstr(2, 0, "Select a file or directory:", curses.color_pair(2))

    entries = ['..'] + directories + files
    selected_index = 0

    while True:
        try:
            for i, entry in enumerate(entries):
                if i == selected_index:
                    stdscr.addstr(i + 4, 0, f"> {entry}", curses.color_pair(3))
                else:
                    stdscr.addstr(i + 4, 0, f"  {entry}", curses.color_pair(4))
        except Exception:
            curses.endwin()
            input("The terminal window is too small. Please resize it, then press Enter to exit")
            exit()
        stdscr.refresh()

        key = stdscr.getch()
        if key == curses.KEY_UP and selected_index > 0:
            selected_index -= 1
        elif key == curses.KEY_DOWN and selected_index < len(entries) - 1:
            selected_index += 1
        elif key == ord('\n') or key == curses.KEY_RIGHT:
            return entries[selected_index]
        elif key == curses.KEY_UP and selected_index == 0:
            selected_index = len(entries) - 1
        elif key == curses.KEY_DOWN and selected_index == len(entries) - 1:
            selected_index = 0
        elif key == curses.KEY_LEFT:
            return entries[0]
        elif key == ord('q'):
            return None

def compile_and_run(file_path):
    directory = os.path.dirname(file_path)
    output_directory = os.path.join(directory, 'output')
    os.makedirs(output_directory, exist_ok=True)

    lex_file = os.path.join(output_directory, 'lex.yy.c')
    try:
        subprocess.run(['flex', '-o', lex_file, file_path], check=True, stderr=subprocess.PIPE, universal_newlines=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred during flex compilation:\n{e.stderr}")
        return

    executable = os.path.join(output_directory, 'a.out')
    try:
        subprocess.run(['gcc', '-o', executable, lex_file], check=True, stderr=subprocess.PIPE, universal_newlines=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred during gcc compilation:\n{e.stderr}")
        return
    print(f"Running {executable}:")
    subprocess.run([executable])

def main(stdscr):
    curses.curs_set(0)  # 隐藏光标
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK)

    current_path = os.getcwd()

    while True:
        files, directories = get_files_and_directories(current_path)
        selected_entry = display_menu(stdscr, current_path, files, directories)

        if selected_entry is None:
            curses.endwin()
            return None
        elif selected_entry == '..':
            current_path = os.path.dirname(current_path)
        elif selected_entry in directories:
            current_path = os.path.join(current_path, selected_entry)
        elif selected_entry in files:
            file_path = os.path.join(current_path, selected_entry)
            curses.endwin()
            return file_path

file_path = curses.wrapper(main)
if file_path is None:
    print("Program terminated.")
compile_and_run(file_path)