# Date and time
date_and_week=$(date "+%d.%m.%Y")
current_time=$(date "+%H:%M")

# Audio and multimedia
volume0=$(wpctl get-volume @DEFAULT_AUDIO_SINK@ 2> /dev/null | cut -f2 -d ' ' | cut -f1 -d '.')
volume=$(wpctl get-volume @DEFAULT_AUDIO_SINK@ 2> /dev/null | cut -f2 -d ' ' | cut -f2 -d '.' 2> /dev/null)
volume="$(($volume0*100+$volume))"
mute=$(wpctl get-volume @DEFAULT_AUDIO_SINK@ 2> /dev/null | cut -f3 -d ' ')

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
ip=$(ip ad | grep inet | grep enp39s0 | tr -s ' ' | cut -f3 -d ' ')
ping=$(ping -c 1 www.google.ch | tail -1| awk '{print $4}' | cut -d '/' -f 2 | cut -d '.' -f 1)

if ! [ $network ]
then
  network="🚫 disconnected"
else
  network="🖧  $ip ($ping ms)"
fi

echo "$network | $volume_status $volume % | $date_and_week $current_time"
