import argparse
import time
import random
import requests
from colorama import Fore, Style, init
from rich.console import Console
from rich.table import Table
from rich.progress import track
from dorks import GOOGLE_DORKS

# Initialize colorama
init(autoreset=True)

# Initialize rich console
console = Console()

init(autoreset=True)

# Banner with colorama
BANNER = f"""
██████╗  ██████╗ ██████╗ ██╗  ██╗██╗███╗   ██╗ ██████╗ 
██╔══██╗██╔═══██╗██╔══██╗██║ ██╔╝██║████╗  ██║██╔════╝ 
██║  ██║██║   ██║██████╔╝█████╔╝ ██║██╔██╗ ██║██║  ███╗
██║  ██║██║   ██║██╔══██╗██╔═██╗ ██║██║╚██╗██║██║   ██║
██████╔╝╚██████╔╝██║  ██║██║  ██╗██║██║ ╚████║╚██████╔╝
╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
        Google Dorking Tool - By sh1vv
                Use Responsibly!
"""

# Replace with your Google API key and Custom Search Engine ID
API_KEY = "AIzaSyCKf9TrvVpnourFuuIMyKJb7hXn1j7cB0U"  # Your API key
CSE_ID = "348bc029cc42f4a1d"  # Your CSE ID

def google_search(query, api_key, cse_id, num_results=5):
    """
    Perform a Google search using the Custom Search JSON API.
    """
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "q": query,
        "key": api_key,
        "cx": cse_id,
        "num": num_results  # Number of results to return
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json().get("items", [])  # Return search results
    except requests.exceptions.RequestException as e:
        console.print(f"[bold red]Error with query '{query}': {e}[/bold red]")
        return []

def display_results(results, query):
    """
    Display search results in a rich table.
    """
    if results:
        table = Table(title=f"Search Results for [bold green]'{query}'[/bold green]")
        table.add_column("Title", style="cyan", no_wrap=True)
        table.add_column("URL", style="magenta")
        table.add_column("Snippet", style="yellow")

        for item in results:
            title = item.get("title", "No Title")
            link = item.get("link", "No URL")
            snippet = item.get("snippet", "No Snippet")
            table.add_row(title, link, snippet)

        console.print(table)
    else:
        console.print(f"[bold red]No results found for query: '{query}'[/bold red]")

def main():
    # Display the banner
    console.print(BANNER)

    parser = argparse.ArgumentParser(
        description="Automate Google dorks search for a given domain or wildcard."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-d", "--domain", help="Target domain (e.g., example.com)")
    group.add_argument("-w", "--wildcard", help="Target wildcard (e.g., *.example.com)")
    args = parser.parse_args()
    
    target = args.domain if args.domain else args.wildcard
    console.print(f"[bold blue]Starting search for target: {target}[/bold blue]\n")
    
    for dork in track(GOOGLE_DORKS, description="Processing dorks..."):
        query = dork.format(target=target)
        console.print(f"[bold yellow][*] Searching for: {query}[/bold yellow]")
        
        # Perform the search using the Google Custom Search API
        results = google_search(query, API_KEY, CSE_ID, num_results=5)
        
        # Display the results
        display_results(results, query)
        
        # Add a random delay between queries to avoid rate limiting
        delay = random.uniform(5, 15)
        console.print(f"[bold cyan]Sleeping for {delay:.2f} seconds...[/bold cyan]")
        time.sleep(delay)
        console.print("-" * 50)

if __name__ == "__main__":
    main()