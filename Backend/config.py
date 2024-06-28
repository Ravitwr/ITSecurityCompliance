import settings


class SystemConfig:
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://{user}:{password}@{host}/{db}?charset=utf8mb4".format(
            **{
                "user": settings.MYSQL_USER,
                "password": settings.MYSQL_PASSWORD,
                "host": settings.MYSQL_HOST,
                "db": settings.MYSQL_DATABASE,
            }
        )
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_ENGINE_OPTIONS = {}
    JSON_AS_ASCII = False

    RESTX_VALIDATE = True
    ERROR_INCLUDE_MESSAGE = False


config = SystemConfig()
