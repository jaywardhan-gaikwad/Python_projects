# ------------------------------------------
# ALARM CLOCK
# ------------------------------------------
# This program can either:
# 1. Set an alarm for a specific time (HH:MM:SS format)
# 2. Set a countdown timer (e.g., ring after 60 seconds)
# It uses a progress bar to show waiting progress and plays
# a beep sound when the time is up.
# ------------------------------------------

import time
from datetime import datetime, timedelta
from rich.progress import Progress
import winsound  # For alarm beep sound (works on Windows)


# Function to play beep sound 5 times
def beep():
    for i in range(5):
        winsound.Beep(1500, 800)  # (frequency, duration)
        time.sleep(1)


# Function for alarm at a specific time (HH:MM:SS)
def alarm_timebased():
    alarm_time = input("Enter alarm time (HH:MM:SS, 24-hour format): ")
    print(f"Alarm set for {alarm_time} ⏰")

    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("\nTime's up! Alarm ringing 🔔")
            beep()
            break
        time.sleep(1)


# Function for countdown-based alarm (in seconds)
def countdown_based():
    delay = int(input("Enter delay in seconds (e.g., 60 for 1 minute): "))
    alarm_time = datetime.now() + timedelta(seconds=delay)
    print(f"Alarm will ring at {alarm_time.strftime('%H:%M:%S')} ⏰")

    with Progress() as progress:
        task = progress.add_task("Waiting for alarm...", total=delay)
        for i in range(delay):
            time.sleep(1)
            progress.update(task, advance=1)

    print("\nTime's up! Alarm ringing 🔔")
    beep()


# Main function to choose between time-based or countdown alarm
def alarm_clock():
    print("\n--- ALARM CLOCK ---")
    print("1. Set alarm at specific time (HH:MM:SS)")
    print("2. Set alarm after certain seconds")

    choice = int(input("Enter choice (1/2): "))

    if choice == 1:
        alarm_timebased()
    elif choice == 2:
        countdown_based()
    else:
        print("Invalid choice! ❌")


# Entry point of program
if __name__ == "__main__":
    alarm_clock()
