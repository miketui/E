# EPUB AI Agent Production System

## Overview

This repository contains a comprehensive AI-powered EPUB production system designed for creating professional, bestseller-quality ebooks. The system uses specialized AI agents for content generation, validation, formatting, and quality assurance.

## 🚀 Quick Start

### 1. Clone and Setup
```bash
git clone [repository-url]
cd E

# Setup environment
make setup
# Edit .env and add your Anthropic API key: ANTHROPIC_API_KEY=your-key-here

# Install dependencies
make install
```

### 2. Health Check
```bash
make health
```

### 3. Generate Your First Chapter
```bash
make chapter-xiii
```

### 4. Validate Output
```bash
make validate
```

## 🏗️ System Architecture

### Core Components

1. **AI Agents (`scripts/epub_agents.py`)**
   - Chapter Generation Agent
   - Validation Agent  
   - Content Agent
   - Formatting Agent

2. **Configuration System (`config/`)**
   - Agent configurations
   - Workflow definitions
   - Chapter batch processing

3. **Data Management (`data/`)**
   - Chapter data files
   - Front/back matter content
   - Sample content for testing

4. **Templates (`templates/`)**
   - XHTML chapter templates
   - CSS styling templates

## 🤖 Available Agents

### Chapter Agent
Generates complete 6-page chapter structure with:
- Title page with Roman numeral and bible quote
- Body content with professional styling
- Endnotes section
- Quiz (max 4 questions)
- Worksheet (static layout)
- Closing image with caption

### Validation Agent
Ensures professional standards:
- XHTML 1.1 compliance
- CSS validity and consistency
- Image reference accuracy
- Accessibility compliance
- Professional formatting

### Content Agent
Specialized in hairstyling content:
- Educational material design
- Professional terminology
- Learning objectives
- Practical applications

### Formatting Agent
Professional layout and design:
- ACISS design system implementation
- Typography consistency
- Responsive design
- Cross-device compatibility

## 📋 Available Commands

### Basic Operations
```bash
# System health check
make health

# Setup environment
make setup

# Install dependencies
make install
```

### Content Generation
```bash
# Generate specific chapters
make chapter-xiii
make chapter-xiv

# Generate all configured chapters
make generate

# Interactive agent chat
make chat-chapter
make chat-validation
```

### Quality Assurance
```bash
# Validate all EPUB files
make validate

# Clean generated files
make clean
```

### Advanced Commands
```bash
# Generate single chapter
python scripts/epub_agents.py generate-chapter \
  --chapter-number "XIII" \
  --data-file "data/chapters/chapter-xiii.yaml" \
  --output "OEBPS/text/23-Chapter-XIII.xhtml"

# Batch generate from config
python scripts/epub_agents.py batch-generate \
  --chapters-config config/chapters.yaml

# Interactive validation chat
python scripts/epub_agents.py chat --agent validation

# Detailed validation with report
python scripts/epub_agents.py validate \
  --directory OEBPS/text \
  --output reports/detailed-validation.json
```

## 🗂️ Project Structure

```
E/
├── META-INF/                  # EPUB metadata
├── OEBPS/                     # EPUB content
│   ├── text/                  # Generated XHTML files
│   ├── styles/                # CSS stylesheets
│   ├── images/                # Images and graphics
│   └── fonts/                 # Embedded fonts
├── scripts/                   # Executable AI agents
│   └── epub_agents.py         # Main agent system
├── data/                      # Content data
│   ├── chapters/              # Chapter data files (YAML)
│   ├── front_matter/          # Front matter data
│   └── back_matter/           # Back matter data
├── config/                    # Configuration files
│   ├── agents.yaml            # Agent configurations
│   └── chapters.yaml          # Batch processing config
├── templates/                 # XHTML templates
├── reports/                   # Validation reports
├── CLAUDE.md                  # Claude integration guide
├── AGENT.md                   # Agent system documentation
├── EPUB_PRODUCTION_INSTRUCTIONS.md  # Complete production guide
└── README.md                  # This file
```

