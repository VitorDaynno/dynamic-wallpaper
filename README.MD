# Dynamic wallpaper

A script to dynamically change the wallpaper in the Pop Os distro using cron.

## Install

*   Copy the content of .env-example to a .env file.
*   Set the variable WALLPAPERS_PATH with the path where the wallpapers are located.
*   Set the variable WALLPAPER_SET_COMMAND with the referent command to your theme.
    *   Light
        ```bash
            gsettings set org.gnome.desktop.background picture-uri
        ```
    *   Dark
        ```bash
            gsettings set org.gnome.desktop.background picture-uri-dark

        ```

## Crontab's config

*   Edit your crontab file.
    ```bash
        crontab -u YOUR_USER -e
    ```
*   Add the schedule expression line at the file (In this example, the wallpaper will be changed at every 30th minute).
    ```
        */30 * * * * python3 PATH_OF_FOLDER/dynamic-wallpaper/main.py
    ```
    If you want to redirect the logs, you can use the next line.
    ```
        */30 * * * * python3 PATH_OF_FOLDER/dynamic-wallpaper/main.py >> $HOME/dynamicWallpaper.log
    ```
* You can use the [crontab guru](https://crontab.guru/#*/30_*_*_*_*) to validate other schedule expressions.