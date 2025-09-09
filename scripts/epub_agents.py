#!/usr/bin/env python3
"""
EPUB Agents - Comprehensive AI Agent System for Professional EPUB Production

This module provides executable commands for EPUB production using specialized AI agents.
Each agent has specific expertise and responsibilities for professional, bestseller-quality output.
"""

import os
import sys
import yaml
import json
import argparse
import asyncio
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Check for anthropic dependency
try:
    import anthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False
    logger.warning("Anthropic library not available. Install with: pip install anthropic")

# Agent System Prompts
CHAPTER_AGENT_SYSTEM_PROMPT = """
You are a specialized EPUB Chapter Generation Agent for the ACISS hairstyling certification book.

RESPONSIBILITIES:
- Generate professional XHTML chapters following the exact 6-page structure
- Apply ACISS design system consistently
- Ensure XHTML 1.1 compliance
- Create engaging, educational content for professional hairstylists

CHAPTER STRUCTURE (6 pages exactly):
1. Title Page: Roman numeral badge + vertical title stack + bible quote + introduction
2. Body Content: Main chapter content with proper styling and structure
3. Endnotes: Numbered references and citations
4. Quiz: Exactly 4 multiple choice questions maximum
5. Worksheet: Interactive elements (static for EPUB)
6. Closing Image: Chapter conclusion with inspirational image and caption

ACISS DESIGN SYSTEM:
- Primary Color: #1a1a1a
- Accent Color: #1797a6  
- Typography: Libre Baskerville (body), Cinzel Decorative (headers), Montserrat (sans)
- Roman numerals: Centered badges with gradient background
- Bible quotes: Pill-shaped containers with accent borders
- Professional spacing: 2rem standard padding

OUTPUT FORMAT:
Always provide complete XHTML with proper DOCTYPE, namespace, head section, and all required CSS class references.
"""

VALIDATION_AGENT_PROMPT = """
You are an EPUB Validation Agent specializing in professional publishing standards.

VALIDATION AREAS:
- XHTML 1.1 compliance and structure
- CSS validity and cross-device compatibility  
- Image references and accessibility
- Typography consistency
- Professional formatting standards
- WCAG 2.1 accessibility compliance

CHECKING PROTOCOL:
1. Validate DOCTYPE and namespace declarations
2. Check HTML structure and nesting
3. Verify CSS class usage and consistency
4. Validate image paths and alt text
5. Ensure accessibility features
6. Check typography scale and consistency
7. Verify professional presentation standards

RESPONSE FORMAT:
Provide specific, actionable feedback with exact line numbers and corrections needed.
"""

CONTENT_AGENT_PROMPT = """
You are a Content Generation Agent specializing in professional hairstyling education content.

EXPERTISE:
- Professional hairstyling techniques and industry standards
- Business development for beauty professionals
- Educational content design and learning objectives
- Professional terminology and best practices

CONTENT TYPES:
- Front matter (two-column professional layouts)
- Chapter content (educational and engaging)
- Back matter (resources and references)
- Quiz questions (professional context, 4 max per chapter)
- Worksheets (practical applications, static design)

QUALITY STANDARDS:
- Professional tone appropriate for certification material
- Accurate technical information
- Engaging educational content
- Clear learning objectives
- Practical applications and real-world examples
"""

FORMATTER_AGENT_PROMPT = """
You are a Professional Formatting Agent for EPUB production.

FORMATTING RESPONSIBILITIES:
- Apply consistent typography scales
- Ensure professional layout and spacing
- Implement responsive design principles
- Maintain ACISS brand consistency
- Optimize for all device types

LAYOUT SPECIFICATIONS:
- Single page layouts for front/back matter
- Six-page structure for chapters
- Two-column layouts where appropriate
- Professional spacing and alignment
- Consistent CSS class application

TYPOGRAPHY RULES:
- Libre Baskerville: Body text, headings
- Cinzel Decorative: Roman numerals, decorative elements
- Montserrat: Sans-serif elements, modern text
- Proper font-size scales and line-height
- Professional color application
"""

