# y=int(input('Enter '))
# if y<1918:
#     if y%4==0:
#         pass

# import re
year=2020
# def change_date_format(dt):
#         return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3.\\2.\\1', dt)
# dt1 = f"{y}-09-12"
# dt2 = f"{y}-09-13"
# print(change_date_format(dt1))
# y=int(input('Enter '))
# if y<1918:
#     if y%4==0:
#         print(change_date_format(dt1))
#     else:
#         print(change_date_format(dt2))

dt1=f"12.09.{year}"
dt2=f"13.09.{year}"
if year==1918:
    print(f"26.09.{year}")
if year<1918:
    if year%4==0:
        print(dt1)
    else:
        print(dt2)
else:
    if year%400==0  or (year%4==0 and year%100 !=0):
        print(dt1)
    else:
        print(dt2)
