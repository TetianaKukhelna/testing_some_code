import sys
import logging
from logging import StreamHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.setLevel(logging.DEBUG)
# handler = StreamHandler(stream=sys.stdout)
logger.addHandler(logging.FileHandler('test.log'))
# logger.addHandler(handler)
tmp = 155678
str = "stringaspt"
key ="user_*"
arr = [1,2,3,"rrr","sss"]
# str2 = str(tmp)
# print(str2)
tmp += 1
# print(tmp)

user = key.split("_")[0]
# print(user)

# logger.debug('debug information')
# logger.info('some info'+' ddd')
logger.info("{}".format(tmp) + str)
logger.info("cancelled")
logger.info(arr)
# logger.info("nn "+"{}".format(tmp) + " _stastus\n" + " dsdds "+"{}".format(tmp) + "as")
# logger.info("dsdds "+"{}".format(tmp) + "as")
# logger.debug("debug")

# active_jod = {'w':["dddffs"]}

# logger.info('after checking the time by 300 seconds')
# if "aspt" in str:
    # print(job)
    # logger.info('after checking the time by 300 seconds')
    # print("daaaaa")
    # logger.info(job)
    # print("\n")


class Geeks:
    def __init__(self):
        self._age = 12
        self._ggg = 768

    # using property decorator
    # a getter function
    @property
    def agge(self):
        print("getter method called")
        return self._age

    @property
    def trt(self):
        print("rrrr method called")
        return self._age

    # a setter function
    # @age.setter
    # def age(self, a):
    #     if (a < 18):
    #         raise ValueError("Sorry you age is below eligibility criteria")
    #     print("setter method called")
    #     self._age = a


mark = Geeks()

# mark.agge = 194

# print(mark.agge)
# print(mark.trt)


# dict = {"name":"release","scan":"fully","sever":"ba-*"}
#
# for i in dict:
#     if i == 'scan':
#         print(dict[i])
res = 5
for i in range(5):
    print("i , ", i)










import testing
# def print_hi(self,timeout = 1000):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi,')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
    # testing.Testing.print_time(600)

