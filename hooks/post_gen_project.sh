#!/bin/bash

echo 'Installing pip packages...'
pip install -r requirements/dev.txt

echo 'Linking manage.py to bin...'
MANAGE_PY=$(find . ! -path './lib/*' ! -path './bin/*' -name 'manage.py' | head -n 1)
ln -s $(readlink -e $MANAGE_PY) ../bin/manage.py

echo 'Done.'
