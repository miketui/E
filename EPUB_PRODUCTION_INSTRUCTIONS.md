# EPUB Production Instructions - Bestseller Ready

## Overview
This document provides step-by-step instructions for creating a professional, bestseller-quality EPUB with consistent formatting, embedded fonts, and optimized layouts for all devices using the AI Agent system.

## System Components

The EPUB production system includes:

1. **AI Agents**: Specialized agents for content generation, validation, formatting
2. **Executable Commands**: CLI tools for all production tasks
3. **Configuration Management**: YAML-based agent and workflow configuration
4. **Template System**: Standardized XHTML templates
5. **Validation Pipeline**: Automated quality assurance
6. **Batch Processing**: Parallel chapter generation

## Quick Start Guide

### 1. Initialize Your EPUB Project
```bash
# Create a new EPUB project with complete agent system
python epub_startup_script.py --project-name "My-Professional-EPUB" --init-all

# Navigate to your project
cd My-Professional-EPUB

# Setup environment
cp .env.template .env
# Edit .env and add your Anthropic API key: ANTHROPIC_API_KEY=your-key-here

# Install dependencies
pip install anthropic pyyaml
```

### 2. Verify System Health
```bash
# Check that everything is working
python scripts/epub_agents.py health-check
```

### 3. Generate Your First Chapter
```bash
# Generate Chapter XIII using sample data
python scripts/epub_agents.py generate-chapter \
  --chapter-number "XIII" \
  --data-file "data/chapters/chapter-xiii.yaml" \
  --output "OEBPS/text/23-Chapter-XIII.xhtml"
```

### 4. Validate Your Output
```bash
# Validate the generated chapter
python scripts/epub_agents.py validate --directory OEBPS/text
```

## Agent Commands Reference

### Chapter Generation Agent
```bash
# Generate single chapter
python scripts/epub_agents.py generate-chapter \
  --chapter-number "XIV" \
  --data-file "data/chapters/chapter-xiv.yaml" \
  --output "OEBPS/text/25-Chapter-XIV.xhtml"

# Interactive chapter agent chat
python scripts/epub_agents.py chat --agent chapter
```

### Validation Agent
```bash
# Validate all EPUB files
python scripts/epub_agents.py validate --directory OEBPS/text

# Save detailed validation report
python scripts/epub_agents.py validate \
  --directory OEBPS/text \
  --output reports/validation_report.json

# Interactive validation chat
python scripts/epub_agents.py chat --agent validation
```

### Content Generation Agent
```bash
# Interactive content generation
python scripts/epub_agents.py chat --agent content

# Example prompts:
# "Generate front matter for a hairstyling certification book"
# "Create quiz questions about sustainable beauty practices"
# "Generate worksheet content for networking skills"
```

### Formatting Agent
```bash
# Interactive formatting assistance
python scripts/epub_agents.py chat --agent formatter

# Example prompts:
# "Apply ACISS design system to this content"
# "Format this text for two-column layout"
# "Optimize this XHTML for accessibility"
```

## Batch Production Workflows

### Generate All Chapters
```bash
# Run complete batch workflow
python scripts/batch_workflow.py

# Or use the configured batch command
python scripts/epub_agents.py batch-generate --chapters-config config/chapters.yaml
```

### Make Commands (Convenience)
```bash
# Setup environment
make setup

# Generate all sample chapters
make generate

# Validate all files
make validate

# System health check
make health

# Generate specific chapters
make chapter-xiii
make chapter-xiv

# Interactive chat sessions
make chat-chapter
make chat-validation
```

## File Structure Requirements

Your EPUB project follows this structure:

```
Your-EPUB-Project/
├── META-INF/
│   └── container.xml
├── OEBPS/
│   ├── content.opf
│   ├── toc.ncx
│   ├── styles/
│   │   ├── fonts.css
│   │   └── style.css
│   ├── fonts/
│   │   ├── librebaskerville-regular.woff2
│   │   ├── librebaskerville-bold.woff2
│   │   ├── librebaskerville-italic.woff2
│   │   ├── CinzelDecorative.woff2
│   │   ├── Montserrat-Regular.woff2
│   │   └── Montserrat-Bold.woff2
│   ├── images/
│   │   └── [chapter and content images]
│   └── text/
│       ├── [front matter files]
│       ├── [chapter files]
│       └── [back matter files]
├── scripts/
│   ├── epub_agents.py          # Main agent system
│   ├── run_agents.py           # Direct execution script
│   └── batch_workflow.py       # Batch processing
├── data/
│   ├── chapters/               # Chapter data files
│   ├── front_matter/           # Front matter data
│   └── back_matter/            # Back matter data
├── config/
│   ├── agents.yaml            # Agent configuration
│   └── chapters.yaml          # Batch chapter config
├── templates/
│   └── chapter_template.xhtml # XHTML templates
└── docs/
    └── usage_guide.md         # Detailed usage guide
```

