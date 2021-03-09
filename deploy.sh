#!/usr/bin/sh
cd ~/projects/project_foldable_robotics
bundle exec jekyll build
rm -rf ~/websites/egr557.github.io/*
cp ~/projects/project_foldable_robotics/_site/* ~/websites/egr557.github.io/
cd ~/websites/egr557.github.io/
git add *
git pull
git commit -m"autobuild"
git push

