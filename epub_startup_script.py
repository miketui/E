#!/usr/bin/env python3
"""
EPUB Agent System Startup Script
Complete initialization and execution commands for AI-assisted EPUB production
"""

import os
import sys
import argparse
import yaml
import json
from pathlib import Path
from typing import Dict, List
import subprocess
import time

class EPUBAgentSystem:
    def __init__(self, project_name: str = "ACISS-Hairstyling-Book"):
        self.project_name = project_name
        self.project_dir = Path.cwd() / "EPUB_PROJECT"
        self.config_dir = self.project_dir / "config"
        self.data_dir = self.project_dir / "data"
        
    def initialize_project(self):
        """Initialize complete EPUB project structure with agent configuration"""
        print("🚀 Initializing EPUB Agent System...")
        
        # Create directory structure
        directories = [
            "OEBPS/text", "OEBPS/styles", "OEBPS/fonts", "OEBPS/images",
            "META-INF", "config", "data/chapters", "data/front_matter", 
            "data/back_matter", "scripts", "output", "logs"
        ]
        
        for dir_path in directories:
            (self.project_dir / dir_path).mkdir(parents=True, exist_ok=True)
            
        print(f"✓ Created project structure in {self.project_dir}")
        
        # Create configuration files
        self.create_agent_config()
        self.create_project_config()
        self.create_style_guide()
        self.create_sample_chapter_data()
        
        print("✓ Configuration files created")
        
    def create_agent_config(self):
        """Create agents.yaml configuration"""
        agent_config = {
            'orchestrator': {
                'model': 'claude-sonnet-4-20250514',
                'max_tokens': 2000,
                'temperature': 0.2,
                'system_prompt': '''You are the Master Orchestrator for EPUB production.
                Coordinate all specialized agents to ensure professional quality output.
                Maintain ACISS design standards and bestseller production quality.'''
            },
            'agents': {
                'chapter_generator': {
                    'model': 'claude-sonnet-4-20250514',
                    'max_tokens': 4000,
                    'temperature': 0.3,
                    'specialty': 'XHTML chapter generation with ACISS design system',
                    'system_prompt': '''You are a specialized EPUB Chapter Generation Agent.
                    Generate professional 6-page chapters following ACISS design standards.
                    Ensure XHTML 1.1 compliance and educational content quality.'''
                },
                'quiz_generator': {
                    'model': 'claude-sonnet-4-20250514',
                    'max_tokens': 2000,
                    'temperature': 0.4,
                    'specialty': 'Educational quiz creation',
                    'system_prompt': '''Create exactly 4 multiple choice questions per chapter.
                    Focus on hairstyling professional education and practical application.'''
                },
                'validator': {
                    'model': 'claude-sonnet-4-20250514',
                    'max_tokens': 1500,
                    'temperature': 0.1,
                    'specialty': 'EPUB compliance and quality validation',
                    'system_prompt': '''Validate EPUB content for technical compliance,
                    accessibility standards, and professional presentation quality.'''
                },
                'image_processor': {
                    'model': 'claude-sonnet-4-20250514',
                    'max_tokens': 1000,
                    'temperature': 0.2,
                    'specialty': 'Image optimization and alt text generation',
                    'system_prompt': '''Process images for EPUB optimization and
                    generate professional alt text for accessibility compliance.'''
                }
            },
            'workflows': {
                'chapter_production': {
                    'agents': ['chapter_generator', 'validator'],
                    'parallel': True,
                    'timeout': 300
                },
                'quality_assurance': {
                    'agents': ['validator', 'image_processor'],
                    'parallel': False,
                    'timeout': 600
                }
            }
        }
        
        with open(self.config_dir / "agents.yaml", 'w') as f:
            yaml.dump(agent_config, f, default_flow_style=False, indent=2)
            
    def create_project_config(self):
        """Create project.yaml configuration"""
        project_config = {
            'project': {
                'name': self.project_name,
                'title': 'ACISS - Advanced Certification in Sustainable Styling',
                'author': 'Professional Hairstyling Institute',
                'language': 'en',
                'description': 'Professional certification course in sustainable hairstyling practices'
            },
            'structure': {
                'chapters': 16,
                'front_matter_files': 8,
                'back_matter_files': 17,
                'pages_per_chapter': 6
            },
            'output': {
                'filename': 'ACISS-Hairstyling-Book.epub',
                'directory': 'output',
                'validate': True,
                'optimize': True
            },
            'quality_standards': {
                'epub_version': '3.0',
                'xhtml_version': '1.1',
                'accessibility': 'WCAG-AA',
                'fonts_embedded': True,
                'max_file_size': '50MB'
            }
        }
        
        with open(self.config_dir / "project.yaml", 'w') as f:
            yaml.dump(project_config, f, default_flow_style=False, indent=2)
            
    def create_style_guide(self):
        """Create ACISS style guide configuration"""
        style_guide = {
            'design_system': {
                'name': 'ACISS',
                'colors': {
                    'primary': '#1a1a1a',
                    'accent': '#1797a6',
                    'border': '#b2dfdb',
                    'background_light': '#f9f9f9',
                    'text_muted': '#666'
                },
                'typography': {
                    'body': 'Libre Baskerville',
                    'headings': 'Libre Baskerville',
                    'decorative': 'Cinzel Decorative',
                    'sans_serif': 'Montserrat'
                },
                'components': {
                    'roman_badge': {
                        'background': 'linear-gradient(135deg, #1797a6, #26a69a)',
                        'color': 'white',
                        'size': '6rem x 4rem',
                        'border_radius': '2rem'
                    },
                    'bible_quote': {
                        'background': '#e0f2f1',
                        'border': '2px solid #1797a6',
                        'border_radius': '10px',
                        'padding': '1rem 1.25rem'
                    },
                    'title_stack': {
                        'font_family': 'Cinzel Decorative',
                        'font_size': '1.8rem',
                        'color': '#1797a6',
                        'vertical_bar': '0.25rem width, #222 color'
                    }
                }
            }
        }
        
        with open(self.config_dir / "aciss_style_guide.yaml", 'w') as f:
            yaml.dump(style_guide, f, default_flow_style=False, indent=2)
            
    def create_sample_chapter_data(self):
        """Create sample chapter data file"""
        chapter_data = {
            'chapter': {
                'roman': 'XIII',
                'number': 13,
                'title_lines': [
                    'EMBRACING', 'ETHICS', 'AND', 'SUSTAINABILITY', 'IN', 'HAIRSTYLING'
                ],
                'bible_quote': {
                    'text': "The earth is the Lord's, and everything in it, the world, and all who live in it.",
                    'ref': 'Psalm 24:1'
                },
                'intro': {
                    'label': 'Introduction',
                    'dropcap': 'F',
                    'text': '''eel the salon buzz with energy, each snip and spritz contributing to your client's transformation. But with every cut and color, a new realization dawns—you're not only shaping appearances but also leaving an impact on the world beyond your salon walls.'''
                },
                'content_sections': [
                    {
                        'heading': 'Cultivating Eco-Friendly Salon Environments',
                        'content': '''As awareness grows around environmental impact, hairstylists around the world are stepping up, reshaping their craft to reflect a commitment to ethical and sustainable practices.'''
                    }
                ],
                'learning_objectives': [
                    'Understanding eco-friendly salon practices',
                    'Identifying sustainable equipment options',
                    'Recognizing ethical sourcing principles',
                    'Applying transparency in pricing'
                ],
                'quiz_focus': [
                    'LED lighting vs traditional lighting',
                    'Sustainable pricing transparency',
                    'Biodegradable products usage',
                    'Alliance benefits for sustainability'
                ],
                'worksheet_sections': [
                    {
                        'title': 'Sustainability Commitments',
                        'prompt': 'List steps you will take (energy, waste, sourcing):',
                        'lines': 3
                    },
                    {
                        'title': 'Inclusivity Practices', 
                        'prompt': 'How will you serve all textures with sustainable options?',
                        'lines': 3
                    }
                ],
                'images': {
                    'closing': {
                        'src': 'OEBPS/images/chapter-xiii-quote.jpeg',
                        'alt': 'Chapter XIII inspirational quote about hairstyling ethics',
                        'caption': 'Your hands mold more than hair—they mold aspirations.'
                    }
                }
            }
        }
        
        with open(self.data_dir / "chapters" / "chapter-xiii.yaml", 'w') as f:
            yaml.dump(chapter_data, f, default_flow_style=False, indent=2)

    def create_executable_scripts(self):
        """Create executable agent command scripts"""
        
        # Main agent execution script
        agent_script = '''#!/usr/bin/env python3
"""
EPUB Agent Execution Module
Run specific agent workflows and tasks
"""

import argparse
import sys
from pathlib import Path
import yaml
import os

def load_config(config_file):
    """Load agent configuration"""
    with open(config_file, 'r') as f:
        return yaml.safe_load(f)

def execute_chapter_generation(chapter_num, data_file, output_file):
    """Execute chapter generation workflow"""
    print(f"🔄 Generating Chapter {chapter_num}...")
    
    # Load chapter data
    with open(data_file, 'r') as f:
        chapter_data = yaml.safe_load(f)
    
    # Agent prompt for chapter generation
    prompt = f"""
    Generate complete EPUB Chapter {chapter_num} following ACISS design system:
    
    Chapter Data: {chapter_data}
    
    Requirements:
    - 6 complete pages: Title, Body, Endnotes, Quiz, Worksheet, Closing
    - XHTML 1.1 compliance
    - ACISS styling with Roman numeral badge
    - Professional typography
    - Bible quote in pill container
    - Dropcap first letter
    - 4-question quiz maximum
    - Static worksheet design
    
    Generate complete XHTML file ready for EPUB compilation.
    """
    
    # Here you would call Claude API
    print(f"📝 Prompt prepared for Claude API")
    print(f"💾 Output will be saved to: {output_file}")
    
    return True

def main():
    parser = argparse.ArgumentParser(description='EPUB Agent System')
    parser.add_argument('command', choices=['init', 'generate-chapter', 'validate', 'qa', 'monitor'])
    parser.add_argument('--chapter-number', help='Chapter number (Roman numeral)')
    parser.add_argument('--data-file', help='Chapter data YAML file')
    parser.add_argument('--output', help='Output file path')
    parser.add_argument('--config', default='config/agents.yaml', help='Agent config file')
    
    args = parser.parse_args()
    
    if args.command == 'generate-chapter':
        if not all([args.chapter_number, args.data_file, args.output]):
            print("❌ Missing required arguments for chapter generation")
            sys.exit(1)
            
        execute_chapter_generation(args.chapter_number, args.data_file, args.output)
    
    elif args.command == 'init':
        print("🚀 Initializing EPUB Agent System...")
        # Initialize system
        
    elif args.command == 'validate':
        print("✅ Running validation workflow...")
        # Run validation
        
    elif args.command == 'qa':
        print("🔍 Running quality assurance...")
        # Run QA workflow
        
    elif args.command == 'monitor':
        print("📊 Starting agent monitor...")
        # Start monitoring dashboard

if __name__ == '__main__':
    main()
'''
        
        with open(self.project_dir / "scripts" / "epub_agents.py", 'w') as f:
            f.write(agent_script)
            
        # Make executable
        os.chmod(self.project_dir / "scripts" / "epub_agents.py", 0o755)
        
    def create_env_template(self):
        """Create .env template file"""
        env_template = '''# EPUB Agent System Environment Variables
# Copy this file to .env and fill in your values

# Claude API Configuration
ANTHROPIC_API_KEY=your_api_key_here
CLAUDE_MODEL=claude-sonnet-4-20250514
MAX_TOKENS=4000
TEMPERATURE=0.3

# Project Configuration
PROJECT_NAME=ACISS_Hairstyling_Book
OUTPUT_DIR=./output
STYLE_GUIDE_PATH=./config/aciss_style_guide.yaml

# Agent System Configuration
AGENT_WORKERS=4
MONITOR_PORT=8080
LOG_LEVEL=INFO

# Quality Standards
EPUB_VERSION=3.0
XHTML_VERSION=1.1
ACCESSIBILITY_LEVEL=WCAG-AA
MAX_FILE_SIZE=50MB
'''
        
        with open(self.project_dir / ".env.template", 'w') as f:
            f.write(env_template)
            
    def generate_usage_instructions(self):
        """Generate README with usage instructions"""
        readme_content = '''# EPUB Agent System - Usage Instructions

## Quick Start

### 1. Setup Environment
```bash
# Copy environment template
cp .env.template .env

# Edit .env file with your API keys
nano .env

# Install dependencies
pip install -r requirements.txt
```

### 2. Initialize System
```bash
# Start the agent system
python scripts/epub_agents.py init

# Verify agents are responsive
python scripts/epub_agents.py monitor
```

### 3. Generate Chapter
```bash
# Generate Chapter XIII example
python scripts/epub_agents.py generate-chapter \\
  --chapter-number "XIII" \\
  --data-file "data/chapters/chapter-xiii.yaml" \\
  --output "OEBPS/text/23-Chapter-XIII.xhtml"
```

### 4. Run Quality Assurance
```bash
# Validate generated content
python scripts/epub_agents.py validate \\
  --files "OEBPS/text/*.xhtml"

# Run comprehensive QA
python scripts/epub_agents.py qa \\
  --epub-dir "OEBPS/"
```

## Agent Commands

### Chapter Generation
- `generate-chapter`: Create single chapter with all 6 pages
- `generate-all-chapters`: Batch generate all chapters
- `generate-component`: Create specific chapter components (quiz, worksheet, etc.)

### Validation
- `validate`: Check XHTML/CSS compliance
- `validate-accessibility`: WCAG compliance check
- `validate-consistency`: Style guide compliance

### Workflows
- `workflow chapter-production`: Complete chapter creation pipeline
- `workflow quality-assurance`: Comprehensive QA workflow
- `workflow full-production`: End-to-end EPUB production

### Monitoring
- `monitor`: Real-time agent dashboard
- `status`: Check agent health and performance
- `logs`: View detailed execution logs

## Configuration Files

- `config/agents.yaml`: Agent specializations and settings
- `config/project.yaml`: Project metadata and structure
- `config/aciss_style_guide.yaml`: Design system standards
- `data/chapters/*.yaml`: Chapter content data

## Troubleshooting

### Common Issues
1. **API Key Issues**: Verify ANTHROPIC_API_KEY in .env
2. **Permission Errors**: Check file permissions on scripts
3. **Validation Failures**: Review XHTML structure and CSS

### Debug Mode
```bash
# Run with verbose logging
LOG_LEVEL=DEBUG python scripts/epub_agents.py generate-chapter ...
```

### Agent Recovery
```bash
# Restart failed agents
python scripts/epub_agents.py restart-agent --agent chapter-generator

# Clear cache and retry
python scripts/epub_agents.py clear-cache
```
'''
        
        with open(self.project_dir / "README.md", 'w') as f:
            f.write(readme_content)

