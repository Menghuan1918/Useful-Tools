[dosbox.webm](https://github.com/Menghuan1918/Useful-Tools/assets/122662527/7cdc7708-ef20-47a6-ab07-affb3bbc7054)

# Fast interaction with DOSBox
English|[简体中文](Run_DOS_box_CN.md)

![Python 3.x](https://img.shields.io/badge/Python-3.X-blue) ![Static Badge](https://img.shields.io/badge/No%20external%20libraries-green) ![Static Badge](https://img.shields.io/badge/Linux-Available-grenn) ![Static Badge](https://img.shields.io/badge/Windows-Unavailable-red)

> [!IMPORTANT]
> Only works on **Linux** because `xdotool` is used to send keystrokes to the DOSBox.  
> Make sure you have `xdotool` installed, but other than that you don't need any other dependencies.  
> Ubuntu/Debian:`sudo apt install xdotool`  
> Arch/Manjaro:`sudo pacman -S xdotool`

> Just run Run_DOS_box.py directly with python.

The programme looks for a dosbox window and starts it if not found. Where pressing a letter key other than `q` during the window selection phase also restarts a new dosbox window.

Use the ↑↓ adjustment to select, the → or Enter key to select, and the `q` key to exit. The program will read the commands in `codes.txt` in its directory.One command per line, blank lines will be recognised as carriage returns.

## Some parameters for custom execution
Just edit the variable names starting on line 6 of Run_flex_file.py to mean the following:

- `way_to_edit`: the text editor to use, default is `nano`.
- `times_between_commands`: the interval to type between each line of code, default is `0.25` seconds.
- `start_command`: parameters for DOSBox startup, default is `dosbox` without any parameters.

## Simple variable functions
You can use `%%` to mean that the name that follows is a variable name, which the programme will automatically recognise and ask you each time what the value of the variable should be. For example:

```txt
MOV BL,%%BL
```

where **%%BL** is a variable, and the program will ask you for the value of the variable each time it runs.

