#!/bin/bash

# Creates git tags!
# Reads version from VERSION file.

version=`cat VERSION`
changelog=CHANGES.md
grep $version $changelog >> /dev/null
if [[ $? -ne 0 ]]; then
  echo "Couldn't find version $version in $changelog"
  exit
fi

read -p "Tag as v$version? [y/n] " -n 1 -r
if [[ $REPLY =~ ^[Yy]$ ]]; then
  # create git tags
  git tag -a v$version -m "version $version"
  git push --tags
fi
