#!/bin/sh

clear

rm -rf public
mkdir public
cd public

git config --global user.email "action@github.com"
git config --global user.name "GitHub Action"

git init
git remote add origin https://github.com/${GITHUB_PATH}
git pull origin master

rm -rf out
mkdir out
cp -r ../.out/* out

git add out
git commit -m "New Build 🎉🎈🎂🍾🎊🍻💃"
git push https://mottaquikarim:${GITHUB_TOKEN}@github.com/${GITHUB_PATH}.git HEAD:master --follow-tags;
