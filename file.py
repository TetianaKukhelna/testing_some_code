import datetime

# start_time_by_user_contex: dict = []
l = [1]
# start_time_by_user_contex = dict.fromkeys(l)
start_time_by_user_contex = {}
k = 5
# start_time = datetime.datetime.now()
# start_time_with_format = int(start_time.strftime("%Y%m%d%H%M%S"))
# print(start_time_by_user_contex)
# start_time_by_user_contex[1] = start_time_with_format
# print(start_time_by_user_contex)
# y = 9
# f = [3]
# start_time_by_user_contex = dict.fromkeys(f, y)
# print(start_time_by_user_contex)
#
for i in range(1):
    start_time = datetime.datetime.now()
    start_time_with_format = start_time
    print(start_time_with_format)
    new_time = datetime.datetime.now()-start_time_with_format

#testing