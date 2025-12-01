# import random

# random.seed(None)

# a = [1]
# print(a[:10])
# print(sorted([]))

# import time
# import sys

# symbols = ['⣾', '⣷', '⣯', '⣟', '⡿', '⢿', '⣻', '⣽']
# i = 0
# while True:
#     i = (i + 1) % len(symbols)
#     # \r moves cursor to start of line, \033[K clears from cursor to end
#     sys.stdout.write('\r\033[K%s Loading...' % symbols[i])
#     sys.stdout.flush() # Ensure immediate output
#     time.sleep(0.1)

from rich.live import Live
from rich.console import Console
import time

console = Console()

def animate_spinner():
    spinners = ["-", "\\", "|", "/"]
    index = 0
    while True:
        yield f"Processing... {spinners[index % len(spinners)]}"
        index += 1
        time.sleep(0.1)

with Live(animate_spinner(), screen=True, refresh_per_second=10) as live:
    # Simulate some background processing
    time.sleep(2)
    
    # Take input while the animation is running
    user_input = console.input("[bold green]Enter your name: [/bold green]")
    live.update(f"Hello, [bold blue]{user_input}[/bold blue]!")
    time.sleep(2)