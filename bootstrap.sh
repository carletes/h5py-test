#!/bin/sh

here="$(cd $(dirname $0) && pwd)"
cache_dir="$here/.pip-cache"

mkdir -p $cache_dir

pip install --cache-dir=$cache_dir -r $here/requirements.txt
