class ProjectException(Exception):

    def __init__(self, msg):
        super(ProjectException, self).__init__(msg)


class LevelError(ProjectException):

    def __init__(self, msg):
        super(LevelError, self).__init__(msg)


class AccessError(ProjectException):

    def __init__(self, msg):
        super(AccessError, self).__init__(msg)