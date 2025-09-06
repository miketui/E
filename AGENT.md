# AGENT.md - AI Agent Workflow System for EPUB Production

## Overview
This document defines a specialized AI agent system for automated EPUB production. Each agent has specific expertise and responsibilities, working together to ensure professional, bestseller-quality output.

## Agent Architecture

### Master Orchestrator Agent
**Role**: Workflow coordination and quality oversight
**Responsibilities**:
- Task delegation to specialized agents
- Progress monitoring and bottleneck identification
- Final quality assurance coordination
- Error escalation and resolution

```python
class MasterOrchestrator:
    def __init__(self):
        self.agents = {
            'content': ContentGenerationAgent(),
            'validator': ValidationAgent(),
            'formatter': FormattingAgent(),
            'image': ImageProcessingAgent(),
            'css': CSSAgent(),
            'epub': EPUBCompilerAgent()
        }
    
    def process_book(self, book_data):
        # Coordinate full production workflow
        for phase in ['generate', 'validate', 'format', 'compile']:
            self.execute_phase(phase, book_data)
```

## Primary Agents

### 1. Content Generation Agent
**Specialty**: Creating structured XHTML content
**Sub-agents**:
- Chapter Agent
- Front Matter Agent  
- Back Matter Agent
- Quiz Agent
- Worksheet Agent

#### Chapter Agent
```python
class ChapterAgent:
    def __init__(self):
        self.template = self.load_chapter_template()
        self.style_guide = self.load_aciss_style_guide()
    
    def generate_chapter(self, chapter_data):
        """
        Generate complete 6-page chapter structure
        """
        return {
            'title_page': self.create_title_page(chapter_data),
            'body': self.create_body_content(chapter_data),
            'endnotes': self.create_endnotes(chapter_data),
            'quiz': self.create_quiz(chapter_data),
            'worksheet': self.create_worksheet(chapter_data),
            'closing': self.create_closing_image(chapter_data)
        }
    
    def create_title_page(self, data):
        """
        Title page with Roman numeral, vertical title stack, bible quote
        """
        prompt = f"""
        Generate ACISS title page for Chapter {data['roman']}:
        
        Title Lines: {data['title_lines']}
        Bible Quote: {data['bible_quote']}
        Introduction: {data['intro_text']}
        
        Use established design system:
        - Roman numeral badge with gradient
        - Vertical title stack with accent bar
        - Pill-shaped bible quote container
        - Dropcap first letter styling
        """
        return self.claude_generate(prompt)
```

#### Quiz Agent
```python
class QuizAgent:
    def __init__(self):
        self.max_questions = 4
        self.difficulty_levels = ['basic', 'intermediate', 'advanced']
    
    def generate_quiz(self, chapter_content, learning_objectives):
        prompt = f"""
        Create exactly 4 multiple choice questions for:
        
        Chapter Content: {chapter_content}
        Learning Objectives: {learning_objectives}
        
        Requirements:
        - Exactly 4 questions maximum
        - A, B, C, D options
        - Professional hairstyling context
        - Varying difficulty levels
        - Clear, unambiguous language
        - Answer key reference to backmatter only
        """
        return self.claude_generate(prompt)
```

#### Worksheet Agent
```python
class WorksheetAgent:
    def generate_worksheet(self, chapter_theme, practical_applications):
        prompt = f"""
        Create static worksheet for Chapter: {chapter_theme}
        
        Practical Applications: {practical_applications}
        
        Include:
        - 3-4 distinct sections
        - Mix of fill-in-the-blank, reflection, and action items
        - Professional presentation
        - Print-friendly layout
        - Static design (no interactivity for EPUB)
        """
        return self.claude_generate(prompt)
```

### 2. Validation Agent
**Specialty**: Quality assurance and standards compliance
**Sub-agents**:
- XHTML Validator
- CSS Validator
- Accessibility Validator
- Content Consistency Validator

#### XHTML Validator
```python
class XHTMLValidator:
    def validate_file(self, filepath):
        checks = [
            self.check_doctype(),
            self.check_namespace(),
            self.check_structure(),
            self.check_attributes(),
            self.check_accessibility(),
            self.check_image_references()
        ]
        return self.compile_validation_report(checks)
    
    def check_structure(self, content):
        """Validate XHTML 1.1 structure"""
        required_elements = ['html', 'head', 'title', 'body']
        return all(element in content for element in required_elements)
```

#### Content Consistency Validator
```python
class ContentConsistencyValidator:
    def __init__(self):
        self.style_guide = self.load_style_guide()
        self.terminology = self.load_terminology_guide()
    
    def validate_consistency(self, files):
        """Check consistency across all files"""
        checks = {
            'typography': self.check_typography_consistency(files),
            'terminology': self.check_terminology_consistency(files),
            'styling': self.check_css_class_consistency(files),
            'structure': self.check_structure_consistency(files)
        }
        return checks
```

