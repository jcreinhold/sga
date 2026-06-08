# Build tasks for the SGA mdBook site.
# See book.toml (mdBook config) and scripts/generate-summary.py (ToC generator).

MDBOOK_VERSION := 0.5.3
# Pre-release: the first mdbook-katex built against mdbook 0.5. Pin exactly.
MDBOOK_KATEX_VERSION := 0.10.0-alpha
BUILD_DIR := book

# mdbook-katex 0.10.0-alpha is built against mdbook 0.5.1 and prints a benign
# cross-version WARN when run under the 0.5.3 we pin (it is the newest release,
# so there is nothing to upgrade to). Quiet just that preprocessor's sub-error
# logs; genuine katex errors are level=error and still surface.
MDBOOK := RUST_LOG=info,mdbook_katex=error mdbook

.DEFAULT_GOAL := help

.PHONY: help
help: ## Show this help.
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'

.PHONY: summary
summary: ## Regenerate book/SUMMARY.md from the chapter files.
	python3 scripts/generate-summary.py

.PHONY: check
check: ## Fail if book/SUMMARY.md is stale (the CI drift gate).
	python3 scripts/generate-summary.py --check

.PHONY: build
build: summary ## Build the static site into $(BUILD_DIR)/.
	$(MDBOOK) build

.PHONY: serve
serve: summary ## Build, serve locally with live reload, and open a browser.
	$(MDBOOK) serve --open

.PHONY: clean
clean: ## Remove the build output.
	mdbook clean

.PHONY: install
install: ## Install the pinned mdBook toolchain (matches CI).
	cargo install mdbook --version $(MDBOOK_VERSION) --locked
	cargo install mdbook-katex --version $(MDBOOK_KATEX_VERSION) --locked
