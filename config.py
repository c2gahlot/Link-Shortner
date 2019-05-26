class ProductionConfig:
    DEBUG = False

class DevelopmentConfig:
    DEBUG = True

app_config = {
    'development' : DevelopmentConfig,
    'production' : ProductionConfig
}