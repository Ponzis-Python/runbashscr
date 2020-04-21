#!/bin/bash

find "dafoo" -type f -exec chmod 664 "{}" ";"
find "dafoo" -iname ".[a-zA-Z_-]*" -maxdepth 1 -type f -exec rm {} \;
find "dafoo" -type f -exec cp "{}" "/Users/chumlee/fooDir" ";"
find "dafoo" -maxdepth 1 -type f -exec rm -rf "{}" ";"
