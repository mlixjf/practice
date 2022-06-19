class MyError(ZeroDivisionError):
    pass


# try:
#     print(1 / 0)
# except MyError as e:
#     print(e.args)


class CustomError(Exception):

    def __init__(self, message, status):
        self.message = message
        self.status = status
        super().__init__(message, status)


try:
    raise CustomError("测试自定义异常", 1)
except CustomError as e:
    print(e.args)
