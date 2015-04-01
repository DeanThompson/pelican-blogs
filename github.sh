#!/bin/sh

cd output
git add .
git commit -m $1
git push

