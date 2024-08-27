def process_player_data(raw_data):
    # Ensure we're working with a list or return an empty list
    if not isinstance(raw_data, list):
        print("Warning: raw_data is not a list. Returning empty list.")
        return []

    processed_data = []
    for player in raw_data:
        # Ensure each player is a dictionary
        if isinstance(player, dict):
            processed_data.append({
                "player_id": player.get("id", "N/A"),
                "name": player.get("name", "N/A"),
                "team": player.get("team", "N/A"),
                "position": player.get("position", "N/A"),
                "points": player.get("points", 0)
            })
        else:
            print("Warning: Expected a dictionary for player data.")
    
    return processed_data
