#!/usr/bin/env bash

export PATH=$PATH:$(pwd)

kaggle competitions download -c house-prices-advanced-regression-techniques -p packages/regression_model/regression_model/datasets/