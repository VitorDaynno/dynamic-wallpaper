import os
import random

from src.config.config import Config


def get_list_wallpapers():
   path = config.get_wallpapers_path()

   wallpapers = os.listdir(path)

   return wallpapers

def draw_wallpaper(wallpapers):
    quantity = len(wallpapers)

    draw_number = random.randint(0, quantity-1);

    return wallpapers[draw_number]

def set_wallpaper(wallpaper):
    command = config.get_wallpaper_set_command()
    path = config.get_wallpapers_path()

    print("Setting {0} as wallpaper".format(wallpaper))

    dbus_session_bus_address = 'PID=$(pgrep gnome-session | tail -n1) && export DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$PID/environ|cut -d= -f2-) && '

    os.system("{0}{1} {2}/'{3}'".format(dbus_session_bus_address, command, path, wallpaper))


def run():
    wallpapers = get_list_wallpapers()

    wallpaper = draw_wallpaper(wallpapers)
    set_wallpaper(wallpaper)


config = Config()
run()