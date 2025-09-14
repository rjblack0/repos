DateRange = ('DateRange', ['start_month', 'start_day', 'end_month', 'end_day'])

spring_range = DateRange('March', 20, 'June', 20)
summer_range = DateRange('June', 21, 'September', 21)
autumn_range = DateRange('September', 22, 'December', 20)
winter_range = DateRange('December', 21, 'March', 19)

month_number = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'].index(month) + 1

if (month_number, day) >= (spring_range.start_month, spring_range.start_day) and (month_number, day) <= (
spring_range.end_month, spring_range.end_day):
    print('Spring')
elif (month_number, day) >= (summer_range.start_month, summer_range.start_day) and (month_number, day) <= (
summer_range.end_month, summer_range.end_day):
    print('Summer')
elif (month_number, day) >= (autumn_range.start_month, autumn_range.start_day) and (month_number, day) <= (
autumn_range.end_month, autumn_range.end_day):
    print('Autumn')
else:
    print('Winter')

month = input()
day = int(input())

if month not in (
'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
'December') or not (1 <= day <= 31):
    print('Invalid')

season = get_season(month, day)
print(season)