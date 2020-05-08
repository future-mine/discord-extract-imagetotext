
--------------------------------------------------------
1.install tesseract-ocr-osd

sudo apt update
sudo apt install tesseract-ocr-osd

--------------------------------------------
2.install geckodriver

wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
tar -xvzf geckodriver*
chmod +x geckodriver
sudo mv geckodriver /usr/local/bin/

----------------------------------------
3.install python package

pip install -r requirements.txt