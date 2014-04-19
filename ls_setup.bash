#!/usr/bin/env bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
source $DIR/../../devel/setup.bash

opencv_path=/usr/local/lib/python2.7/dist-packages

export PYTHONPATH=$opencv_path:${PYTHONPATH/$opencv_path}

echo $PYTHONPATH

