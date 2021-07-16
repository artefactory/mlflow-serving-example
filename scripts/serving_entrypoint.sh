#!/bin/sh

mlflow models serve --model-uri $MODEL_URI -h 0.0.0.0 -p $SERVING_PORT --no-conda
