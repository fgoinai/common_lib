'''
Arthor:		FGO
Usage:		Compare day difference that have exceeded limit or not
Param:
date_str: date string in "yyyy?mm?dd", ? is the seperator
separator: refer date_str
diff_flag: the days limit

Return:		if abs(today - target date) >= days limit
Example:
overdue = days_diff_flag('2010-3-1', '-', 1000)
'''
def days_diff_flag(date_str, separator, diff_flag):
    from datetime import date
    date_list = date_str.split(separator)
    if abs((date.today() - date(
            year=int(date_list[0]),
            month=int(date_list[1]),
            day=int(date_list[2])
    )).days) >= diff_flag:
        return True
    else:
        return False

'''
Arthor:		FGO
Usage:		Get the millisecond of the beginning of specfic day (00:00)
Param:
day_shift_from_today: today - specfic day

Return:		specfic day 00:00 in ms
Example:
day_flag = get_milli_bound_of_day(50)
'''
def get_milli_bound_of_day(day_shift_from_today):
    from datetime import datetime, timedelta
    today = ''.join((str(datetime.today().year), str(datetime.today().month), str(datetime.today().day)))
    return int((datetime.strptime(today, '%Y%m%d').date() - timedelta(day_shift_from_today)).strftime('%s')) * 1000, \
           int((datetime.strptime(today, '%Y%m%d').date() - timedelta(day_shift_from_today - 1)).strftime('%s')) * 1000
