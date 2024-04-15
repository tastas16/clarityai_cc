import time
from datetime import datetime, timedelta

def parse_log(file_path, start_ts, end_ts, hostname):
    connections = []
    with open(file_path, 'r') as file:
        for line in file:
            ts, src_host, dst_host = line.strip().split()
            if start_ts <= int(ts) <= end_ts and (src_host == hostname or dst_host == hostname):
                connections.append(dst_host if src_host == hostname else src_host)
    return connections

def parse_live_log(file_path, target_host, refresh_interval=3600):
    """
    Parses a live log file and tracks connections made and received by a target host within the last hour.

    Args:
        file_path (str): The path to the log file.
        target_host (str): The target host to track connections for.
        refresh_interval (int, optional): The interval in seconds to refresh the log file. Defaults to 3600.

    Returns:
        None
    """
    # The first time the function is called, it will start tracking connections from the last hour
    last_hour_ts = int((datetime.now() - timedelta(hours=1)).timestamp() * 1000)
    connections_made = []
    connections_received = []
    
    while True:
        current_ts = int(datetime.now().timestamp() * 1000)
        with open(file_path, 'r') as file:
            for line in file:
                ts, src_host, dst_host = line.strip().split()
    
                if int(ts) / 1000 >= last_hour_ts:
                    if src_host == target_host:
                        connections_made.append(dst_host)
                    if dst_host == target_host:
                        connections_received.append(src_host)

        if current_ts - last_hour_ts >= 3600 * 1000:
            print(f"Connections made by {target_host} in the last hour: {connections_made}")
            print(f"Connections received by {target_host} in the last hour: {connections_received}")

            most_connections_host = max(connections_made, key=lambda k: len(connections_made[k]))
            print(f"Hostname that generated most connections in the last hour: {most_connections_host}")

            # Reset for the next hour
            connections_made.clear()
            connections_received.clear()
            last_hour_ts = current_ts

        time.sleep(refresh_interval)  # Sleep for a minute before checking the log file again