from datetime import datetime
from collections import Counter

def find_peak_usage(logs):

    hour = [datetime.fromisoformat(ts).hour for ts in logs]

    hour_counts = Counter(hour)

    peak_hour = min ([h for h in hour_counts if hour_counts[h] == max(hour_counts.values())])
    return peak_hour


logs = [
    "2026-08-04T13:21:18", # early morning login
    "2026-08-04T13:45:10",
    "2026-08-04T09:15:20", # afternoon login
    "2026-08-04T13:50:05",
    "2026-08-04T09:30:12", # evening login
    "2026-08-04T18:10:30",
]

print(f"\nPeak login hour: {find_peak_usage(logs)}")