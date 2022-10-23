import os
import sys
from dotenv import load_dotenv


class Config:

    def __init__(self):
        print("Starting Config")
        load_dotenv()

    def get_wallpapers_path(self):
        print("Getting wallpapers' path from enviroment")
        wallpapers_path = self.get_variable_by_environment("WALLPAPERS_PATH")
        print("Get wallpapers' path with success")
        return wallpapers_path

    def get_wallpaper_set_command(self):
        print("Getting wallpaper set command from enviroment")
        command = self.get_variable_by_environment("WALLPAPER_SET_COMMAND")
        print("Get wallpaper set command  with success")
        return command

    @staticmethod
    def get_variable_by_environment(variable_name):
        variable_value = os.getenv(variable_name)
        if variable_value is None:
            print("{0} not found".format(variable_name))
            sys.exit()
        return variable_value