## Chapter Data Format

Create chapter data in YAML format:

```yaml
# data/chapters/chapter-example.yaml
roman: 'XV'
title: 'Your Chapter Title'
title_lines:
  - 'FIRST LINE'
  - 'SECOND LINE'
  - 'THIRD LINE'
bible_quote: 'Your inspirational quote'
bible_reference: 'Quote Source'
introduction: 'Chapter introduction paragraph...'
content: |
  <h2>Section Title</h2>
  <p>Your chapter content with proper HTML formatting...</p>
  
  <h3>Subsection</h3>
  <p>More content...</p>
  
  <blockquote>
  "Important quote or callout text"
  </blockquote>
endnotes:
  - 'First endnote citation'
  - 'Second endnote citation'
  - 'Third endnote citation'
quiz_questions:
  - question: 'Your quiz question here?'
    options:
      - 'A) First option'
      - 'B) Second option'
      - 'C) Third option'
      - 'D) Fourth option'
  # Maximum 4 questions per chapter
worksheet:
  title: 'Chapter Worksheet Title'
  sections:
    - heading: 'Section 1'
      content: 'Instructions or prompts'
    - heading: 'Section 2'
      content: 'More worksheet content'
closing_image: '../images/chapter-example.jpg'
closing_caption: 'Inspirational caption for the closing image'
```

## Agent Configuration

Customize agent behavior in `config/agents.yaml`:

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
  content:
    model: "claude-3-sonnet-20240229"
    max_tokens: 3000
    temperature: 0.2
  formatter:
    model: "claude-3-sonnet-20240229"
    max_tokens: 4000
    temperature: 0.2

project:
  name: "Your EPUB Project"
  output_directory: "OEBPS/text"
  validation_enabled: true
  max_workers: 4

workflows:
  chapter_production:
    agents: [chapter, formatter, validation]
    parallel: true
    timeout: 300
```

## Quality Assurance Workflow

### 1. Generation
```bash
# Generate content with agents
python scripts/epub_agents.py generate-chapter [options]
```

### 2. Validation
```bash
# Validate with specialized agent
python scripts/epub_agents.py validate --directory OEBPS/text
```

### 3. Review Reports
```bash
# Check validation reports
cat reports/validation_report.json
```

### 4. Interactive Improvement
```bash
# Chat with validation agent for improvements
python scripts/epub_agents.py chat --agent validation
```

## Advanced Features

### Custom Agent Prompts
Modify agent system prompts in the `epub_agents.py` file to customize behavior for your specific needs.

### Parallel Processing
The system supports parallel chapter generation for faster batch processing.

### Template Customization
Modify templates in the `templates/` directory to change output formatting.

### Workflow Automation
Use the batch workflow script to automate complete EPUB generation processes.

## Professional Standards

The system ensures:

### Chapter Structure (6 pages exactly)
1. **Title Page**: Roman numeral badge + vertical title stack + bible quote + introduction
2. **Body Content**: Main chapter content with proper styling and structure
3. **Endnotes**: Numbered references and citations
4. **Quiz**: Exactly 4 multiple choice questions maximum
5. **Worksheet**: Interactive elements (static for EPUB)
6. **Closing Image**: Chapter conclusion with inspirational image and caption

### ACISS Design System
- **Primary Color**: #1a1a1a
- **Accent Color**: #1797a6  
- **Typography**: Libre Baskerville (body), Cinzel Decorative (headers), Montserrat (sans)
- **Roman numerals**: Centered badges with gradient background
- **Bible quotes**: Pill-shaped containers with accent borders
- **Professional spacing**: 2rem standard padding

### Quality Standards
- XHTML 1.1 compliance
- WCAG 2.1 accessibility
- Cross-device compatibility
- Professional typography
- Consistent styling
- Optimized images

## Troubleshooting

### Common Issues

**"Anthropic API key not found"**
```bash
# Set your API key in .env file
echo "ANTHROPIC_API_KEY=your-key-here" >> .env
```

**"Module not found: anthropic"**
```bash
# Install dependencies
pip install anthropic pyyaml
```

**"Permission denied"**
```bash
# Make scripts executable
chmod +x scripts/*.py
```

**"Validation errors"**
```bash
# Run validation and check reports
python scripts/epub_agents.py validate --directory OEBPS/text --output reports/debug.json
cat reports/debug.json
```

### Health Check
```bash
# Run complete system health check
python scripts/epub_agents.py health-check
```

## Next Steps

1. **Customize chapter data** in `data/chapters/`
2. **Modify CSS styles** in `OEBPS/styles/`
3. **Add images** to `OEBPS/images/`
4. **Run batch generation** with `make generate`
5. **Validate and review** outputs
6. **Create your complete EPUB** with professional quality

This system provides a complete, professional EPUB production workflow with AI assistance at every step, ensuring consistent quality and bestseller-ready output.