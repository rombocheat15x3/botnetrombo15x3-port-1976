import time
import os
import random
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

rombo_text = "★ starting botnet...C2 ★"

dragon_frame = r"""
░░███╗░░███████╗██╗░░██╗██████╗░
░████║░░██╔════╝╚██╗██╔╝╚════██╗
██╔██║░░██████╗░░╚███╔╝░░█████╔╝
╚═╝██║░░╚════██╗░██╔██╗░░╚═══██╗
███████╗██████╔╝██╔╝╚██╗██████╔╝
╚══════╝╚═════╝░╚═╝░░╚═╝╚═════╝░"""

line_colors = ["green", "bright_green", "cyan", "magenta"]
rain_chars = ["|", "!", "/", "\\", "1", "I"]

def generate_rain(width, height, density=0.05):
    rain = []
    for _ in range(height):
        line = "".join(random.choice(rain_chars) if random.random() < density else " " for _ in range(width))
        rain.append(line)
    return rain

def scroll_rain(rain_lines, width, density=0.05):
    rain_lines.pop(0)
    rain_lines.append("".join(random.choice(rain_chars) if random.random() < density else " " for _ in range(width)))

def hacker_interface(animated_time=5):
    width = console.width
    height = console.height - 10
    rain_lines = generate_rain(width, height)
    start_time = time.time()
    pos = 0
    direction = 1

    while time.time() - start_time < animated_time:
        clear()
        scroll_rain(rain_lines, width)
        for i, line in enumerate(rain_lines):
            color = line_colors[i % len(line_colors)]
            console.print(line, style=color)

        console.print(" " * pos + f"[bold cyan]{rombo_text}[/bold cyan]")

        panel = Panel(Text(dragon_frame, style="bold cyan"), title="[bold cyan]RoMboo15x3[/bold cyan]", border_style="cyan", width=min(80, width - 6))
        console.print(panel, justify="center")

        pos += direction
        if pos >= width - len(rombo_text) - 10:
            direction = -1
        elif pos <= 0:
            direction = 1

        time.sleep(0.03)

def login_interface():
    clear()
    console.print(Panel("[bold cyan]★ Welcome to Rombo Security BotnEt C2 ★[/bold cyan]", border_style="cyan"))
    username = console.input("[bold cyan]Enter Username: [/bold cyan]")
    password = console.input("[bold cyan]Enter Password: [/bold cyan]", password=True)

    if username == "rombo" and password == "15x3":
        console.print(f"[bold green]  Welcome, {username}! Access granted.[/bold green]")
        time.sleep(0.5)
        hacker_interface(animated_time=5)
        clear()
        console.print("[bold green] Starting the main tool...[/bold green]")
        time.sleep(1)
    else:
        console.print(Panel("[bold cyan] Incorrect Username or Password![/bold cyan]", border_style="cyan"))
        time.sleep(1)
        main()

def main():
    login_interface()

if __name__ == "__main__":
    main()
import os
import random
import socket
import sys
import threading
import time

class colors:
    CYAN = '\033[96m'
    RESET = '\033[0m'
    GREEN = '\033[92m'
    cyan = '\033[91m'
    YELLOW = '\033[93m'

banner = f"""{colors.CYAN}
     ██████╗░░█████╗░███╗░░░███╗██████╗░░█████╗░
     ██╔══██╗██╔══██╗████╗░████║██╔══██╗██╔══██╗
     ██████╔╝██║░░██║██╔████╔██║██████╦╝██║░░██║
     ██╔══██╗██║░░██║██║╚██╔╝██║██╔══██╗██║░░██║
     ██║░░██║╚█████╔╝██║░╚═╝░██║██████╦╝╚█████╔╝
     ╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝╚═════╝░░╚════╝░▀ ░
{colors.RESET}
"""

def print_methods():
    print(f"""
{colors.CYAN}Available Commands:{colors.RESET}
{colors.CYAN}Layer 7 Attacks:{colors.RESET}
  http-flood     - HTTP Flood Attack
  slowloris      - Slowloris Attack
  get-flood      - GET Request Flood
  post-flood     - POST Request Flood
  ssl-flood      - SSL/TLS Handshake Flood

{colors.CYAN}Layer 4 Attacks:{colors.RESET}
  udp-flood      - UDP Flood Attack
  tcp-flood      - TCP SYN Flood
  udp-kill       - Custom UDP Packet Attack
  tcp-ack        - TCP ACK Flood
  tcp-psh        - TCP PUSH Flood

{colors.CYAN}Other Commands:{colors.RESET}
  methods        - Show this methods menu
  exit           - Exit the program
  clear          - Clear the screen
""")

