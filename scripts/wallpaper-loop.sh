#!/bin/bash
wallpapers_dir="$HOME/Pictures/Wallpapers"
interval=300

while true; do
    img=$(find "$wallpapers_dir" -type f \( -iname '*.jpg' -o -iname '*.png' \) | shuf -n 1)
    [[ -e "$img" ]] && hyprctl hyprpaper wallpaper "eDP-1,$img"
    sleep $interval
done
