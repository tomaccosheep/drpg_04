#!/bin/bash
docker stop $1
docker container rm $1
