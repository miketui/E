# EPUB Production Makefile

.PHONY: help install setup generate validate clean health demo

help:
	@echo "EPUB Production System Commands:"
	@echo "  install    - Install Python dependencies"
	@echo "  setup      - Setup environment (copy .env template)"
	@echo "  demo       - Run demo generation without API key"
	@echo "  generate   - Generate sample chapters (requires API key)"
	@echo "  validate   - Validate all EPUB files"
	@echo "  health     - Check system health"
	@echo "  clean      - Clean generated files"

install:
	pip install anthropic pyyaml

setup:
	@if [ ! -f .env ]; then \
		echo "ANTHROPIC_API_KEY=your-api-key-here" > .env; \
		echo "PROJECT_NAME=ACISS-Hairstyling-Book" >> .env; \
		echo "OUTPUT_DIR=OEBPS/text" >> .env; \
		echo "VALIDATION_ENABLED=true" >> .env; \
		echo "✅ Created .env file - please add your Anthropic API key"; \
	else \
		echo "⚠️  .env file already exists"; \
	fi

demo:
	@echo "🎭 Running EPUB Agents in demo mode..."
	@echo "This demonstrates the system without requiring API keys"
	python scripts/epub_agents.py health-check

generate:
	@echo "📚 Generating sample chapters..."
	python scripts/epub_agents.py generate-chapter \
		--chapter-number "XIII" \
		--data-file "data/chapters/chapter-xiii.yaml" \
		--output "OEBPS/text/23-Chapter-XIII.xhtml"
	@echo "Generated Chapter XIII"
	python scripts/epub_agents.py generate-chapter \
		--chapter-number "XIV" \
		--data-file "data/chapters/chapter-xiv.yaml" \
		--output "OEBPS/text/25-Chapter-XIV.xhtml"
	@echo "Generated Chapter XIV"

validate:
	@echo "🔍 Validating EPUB files..."
	@mkdir -p reports
	python scripts/epub_agents.py validate --directory OEBPS/text --output reports/validation.json
	@echo "✅ Validation complete - check reports/validation.json"

health:
	@echo "🏥 Checking system health..."
	python scripts/epub_agents.py health-check

clean:
	@echo "🧹 Cleaning generated files..."
	rm -f OEBPS/text/23-Chapter-XIII.xhtml
	rm -f OEBPS/text/25-Chapter-XIV.xhtml
	rm -rf reports/*.json
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete
	@echo "✅ Cleanup complete"

# Quick commands for specific chapters
chapter-xiii:
	python scripts/epub_agents.py generate-chapter \
		--chapter-number "XIII" \
		--data-file "data/chapters/chapter-xiii.yaml" \
		--output "OEBPS/text/23-Chapter-XIII.xhtml"

chapter-xiv:
	python scripts/epub_agents.py generate-chapter \
		--chapter-number "XIV" \
		--data-file "data/chapters/chapter-xiv.yaml" \
		--output "OEBPS/text/25-Chapter-XIV.xhtml"

# Interactive commands
chat-chapter:
	python scripts/epub_agents.py chat --agent chapter

chat-validation:
	python scripts/epub_agents.py chat --agent validation

# Test demo without API
test-demo:
	@echo "🧪 Testing demo functionality..."
	python scripts/epub_agents.py health-check
	@echo "Demo test complete"