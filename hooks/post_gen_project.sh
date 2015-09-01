#!/bin/bash

echo 'Installing pip packages...'
pip install -r requirements/dev.txt
echo 'Linking manage.py to bin...'
ln -s manage.py ../bin/manage.py
echo 'Done.'
