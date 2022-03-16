import gdown
import os

os.system("unzip bott.zip")
os.system("pip install numpy;pip install Pillow;pip install setuptools;pip install six;pip install torchvision;pip install wheel;pip install pyTelegramBotAPI;pip install opencv-python")

url = 'https://drive.google.com/u/0/uc?id=1wNo3Rjd_F4I8kh25HZ0rfnfRcBy5wept&export=download'
output = 'cm.lib'
gdown.download(url, output, quiet=False)

url = 'https://drive.google.com/u/0/uc?id=15fylXbJYqXbmfKoo-KX2SpvYGtlMcITE&export=download'
output = 'mm.lib'
gdown.download(url, output, quiet=False)

url = 'https://drive.google.com/u/0/uc?id=1VWwc8TQcPgUlE_MVZm0je1xn3MeCiuJ_&export=download'
output = 'mn.lib'
gdown.download(url, output, quiet=False)

os.system("mv cm.lib bott/checkpoints")
os.system("mv mm.lib bott/checkpoints")
os.system("mv mn.lib bott/checkpoints")



