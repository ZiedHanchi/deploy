#!/usr/bin/env bash

export PATH=$PATH:$(pwd)
 
cp -f kaggle.json ~/.kaggle

chmod 600 ~/.kaggle/kaggle.json

kaggle competitions download -c house-prices-advanced-regression-techniques -p packages/regression_model/regression_model/datasets/

unzip -n packages/regression_model/regression_model/datasets/house-prices-advanced-regression-techniques.zip