from ics import Calendar
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
from twilio.rest import Client
from datetime import datetime
import time
import pytz

# Load environment variables from the .env file
load_dotenv()

secret_url = os.environ.get("ICAL_SECRET")


def getBdays():
    response = requests.get(secret_url)

    if response.status_code == 200:
        ical_data = response.text
    else:
        print("Failed to fetch iCal data")
        exit()

    calendar = Calendar(ical_data)

    # Get today's date
    today = datetime.now().strftime("%m-%d")

    # Calculate the date 7 days from today
    seven_days_from_today = (
        datetime.now() + timedelta(days=7)).strftime("%m-%d")

    # Initialize arrays to store events
    events_today = []
    events_in_seven_days = []

    # Iterate through the events in the calendar
    for event in calendar.events:
        event_start = event.begin.date()
        formatted_eventstart = event_start.strftime("%m-%d")
        # Check if the event is today
        if today == formatted_eventstart:
            events_today.append(event.name)

        # Check if the event falls within the next 7 days
        elif seven_days_from_today == formatted_eventstart:
            events_in_seven_days.append(event.name)

    return events_today, events_in_seven_days


def sendTexts(today, seven_days):

    # Your Account SID from twilio.com/console
    account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
    # Your Auth Token from twilio.com/console
    auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

    client = Client(account_sid, auth_token)

    if len(today) > 0:
        for event in today:
            message = client.messages.create(
                to=os.environ.get("TWILIO_TO_NUMBER"),
                from_=os.environ.get("TWILIO_FROM_NUMBER"),
                body=f"{event}'s birthday is today! wish them a happy Birthday!")

    if len(seven_days) > 0:
        for event in seven_days:
            message = client.messages.create(
                to=os.environ.get("TWILIO_TO_NUMBER"),
                from_=os.environ.get("TWILIO_FROM_NUMBER"),
                body=f"{event}'s birthday is in 7 days! Make sure to send them a card!")


def calculate_seconds_until_next_nine_am():
    # Get the current time in GMT timezone
    gmt = pytz.timezone('GMT')
    now = datetime.now(gmt)

    # Set the target time to 9:00 AM in GMT
    target_time = now.replace(hour=9, minute=0, second=0, microsecond=0)

    if now >= target_time:
        # If it's already past 9:00 AM GMT today, calculate for tomorrow
        target_time += timedelta(days=1)

    # Calculate the time difference in seconds
    time_until_next_nine_am = (target_time - now).total_seconds()
    return time_until_next_nine_am


def checkBdaysAndSendTexts():
    today, seven_days = getBdays()
    sendTexts(today, seven_days)


if __name__ == "__main__":
    # Run the task once on startup
    print("Checking birthdays and sending texts on startup...")
    checkBdaysAndSendTexts()

    while True:
        sleep_duration = calculate_seconds_until_next_nine_am()
        print(f"Waiting for {sleep_duration} seconds until 9:00 AM GMT...")
        time.sleep(sleep_duration)

        # Now it's 9:00 AM GMT, you can perform your tasks
        print("It's 9:00 AM GMT. Checking birthdays and sending texts...")
        checkBdaysAndSendTexts()
