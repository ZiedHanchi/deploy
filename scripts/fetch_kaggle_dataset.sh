#!/usr/bin/env bash

export PATH=$PATH:$(pwd)
 
cp -f .kaggle/kaggle.json ~/.kaggle

chmod 600 ~/.kaggle/kaggle.json

kaggle competitions download -c house-prices-advanced-regression-techniques -p ~/project/packages/regression_model/regression_model/datasets/

unzip -o ~/project/packages/regression_model/regression_model/datasets/house-prices-advanced-regression-techniques.zip -d "~/project/packages/regression_model/regression_model/datasets/"

rm ~/project/packages/regression_model/regression_model/datasets/house-prices-advanced-regression-techniques.zip
