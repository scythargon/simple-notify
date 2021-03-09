#!/usr/bin/env bash

docker build -t simple-notify .
docker tag simple-notify scythargon/simple-notify:latest
docker push scythargon/simple-notify:latest