class EPUBAgent:
    """Base class for all EPUB production agents"""
    
    def __init__(self, model="claude-3-sonnet-20240229", api_key=None):
        if not ANTHROPIC_AVAILABLE:
            logger.warning("Anthropic library not available - running in demo mode")
            self.client = None
        else:
            self.client = anthropic.Anthropic(api_key=api_key or os.getenv('ANTHROPIC_API_KEY'))
        self.model = model
        self.system_prompt = ""
        
    def generate(self, prompt: str, max_tokens: int = 4000) -> str:
        """Generate response using Claude"""
        if not self.client:
            return f"[DEMO MODE - Anthropic not available]\n\nWould generate response for:\n{prompt[:200]}..."
        
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=max_tokens,
                system=self.system_prompt,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text
        except Exception as e:
            logger.error(f"Error generating response: {e}")
            raise

class ChapterAgent(EPUBAgent):
    """Specialized agent for chapter generation"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.system_prompt = CHAPTER_AGENT_SYSTEM_PROMPT
    
    def generate_chapter(self, chapter_data: Dict[str, Any]) -> str:
        """Generate complete chapter XHTML"""
        prompt = f"""
        Generate complete Chapter {chapter_data.get('roman', 'X')} XHTML using this data:

        CHAPTER DATA:
        Title: {chapter_data.get('title', 'Chapter Title')}
        Roman Numeral: {chapter_data.get('roman', 'X')}
        Bible Quote: {chapter_data.get('bible_quote', 'Inspirational quote')}
        Bible Reference: {chapter_data.get('bible_reference', 'Reference')}
        Introduction: {chapter_data.get('introduction', 'Chapter introduction')}
        Content: {chapter_data.get('content', 'Chapter content')}
        Endnotes: {chapter_data.get('endnotes', [])}
        Quiz Questions: {chapter_data.get('quiz_questions', [])}
        Worksheet Content: {chapter_data.get('worksheet', 'Worksheet content')}
        Closing Image: {chapter_data.get('closing_image', 'images/chapter-default.jpg')}

        REQUIREMENTS:
        - Complete XHTML document with proper DOCTYPE and namespace
        - All 6 pages with page breaks
        - ACISS design system implementation
        - Professional styling and layout
        - Accessibility features included
        - Image references with alt text
        
        Generate the complete XHTML file ready for EPUB inclusion.
        """
        return self.generate(prompt, max_tokens=6000)

class ValidationAgent(EPUBAgent):
    """Specialized agent for validation and quality assurance"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.system_prompt = VALIDATION_AGENT_PROMPT
    
    def validate_file(self, file_path: str, content: str) -> Dict[str, Any]:
        """Validate a single file"""
        prompt = f"""
        Validate this EPUB file for professional standards:

        FILE: {file_path}
        CONTENT: {content[:3000]}...

        VALIDATION CHECKLIST:
        □ XHTML 1.1 compliance
        □ Proper DOCTYPE and namespace
        □ CSS class consistency  
        □ Image reference accuracy
        □ Accessibility compliance
        □ Typography consistency
        □ Professional formatting
        □ Cross-device compatibility

        Provide detailed validation report with:
        - Issues found (with line numbers)
        - Severity levels (critical, warning, info)
        - Specific corrections needed
        - Overall quality score (1-10)
        """
        
        response = self.generate(prompt, max_tokens=2000)
        
        # Parse response into structured format
        return {
            'file': file_path,
            'validation_response': response,
            'timestamp': datetime.now().isoformat()
        }

class ContentAgent(EPUBAgent):
    """Specialized agent for content generation"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.system_prompt = CONTENT_AGENT_PROMPT
    
    def generate_front_matter(self, content_type: str, data: Dict[str, Any]) -> str:
        """Generate front matter content"""
        prompt = f"""
        Generate professional {content_type} page for EPUB:

        DATA: {json.dumps(data, indent=2)}

        REQUIREMENTS:
        - Single page layout (no pagination)
        - Two-column layout where appropriate
        - Professional typography
        - XHTML 1.1 compliance
        - ACISS design system
        - Complete content (no truncation)

        Generate complete XHTML ready for EPUB inclusion.
        """
        return self.generate(prompt, max_tokens=3000)

class FormatterAgent(EPUBAgent):
    """Specialized agent for formatting and layout"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.system_prompt = FORMATTER_AGENT_PROMPT
    
    def format_content(self, content: str, content_type: str) -> str:
        """Apply professional formatting to content"""
        prompt = f"""
        Apply professional formatting to this {content_type} content:

        CONTENT: {content}

        FORMATTING REQUIREMENTS:
        - ACISS design system compliance
        - Professional typography application
        - Consistent spacing and layout
        - Responsive design principles
        - Cross-device compatibility
        - Accessibility optimization

        Return the formatted content with proper CSS classes applied.
        """
        return self.generate(prompt, max_tokens=4000)