### 3. Formatting Agent
**Specialty**: Professional layout and typography
**Sub-agents**:
- Typography Agent
- Layout Agent
- Color Scheme Agent
- Responsive Design Agent

#### Typography Agent
```python
class TypographyAgent:
    def __init__(self):
        self.fonts = {
            'body': 'Libre Baskerville',
            'headings': 'Libre Baskerville', 
            'decorative': 'Cinzel Decorative',
            'sans': 'Montserrat'
        }
        self.scales = self.load_typography_scales()
    
    def apply_typography(self, content, content_type):
        """Apply consistent typography based on content type"""
        if content_type == 'chapter_title':
            return self.apply_chapter_title_typography(content)
        elif content_type == 'body':
            return self.apply_body_typography(content)
        # ... other content types
```

#### Layout Agent
```python
class LayoutAgent:
    def create_two_column_layout(self, content, layout_type):
        """Create responsive two-column layouts for front/back matter"""
        if layout_type == 'front_matter':
            return self.front_matter_layout(content)
        elif layout_type == 'back_matter':
            return self.back_matter_layout(content)
    
    def ensure_single_page(self, content):
        """Ensure content fits on single page across all devices"""
        return self.optimize_for_single_page(content)
```

### 4. CSS Agent
**Specialty**: Stylesheet management and optimization
**Sub-agents**:
- Font Embedding Agent
- Responsive Design Agent
- Print Optimization Agent

#### Font Embedding Agent
```python
class FontEmbeddingAgent:
    def __init__(self):
        self.font_formats = ['woff2', 'woff', 'ttf']
        self.font_families = {
            'libre': ['regular', 'bold', 'italic'],
            'cinzel': ['regular'],
            'montserrat': ['regular', 'bold']
        }
    
    def generate_font_css(self, font_directory):
        """Generate @font-face declarations with proper paths"""
        css = ""
        for family, weights in self.font_families.items():
            for weight in weights:
                css += self.create_font_face(family, weight, font_directory)
        return css
    
    def optimize_font_loading(self):
        """Optimize font loading performance"""
        return """
        /* Font loading optimization */
        @font-face {
            font-display: swap;
            /* Additional optimization rules */
        }
        """
```

### 5. Image Processing Agent
**Specialty**: Image optimization and management
**Sub-agents**:
- Image Optimization Agent
- Alt Text Generator Agent
- Responsive Image Agent

#### Image Optimization Agent
```python
class ImageOptimizationAgent:
    def optimize_for_epub(self, image_path):
        """Optimize images for EPUB distribution"""
        optimizations = [
            self.resize_for_epub(image_path),
            self.compress_image(image_path),
            self.convert_format_if_needed(image_path),
            self.validate_epub_compatibility(image_path)
        ]
        return optimizations
    
    def generate_responsive_images(self, image_path):
        """Create multiple sizes for different devices"""
        sizes = ['small', 'medium', 'large']
        return {size: self.resize_image(image_path, size) for size in sizes}
```

#### Alt Text Generator Agent
```python
class AltTextGenerator:
    def generate_alt_text(self, image_path, context):
        prompt = f"""
        Generate descriptive alt text for image in hairstyling book:
        
        Image: {image_path}
        Context: {context}
        
        Requirements:
        - Descriptive but concise
        - Professional terminology
        - Accessibility compliant
        - Context-appropriate
        """
        return self.claude_generate(prompt)
```

### 6. EPUB Compiler Agent
**Specialty**: Final EPUB assembly and packaging
**Sub-agents**:
- Manifest Generator Agent
- TOC Generator Agent
- Package Validator Agent

#### Manifest Generator Agent
```python
class ManifestGenerator:
    def generate_content_opf(self, book_metadata, file_list):
        """Generate complete content.opf manifest"""
        manifest = self.create_manifest_header(book_metadata)
        manifest += self.add_stylesheet_items()
        manifest += self.add_font_items()
        manifest += self.add_content_items(file_list)
        manifest += self.add_image_items()
        manifest += self.create_spine(file_list)
        return manifest
```

## Agent Coordination Workflows

### Chapter Production Workflow
```python
def produce_chapter(chapter_data):
    # 1. Content Generation
    content = ContentGenerationAgent().generate_chapter(chapter_data)
    
    # 2. Formatting
    formatted = FormattingAgent().apply_chapter_formatting(content)
    
    # 3. Image Processing
    images = ImageProcessingAgent().process_chapter_images(chapter_data.images)
    
    # 4. CSS Application
    styled = CSSAgent().apply_chapter_styles(formatted)
    
    # 5. Validation
    validation = ValidationAgent().validate_chapter(styled)
    
    # 6. Final Assembly
    return EPUBCompilerAgent().assemble_chapter(styled, images, validation)
```

