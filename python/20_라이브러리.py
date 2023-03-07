# 시간과 날짜
import datetime

# date() : 날짜정보
# time() : 시간정보
# now() : 시스템의 현재날짜, 시간정보
# weekday() : 요일

# dt = datetime.date(2022, 5, 20)
# print(dt)
# print(dt.year, dt.month, dt.day)
# dt = datetime.time(11, 10, 15, 30)
# print(dt)
# print(dt.hour, dt.minute, dt.second, dt.microsecond)
# dt = datetime.datetime(1999, 1, 1, 10, 13, 10)
# print(dt)
#
# dt = datetime.datetime.now()
# print(dt)
#
# print(dt.strftime("%Y/%m/%d %p %A"))
#
# # 달력
# import calendar
#
# print(calendar.calendar(2022)) #한해 전체 출력
#
# print(calendar.prmonth(2022, 5)) #원하는 달만 출력
#
# print(calendar.weekday(2022, 12, 31))
# 0 월, 1 화, 2 수, 3 목, 4 금, 5 토, 6 일

# webbrowser
import webbrowser
webbrowser.open("google.com")
webbrowser.open_new("naver.com")