class EPUBAgentOrchestrator:
    """Master orchestrator for coordinating all agents"""
    
    def __init__(self, config_path: Optional[str] = None):
        self.config = self._load_config(config_path)
        self.agents = self._initialize_agents()
    
    def _load_config(self, config_path: Optional[str]) -> Dict[str, Any]:
        """Load configuration from YAML file"""
        default_config = {
            'model': 'claude-3-sonnet-20240229',
            'max_workers': 4,
            'output_directory': 'OEBPS/text',
            'validation_enabled': True
        }
        
        if config_path and os.path.exists(config_path):
            with open(config_path, 'r') as f:
                user_config = yaml.safe_load(f)
                default_config.update(user_config)
        
        return default_config
    
    def _initialize_agents(self) -> Dict[str, EPUBAgent]:
        """Initialize all specialized agents"""
        return {
            'chapter': ChapterAgent(model=self.config['model']),
            'validation': ValidationAgent(model=self.config['model']),
            'content': ContentAgent(model=self.config['model']),
            'formatter': FormatterAgent(model=self.config['model'])
        }
    
    def generate_chapter(self, chapter_number: str, data_file: str, output_file: str) -> bool:
        """Generate a complete chapter"""
        try:
            # Load chapter data
            with open(data_file, 'r') as f:
                if data_file.endswith('.yaml') or data_file.endswith('.yml'):
                    chapter_data = yaml.safe_load(f)
                else:
                    chapter_data = json.load(f)
            
            logger.info(f"Generating Chapter {chapter_number}")
            
            # Generate chapter content
            chapter_agent = self.agents['chapter']
            chapter_content = chapter_agent.generate_chapter(chapter_data)
            
            # Validate if enabled
            if self.config.get('validation_enabled', True):
                validation_agent = self.agents['validation']
                validation_result = validation_agent.validate_file(output_file, chapter_content)
                logger.info(f"Validation completed: {validation_result.get('file', 'unknown')}")
            
            # Write to output file
            os.makedirs(os.path.dirname(output_file), exist_ok=True)
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(chapter_content)
            
            logger.info(f"Chapter {chapter_number} generated successfully: {output_file}")
            return True
            
        except Exception as e:
            logger.error(f"Error generating chapter {chapter_number}: {e}")
            return False
    
    def validate_all_files(self, directory: str) -> Dict[str, Any]:
        """Validate all XHTML files in directory"""
        validation_results = {}
        validation_agent = self.agents['validation']
        
        for file_path in Path(directory).glob('*.xhtml'):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                result = validation_agent.validate_file(str(file_path), content)
                validation_results[str(file_path)] = result
                
            except Exception as e:
                logger.error(f"Error validating {file_path}: {e}")
                validation_results[str(file_path)] = {'error': str(e)}
        
        return validation_results

def create_project_structure(project_name: str, base_dir: str = ".") -> bool:
    """Create complete EPUB project structure"""
    try:
        project_path = Path(base_dir) / project_name
        
        # Create directory structure
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
            "templates"
        ]
        
        for dir_path in directories:
            (project_path / dir_path).mkdir(parents=True, exist_ok=True)
            logger.info(f"Created directory: {dir_path}")
        
        # Create essential files
        files_to_create = {
            "mimetype": "application/epub+zip",
            "META-INF/container.xml": '''<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>''',
            "config/agents.yaml": '''agents:
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
  name: "''' + project_name + '''"
  output_directory: "OEBPS/text"
  validation_enabled: true
  max_workers: 4''',
            ".env.template": '''# EPUB Agents Configuration
ANTHROPIC_API_KEY=your-api-key-here

# Project Settings
PROJECT_NAME=''' + project_name + '''
OUTPUT_DIR=OEBPS/text
VALIDATION_ENABLED=true
'''
        }
        
        for file_path, content in files_to_create.items():
            full_path = project_path / file_path
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(content)
            logger.info(f"Created file: {file_path}")
        
        return True
        
    except Exception as e:
        logger.error(f"Error creating project structure: {e}")
        return False

