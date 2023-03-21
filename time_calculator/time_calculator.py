def add_time(start_time, duration, start_day=None):
    start_hour, start_minute = map(int, start_time[:-3].split(':'))
    am_pm = start_time[-2:]

    duration_hour, duration_minute = map(int, duration.split(':'))

    if am_pm == 'PM' and start_hour != 12:
        start_hour += 12

    end_minute = (start_minute + duration_minute) % 60
    extra_hour = (start_minute + duration_minute) // 60

    end_hour = (start_hour + duration_hour + extra_hour) % 24
    days_later = (start_hour + duration_hour + extra_hour) // 24

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

    result = f'{end_hour:02d}:{end_minute:02d} {am_pm}'

    if start_day:
        start_day_index = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'].index(
            start_day.lower())

        end_day_index = (start_day_index + days_later) % 7

        result += f", {['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'][end_day_index]}"

        if days_later == 1:
            result += ' (next day)'
        elif days_later > 1:
            result += f' ({days_later} days later)'

    return result
