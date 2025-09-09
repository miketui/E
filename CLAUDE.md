# CLAUDE.md - Claude Integration Guide for EPUB Production

## Overview
This document outlines how to effectively use Claude for professional EPUB production, from content creation to final compilation. Claude serves as your AI assistant for maintaining consistency, quality, and professional standards throughout the entire workflow.

## Claude's Role in EPUB Production

### Primary Functions
- **Content Validation**: Ensure all XHTML/CSS meets standards
- **Style Consistency**: Maintain uniform formatting across all files
- **Quality Assurance**: Review content for completeness and professional presentation
- **Code Generation**: Create templates and boilerplate code
- **Problem Solving**: Debug issues and optimize workflows

## Quick Start with Claude

### Essential Prompts for EPUB Work

#### 1. Content Review Prompt
```
Review this XHTML file for EPUB compatibility and professional standards:

[PASTE XHTML CONTENT]

Check for:
- XHTML 1.1 compliance
- Proper CSS class usage
- Image path accuracy
- Typography consistency
- Accessibility standards
- Professional formatting
```

#### 2. CSS Validation Prompt
```
Validate this CSS for EPUB production:

[PASTE CSS]

Ensure:
- Cross-device compatibility
- Embedded font references are correct
- Color accessibility (WCAG compliance)
- Responsive design principles
- Print-ready formatting
```

#### 3. Chapter Structure Verification
```
Verify this chapter follows the required 6-page structure:

Chapter Data: [PASTE CHAPTER INFO]

Requirements:
1. Title page with Roman numeral and bible quote
2. Body content with proper styling
3. Endnotes section
4. Quiz (max 4 questions)
5. Worksheet (static layout)
6. Closing image with caption

Confirm all elements are present and properly formatted.
```

## Workflow Integration

### Phase 1: Planning and Setup
```bash
# Use Claude to generate project structure
claude --prompt "Create EPUB project structure for professional hairstyling book with 16 chapters, 8 front matter files, 17 backmatter files"
```

### Phase 2: Content Creation
#### Chapter Creation Workflow
1. **Data Preparation**
   ```
   Claude, help me structure Chapter [X] data:
   - Title: [TITLE]
   - Roman Numeral: [ROMAN]
   - Bible Quote: [QUOTE]
   - Content: [MAIN_CONTENT]
   - Generate the complete chapter object following the React template
   ```

2. **XHTML Generation**
   ```
   Generate production-ready XHTML for Chapter [X] using this data:
   [CHAPTER_DATA]
   
   Include:
   - Proper DOCTYPE and namespace
   - Linked CSS references
   - Six complete pages with page breaks
   - All required CSS classes
   - Image references with alt text
   ```

### Phase 3: Quality Assurance
#### Batch Validation
```
Claude, review these files for consistency:

Files to check:
- [LIST_OF_FILES]

Validation criteria:
- Typography consistency
- Color scheme adherence
- Image path accuracy
- CSS class naming consistency
- Professional presentation standards
```

## Advanced Claude Workflows

### 1. Automated Content Generation

#### Front Matter Generator
```python
# Use with Claude API
import anthropic

def generate_front_matter(content_type, data):
    prompt = f"""
    Generate professional {content_type} page for EPUB:
    
    Data: {data}
    
    Requirements:
    - Two-column layout where appropriate
    - Single page format
    - Professional typography
    - XHTML 1.1 compliance
    - Proper CSS class usage
    """
    
    client = anthropic.Anthropic()
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=2000,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text
```

#### Chapter Batch Processor
```python
def process_chapters_with_claude(chapters_data):
    for chapter in chapters_data:
        prompt = f"""
        Create complete Chapter {chapter['roman']} XHTML:
        
        Title: {chapter['title']}
        Content: {chapter['content']}
        Images: {chapter['images']}
        
        Use the established ACISS design system.
        Include all 6 required pages.
        Ensure professional presentation.
        """
        
        # Process with Claude
        result = claude_client.generate(prompt)
        save_chapter_file(chapter['filename'], result)
```

### 2. Consistency Checking

