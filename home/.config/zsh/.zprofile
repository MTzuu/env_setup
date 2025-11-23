export GDK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS=@im=fcitx

[ "$(tty)" = "/dev/tty1" ] && exec sway --unsupported-gpu
