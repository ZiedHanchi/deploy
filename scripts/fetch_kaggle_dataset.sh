#!/usr/bin/env bash

export PATH=$PATH:$(pwd)
 
cp -f .kaggle/kaggle.json ~/.kaggle

chmod 600 ~/.kaggle/kaggle.json

kaggle competitions download -c house-prices-advanced-regression-techniques -p packages/regression_model/regression_model/datasets/

unzip -o packages/regression_model/regression_model/datasets/house-prices-advanced-regression-techniques.zip -d "packages/regression_model/regression_model/datasets/"

rm packages/regression_model/regression_model/datasets/house-prices-advanced-regression-techniques.zip
