import sys
import os

# Add the project root directory to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from data_sources.espn import fetch_espn_data
from data_sources.yahoo import fetch_yahoo_data
from data_sources.nfl import fetch_nfl_data
from utils.data_processing import process_player_data
from utils.database import connect_db, create_table, insert_data



def main():
    # Fetch data from multiple sources
    espn_data = fetch_espn_data()
    if espn_data is None:
        print("Skipping ESPN data due to fetch error.")
        espn_data = []

    yahoo_data = fetch_yahoo_data()
    if yahoo_data is None:
        print("Skipping Yahoo data due to fetch error.")
        yahoo_data = []

    nfl_data = fetch_nfl_data()
    if nfl_data is None:
        print("Skipping NFL data due to fetch error.")
        nfl_data = []

    # Print data to debug
    print("Yahoo Data:", yahoo_data)
    print("ESPN Data:", espn_data)
    print("NFL Data:", nfl_data)

    # Process and combine the data
    espn_processed = process_player_data(espn_data)
    yahoo_processed = process_player_data(yahoo_data)
    nfl_processed = process_player_data(nfl_data)
    
    combined_data = espn_processed + yahoo_processed + nfl_processed
    
    # Store the data in the database
    conn = connect_db()
    create_table(conn)
    insert_data(conn, combined_data)
    conn.close()

if __name__ == "__main__":
    main()
