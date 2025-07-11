import time
import os
from rich.panel import Panel
from rich import print as Print
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table
from rich.text import Text

console = Console()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    clear_screen()
    Print(
        Panel(
            r"""
      [bold red]M   M      III           t      FFFF     l l           
      MM MM       I            t      F        l l           
      M M M y  y  I  nnn   ss ttt  aa FFF  ooo l l ooo w   w 
      M   M y  y  I  n  n  s   t  a a F    o o l l o o w w w 
      [bold white]M   M  yyy III n  n ss   tt aaa F    ooo l l ooo  w w  
               y || Coded by Rozhak
            yyy""",
            style="bold bright_yellow",
            width=70
        )
    )

def show_info(message, title="INFO"):
    Print(f"[bold bright_blue][{title}][/bold bright_blue] {message}")

def show_warning(message):
    Print(f"[bold yellow][WARNING][/bold yellow] {message}")

def show_error(message):
    Print(f"[bold red][ERROR][/bold red] {message}")

def show_success(message):
    Print(f"[bold green][SUCCESS][/bold green] {message}")

def show_fatal(message):
    Print(
        Panel(
            f"[bold red]{message}",
            style="bold red",
            title="[bold red]FATAL ERROR",
            width=70
        )
    )

def show_cycle_start(timestamp):
    Print(
        Panel(
            f"[bold white]Starting New Cycle: [bold green]{timestamp}",
            style="bold bright_cyan",
            title="[bold bright_cyan]CYCLE INITIATED",
            width=70
        )
    )

def show_service_init(service_name):
    Print(f"\n[bold bright_magenta][INIT][/bold bright_magenta] Running '[bold white]{service_name}[/bold white]' service...")

def show_cycle_complete():
    Print(
        Panel(
            "[bold white]All enabled services have been executed successfully!",
            style="bold green",
            title="[bold green]CYCLE COMPLETE",
            width=70
        )
    )

def show_sleep_info(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    
    if hours > 0:
        time_str = f"{hours} hour(s) {minutes} minute(s)"
    elif minutes > 0:
        time_str = f"{minutes} minute(s) {secs} second(s)"
    else:
        time_str = f"{secs} second(s)"
    
    Print(f"[bold bright_yellow][SLEEP][/bold bright_yellow] Waiting for [bold white]{time_str}[/bold white] before the next cycle...")

def show_countdown_progress(total_seconds):
    Print("\n" + "-"*69)
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
        transient=True
    ) as progress:
        initial_hours = total_seconds // 3600
        initial_minutes = (total_seconds % 3600) // 60
        
        task = progress.add_task(
            description=f"[bold bright_yellow]Sleeping for {initial_hours}h {initial_minutes}m...",
            total=total_seconds
        )
        
        remaining_seconds = total_seconds
        while remaining_seconds > 0:
            hours = remaining_seconds // 3600
            minutes = (remaining_seconds % 3600) // 60
            seconds = remaining_seconds % 60
            
            progress.update(
                task, 
                completed=total_seconds - remaining_seconds,
                description=f"[bold bright_yellow]Next cycle in: [bold white]{hours:02d}:{minutes:02d}:{seconds:02d}"
            )
            
            time.sleep(1)
            remaining_seconds -= 1

def show_wake_message():
    Print(
        Panel(
            "[bold white]Sleep completed! Starting next cycle...",
            style="bold bright_green",
            title="[bold bright_green]WAKE UP",
            width=70
        )
    )

def show_service_status_table(enabled_services):
    table = Table(title="[bold bright_cyan]Enabled Services Status", width=70)
    
    table.add_column("Service", style="bold white", justify="center")
    table.add_column("Status", style="bold green", justify="center")
    table.add_column("Interval", style="bold yellow", justify="center")
    
    for service in enabled_services:
        interval = service.config.get('interval_hours', 24)
        table.add_row(
            service.service_type.title(),
            "✓ Active",
            f"{interval}h"
        )
    
    console.print(table)

def show_no_services_message():
    Print(
        Panel(
            "[bold red]No services are enabled in the configuration.\n[bold white]Please check your config/services.json file.",
            style="bold red",
            title="[bold red]NO SERVICES ENABLED",
            width=70
        )
    )