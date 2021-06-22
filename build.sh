#! /bin/bash

buildah bud -t fgerrbot:matrix .
buildah push fgerrbot:matrix docker://git.fossgalaxy.com:8042/irc/errbot/fg-errbot:matrix                 
