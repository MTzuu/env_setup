# Date and time
date_and_week=$(date "+%d.%m.%Y")
current_time=$(date "+%H:%M")

# Battery or charger
battery_charge=$(upower --show-info $(upower --enumerate | grep 'BAT') | grep -E "percentage" | awk '{print $2}')
battery_status=$(upower --show-info $(upower --enumerate | grep 'BAT') | grep -E "state" | awk '{print $2}')

if [ $battery_status = "discharging" ];
then
  battery_pluggedin='🔋'
else
  battery_pluggedin='⚡'
fi

# Audio and multimedia
volume0=$(wpctl get-volume @DEFAULT_AUDIO_SINK@ | cut -f2 -d ' ' | cut -f1 -d '.')
volume=$(wpctl get-volume @DEFAULT_AUDIO_SINK@ | cut -f2 -d ' ' | cut -f2 -d '.')
volume="$(($volume0*100+$volume))"
mute=$(wpctl get-volume @DEFAULT_AUDIO_SINK@ | cut -f3 -d ' ')

if [[ $volume -ge 50 ]]; then
  volume_status='🔊'
elif [[ $volume -ge 10 ]]; then
  volume_status='🔉'
elif [[ $volume -ge 5 ]]; then
  volume_status='🔉'
else
  volume_status='🔇'
fi

if [ $mute ]; then
  volume_status='🔇'
fi

# Network
network=$(ip route get 1.1.1.1 | grep -Po '(?<=dev\s)\w+' | cut -f1 -d ' ')
ssid=$(iwctl station wlan0 show | grep 'Connected network' | tr -s ' ' | cut -d ' ' -f 4)
signal_strength=$(iwctl station wlan0 show | grep AverageRSSI | tr -s ' ' | cut -f3 -d ' ')
ip=$(ip ad | grep inet | grep wlan0 | tr -s ' ' | cut -f3 -d ' ')
ping=$(ping -c 1 www.google.ch | tail -1| awk '{print $4}' | cut -d '/' -f 2 | cut -d '.' -f 1)

if ! [ $network ]
then
  network="🚫 disconnected"
else
  network="📶 $ip @ $ssid ($ping ms, $signal_strength dB)"
fi

echo "$network | $battery_pluggedin $battery_charge | $volume_status $volume % | $date_and_week $current_time"
