import os
import sys
import time
import random
import threading

COLORS = [
    "\033[31m",  # red
    "\033[32m",  # green
    "\033[33m",  # yellow
    "\033[34m",  # blue
    "\033[35m",  # magenta
    "\033[36m",  # cyan
]
RESET = "\033[0m"

TREE = [
    "         *         ",
    "        ***        ",
    "       *****       ",
    "      *******      ",
    "     *********     ",
    "    ***********    ",
    "   *************   ",
    "  ***************  ",
    " ***************** ",
    "        |||        ",
]

SONG = [
    "🎵 A face on a lover with a fire in his heart ❤️ ,",
    "🎵 A man under cover, but you tore me apart...❤️",
    "🎵 Ooh, now I've found a real love ❤️ ,",
    "🎵 You'll never fool me again! ❤️",
    "",
    "🎄 Merry Christmas 🎄",
]

running = True
lines_to_show = []


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def draw_tree():
    """Draw the tree in random colors."""
    for line in TREE:
        colored = ""
        for ch in line:
            if ch == "*":
                colored += random.choice(COLORS) + "*" + RESET
            else:
                colored += ch
        print(colored)


def draw_scene():
    """Draw both tree and lyrics together."""
    clear_screen()
    draw_tree()
    print()
    for line in lines_to_show:
        print(line)


def tree_animation():
    """Continuously blink the tree while the lyrics appear."""
    while running:
        draw_scene()
        time.sleep(0.3)


def slow_text(line, delay=0.05):
    """Type text one character at a time."""
    text = ""
    for ch in line:
        text += ch
        lines_to_show[-1] = text 
        time.sleep(delay)
    time.sleep(0.5)


def main():
    global running
    t = threading.Thread(target=tree_animation)
    t.start()

    for line in SONG:
        lines_to_show.append("") 
        slow_text(line, 0.06)

    running = False
    t.join()

if __name__ == "__main__":
    main()
