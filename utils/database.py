import sqlite3

def connect_db(db_name="db/fantasy_football.db"):
    conn = sqlite3.connect(db_name)
    return conn

def create_table(conn):
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS player_stats (
        player_id INTEGER PRIMARY KEY,
        name TEXT,
        team TEXT,
        position TEXT,
        points REAL
    );
    """
    conn.execute(create_table_sql)
    conn.commit()

def insert_data(conn, data):
    insert_sql = """
    INSERT INTO player_stats (player_id, name, team, position, points)
    VALUES (?, ?, ?, ?, ?)
    ON CONFLICT(player_id) DO UPDATE SET
    name=excluded.name,
    team=excluded.team,
    position=excluded.position,
    points=excluded.points;
    """
    conn.executemany(insert_sql, [(d["player_id"], d["name"], d["team"], d["position"], d["points"]) for d in data])
    conn.commit()
