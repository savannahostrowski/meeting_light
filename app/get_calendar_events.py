from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def get_events():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 100 events on the user's calendar that 
    are not all day events
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    work_calendar = 'jeiccgk9v71mr3jrs2c6ed758cusdb6f@import.calendar.google.com'
    events_result = service.events().list(calendarId=work_calendar, timeMin=now,
                                        maxResults=100, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    valid_events = []
    for event in events:
        if 'dateTime' in event['start']:
            start = event['start']['dateTime']
            end = event['end']['dateTime']
            valid_events.append((start, end))
    return valid_events

def is_savannah_in_meeting():
    events = get_events()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    next_or_current_event = events[0]

    # Five minutes that we will buffer each event on the calendar with
    five_minutes = datetime.timedelta(minutes=5)

    # Convert datetime strings to datetime objects
    start_minus_five = datetime.datetime.fromisoformat(next_or_current_event[0][:-1]) - five_minutes
    end_plus_five = datetime.datetime.fromisoformat(next_or_current_event[1][:-1]) + five_minutes

    # Buffer the event
    start = start_minus_five.strftime("%Y-%m-%d %H:%M:%S")
    end = end_plus_five.strftime("%Y-%m-%d %H:%M:%S")

    return start < now < end

if __name__ == '__main__':
    is_savannah_in_meeting()