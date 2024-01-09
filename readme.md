# BDAYREMINDERPY

This is a simple birthday reminder application written in Python.

## Features

- sends sms reminders for birthdays every day at 9.00 GMT
- sends an SMS for any bdays events in the cal that are today and 7 days in the future

## Prerequisites

- Python 3.6 or higher
- A [Twilio](https://console.twilio.com/) account with a purchased phone number that can send SMS messages
- A [Google Calendar](https://calendar.google.com/) account with a calendar or similar that contains birthdays as the event title
- SMS's are sent in the format

```bash
{event}'s birthday is today! wish them a happy Birthday!"
```

```bash
{event}'s birthday is in 7 days! Make sure to send them a card!"
```

Ensure your event titles are the name of the person you want to wish a happy birthday to or the message will not read correctly.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/username/bdayreminderpy.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory of the project like the `.env.example` and add the following environment variables:

   ```bash
   ICAL_SECRET= your ical secret url
   TWILIO_AUTH_TOKEN= your twilio auth token
   TWILIO_FROM_NUMBER= your twillio number you purchased
   TWILIO_TO_NUMBER= your phone number to sms to
   ```

## Usage

1. Run the application:

   ```bash
   python bdayreminder.py
   ```

2. Follow the on-screen instructions to manage birthdays and set up email reminders.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
