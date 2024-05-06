# 快捷地与DOSBox进行交互
![Python 3.x](https://img.shields.io/badge/Python-3.X-blue) ![Static Badge](https://img.shields.io/badge/%E4%B8%8D%E9%9C%80%E8%A6%81%E5%A4%96%E9%83%A8%E5%BA%93-green) ![Static Badge](https://img.shields.io/badge/Linux-%E5%8F%AF%E7%94%A8-green) ![Static Badge](https://img.shields.io/badge/Windows-%E4%B8%8D%E5%8F%AF%E7%94%A8-red)


> [!IMPORTANT]
> 仅在**Linux**上生效，因为使用了`xdotool`对DOSBox发送按键。
> 请确保你已经安装了`xdotool`，不过除此之外不需要任何别的依赖。
> Ubuntu/Debian:`sudo apt install xdotool`
> Arch/Manjaro:`sudo pacman -S xdotool`

> 在`xdotool`已经安装的前提下，直接使用python运行Run_flex_file.py即可。

程序查找dosbox窗口，如未找到则会启动。其中在窗口选择阶段按下除了`q`之外的字母键也会重新启动一个新的dosbox窗口。

使用↑↓调整选择，→或Enter键选择，`q`键退出。程序将会读取其目录下的`codes.txt`中的命令,一行一个命令，空行将识别为回车。

## 自定义执行的一些参数
编辑Run_flex_file.py第6行开始的变量名即可，其含意如下：

- `way_to_edit`：使用的文本编辑器，默认是`nano`。
- `times_between_commands`：每行代码之间输入的间隔，默认是`0.25`秒。
- `start_command`：DOSBox启动的参数，默认是不带任何参数的`dosbox`。

## 简单的变量功能
你可以使用 `%%` 代表其后所跟随的名字是一个变量名，程序会自动识别并每次询问你变量值应当是多少。例如：

```txt
MOV BL,%%BL
```

其中**%%BL**就是一个变量，每次运行时程序将会询问你变量的值。