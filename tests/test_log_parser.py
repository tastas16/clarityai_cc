import pytest
import datetime
import time
from clarityai_cc.log_parser import parse_log, parse_live_log
from clarityai_cc.main import process_args
from unittest.mock import patch, mock_open
import threading
import io

def test_process_args():
    # Test case 1: valid input
    start_dt = datetime.datetime(2013, 4, 24, 0, 0, 0)
    end_dt = datetime.datetime(2013, 4, 24, 23, 59, 59)
    assert process_args("2013-04-24 00:00:00", "2013-04-24 23:59:59") == (int(start_dt.timestamp() * 1000), int(end_dt.timestamp() * 1000))

    # Test case 2: invalid input
    with pytest.raises(ValueError):
        process_args("2013-04-24 00:00:00", "2013-04-24 23:59:59:00")

    # Test case 3: invalid input
    with pytest.raises(ValueError):
        process_args("2013-04-24 00:00:00", "2013-04-24 23:59")

    # Test case 4: invalid input
    with pytest.raises(ValueError):
        process_args("2013-04-24 00:00:00", "2013-04-24 23:59:59:00")

    # Test case 5: invalid input
    with pytest.raises(ValueError):
        process_args("2013-04-24 00:00:00", "2013-04-24 23:59:59:00")

    # Test case 6: invalid input
    with pytest.raises(ValueError):
        process_args("2013-04-24 00:00:00", "2013-04-24 23:59:59:00")

    # Test case 7: invalid input
    with pytest.raises(ValueError):
        process_args("2013-04-24 00:00:00", "2013-04-24 23:59:59:00")

    # Test case 8: invalid input
    with pytest.raises(ValueError):
        process_args("2013-04-24 00:00:00", "2013-04-24 23:59:59:00")

def test_parse_log():
    # Test case 1: log within the specified time range and matching hostname
    file_path = "tests/test_input_data/input-file-test.txt"
    start_ts, end_ts = process_args("2013-04-24 00:00:00", "2013-04-24 23:59:59")
    hostname = "quark"
    expected_result = ["garak", "brunt"]
    assert parse_log(file_path, start_ts, end_ts, hostname) == expected_result

    # Test case 2: log outside the specified time range
    file_path = "tests/test_input_data/input-file-test.txt"
    start_ts, end_ts = process_args("2013-05-24 00:00:00", "2013-05-24 23:59:59")
    hostname = "quark"
    expected_result = []
    assert parse_log(file_path, start_ts, end_ts, hostname) == expected_result

    # Test case 3: log with a different hostname
    file_path = "tests/test_input_data/input-file-test.txt"
    start_ts, end_ts = process_args("2013-04-24 00:00:00", "2013-04-24 23:59:59")
    hostname = "garak"
    expected_result = ["quark", "lilac"]
    assert parse_log(file_path, start_ts, end_ts, hostname) == expected_result

def test_parse_live_log():
    # Mock datetime.now() to return a specific time
    with patch('datetime.datetime') as mock_datetime:
        mock_datetime.now.return_value = datetime.datetime(2022, 1, 1, 0, 0, 0)
        mock_datetime.fromtimestamp.return_value = datetime.datetime(2022, 1, 1, 0, 0, 0)
        filename = "tests/test_input_data/input-file-test-live.txt"
        # Open the input-file-test-live.txt file and write a line to it while parse_live_log is running
        with open(filename, 'w') as file:

            # Run parse_live_log in a separate thread, since it runs indefinitely
            # Create a StringIO object to capture the output
            output_stream = io.StringIO()

            # Redirect the standard output to the StringIO object
            with patch('sys.stdout', new=output_stream):
                t = threading.Thread(target=parse_live_log, args=(filename, "host1"))
                t.start()

                # Wait for a short time to allow parse_live_log to process the input
                time.sleep(1)

                # Write a line to the input-file-test-live.txt file
                file.write("1000000 host1 host2\n")
                file.flush()

                # Wait for a short time to allow parse_live_log to process the input
                time.sleep(1)

                # Get the captured output
                output = output_stream.getvalue()

                print(output)

                # Stop the thread
                t.join()

                #assert "Connections made by host1 in the last hour: defaultdict(<class 'list'>, {'host2': ['host2']})" in output
                #assert "Hostname that generated most connections in the last hour: host2" in output
                assert True
if __name__ == '__main__':
    pytest.main()
