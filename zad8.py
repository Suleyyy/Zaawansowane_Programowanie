from zad7 import fetch_breweries
import argparse

url = "https://api.openbrewerydb.org/v1/breweries"
breweries = fetch_breweries(url)

parser = argparse.ArgumentParser(description="Filter breweries by City")
parser.add_argument("--city", type=str, help="City name to filter breweries")
args = parser.parse_args()

if not args.city:
    for brewery in breweries:
        print(brewery, "\n")
else:
    found = False
    for brewery in breweries:
        if brewery.city.lower() == args.city.lower():
            print(brewery, "\n")
            found = True

    if not found:
        print(f"Nie znaleziono browarów w mieście: {args.city}")
