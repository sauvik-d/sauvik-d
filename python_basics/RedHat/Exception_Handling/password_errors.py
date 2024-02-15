class PasswordError(Exception):
    """Base class for exceptions in this module"""
    pass


class TrivialPasswordError(PasswordError):
    """Passwords that are too Trivial like: 'password'"""
    def __int__(self, msg):
        super().__init__("Trivial Password:" + msg)


class PasswordLengthError(PasswordError):
    """Passwords that do not meet certain length criteria"""
    def __int__(self, msg, length):
        super.__init__(msg)
        self.length = length

    def get_length(self):
        return self.length


class RepetitiveError(PasswordError):
    """Passwords that have repetitive characters"""
    def __int__(self, msg):
        super().__init__(msg)