#### Style Guide Enforcement
```
Claude, enforce these style guidelines across all files:

ACISS Style Guide:
- Primary Color: #1a1a1a
- Accent Color: #1797a6
- Typography: Libre Baskerville (body), Cinzel Decorative (headers)
- Spacing: 2rem standard padding
- Roman numerals: Centered badges with gradient
- Bible quotes: Pill-shaped containers with accent borders

Check file: [FILENAME]
Report any deviations and provide corrections.
```

#### Cross-Reference Validation
```
Validate all internal references in this EPUB:

Content Files: [LIST]
Image Files: [LIST]
CSS Files: [LIST]

Ensure:
- All image src paths are correct
- CSS file references work
- No broken internal links
- Consistent file naming conventions
```

### 3. Optimization Workflows

#### Performance Optimization
```
Optimize this EPUB for performance:

Current Issues:
- File size: [SIZE]
- Image count: [COUNT]
- CSS complexity: [DETAILS]

Recommendations needed for:
- Image compression
- CSS optimization
- File structure improvements
- Loading performance
```

## Claude API Integration

### Environment Setup
```bash
# Install Claude SDK
pip install anthropic

# Set API key
export ANTHROPIC_API_KEY="your-api-key"
```

### Production Scripts

#### Validation Script
```python
import anthropic
import glob

class EPUBValidator:
    def __init__(self):
        self.client = anthropic.Anthropic()
    
    def validate_file(self, filepath, file_type):
        with open(filepath, 'r') as f:
            content = f.read()
        
        prompt = f"""
        Validate this {file_type} file for EPUB production:
        
        File: {filepath}
        Content: {content[:2000]}...
        
        Check for:
        - Standards compliance
        - Professional formatting
        - Consistency with style guide
        - Technical accuracy
        
        Provide specific feedback and corrections.
        """
        
        response = self.client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1000,
            messages=[{"role": "user", "content": prompt}]
        )
        
        return response.content[0].text

# Usage
validator = EPUBValidator()
for file in glob.glob("OEBPS/text/*.xhtml"):
    result = validator.validate_file(file, "XHTML")
    print(f"Validation for {file}: {result}")
```

#### Content Generator
```python
class EPUBContentGenerator:
    def __init__(self):
        self.client = anthropic.Anthropic()
        self.style_guide = self.load_style_guide()
    
    def generate_chapter(self, chapter_data):
        prompt = f"""
        Generate complete EPUB chapter using ACISS design system:
        
        Chapter Data: {chapter_data}
        Style Guide: {self.style_guide}
        
        Output requirements:
        - Valid XHTML 1.1
        - Six complete pages
        - Professional typography
        - Proper image references
        - CSS class consistency
        """
        
        response = self.client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=4000,
            messages=[{"role": "user", "content": prompt}]
        )
        
        return response.content[0].text
```

## Best Practices with Claude

### 1. Prompt Optimization
- **Be Specific**: Include exact requirements, constraints, and standards
- **Provide Context**: Share the complete style guide and requirements
- **Use Examples**: Reference the React templates as models
- **Iterate**: Refine prompts based on output quality

### 2. Quality Workflow
```
Step 1: Generate → Claude creates initial content
Step 2: Review → Claude validates against standards  
Step 3: Refine → Claude optimizes and corrects
Step 4: Verify → Claude performs final quality check
```

### 3. Consistency Maintenance
- Keep a master style guide document
- Use consistent terminology across all prompts
- Maintain a log of successful prompts for reuse
- Regular validation passes with Claude

## Troubleshooting with Claude

### Common Issues and Prompts

#### CSS Not Applying
```
Claude, diagnose why CSS isn't applying to this XHTML:

XHTML: [CONTENT]
CSS: [STYLES]

Check:
- File path references
- CSS selector specificity
- EPUB reader compatibility
- Syntax errors
```

#### Image Display Problems
```
Troubleshoot image display issues:

Image references: [LIST]
File structure: [STRUCTURE]
XHTML img tags: [EXAMPLES]

Identify and fix:
- Path errors
- Missing alt attributes
- Size/format issues
- Accessibility problems
```

#### Validation Errors
```
Resolve EPUB validation errors:

EPUBCheck output: [ERROR_LOG]
Affected files: [FILE_LIST]

Provide:
- Root cause analysis
- Specific fixes
- Prevention strategies
```

