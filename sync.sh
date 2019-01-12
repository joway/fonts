# /bin/bash

curl 'https://google-webfonts-helper.herokuapp.com/api/fonts' > fonts.json
python ./sync.py
