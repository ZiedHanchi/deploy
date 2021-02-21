#!/usr/bin/env bash

export PATH=$PATH:$(pwd)
 
cp -f kaggle.json ~/.kaggle

kaggle competitions download -c house-prices-advanced-regression-techniques -p packages/regression_model/regression_model/datasets/