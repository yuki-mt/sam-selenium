#!/bin/bash
mkdir -p ./layers/selenium-binaries
rm -rf ./layers/selenium-binaries
mkdir -p ./layers/selenium-binaries


filename=chromedriver_linux64.zip
curl -SLO https://chromedriver.storage.googleapis.com/2.37/$filename
unzip $filename -d ./layers/selenium-binaries
rm $filename

filename=stable-headless-chromium-amazonlinux-2017-03.zip
curl -SLO https://github.com/adieuadieu/serverless-chrome/releases/download/v1.0.0-37/$filename
unzip $filename -d ./layers/selenium-binaries
rm $filename