## Integration with Build Tools

### Makefile Integration
```makefile
# Use Claude for validation during build
validate-with-claude:
	@echo "Validating with Claude..."
	@python scripts/claude-validator.py

generate-content:
	@echo "Generating content with Claude..."
	@python scripts/claude-generator.py

.PHONY: validate-with-claude generate-content
```

### CI/CD Integration
```yaml
# .github/workflows/epub-claude.yml
- name: Claude Quality Check
  run: |
    python scripts/claude-validator.py --all
    python scripts/claude-consistency-check.py
```

## Performance Tips

### 1. Batch Processing
- Group similar tasks (all chapters, all front matter)
- Use consistent prompts for efficiency
- Cache Claude responses for repeated validations

### 2. Incremental Workflow
- Validate as you create, don't wait until the end
- Use Claude for quick spot checks during development
- Maintain a feedback loop for continuous improvement

### 3. Automation Balance
- Automate repetitive validation tasks
- Keep human oversight for creative decisions
- Use Claude for consistency, not creativity replacement

## Monitoring and Metrics

Track Claude's effectiveness:
- **Validation Accuracy**: How often Claude catches real issues
- **Time Savings**: Compare manual vs Claude-assisted workflows  
- **Quality Improvement**: Before/after Claude integration metrics
- **Consistency Scores**: Measure style guide adherence

This integration approach ensures Claude becomes an integral part of your professional EPUB production workflow, maintaining quality and consistency while accelerating development.

## Complete Agent Execution System

### 1. **Specific Agent Prompts**
Each agent has detailed system prompts defining their role:

```python
CHAPTER_AGENT_SYSTEM_PROMPT = """
You are a specialized EPUB Chapter Generation Agent for the ACISS hairstyling certification book.
Generate professional XHTML chapters following the exact 6-page structure...
"""

VALIDATION_AGENT_PROMPT = """
You are an EPUB Validation Agent specializing in professional publishing standards.
Validation Areas: XHTML 1.1 compliance, CSS validity, accessibility...
"""
```

### 2. **Initialization Commands**
```bash
# Setup complete agent environment in existing repository
make setup
make install

# Verify system ready
make health

# Run demo mode (no API key required)
make demo
```

### 3. **Execution Commands**
```bash
# Generate single chapter
python scripts/epub_agents.py generate-chapter \
  --chapter-number "XIII" \
  --data-file "data/chapters/chapter-xiii.yaml" \
  --output "OEBPS/text/23-Chapter-XIII.xhtml"

# Run complete validation workflow
python scripts/epub_agents.py validate --directory OEBPS/text

# Batch generate chapters
make generate
```

### 4. **Interactive Agent Commands**
```bash
# Chat with specific agent
python scripts/epub_agents.py chat --agent chapter

# Chat with validation agent
python scripts/epub_agents.py chat --agent validation

# Custom content generation
python scripts/epub_agents.py chat --agent content
```

### 5. **Complete Ready-to-Run System**
The repository now includes a complete executable system:

```bash
# Quick start commands
make setup      # Initialize environment
make health     # Check system status
make demo       # Run without API key
make generate   # Generate all chapters
make validate   # Quality assurance

# Specific chapter generation
make chapter-xiii
make chapter-xiv

# Interactive sessions
make chat-chapter
make chat-validation
```

### 6. **Configuration and Data Files**
Ready-to-use configuration and sample data:

- **`config/agents.yaml`**: Complete agent configuration
- **`config/chapters.yaml`**: Batch processing configuration  
- **`data/chapters/chapter-xiii.yaml`**: Sample chapter data
- **`data/chapters/chapter-xiv.yaml`**: Sample chapter data
- **`Makefile`**: Convenient command shortcuts
- **`README.md`**: Complete usage documentation

### 7. **System Validation and Health Checks**
```bash
# Complete system health check
make health

# Validate generated content
make validate

# Clean and reset
make clean
```

The system is now complete with executable commands, configuration files, sample data, and comprehensive documentation. Users can immediately start generating professional EPUB content using the AI agent system.