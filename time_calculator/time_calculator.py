def add_time(start_time, duration, start_day=None):
    # Parsing the start_time to extract the hour, minute and am/pm information
    start_hour, start_minute = map(int, start_time[:-3].split(':'))
    am_pm = start_time[-2:]

    # Parsing the duration to extract the hour and minute information
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Converting start_time to 24-hour clock format
    if am_pm == 'PM' and start_hour != 12:
        start_hour += 12

    # Adding the duration to start_time
    end_minute = (start_minute + duration_minute) % 60
    extra_hour = (start_minute + duration_minute) // 60

    end_hour = (start_hour + duration_hour + extra_hour) % 24
    days_later = (start_hour + duration_hour + extra_hour) // 24

    # Converting the result back to 12-hour clock format
    if end_hour == 0:
        end_hour = 12
        am_pm = 'AM'
    elif end_hour < 12:
        am_pm = 'AM'
    elif end_hour == 12:
        am_pm = 'PM'
    else:
        end_hour -= 12
        am_pm = 'PM'

    # Formatting the result string
    result = f'{end_hour:02d}:{end_minute:02d} {am_pm}'

    if start_day:
        # Converting the start_day to its corresponding index (0 for Sunday, 1 for Monday, etc.)
        start_day_index = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'].index(
            start_day.lower())

        # Adding the number of days later to the start_day_index
        end_day_index = (start_day_index + days_later) % 7

        # Adding the day of the week to the result string
        result += f", {['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'][end_day_index]}"

        # Adding the days_later string to the result string, if applicable
        if days_later == 1:
            result += ' (next day)'
        elif days_later > 1:
            result += f' ({days_later} days later)'

    return result
