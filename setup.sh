#!/bin/bash

cd ..

pip list | grep -q pygame || pip install pygame
# pip list | grep -q pygbag || git clone https://github.com/andreagalle/pygbag.git
pip list | grep -q pygbag || pip install -e $PWD/pygbag

#sed $1