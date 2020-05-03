class Config(object):
    DEBUG = False
    TESTING = False

    DB = "mysql"
    DB_NAME = "production-db"
    DB_USERNAME = "prod"
    DB_PASSWORD = "password"

    SESSION_COOKIE_SECURE = True
    SECRET_KEY = 'D57E36D19979731FA79622DB4D57B'    


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    DB = "mysql"
    DB_NAME = "development-db"
    DB_USERNAME = "dev"
    DB_PASSWORD = "password"

    SESSION_COOKIE_SECURE = False


class TestingConfig(Config):
    TESTING = True

    DB = "mysql"
    DB_NAME = "testing-db"
    DB_USERNAME = "test"
    DB_PASSWORD = "password"

    SESSION_COOKIE_SECURE = False