def main():
    parser = argparse.ArgumentParser(description='Initialize EPUB Agent System')
    parser.add_argument('--project-name', default='ACISS-Hairstyling-Book', 
                       help='Project name')
    parser.add_argument('--init-all', action='store_true',
                       help='Initialize complete system with all files')
    
    args = parser.parse_args()
    
    system = EPUBAgentSystem(args.project_name)
    
    if args.init_all:
        print("🚀 Initializing Complete EPUB Agent System...")
        system.initialize_project()
        system.create_executable_scripts()
        system.create_env_template()
        system.generate_usage_instructions()
        
        print("✅ Complete EPUB Agent System initialized!")
        print(f"📁 Project location: {system.project_dir}")
        print("\n🔧 Next steps:")
        print("1. cd EPUB_PROJECT")
        print("2. cp .env.template .env")
        print("3. Edit .env with your API keys")
        print("4. python scripts/epub_agents.py init")
        print("5. python scripts/epub_agents.py generate-chapter --chapter-number XIII --data-file data/chapters/chapter-xiii.yaml --output OEBPS/text/23-Chapter-XIII.xhtml")
        
    else:
        system.initialize_project()
        print("✅ Basic project structure created!")
        print("Run with --init-all to create complete system")

if __name__ == '__main__':
    main()
