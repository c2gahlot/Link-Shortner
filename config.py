from os import environ


class BaseConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI',
                                          'mysql+pymysql://root:root@localhost/link_shortner')


class ProductionConfig(BaseConfig):
    DEBUG = False
    BASE_URL = 'http://linker.c2gahlot.com/'


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    BASE_URL = 'http://192.168.10.11:82/'


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
