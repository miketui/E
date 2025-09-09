#!/usr/bin/env python3
"""
EPUB Production Startup Script - Complete AI Agent System for Professional EPUB Creation

This comprehensive startup script initializes a complete EPUB production environment
with AI agents, templates, configuration files, and sample data for immediate use.

Features:
- Project structure initialization
- Agent configuration and templates
- Sample chapter data generation
- Complete CSS and font setup
- Executable scripts and workflows
- Documentation and usage examples
"""

import os
import sys
import json
import yaml
from pathlib import Path
from datetime import datetime
import argparse
import shutil

class EPUBStartupSystem:
    """Complete EPUB production system initialization"""
    
    def __init__(self, project_name: str, base_dir: str = "."):
        self.project_name = project_name
        self.base_dir = Path(base_dir)
        self.project_path = self.base_dir / project_name
        
    def initialize_complete_system(self):
        """Initialize the complete EPUB production system"""
        print(f"🚀 Initializing EPUB Production System: {self.project_name}")
        print("=" * 60)
        
        steps = [
            ("Creating project structure", self.create_project_structure),
            ("Setting up agent configurations", self.setup_agent_configurations),
            ("Creating sample chapter data", self.create_sample_data),
            ("Setting up CSS and fonts", self.setup_css_and_fonts),
            ("Creating executable scripts", self.create_executable_scripts),
            ("Setting up templates", self.setup_templates),
            ("Creating documentation", self.create_documentation),
            ("Setting up environment", self.setup_environment),
        ]
        
        for step_name, step_func in steps:
            print(f"📋 {step_name}...")
            try:
                step_func()
                print(f"   ✅ {step_name} completed")
            except Exception as e:
                print(f"   ❌ {step_name} failed: {e}")
                return False
        
        print("\n🎉 EPUB Production System initialized successfully!")
        self.print_next_steps()
        return True
    
    def create_project_structure(self):
        """Create complete directory structure"""
        directories = [
            "META-INF",
            "OEBPS/text",
            "OEBPS/styles", 
            "OEBPS/images",
            "OEBPS/fonts",
            "scripts",
            "data/chapters",
            "data/front_matter",
            "data/back_matter",
            "config",
            "templates",
            "docs",
            "tools",
            "reports",
            "workflows"
        ]
        
        for dir_path in directories:
            (self.project_path / dir_path).mkdir(parents=True, exist_ok=True)
    
    def setup_agent_configurations(self):
        """Create comprehensive agent configuration files"""
        
        # Main agent configuration
        agent_config = {
            'agents': {
                'chapter': {
                    'model': 'claude-3-sonnet-20240229',
                    'max_tokens': 6000,
                    'temperature': 0.3,
                    'system_prompt': 'specialized chapter generation with ACISS design system'
                },
                'validation': {
                    'model': 'claude-3-sonnet-20240229',
                    'max_tokens': 2000,
                    'temperature': 0.1,
                    'system_prompt': 'EPUB validation and quality assurance'
                },
                'content': {
                    'model': 'claude-3-sonnet-20240229',
                    'max_tokens': 3000,
                    'temperature': 0.2,
                    'system_prompt': 'professional hairstyling content generation'
                },
                'formatter': {
                    'model': 'claude-3-sonnet-20240229',
                    'max_tokens': 4000,
                    'temperature': 0.2,
                    'system_prompt': 'professional formatting and layout'
                }
            },
            'project': {
                'name': self.project_name,
                'output_directory': 'OEBPS/text',
                'validation_enabled': True,
                'max_workers': 4,
                'backup_enabled': True
            },
            'workflows': {
                'chapter_production': {
                    'agents': ['chapter', 'formatter', 'validation'],
                    'parallel': True,
                    'timeout': 300
                },
                'quality_assurance': {
                    'agents': ['validation'],
                    'parallel': False,
                    'timeout': 600
                },
                'batch_generation': {
                    'agents': ['chapter', 'content', 'formatter'],
                    'parallel': True,
                    'timeout': 900
                }
            }
        }
        
        with open(self.project_path / 'config/agents.yaml', 'w') as f:
            yaml.dump(agent_config, f, default_flow_style=False, indent=2)
        
        # Chapters batch configuration
        chapters_config = {
            'chapters': [
                {
                    'number': 'XIII',
                    'title': 'Embracing Ethics and Sustainability in Hairstyling',
                    'data_file': 'data/chapters/chapter-xiii.yaml',
                    'output_file': 'OEBPS/text/23-Chapter-XIII.xhtml'
                },
                {
                    'number': 'XIV',
                    'title': 'The Impact of AI on the Beauty Industry',
                    'data_file': 'data/chapters/chapter-xiv.yaml',
                    'output_file': 'OEBPS/text/25-Chapter-XIV.xhtml'
                },
                {
                    'number': 'XV',
                    'title': 'Cultivating Resilience and Well-being in Hairstyling',
                    'data_file': 'data/chapters/chapter-xv.yaml',
                    'output_file': 'OEBPS/text/26-Chapter-XV.xhtml'
                },
                {
                    'number': 'XVI',
                    'title': 'Tresses and Textures: Embracing Diversity in Hairstyling',
                    'data_file': 'data/chapters/chapter-xvi.yaml',
                    'output_file': 'OEBPS/text/27-Chapter-XVI.xhtml'
                }
            ]
        }
        
        with open(self.project_path / 'config/chapters.yaml', 'w') as f:
            yaml.dump(chapters_config, f, default_flow_style=False, indent=2)
    
    def create_sample_data(self):
        """Create sample chapter data files"""
        
        sample_chapters = {
            'chapter-xiii': {
                'roman': 'XIII',
                'title': 'Embracing Ethics and Sustainability in Hairstyling',
                'title_lines': [
                    'EMBRACING ETHICS',
                    'AND SUSTAINABILITY',
                    'IN HAIRSTYLING'
                ],
                'bible_quote': 'And God saw every thing that he had made, and, behold, it was very good.',
                'bible_reference': 'Genesis 1:31',
                'introduction': 'In our ever-evolving beauty industry, the conscious stylist recognizes that true artistry extends beyond the chair to encompass our responsibility to the planet and our communities.',
                'content': '''
                <h2>The Foundation of Ethical Practice</h2>
                <p>Sustainable hairstyling begins with understanding our environmental impact. Every product choice, every technique we employ, and every business decision we make ripples through our community and beyond.</p>
                
                <h3>Eco-Conscious Product Selection</h3>
                <p>Modern hairstylists have unprecedented access to environmentally responsible products. From ammonia-free color formulations to biodegradable styling products, the choices we make directly influence our carbon footprint.</p>
                
                <blockquote>
                "Sustainability in beauty is not just a trend—it's a responsibility we owe to future generations of stylists and clients alike."
                </blockquote>
                
                <h3>Waste Reduction Strategies</h3>
                <p>Implementing zero-waste practices in the salon environment demonstrates environmental stewardship while often reducing operational costs.</p>
                ''',
                'endnotes': [
                    'Environmental Protection Agency. "Green Chemistry in Cosmetics." EPA Publication 2024.',
                    'Sustainable Beauty Coalition. "Best Practices for Eco-Friendly Salons." Industry Report 2024.',
                    'Journal of Environmental Cosmetology. "Reducing Chemical Waste in Professional Settings." Vol. 15, 2024.'
                ],
                'quiz_questions': [
                    {
                        'question': 'Which of the following best describes sustainable hairstyling practices?',
                        'options': [
                            'A) Using only the most expensive products',
                            'B) Minimizing environmental impact through conscious choices',
                            'C) Avoiding all chemical treatments',
                            'D) Working only with organic hair types'
                        ]
                    },
                    {
                        'question': 'What is the primary benefit of ammonia-free color formulations?',
                        'options': [
                            'A) They cost less than traditional formulas',
                            'B) They provide better color coverage',
                            'C) They reduce environmental and health impact',
                            'D) They work faster than conventional colors'
                        ]
                    },
                    {
                        'question': 'Zero-waste salon practices primarily benefit:',
                        'options': [
                            'A) Only the salon\'s profit margins',
                            'B) The environment and often reduce costs',
                            'C) Client satisfaction exclusively',
                            'D) Marketing opportunities only'
                        ]
                    },
                    {
                        'question': 'Environmental stewardship in hairstyling includes:',
                        'options': [
                            'A) Product selection and waste management',
                            'B) Only using natural hair colors',
                            'C) Avoiding all chemical processes',
                            'D) Working exclusively outdoors'
                        ]
                    }
                ],
                'worksheet': {
                    'title': 'Sustainability Action Plan',
                    'sections': [
                        {
                            'heading': 'Current Practice Assessment',
                            'content': 'Evaluate your current environmental practices and identify areas for improvement.'
                        },
                        {
                            'heading': 'Product Audit',
                            'content': 'List three products you currently use and research sustainable alternatives.'
                        },
                        {
                            'heading': 'Waste Reduction Goals',
                            'content': 'Set specific, measurable goals for reducing waste in your practice.'
                        }
                    ]
                },
                'closing_image': '../images/chapter-xiii-sustainability.jpg',
                'closing_caption': 'Sustainable beauty practices create ripples of positive change throughout our industry and beyond.'
            },
            'chapter-xiv': {
                'roman': 'XIV',
                'title': 'The Impact of AI on the Beauty Industry',
                'title_lines': [
                    'THE IMPACT OF AI',
                    'ON THE BEAUTY',
                    'INDUSTRY'
                ],
                'bible_quote': 'For I know the thoughts that I think toward you, says the Lord, thoughts of peace and not of evil, to give you an expected end.',
                'bible_reference': 'Jeremiah 29:11',
                'introduction': 'As artificial intelligence reshapes our world, forward-thinking stylists embrace technology as a tool to enhance creativity and client experience while maintaining the human artistry at the heart of our craft.',
                'content': '''
                <h2>AI as Creative Collaborator</h2>
                <p>Modern AI tools serve as sophisticated assistants, helping stylists visualize potential outcomes, analyze hair characteristics, and suggest personalized treatments based on comprehensive data analysis.</p>
                
                <h3>Virtual Consultation Technology</h3>
                <p>AI-powered consultation platforms allow stylists to offer preliminary assessments and style recommendations before clients even enter the salon, streamlining the consultation process and enhancing client satisfaction.</p>
                
                <blockquote>
                "Technology amplifies human creativity—it doesn't replace it. The skilled stylist remains irreplaceable in delivering personalized artistry."
                </blockquote>
                
                <h3>Predictive Analytics for Hair Health</h3>
                <p>Advanced algorithms can analyze hair condition, predict treatment outcomes, and recommend maintenance schedules, enabling more precise and effective hair care protocols.</p>
                ''',
                'endnotes': [
                    'Technology in Beauty Review. "AI Applications in Professional Hairstyling." Q4 2024.',
                    'Digital Salon Management. "Implementing AI Tools for Client Success." Industry Analysis 2024.',
                    'Future of Beauty Technology. "Predictive Analytics in Hair Care." Research Report 2024.'
                ],
                'quiz_questions': [
                    {
                        'question': 'How does AI primarily benefit professional hairstylists?',
                        'options': [
                            'A) By replacing the need for human creativity',
                            'B) By enhancing consultation and analysis capabilities',
                            'C) By eliminating the need for product knowledge',
                            'D) By automating all styling techniques'
                        ]
                    },
                    {
                        'question': 'Virtual consultation technology helps stylists by:',
                        'options': [
                            'A) Completely replacing in-person consultations',
                            'B) Streamlining preliminary assessments and recommendations',
                            'C) Eliminating the need for client communication',
                            'D) Providing automatic styling services'
                        ]
                    },
                    {
                        'question': 'Predictive analytics in hair care can:',
                        'options': [
                            'A) Guarantee perfect results every time',
                            'B) Analyze condition and predict treatment outcomes',
                            'C) Replace professional training requirements',
                            'D) Eliminate the need for follow-up appointments'
                        ]
                    },
                    {
                        'question': 'The relationship between AI and human creativity in hairstyling is best described as:',
                        'options': [
                            'A) Competitive replacement',
                            'B) Collaborative enhancement',
                            'C) Completely separate domains',
                            'D) Temporary technological phase'
                        ]
                    }
                ],
                'worksheet': {
                    'title': 'Technology Integration Plan',
                    'sections': [
                        {
                            'heading': 'Current Technology Use',
                            'content': 'Assess your current use of technology in client consultations and service delivery.'
                        },
                        {
                            'heading': 'AI Tool Research',
                            'content': 'Research three AI tools that could enhance your practice and evaluate their potential benefits.'
                        },
                        {
                            'heading': 'Implementation Strategy',
                            'content': 'Develop a plan for gradually incorporating technology while maintaining personal client connections.'
                        }
                    ]
                },
                'closing_image': '../images/chapter-xiv-ai-beauty.jpg',
                'closing_caption': 'Technology and artistry unite to create unprecedented possibilities in modern hairstyling.'
            }
        }
        
        for chapter_id, chapter_data in sample_chapters.items():
            with open(self.project_path / f'data/chapters/{chapter_id}.yaml', 'w') as f:
                yaml.dump(chapter_data, f, default_flow_style=False, indent=2)
    
    def setup_css_and_fonts(self):
        """Create complete CSS and font setup"""
        
        # Main stylesheet
        main_css = '''/* ACISS EPUB Stylesheet - Professional Hairstyling Book */

/* CSS Variables */
:root {
  --primary-color: #1a1a1a;
  --secondary-color: #333;
  --accent-color: #1797a6;
  --border-color: #b2dfdb;
  --background-light: #f9f9f9;
  --background-worksheet: #fafafa;
  --text-muted: #666;
  --white: #fff;
  --page-max-width: 35em;
  --page-padding: 2rem;
}

/* Base Styles */
html, body {
  margin: 0;
  padding: 0;
}

body {
  font-family: "Libre Baskerville", Georgia, serif;
  line-height: 1.6;
  color: var(--primary-color);
  background: #fff;
  margin: 0 auto;
  max-width: var(--page-max-width);
  padding: var(--page-padding);
}

/* Typography */
h1, h2, h3, h4 {
  font-family: "Libre Baskerville", Georgia, serif;
  color: var(--primary-color);
  line-height: 1.2;
  text-align: center;
}

h1 {
  font-size: 2.2rem;
  text-transform: uppercase;
  letter-spacing: .05em;
  margin: 2rem 0 1rem;
}

h2 {
  font-size: 1.6rem;
  margin: 1.5rem 0 1rem;
  color: var(--accent-color);
  border-bottom: 3px solid var(--border-color);
  padding-bottom: .35rem;
  text-align: left;
}

h3 {
  font-size: 1.25rem;
  margin: 1.2rem 0 .8rem;
  text-align: left;
  color: var(--accent-color);
}

p {
  margin: 0 0 1em;
  text-align: justify;
}

/* Chapter Title Page */
.chap-title {
  background: var(--background-light);
  padding: 2rem;
  page-break-after: always;
}

.chapter-number-container {
  display: flex;
  justify-content: center;
  margin: 1rem 0 2rem;
}

.roman-badge {
  width: 6rem;
  height: 4rem;
  border-radius: 2rem;
  background: linear-gradient(135deg, #1797a6, #26a69a);
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 12px rgba(23, 151, 166, .35);
}

.roman-badge span {
  font-family: "Cinzel Decorative", serif;
  font-size: 2rem;
  color: #fff;
  text-shadow: 0 1px 2px rgba(0, 0, 0, .35);
}

.title-stack {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  margin: 1rem 0 2rem;
}

.title-bar {
  width: .25rem;
  background: #222;
  min-height: 14rem;
}

.title-lines {
  display: flex;
  flex-direction: column;
  gap: .15rem;
}

.title-line {
  font-family: "Cinzel Decorative", serif;
  font-size: 1.8rem;
  letter-spacing: .05em;
  color: var(--accent-color);
  text-align: left;
}

.bible-quote-container {
  background: #e0f2f1;
  border: 2px solid var(--accent-color);
  border-radius: 10px;
  padding: 1rem 1.25rem;
  margin: 1.5rem auto;
  max-width: 85%;
  text-align: center;
  box-shadow: 0 2px 8px rgba(23, 151, 166, .15);
}

.bible-quote-text {
  font-style: italic;
}

.introduction-heading {
  text-transform: uppercase;
  font-weight: 700;
  letter-spacing: .08em;
  margin: 1.5rem 0 .5rem;
  color: #555;
}

.dropcap-first-letter::first-letter {
  float: left;
  font-family: "Libre Baskerville", serif;
  font-weight: 700;
  font-size: 3.2rem;
  line-height: .9;
  margin: .1em .3em 0 0;
  color: var(--accent-color);
  background: rgba(23, 151, 166, .1);
  padding: .1em .25em;
  border-radius: .3em;
}

/* Chapter Body */
.chap-body {
  page-break-before: always;
}

blockquote {
  margin: 1.5rem 0;
  padding: 1rem 1.25rem;
  border-left: 4px solid var(--accent-color);
  background: var(--background-light);
  font-style: italic;
}

/* Endnotes */
.endnotes {
  margin-top: 2rem;
  padding-top: 1.25rem;
  border-top: 2px solid var(--border-color);
}

.endnotes-title {
  color: var(--accent-color);
  text-align: left;
}

.endnotes ol {
  padding-left: 1.2rem;
}

.endnotes li {
  margin: .6rem 0;
  color: #444;
}

/* Quiz */
.quiz-container {
  margin: 1.5rem 0;
  padding: 1.25rem;
  border: 2px solid var(--border-color);
  border-radius: 10px;
  background: #f8fffe;
}

.quiz-title {
  text-align: center;
  color: var(--accent-color);
  margin-bottom: .5rem;
}

.quiz-questions {
  list-style: none;
  padding: 0;
}

.quiz-q {
  background: #fff;
  border: 1px solid #e0f2f1;
  border-radius: 8px;
  padding: .9rem;
  margin: 0 0 1rem;
}

.quiz-opt {
  display: flex;
  gap: .5rem;
  align-items: flex-start;
}

/* Worksheet */
.worksheet {
  background: var(--background-worksheet);
  border: 2px solid var(--border-color);
  border-radius: 10px;
  padding: 1.25rem;
  margin: 1.5rem 0;
}

.ws-row {
  margin: .8rem 0;
}

.ws-label {
  font-weight: 700;
  color: #0d7480;
  margin: .25rem 0;
}

.ws-line {
  display: block;
  border-bottom: 1px solid #bbb;
  height: 1.8rem;
  margin: .4rem 0;
}

/* Closing Image */
.closing {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
  min-height: 60vh;
  justify-content: center;
  padding: 1.5rem;
}

.closing figure {
  max-width: 90%;
  margin: 0;
}

.closing img {
  max-width: 100%;
  height: auto;
  border-radius: 10px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, .15);
}

.closing figcaption {
  font-family: "Montserrat", sans-serif;
  font-size: .9rem;
  color: #666;
  text-align: center;
  margin-top: .5rem;
}

/* Page Breaks */
.page-break {
  page-break-before: always;
  height: 0;
  visibility: hidden;
}

/* Front Matter Two-Column Layout */
.front-matter-container {
  max-width: 100%;
  margin: 0 auto;
  padding: 2rem;
}

.two-column-layout {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
  align-items: start;
}

@media screen and (max-width: 768px) {
  .two-column-layout {
    grid-template-columns: 1fr;
    gap: 1rem;
  }
  
  body {
    padding: 1rem;
  }
  
  .title-line {
    font-size: 1.4rem;
  }
  
  .roman-badge {
    width: 5rem;
    height: 3.5rem;
  }
  
  .roman-badge span {
    font-size: 1.6rem;
  }
}

.column-left, .column-right {
  width: 100%;
}

/* Utility Classes */
.text-center { text-align: center; }
.text-left { text-align: left; }
.text-right { text-align: right; }
.mt-1 { margin-top: 1rem; }
.mt-2 { margin-top: 2rem; }
.mb-1 { margin-bottom: 1rem; }
.mb-2 { margin-bottom: 2rem; }'''
        
        with open(self.project_path / 'OEBPS/styles/style.css', 'w') as f:
            f.write(main_css)
        
        # Font CSS
        fonts_css = '''/* Font Definitions for ACISS EPUB */

@font-face {
  font-family: "Libre Baskerville";
  src: url("../fonts/librebaskerville-regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: "Libre Baskerville";
  src: url("../fonts/librebaskerville-bold.woff2") format("woff2");
  font-weight: 700;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: "Libre Baskerville";
  src: url("../fonts/librebaskerville-italic.woff2") format("woff2");
  font-weight: 400;
  font-style: italic;
  font-display: swap;
}

@font-face {
  font-family: "Cinzel Decorative";
  src: url("../fonts/CinzelDecorative.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: "Montserrat";
  src: url("../fonts/Montserrat-Regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: "Montserrat";
  src: url("../fonts/Montserrat-Bold.woff2") format("woff2");
  font-weight: 700;
  font-style: normal;
  font-display: swap;
}'''
        
        with open(self.project_path / 'OEBPS/styles/fonts.css', 'w') as f:
            f.write(fonts_css)
    
    def create_executable_scripts(self):
        """Create additional executable scripts and tools"""
        
        # Copy the main agent script from the current directory
        current_dir = Path(__file__).parent
        main_script_source = current_dir / 'scripts' / 'epub_agents.py'
        
        if main_script_source.exists():
            # Copy the main script
            shutil.copy2(main_script_source, self.project_path / 'scripts' / 'epub_agents.py')
            os.chmod(self.project_path / 'scripts' / 'epub_agents.py', 0o755)
        else:
            # Create a simplified version if source not available
            main_script_content = '''#!/usr/bin/env python3
"""
EPUB Agents - Simplified version for standalone projects
"""

print("EPUB Agents system - please install full version from repository")
print("This is a minimal demonstration version.")

import sys
import os
import argparse

def main():
    parser = argparse.ArgumentParser(description='EPUB Agents - Simplified Version')
    parser.add_argument('command', choices=['health-check', 'init'], help='Available commands')
    args = parser.parse_args()
    
    if args.command == 'health-check':
        print("🏥 EPUB Agents Health Check (Simplified Version)")
        print("⚠️  This is a demonstration version")
        print("Please install the full system from the repository")
    elif args.command == 'init':
        print("Initialize command not available in simplified version")

if __name__ == '__main__':
    main()
'''
            
            with open(self.project_path / 'scripts/epub_agents.py', 'w') as f:
                f.write(main_script_content)
            
            os.chmod(self.project_path / 'scripts/epub_agents.py', 0o755)
        
        # Batch workflow script
        batch_script = '''#!/usr/bin/env python3
"""
Batch EPUB Generation Workflow
Generates all chapters and validates the complete EPUB.
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(cmd):
    """Run a command and return success status"""
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ Command succeeded: {cmd}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Command failed: {cmd}")
        print(f"Error: {e.stderr}")
        return False

def main():
    """Run complete batch workflow"""
    print("🚀 Starting EPUB Batch Generation Workflow")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists('config/chapters.yaml'):
        print("❌ Please run this script from the project root directory")
        sys.exit(1)
    
    # Generate all chapters
    print("📚 Generating chapters...")
    success = run_command("python scripts/epub_agents.py batch-generate --chapters-config config/chapters.yaml")
    
    if not success:
        print("❌ Chapter generation failed")
        sys.exit(1)
    
    # Validate all files
    print("🔍 Validating EPUB files...")
    success = run_command("python scripts/epub_agents.py validate --directory OEBPS/text --output reports/validation_report.json")
    
    if success:
        print("✅ Batch workflow completed successfully!")
        print("📊 Check reports/validation_report.json for detailed results")
    else:
        print("⚠️  Validation completed with warnings - check the report")

if __name__ == '__main__':
    main()
'''
        
        with open(self.project_path / 'scripts/batch_workflow.py', 'w') as f:
            f.write(batch_script)
        
        os.chmod(self.project_path / 'scripts/batch_workflow.py', 0o755)
    
    def setup_templates(self):
        """Create chapter and content templates"""
        
        chapter_template = '''<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
  <meta charset="utf-8"/>
  <title>Chapter {{roman}} - {{title}}</title>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <link rel="stylesheet" type="text/css" href="../styles/fonts.css"/>
  <link rel="stylesheet" type="text/css" href="../styles/style.css"/>
</head>
<body class="chapter-page">
  
  <!-- TITLE PAGE -->
  <div class="chap-title">
    <div class="chapter-number-container">
      <div class="roman-badge"><span>{{roman}}</span></div>
    </div>
    <div class="chapter-title-container">
      <div class="title-stack">
        <div class="title-bar"></div>
        <div class="title-lines">
          {% for line in title_lines %}
          <div class="title-line">{{line}}</div>
          {% endfor %}
        </div>
      </div>
    </div>
    <div class="bible-quote-container">
      <div class="bible-quote-text">{{bible_quote}}</div>
      <div class="bible-quote-reference">{{bible_reference}}</div>
    </div>
    <div class="introduction-heading">Introduction</div>
    <p class="dropcap-first-letter">{{introduction}}</p>
  </div>
  
  <!-- PAGE BREAK -->
  <div class="page-break"></div>
  
  <!-- BODY CONTENT -->
  <div class="chap-body">
    {{content}}
  </div>
  
  <!-- PAGE BREAK -->
  <div class="page-break"></div>
  
  <!-- ENDNOTES -->
  <div class="chap-body">
    <div class="endnotes">
      <h2 class="endnotes-title">Endnotes</h2>
      <ol>
        {% for note in endnotes %}
        <li>{{note}}</li>
        {% endfor %}
      </ol>
    </div>
  </div>
  
  <!-- PAGE BREAK -->
  <div class="page-break"></div>
  
  <!-- QUIZ -->
  <div class="chap-body">
    <div class="quiz-container">
      <h2 class="quiz-title">Chapter Quiz</h2>
      <p class="text-center">Choose the single best answer</p>
      <ol class="quiz-questions">
        {% for question in quiz_questions %}
        <li class="quiz-q">
          <div class="quiz-question">{{question.question}}</div>
          {% for option in question.options %}
          <div class="quiz-opt">{{option}}</div>
          {% endfor %}
        </li>
        {% endfor %}
      </ol>
    </div>
  </div>
  
  <!-- PAGE BREAK -->
  <div class="page-break"></div>
  
  <!-- WORKSHEET -->
  <div class="chap-body">
    <div class="worksheet">
      <h2 class="text-center">{{worksheet.title}}</h2>
      {% for section in worksheet.sections %}
      <div class="ws-row">
        <div class="ws-label">{{section.heading}}</div>
        <p>{{section.content}}</p>
        <span class="ws-line"></span>
      </div>
      {% endfor %}
    </div>
  </div>
  
  <!-- PAGE BREAK -->
  <div class="page-break"></div>
  
  <!-- CLOSING IMAGE -->
  <div class="chap-body">
    <div class="closing">
      <figure>
        <img src="{{closing_image}}" alt="{{closing_caption}}"/>
        <figcaption>{{closing_caption}}</figcaption>
      </figure>
    </div>
  </div>
  
</body>
</html>'''
        
        with open(self.project_path / 'templates/chapter_template.xhtml', 'w') as f:
            f.write(chapter_template)
    
    def create_documentation(self):
        """Create comprehensive documentation"""
        
        readme_content = f'''# {self.project_name} - EPUB Production System

## Overview
This is a complete AI-powered EPUB production system for creating professional-quality ebooks using specialized agents.

## Quick Start

### 1. Environment Setup
```bash
# Copy environment template
cp .env.template .env

# Edit .env and add your Anthropic API key
# ANTHROPIC_API_KEY=your-api-key-here
```

### 2. Install Dependencies
```bash
pip install anthropic pyyaml
```

### 3. Generate a Chapter
```bash
# Generate single chapter
python scripts/epub_agents.py generate-chapter \\
  --chapter-number "XIII" \\
  --data-file "data/chapters/chapter-xiii.yaml" \\
  --output "OEBPS/text/23-Chapter-XIII.xhtml"
```

### 4. Batch Generation
```bash
# Generate all chapters
python scripts/batch_workflow.py
```

### 5. Validation
```bash
# Validate all EPUB files
python scripts/epub_agents.py validate --directory OEBPS/text
```

## Available Commands

### Initialize New Project
```bash
python scripts/epub_agents.py init --project-name "My-EPUB-Book"
```

### Generate Single Chapter
```bash
python scripts/epub_agents.py generate-chapter \\
  --chapter-number "XIV" \\
  --data-file "data/chapters/chapter-xiv.yaml" \\
  --output "OEBPS/text/25-Chapter-XIV.xhtml"
```

### Interactive Agent Chat
```bash
# Chat with chapter generation agent
python scripts/epub_agents.py chat --agent chapter

# Chat with validation agent
python scripts/epub_agents.py chat --agent validation
```

### System Health Check
```bash
python scripts/epub_agents.py health-check
```

## Project Structure

```
{self.project_name}/
├── META-INF/                  # EPUB metadata
├── OEBPS/                     # EPUB content
│   ├── text/                  # XHTML files
│   ├── styles/                # CSS files
│   ├── images/                # Images
│   └── fonts/                 # Embedded fonts
├── scripts/                   # Executable scripts
├── data/                      # Chapter and content data
├── config/                    # Configuration files
├── templates/                 # XHTML templates
├── docs/                      # Documentation
└── reports/                   # Validation reports
```

## Agent Capabilities

### Chapter Agent
- Generates complete 6-page chapter structure
- Applies ACISS design system
- Ensures XHTML 1.1 compliance
- Creates professional typography

### Validation Agent
- EPUB standards compliance checking
- Accessibility validation
- Cross-device compatibility
- Professional quality assurance

### Content Agent
- Front/back matter generation
- Professional hairstyling content
- Educational material design
- Quiz and worksheet creation

### Formatter Agent
- Professional layout application
- Typography consistency
- Responsive design implementation
- Brand guideline compliance

## Configuration

Edit `config/agents.yaml` to customize:
- Agent models and parameters
- Workflow configurations
- Project settings
- Validation rules

## Support

For issues or questions:
1. Check the health status: `python scripts/epub_agents.py health-check`
2. Review validation reports in `reports/`
3. Consult the agent documentation in `docs/`

## Next Steps

1. Customize chapter data in `data/chapters/`
2. Modify CSS styles in `OEBPS/styles/`
3. Add images to `OEBPS/images/`
4. Run batch generation workflow
5. Validate and review outputs
'''
        
        with open(self.project_path / 'README.md', 'w') as f:
            f.write(readme_content)
        
        # Usage guide
        usage_guide = '''# EPUB Agents Usage Guide

## Complete Workflow Examples

### Example 1: Generate Chapter XIII
```bash
# Generate Chapter XIII using provided sample data
python scripts/epub_agents.py generate-chapter \\
  --chapter-number "XIII" \\
  --data-file "data/chapters/chapter-xiii.yaml" \\
  --output "OEBPS/text/23-Chapter-XIII.xhtml"
```

### Example 2: Custom Chapter Data
Create your own chapter data file:

```yaml
# data/chapters/my-chapter.yaml
roman: 'XV'
title: 'My Custom Chapter'
title_lines:
  - 'MY CUSTOM'
  - 'CHAPTER TITLE'
bible_quote: 'Your inspirational quote here'
bible_reference: 'Source Reference'
introduction: 'Chapter introduction paragraph...'
content: |
  <h2>Section Title</h2>
  <p>Your content here...</p>
# ... additional fields
```

Then generate:
```bash
python scripts/epub_agents.py generate-chapter \\
  --chapter-number "XV" \\
  --data-file "data/chapters/my-chapter.yaml" \\
  --output "OEBPS/text/my-chapter.xhtml"
```

### Example 3: Interactive Agent Usage
```bash
# Start interactive session with chapter agent
python scripts/epub_agents.py chat --agent chapter

# Example prompts to try:
# "Generate a quiz question about sustainable hairstyling"
# "Create endnotes for a chapter on business ethics"
# "Suggest improvements for this chapter title"
```

### Example 4: Validation Workflow
```bash
# Validate single file
python scripts/epub_agents.py validate --directory OEBPS/text

# Save detailed report
python scripts/epub_agents.py validate \\
  --directory OEBPS/text \\
  --output reports/detailed_validation.json
```

## Pro Tips

1. **Batch Processing**: Use `scripts/batch_workflow.py` for multiple chapters
2. **Validation**: Always run validation after generation
3. **Templates**: Customize templates in `templates/` directory
4. **Backup**: Keep backups of your chapter data files
5. **Testing**: Use health-check regularly to ensure system integrity

## Troubleshooting

### Common Issues

**Issue**: "Anthropic API key not found"
**Solution**: Set ANTHROPIC_API_KEY in your .env file

**Issue**: "Module not found: anthropic"
**Solution**: Install dependencies: `pip install anthropic pyyaml`

**Issue**: "Permission denied"
**Solution**: Make scripts executable: `chmod +x scripts/*.py`

**Issue**: "Validation errors"
**Solution**: Check validation report and fix issues in source data
'''
        
        with open(self.project_path / 'docs/usage_guide.md', 'w') as f:
            f.write(usage_guide)
    
    def setup_environment(self):
        """Create environment and configuration files"""
        
        # Environment template
        env_content = f'''# EPUB Agents Configuration
ANTHROPIC_API_KEY=your-api-key-here

# Project Settings
PROJECT_NAME={self.project_name}
OUTPUT_DIR=OEBPS/text
VALIDATION_ENABLED=true
MAX_WORKERS=4

# Agent Settings
DEFAULT_MODEL=claude-3-sonnet-20240229
DEFAULT_MAX_TOKENS=4000
DEFAULT_TEMPERATURE=0.3

# Development Settings
DEBUG_MODE=false
VERBOSE_LOGGING=false
'''
        
        with open(self.project_path / '.env.template', 'w') as f:
            f.write(env_content)
        
        # Makefile for convenience
        makefile_content = '''# EPUB Production Makefile

.PHONY: help install setup generate validate clean

help:
	@echo "EPUB Production System Commands:"
	@echo "  install    - Install Python dependencies"
	@echo "  setup      - Setup environment (copy .env template)"
	@echo "  generate   - Generate sample chapters"
	@echo "  validate   - Validate all EPUB files"
	@echo "  health     - Check system health"
	@echo "  clean      - Clean generated files"

install:
	pip install anthropic pyyaml

setup:
	@if [ ! -f .env ]; then \\
		cp .env.template .env; \\
		echo "✅ Created .env file - please add your Anthropic API key"; \\
	else \\
		echo "⚠️  .env file already exists"; \\
	fi

generate:
	python scripts/batch_workflow.py

validate:
	python scripts/epub_agents.py validate --directory OEBPS/text --output reports/validation.json

health:
	python scripts/epub_agents.py health-check

clean:
	rm -rf OEBPS/text/*.xhtml
	rm -rf reports/*.json
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete

# Quick commands
chapter-xiii:
	python scripts/epub_agents.py generate-chapter \\
		--chapter-number "XIII" \\
		--data-file "data/chapters/chapter-xiii.yaml" \\
		--output "OEBPS/text/23-Chapter-XIII.xhtml"

chapter-xiv:
	python scripts/epub_agents.py generate-chapter \\
		--chapter-number "XIV" \\
		--data-file "data/chapters/chapter-xiv.yaml" \\
		--output "OEBPS/text/25-Chapter-XIV.xhtml"

chat-chapter:
	python scripts/epub_agents.py chat --agent chapter

chat-validation:
	python scripts/epub_agents.py chat --agent validation
'''
        
        with open(self.project_path / 'Makefile', 'w') as f:
            f.write(makefile_content)
        
        # .gitignore
        gitignore_content = '''.env
*.pyc
__pycache__/
*.log
reports/*.json
.DS_Store
*.tmp
*.bak
dist/
build/
'''
        
        with open(self.project_path / '.gitignore', 'w') as f:
            f.write(gitignore_content)
    
    def print_next_steps(self):
        """Print detailed next steps for the user"""
        print("\n" + "="*60)
        print("🎯 NEXT STEPS - Your EPUB Production System is Ready!")
        print("="*60)
        
        print(f"\n📂 Navigate to your project:")
        print(f"   cd {self.project_name}")
        
        print(f"\n🔧 Setup your environment:")
        print(f"   1. Copy environment template: cp .env.template .env")
        print(f"   2. Edit .env and add your Anthropic API key")
        print(f"   3. Install dependencies: pip install anthropic pyyaml")
        
        print(f"\n🚀 Generate your first chapter:")
        print(f"   python scripts/epub_agents.py generate-chapter \\")
        print(f"     --chapter-number 'XIII' \\")
        print(f"     --data-file 'data/chapters/chapter-xiii.yaml' \\")
        print(f"     --output 'OEBPS/text/23-Chapter-XIII.xhtml'")
        
        print(f"\n⚡ Quick commands with Make:")
        print(f"   make setup      # Setup environment")
        print(f"   make generate   # Generate all chapters")
        print(f"   make validate   # Validate EPUB files")
        print(f"   make health     # System health check")
        
        print(f"\n💬 Interactive agent chat:")
        print(f"   python scripts/epub_agents.py chat --agent chapter")
        print(f"   python scripts/epub_agents.py chat --agent validation")
        
        print(f"\n📚 Available sample chapters:")
        print(f"   - Chapter XIII: Ethics and Sustainability")
        print(f"   - Chapter XIV: AI in Beauty Industry")
        
        print(f"\n🔍 System validation:")
        print(f"   python scripts/epub_agents.py health-check")
        
        print(f"\n📖 Documentation:")
        print(f"   - README.md: Complete usage guide")
        print(f"   - docs/usage_guide.md: Detailed examples")
        print(f"   - config/agents.yaml: Agent configuration")
        
        print(f"\n✨ You're ready to create professional EPUBs with AI!")

def main():
    parser = argparse.ArgumentParser(description='EPUB Production System Startup Script')
    parser.add_argument('--project-name', required=True, help='Name of the EPUB project')
    parser.add_argument('--base-dir', default='.', help='Base directory for project')
    parser.add_argument('--init-all', action='store_true', help='Initialize complete system')
    
    args = parser.parse_args()
    
    startup = EPUBStartupSystem(args.project_name, args.base_dir)
    
    if args.init_all:
        success = startup.initialize_complete_system()
        sys.exit(0 if success else 1)
    else:
        startup.initialize_complete_system()

if __name__ == '__main__':
    main()