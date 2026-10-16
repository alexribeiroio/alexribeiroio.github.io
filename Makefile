.PHONY: setup serve preview build check
setup:
	./scripts/install-hugo.sh
serve:
	./scripts/hugo.sh server --bind 127.0.0.1 --renderToMemory
preview:
	./scripts/hugo.sh server --bind 127.0.0.1 --buildDrafts --environment preview --renderToMemory
build:
	./scripts/hugo.sh --gc --minify --cleanDestinationDir
check:
	./scripts/check.sh