### Quality Assurance Workflow
```python
def quality_assurance_pass(epub_files):
    # Multi-agent validation
    results = {
        'xhtml': XHTMLValidator().batch_validate(epub_files.xhtml),
        'css': CSSValidator().validate_stylesheets(epub_files.css),
        'images': ImageValidator().validate_images(epub_files.images),
        'accessibility': AccessibilityValidator().check_accessibility(epub_files),
        'consistency': ConsistencyValidator().check_cross_file_consistency(epub_files)
    }
    
    # Compile comprehensive report
    return QualityReportGenerator().generate_report(results)
```

## Agent Communication Protocol

### Message Passing System
```python
class AgentMessage:
    def __init__(self, sender, recipient, task, data, priority='normal'):
        self.sender = sender
        self.recipient = recipient
        self.task = task
        self.data = data
        self.priority = priority
        self.timestamp = datetime.now()

class AgentCommunicationHub:
    def __init__(self):
        self.message_queue = PriorityQueue()
        self.agent_registry = {}
    
    def send_message(self, message):
        self.message_queue.put((message.priority, message))
    
    def process_messages(self):
        while not self.message_queue.empty():
            priority, message = self.message_queue.get()
            self.route_message(message)
```

## Error Handling and Recovery

### Error Categories
1. **Content Errors**: Missing data, malformed content
2. **Validation Errors**: Standards compliance failures
3. **Format Errors**: Layout or styling issues
4. **Technical Errors**: File system, compilation problems

### Recovery Strategies
```python
class ErrorRecoveryAgent:
    def handle_error(self, error_type, error_data):
        if error_type == 'content_missing':
            return self.generate_placeholder_content(error_data)
        elif error_type == 'validation_failure':
            return self.auto_fix_validation_issues(error_data)
        elif error_type == 'format_error':
            return self.apply_fallback_formatting(error_data)
        else:
            return self.escalate_to_human(error_data)
```

## Performance Optimization

### Parallel Processing
```python
import asyncio
from concurrent.futures import ThreadPoolExecutor

class ParallelProcessingManager:
    def __init__(self, max_workers=4):
        self.executor = ThreadPoolExecutor(max_workers=max_workers)
    
    async def process_chapters_parallel(self, chapters):
        loop = asyncio.get_event_loop()
        tasks = [
            loop.run_in_executor(
                self.executor, 
                self.process_single_chapter, 
                chapter
            ) for chapter in chapters
        ]
        return await asyncio.gather(*tasks)
```

### Caching System
```python
class AgentCache:
    def __init__(self):
        self.cache = {}
        self.ttl = 3600  # 1 hour
    
    def get_cached_result(self, key):
        if key in self.cache:
            if time.time() - self.cache[key]['timestamp'] < self.ttl:
                return self.cache[key]['data']
        return None
    
    def cache_result(self, key, data):
        self.cache[key] = {
            'data': data,
            'timestamp': time.time()
        }
```

## Agent Deployment and Configuration

### Configuration File (agents.yaml)
```yaml
agents:
  content_generator:
    model: "claude-sonnet-4-20250514"
    max_tokens: 4000
    temperature: 0.3
    
  validator:
    model: "claude-sonnet-4-20250514"
    max_tokens: 2000
    temperature: 0.1
    
  formatter:
    model: "claude-sonnet-4-20250514"
    max_tokens: 3000
    temperature: 0.2

workflows:
  chapter_production:
    agents: [content_generator, formatter, validator]
    parallel: true
    timeout: 300
    
  quality_assurance:
    agents: [validator, consistency_checker]
    parallel: false
    timeout: 600
```

### Agent Factory
```python
class AgentFactory:
    def __init__(self, config_path):
        self.config = self.load_config(config_path)
    
    def create_agent(self, agent_type):
        config = self.config['agents'][agent_type]
        return Agent(
            model=config['model'],
            max_tokens=config['max_tokens'],
            temperature=config['temperature']
        )
    
    def create_workflow(self, workflow_name):
        workflow_config = self.config['workflows'][workflow_name]
        agents = [
            self.create_agent(agent_name) 
            for agent_name in workflow_config['agents']
        ]
        return Workflow(agents, workflow_config)
```

## Monitoring and Analytics

### Agent Performance Tracking
```python
class AgentMonitor:
    def __init__(self):
        self.metrics = {}
    
    def track_agent_performance(self, agent_name, task, execution_time, success):
        if agent_name not in self.metrics:
            self.metrics[agent_name] = []
        
        self.metrics[agent_name].append({
            'task': task,
            'execution_time': execution_time,
            'success': success,
            'timestamp': datetime.now()
        })
    
    def generate_performance_report(self):
        """Generate comprehensive performance analytics"""
        return {
            agent: self.analyze_agent_metrics(metrics)
            for agent, metrics in self.metrics.items()
        }
```

This agent system provides comprehensive automation for EPUB production while maintaining quality and consistency standards. Each agent specializes in specific tasks while working together through the orchestrator to deliver professional results.