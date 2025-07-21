result="$(ps -e | grep waybar)";
length=${#result}
if [ $length -gt 0 ]; then
	echo "kill waybar"
	killall waybar
else
	echo "run waybar"
	waybar &
fi
echo "$length"
