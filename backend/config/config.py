class Config(object):
    DEBUG = False
    TESTING = False

    SESSION_COOKIE_SECURE = True
    SECRET_KEY = 'D57E36D19979731FA79622DB4D57B'    


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    SESSION_COOKIE_SECURE = False


class TestingConfig(Config):
    TESTING = True

    SESSION_COOKIE_SECURE = False
