import requests # type: ignore
from bs4 import BeautifulSoup # type: ignore

def fetch_espn_data():
    url = "https://www.espn.com/nfl/player/stats/_/id/4241479/tua-tagovailoa"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to fetch data: HTTP Status {response.status_code}")
        return None
    
    # Parse HTML content
    soup = BeautifulSoup(response.content, 'lxml')
    
    # Extract relevant data
    stats_table = soup.find('table')  # Example, replace with correct HTML element
    if stats_table:
        data = []
        for row in stats_table.find_all('tr'):
            cols = row.find_all('td')
            data.append([col.text for col in cols])
        return data
    else:
        print("Failed to find the stats table.")
        return None
