import json
from datetime import datetime

# Helper function to convert ISO 8601 timestamp to milliseconds
def iso_to_millis(iso_str):
    """
    Convert ISO 8601 timestamp string (e.g. '2023-09-01T12:34:56Z')
    into milliseconds since epoch (Unix time).
    """
    # Replace 'Z' with '+00:00' to make it timezone-aware
    dt = datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
    return int(dt.timestamp() * 1000)


def convert_from_format_1(data):
    """
    Convert from format used in data-1.json to unified format.
    Example keys:
        machine -> device_id
        temp -> temperature
        timestamp (ISO) -> timestamp (ms)
    """
    return {
        "device_id": data["machine"],
        "temperature": data["temp"],
        "timestamp": iso_to_millis(data["timestamp"])
    }


def convert_from_format_2(data):
    """
    Convert from format used in data-2.json to unified format.
    Example keys:
        deviceId -> device_id
        temperature -> temperature
        time (ms) -> timestamp (ms)
    """
    return {
        "device_id": data["deviceId"],
        "temperature": data["temperature"],
        "timestamp": data["time"]
    }


# --- Runner for debugging (optional) ---
if __name__ == "__main__":
    # Load sample files to test manually
    with open("data-1.json") as f1, open("data-2.json") as f2:
        d1 = json.load(f1)
        d2 = json.load(f2)

    print("Converted from format 1:", convert_from_format_1(d1))
    print("Converted from format 2:", convert_from_format_2(d2))
