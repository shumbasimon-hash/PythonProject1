from datetime import datetime

def find_peak_usage(logs):
    # Create a list to store login counts for hours 0–23
    hour_counts = [0] * 24

    # Process each timestamp
    for log in logs:
        time = datetime.fromisoformat(log)
        hour_counts[time.hour] += 1

    # Find the hour with the highest number of logins
    peak_hour = hour_counts.index(max(hour_counts))

    return peak_hour


# Example
logs = [
    "2026-08-04T13:21:18",
    "2026-08-04T13:45:10",
    "2026-08-04T14:05:22",
    "2026-08-04T13:50:30",
    "2026-08-04T14:20:15",
    "2026-08-04T09:10:05"
]

print("Peak usage hour:", find_peak_usage(logs))