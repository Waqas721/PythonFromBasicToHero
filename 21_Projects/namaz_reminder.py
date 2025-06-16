import time
from plyer import notification
from datetime import datetime

# Namaz timings (24-hour format)
namaz_times = {
    "Fajr Start": "04:12",
    "Fajr End": "05:41",
    "Ishraq": "05:53",
    "Chasht": "08:45",
    "Zuhr": "12:36",
    "Asr (Shafi)": "15:54",
    "Asr (Hanafi)": "17:15",
    "Maghrib": "19:22",
    "Isha": "22:51"
}

# Keep track of notifications to avoid repeating
notified_today = set()

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M")

    for namaz, namaz_time in namaz_times.items():
        if current_time == namaz_time and namaz not in notified_today:
            notification.notify(
                title="Namaz Reminder",
                message=f"It's time for {namaz} prayer.",
                timeout=10
            )
            print(f"Reminder: {namaz} at {current_time}")
            notified_today.add(namaz)

    # Reset notifications at midnight
    if current_time == "00:00":
        notified_today.clear()

    time.sleep(60)
