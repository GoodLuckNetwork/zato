#!/bin/bash

git log -n 1 --pretty=format:"%H" > $CURDIR/code/release-info/revision.txt