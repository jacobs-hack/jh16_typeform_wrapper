class TypeFormError(BaseException):
    def __init__(self, error):
        self.__init__("The Typeform API returned the following error: {}"
                      .format(error))

    def __new__(cls, *args):
        pass


class ClientError(BaseException):
    def __init__(self, response=None):
        pass

    def __new__(cls, *args):
        pass


class ServerError(BaseException):
    def __init__(self):
        pass

    def __new__(cls, *args):
        pass


class BadRequest(BaseException):
    def __init__(self, response=None):
        pass

    def __new__(cls, *args):
        pass


class UnauthorizedAccess(BaseException):
    def __init__(self):
        pass

    def __new__(cls, *args):
        pass


class NotFound(BaseException):
    def __init__(self):
        pass

    def __new__(cls, *args):
        pass


class Unavailable(BaseException):
    def __init__(self):
        pass

    def __new__(cls, *args):
        pass