## 📝 Chapter Data Format

Create chapter data in YAML format:

```yaml
# data/chapters/example.yaml
roman: 'XIII'
title: 'Your Chapter Title'
title_lines:
  - 'FIRST LINE'
  - 'SECOND LINE'
bible_quote: 'Inspirational quote'
bible_reference: 'Source'
introduction: 'Chapter introduction...'
content: |
  <h2>Section Title</h2>
  <p>Content with HTML formatting...</p>
endnotes:
  - 'Citation 1'
  - 'Citation 2'
quiz_questions:
  - question: 'Question text?'
    options:
      - 'A) Option 1'
      - 'B) Option 2'
      - 'C) Option 3'
      - 'D) Option 4'
worksheet:
  title: 'Worksheet Title'
  sections:
    - heading: 'Section 1'
      content: 'Instructions'
closing_image: '../images/chapter-image.jpg'
closing_caption: 'Image caption'
```

## ⚙️ Configuration

### Agent Configuration (`config/agents.yaml`)
```yaml
agents:
  chapter:
    model: "claude-3-sonnet-20240229"
    max_tokens: 6000
    temperature: 0.3
  validation:
    model: "claude-3-sonnet-20240229"
    max_tokens: 2000
    temperature: 0.1

project:
  name: "Your EPUB Project"
  output_directory: "OEBPS/text"
  validation_enabled: true
  max_workers: 4
```

### Environment Variables (`.env`)
```bash
ANTHROPIC_API_KEY=your-api-key-here
PROJECT_NAME=ACISS-Hairstyling-Book
OUTPUT_DIR=OEBPS/text
VALIDATION_ENABLED=true
```

## 🎨 Design System

The system implements the ACISS design system:

- **Primary Color**: #1a1a1a
- **Accent Color**: #1797a6
- **Typography**: Libre Baskerville (body), Cinzel Decorative (headers), Montserrat (sans)
- **Layout**: Professional spacing, responsive design
- **Components**: Roman numeral badges, bible quote containers, professional formatting

## 🧪 Demo Mode

The system includes demo functionality that works without API keys:

```bash
# Run demo without API setup
make demo

# Test system functionality
make test-demo
```

## 📚 Documentation

- **`CLAUDE.md`**: Complete Claude integration guide
- **`AGENT.md`**: Detailed agent system documentation  
- **`EPUB_PRODUCTION_INSTRUCTIONS.md`**: Step-by-step production guide
- **`README.md`**: This overview (you are here)

## 🔧 Development

### Adding New Agents
1. Create agent class in `scripts/epub_agents.py`
2. Add configuration in `config/agents.yaml`
3. Implement specialized prompts and functionality

### Customizing Templates
1. Edit templates in `templates/`
2. Modify CSS in `OEBPS/styles/`
3. Update agent prompts for new formatting

### Creating New Workflows
1. Add workflow definition to `config/agents.yaml`
2. Implement workflow logic in agent orchestrator
3. Add corresponding make commands

## 🚨 Troubleshooting

### Common Issues

**"Anthropic API key not found"**
```bash
# Set API key in .env
echo "ANTHROPIC_API_KEY=your-key-here" > .env
```

**"Module not found: anthropic"**
```bash
make install
```

**"Permission denied"**
```bash
chmod +x scripts/*.py
```

**"Validation errors"**
```bash
make validate
cat reports/validation.json
```

### Health Check
```bash
make health
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with `make demo` and `make health`
5. Submit a pull request

## 📄 License

[License information to be added]

## 🎯 Next Steps

1. **Customize Content**: Add your chapter data to `data/chapters/`
2. **Modify Styling**: Update CSS in `OEBPS/styles/`
3. **Generate Content**: Use `make generate` for batch processing
4. **Validate Quality**: Run `make validate` regularly
5. **Create Complete EPUB**: Follow the production guide

---

**Ready to create professional EPUBs with AI assistance!** 🚀

For detailed usage instructions, see `EPUB_PRODUCTION_INSTRUCTIONS.md`.