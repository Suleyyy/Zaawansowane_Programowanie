from typing import Optional
import requests

class Brewery:
    def __init__(self, id: str, name: str, brewery_type: str,
                address_1: Optional[str], address_2: Optional[str], address_3: Optional[str],
                city: str, state_province: str, postal_code: str, country: str, longitude: Optional[float], latitude: Optional[float],
                phone: Optional[str], website_url: Optional[str], state: str, street: Optional[str]):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.address_1 = address_1
        self.address_2 = address_2
        self.address_3 = address_3
        self.city = city
        self.state_province = state_province
        self.postal_code = postal_code
        self.country = country
        self.longitude = longitude
        self.latitude = latitude
        self.phone = phone
        self.website_url = website_url
        self.state = state
        self.street = street

    def __str__(self):
        return f"Brewery(id={self.id}, name={self.name}, brewery_type={self.brewery_type}, \n" \
                f"address_1={self.address_1}, address_2={self.address_2}, address_3={self.address_3}, \n" \
                f"city={self.city}, state_province={self.state_province}, postal_code={self.postal_code}, \n" \
                f"country={self.country}, longitude={self.longitude}, latitude={self.latitude}, \n"\
                f"phone={self.phone}, website_url={self.website_url}, state={self.state}, street={self.street})"

def fetch_breweries(url: str):
    response = requests.get(url)
    if response.status_code == 200:
        breweries_data = response.json()[:20]
        breweries = []
        for brewery_data in breweries_data:
            brewery = Brewery(
                id=brewery_data.get('id'),
                name=brewery_data.get('name'),
                brewery_type=brewery_data.get('brewery_type'),
                address_1=brewery_data.get('address_1'),
                address_2=brewery_data.get('address_2'),
                address_3=brewery_data.get('address_3'),
                city=brewery_data.get('city'),
                state_province=brewery_data.get('state_province'),
                postal_code=brewery_data.get('postal_code'),
                country=brewery_data.get('country'),
                longitude=float(brewery_data['longitude']) if brewery_data.get('longitude') else None,
                latitude=float(brewery_data['latitude']) if brewery_data.get('latitude') else None,
                phone=brewery_data.get('phone'),
                website_url=brewery_data.get('website_url'),
                state=brewery_data.get('state'),
                street=brewery_data.get('street')
            )
            breweries.append(brewery)
    return breweries

if __name__ == '__main__':
    url = 'https://api.openbrewerydb.org/v1/breweries'
    breweries = fetch_breweries(url)

    for brewery in breweries:
        print(brewery, '\n')