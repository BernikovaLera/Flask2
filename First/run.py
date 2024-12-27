from my_app import app
from config import DevelopmentConfig


if __name__ == " _main_":
    app.run(port=DevelopmentConfig.PORT)



