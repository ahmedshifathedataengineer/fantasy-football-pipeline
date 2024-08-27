import requests # type: ignore
from bs4 import BeautifulSoup # type: ignore

def fetch_nfl_data():
    url = "https://www.nfl.com/players/tua-tagovailoa/stats/"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to fetch data: HTTP Status {response.status_code}")
        return None
    
    # Parse HTML content
    soup = BeautifulSoup(response.content, 'lxml')
    
    # Extract relevant data - Example: Extracting player stats
    stats_table = soup.find('table')  # Find the stats table, this will need to be customized
    if stats_table:
        # Extract data from table rows and cells
        data = []
        for row in stats_table.find_all('tr'):
            cols = row.find_all('td')
            data.append([col.text for col in cols])
        return data
    else:
        print("Failed to find the stats table.")
        return None