def hacker_animation():
    ascii_text = [
        f"{colors.GREEN}░░███╗░░███████╗██╗░░██╗██████╗░{colors.RESET}",
        f"{colors.GREEN}░████║░░██╔════╝╚██╗██╔╝╚════██╗{colors.RESET}",
        f"{colors.GREEN}██╔██║░░██████╗░░╚███╔╝░░█████╔╝{colors.RESET}",
        f"{colors.GREEN}╚═╝██║░░╚════██╗░██╔██╗░░╚═══██╗{colors.RESET}",
        f"{colors.GREEN}███████╗██████╔╝██╔╝╚██╗██████╔╝{colors.RESET}",
        f"{colors.GREEN}╚══════╝╚═════╝░╚═╝░░╚═╝╚═════╝░{colors.RESET}"
    ]
    for _ in range(5):
        os.system('cls' if os.name == 'nt' else 'clear')
        for line in ascii_text:
            print(line)
        time.sleep(0.15)

def fast_attack(name, target, port, duration):
    hacker_animation()
    print(f"{colors.CYAN}[+] Starting {name} to {target}:{port} for {duration} seconds...{colors.RESET}")
    end_time = time.time() + duration
    counter = 0
    while time.time() < end_time:
        counter += 1
        print(f"{colors.cyan}[{counter}] AttAcks Sond.. to {target}:{port} ...{colors.cyan}")
        time.sleep(0.01)  # very fast loop
    print(f"{colors.cyan}[✓] {name} completed! Total packets: {counter}{colors.cyan}")

def http_flood(target, port=80, duration=60):
    fast_attack("HTTP Flood", target, port, duration)

def slowloris(target, port=80, duration=60):
    fast_attack("Slowloris", target, port, duration)

def udp_flood(target, port=53, duration=60):
    fast_attack("UDP Flood", target, port, duration)

def tcp_syn_flood(target, port=80, duration=60):
    fast_attack("TCP SYN Flood", target, port, duration)

def udp_kill(target, port=random.randint(1024, 65535), duration=60):
    fast_attack("UDP Kill", target, port, duration)

def main():
    print(banner)
    print(f"{colors.CYAN}[!] Info: Botnet 15x3 C++ Online 2 Owner Instagram romboudp !{colors.RESET}\n")
    
    while True:
        try:
            cmd = input(f"{colors.CYAN}[root]-RoMboo15x3> {colors.RESET}").strip().lower()
            
            if cmd == "methods":
                print_methods()
            elif cmd == "clear":
                os.system('clear' if os.name == 'posix' else 'cls')
                print(banner)
            elif cmd == "exit":
                print(f"{colors.CYAN}[+] Exiting...{colors.RESET}")
                break
            elif cmd.startswith(("http-flood","slowloris","udp-flood","tcp-flood","udp-kill")):
                args = cmd.split()
                target = args[1] if len(args) > 1 else input("Target IP/Host: ")
                port = int(args[2]) if len(args) > 2 else 80
                duration = int(args[3]) if len(args) > 3 else 60
                if cmd.startswith("http-flood"):
                    http_flood(target, port, duration)
                elif cmd.startswith("slowloris"):
                    slowloris(target, port, duration)
                elif cmd.startswith("udp-flood"):
                    udp_flood(target, port, duration)
                elif cmd.startswith("tcp-flood"):
                    tcp_syn_flood(target, port, duration)
                elif cmd.startswith("udp-kill"):
                    udp_kill(target, port, duration)
            else:
                print(f"{colors.CYAN}[-] Unknown command. Type 'methods' for available commands.{colors.RESET}")
        except KeyboardInterrupt:
            print(f"\n{colors.CYAN}[+] Exiting...{colors.RESET}")
            break
        except Exception as e:
            print(f"{colors.CYAN}[-] Error: {str(e)}{colors.RESET}")

if __name__ == "__main__":
    main()