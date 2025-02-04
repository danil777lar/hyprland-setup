import subprocess
import sys
import os

if __name__ == "__main__":
    result = subprocess.run('hyprctl -j monitors | grep "scale"', shell=True, capture_output=True, text=True)
    screenScale = result.stdout.strip()
    screenScale = screenScale.split(" ")[-1]
    screenScale = screenScale.replace(",", "")
    targetScale = 1 / float(screenScale)
    print(targetScale)
    os.system(f'bash -c -- "QT_QPA_PLATFORM=wayland QT_SCREEN_SCALE_FACTORS="{targetScale}" flameshot gui -r -p ~/Pictures/Screenshots/"')
    sys.exit()