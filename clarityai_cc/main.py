import argparse
import datetime
from clarityai_cc.log_parser import parse_log, parse_live_log

def parse_arguments():
    parser = argparse.ArgumentParser(description='Parse log file to find connections to a specific host within a given time range.')
    parser.add_argument('file_path', type=str, help='Path to the log file.')
    parser.add_argument('init_datetime', type=str, help='Start datetime in the format YYYY-MM-DD HH:MM:SS.')
    parser.add_argument('end_datetime', type=str, help='End datetime in the format YYYY-MM-DD HH:MM:SS.')
    parser.add_argument('hostname', type=str, help='Hostname to search connections for.')
    return parser.parse_args()

def process_args(init_datetime, end_datetime):
    try:
        start_dt = datetime.datetime.strptime(init_datetime, '%Y-%m-%d %H:%M:%S')
        end_dt = datetime.datetime.strptime(end_datetime, '%Y-%m-%d %H:%M:%S')
        start_ts = int(start_dt.timestamp() * 1000)
        end_ts = int(end_dt.timestamp() * 1000)
    except ValueError:
        raise ValueError("Invalid datetime format. Please use the format YYYY-MM-DD HH:MM:SS.")
    return start_ts, end_ts

def main():
    args = parse_arguments()
    start_ts, end_ts = process_args(args.init_datetime, args.end_datetime)
    connections = parse_log(args.file_path, start_ts, end_ts, args.hostname)
    unique_connections = set(connections)
    # Considering the list is meant to be printed in console. It could be also written to an output file.
    print(f"Hosts connected to {args.hostname} from {args.init_datetime} to {args.end_datetime}:")
    for host in unique_connections:
        print(host)

def main_streaming():
    # Streaming version of the main function
    args = parse_arguments()
    parse_live_log(args.file_path, args.hostname)

if __name__ == "__main__":
    main()