def main():
    """Main CLI interface for EPUB Agents"""
    parser = argparse.ArgumentParser(description='EPUB Agents - AI-Powered EPUB Production System')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Initialize command
    init_parser = subparsers.add_parser('init', help='Initialize new EPUB project')
    init_parser.add_argument('--project-name', required=True, help='Name of the EPUB project')
    init_parser.add_argument('--base-dir', default='.', help='Base directory for project')
    
    # Generate chapter command
    chapter_parser = subparsers.add_parser('generate-chapter', help='Generate single chapter')
    chapter_parser.add_argument('--chapter-number', required=True, help='Chapter number (Roman numeral)')
    chapter_parser.add_argument('--data-file', required=True, help='Path to chapter data file (YAML/JSON)')
    chapter_parser.add_argument('--output', required=True, help='Output XHTML file path')
    chapter_parser.add_argument('--config', help='Configuration file path')
    
    # Validate command
    validate_parser = subparsers.add_parser('validate', help='Validate EPUB files')
    validate_parser.add_argument('--directory', required=True, help='Directory to validate')
    validate_parser.add_argument('--output', help='Output validation report file')
    
    # Interactive chat command
    chat_parser = subparsers.add_parser('chat', help='Interactive chat with agents')
    chat_parser.add_argument('--agent', choices=['chapter', 'validation', 'content', 'formatter'],
                           required=True, help='Agent to chat with')
    
    # Health check command
    health_parser = subparsers.add_parser('health-check', help='Check system health')
    
    args = parser.parse_args()
    
    if args.command == 'init':
        success = create_project_structure(args.project_name, args.base_dir)
        if success:
            print(f"✅ Project '{args.project_name}' initialized successfully!")
            print(f"📁 Project directory: {Path(args.base_dir) / args.project_name}")
            print("🔧 Next steps:")
            print("  1. Copy .env.template to .env and add your Anthropic API key")
            print("  2. Customize config/agents.yaml if needed")
            print("  3. Add chapter data files to data/chapters/")
            print("  4. Run: python scripts/epub_agents.py generate-chapter --help")
        else:
            print("❌ Failed to initialize project")
            sys.exit(1)
    
    elif args.command == 'generate-chapter':
        orchestrator = EPUBAgentOrchestrator(args.config)
        success = orchestrator.generate_chapter(args.chapter_number, args.data_file, args.output)
        if success:
            print(f"✅ Chapter {args.chapter_number} generated successfully!")
        else:
            print(f"❌ Failed to generate Chapter {args.chapter_number}")
            sys.exit(1)
    
    elif args.command == 'validate':
        orchestrator = EPUBAgentOrchestrator()
        results = orchestrator.validate_all_files(args.directory)
        
        if args.output:
            with open(args.output, 'w') as f:
                json.dump(results, f, indent=2)
            print(f"✅ Validation report saved to: {args.output}")
        else:
            print("📋 Validation Results:")
            for file_path, result in results.items():
                print(f"  {file_path}: {'✅' if 'error' not in result else '❌'}")
    
    elif args.command == 'chat':
        print(f"💬 Starting interactive chat with {args.agent} agent...")
        print("Type 'exit' to quit, 'help' for commands")
        
        orchestrator = EPUBAgentOrchestrator()
        agent = orchestrator.agents[args.agent]
        
        while True:
            try:
                user_input = input(f"\n{args.agent}> ").strip()
                
                if user_input.lower() == 'exit':
                    break
                elif user_input.lower() == 'help':
                    print("Available commands:")
                    print("  exit - Quit chat")
                    print("  help - Show this help")
                    print("  <message> - Send message to agent")
                    continue
                
                if user_input:
                    response = agent.generate(user_input)
                    print(f"\n🤖 {response}")
                    
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"❌ Error: {e}")
        
        print("👋 Chat session ended")
    
    elif args.command == 'health-check':
        print("🏥 EPUB Agents Health Check")
        
        # Check API key
        api_key = os.getenv('ANTHROPIC_API_KEY')
        if api_key:
            print("✅ Anthropic API key found")
        else:
            print("❌ Anthropic API key not found (set ANTHROPIC_API_KEY)")
        
        # Check dependencies
        if ANTHROPIC_AVAILABLE:
            print("✅ Anthropic library available")
        else:
            print("❌ Anthropic library not installed (pip install anthropic)")
        
        try:
            import yaml
            print("✅ PyYAML library available")
        except ImportError:
            print("❌ PyYAML library not installed (pip install pyyaml)")
        
        # Test agent initialization
        try:
            if ANTHROPIC_AVAILABLE and api_key:
                agent = ChapterAgent()
                print("✅ Agent initialization successful")
            else:
                print("⚠️  Cannot test agent without API key or library")
        except Exception as e:
            print(f"❌ Agent initialization failed: {e}")
    
    else:
        parser.print_help()

if __name__ == '__main__':
    main()