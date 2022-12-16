# import time
#
# class Testing():
#
#     def __int__(self, timeout_time = None):
#         self._timeout_time = timeout_time
#
#     def _recalculate_timeout(self):
#         # self._last_found = time.time()
#         # print("time: ",time.time())
#         print(self)
#
#
#     def print_time(self,timeout = 1000):
#         self._recalculate_timeout(600)
#         # self._f = self
#         print("timeout: ",timeout)
#         # print("self.f : ",self._f)
# import argparse
# import os
#
#
# def testing(file_path_list: list[str]):
#     # pass
#     for file in file_path_list:
#         print(file)
#
# def main(files: list[str]):
#     testing(files)
#
# def PathType(path):
#     try:
#         if os.path.exists(path) and os.path.isfile(path):
#             with open(path, "r") as f:
#                 list = f.readlines()
#                 return list
#     except Exception as err:
#         print(err)
#     # else:
#     #     raise argparse.ArgumentTypeError(f"readable_dir:{path} is not a valid path")
#
#
# if __name__ == "__main__":
#
#     parser = argparse.ArgumentParser(
#         description='Run script with parameters',
#     )
#
#     parser.add_argument("--path_to_files", type=PathType, default="", required=True)
#     args = parser.parse_args()
#     list_files = args.path_to_files
#
#     main(list_files)
import os
import time


def old_files(ddir, daysnumber):
    days_treshold_in_sec = time.time() - (int(daysnumber) * 24 * 60 * 60)
    if os.path.isdir(ddir):
        for fname in os.listdir(ddir):
            print("fname ",fname )
            fpath = os.path.join(ddir, fname)
            print("fpath ", fpath)
            if os.path.isdir(fpath):
                old_files(fpath, daysnumber)
            else:
                if os.path.exists(fpath) and os.stat(fpath).st_mtime < days_treshold_in_sec:
                    try:
                        os.unlink(fpath)
                    except:
                        # logging.warning("{}: cannot delete file '{}'".format(self.avname, fpath))
                        print("fuck")
                        pass
        # something was proceeded
        return 1
    else:
        return None


def main(ddir, daynumber):
    old_files(ddir,daynumber)


if __name__ == "__main__":
    daysnumber = 5
    ddir = 'C:\\Users\\tetiana.kukhelna.HQ\\PycharmProjects\\testovaci_folder'
    main(ddir,daysnumber)