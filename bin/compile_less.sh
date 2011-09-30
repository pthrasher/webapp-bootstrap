#!/bin/bash

if [[ "$1" ]]; then
	new_file=static/css/$(basename "$1" | sed 's/less/css/')
	lessc $1 > $new_file
	[ -f $newfile ] && echo "Successfully compiled '$1' into '$new_file'." && exit 0
	echo "Something went wrong. The file '$new_file' didn't compile." && exit 1
fi

echo "No arg"
exit 1
