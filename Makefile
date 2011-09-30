all:
	find static/less -type f -name '*.less' -maxdepth 1 -exec bin/compile_less.sh "{}" \;
	coffee -o static/js -c static/coffee
