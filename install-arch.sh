checkroot() {

if [[ "$(id -u)" -ne 0 ]]; then
   printf "\e[1;77mPlease, run this program as root!\n\e[0m"
   exit 1
fi

}

checkroot
pacman -Sy
pacman -S python -y
pacman -S python3 -y
pacman -S python3-pip -y
pacman -S ffmpeg -y
pacman -S lame -y
pip install --upgrade pip
python3 -m pip install -r requirments.txt
echo "Installed!"
