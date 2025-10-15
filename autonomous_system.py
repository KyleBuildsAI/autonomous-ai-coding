# autonomous_system.py
import os
import json
import subprocess
import time
from pathlib import Path
import logging

# Load configuration
config_path = Path(__file__).parent / "setup_config.json"
with open(config_path, 'r') as f:
    config = json.load(f)

# Set up logging
log_dir = Path(config["paths"]["logs"])
log_dir.mkdir(exist_ok=True)
logging.basicConfig(
    filename=log_dir / "autonomous.log",
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

class AutonomousSystem:
    def __init__(self, project_path=None):
        self.config = config
        self.project_path = Path(project_path) if project_path else Path(config["paths"]["projects"])
        self.model = config["models"]["primary"]
        
        # Ensure Ollama uses G drive
        os.environ["OLLAMA_MODELS"] = config["paths"]["models"]
        
        print(f"System initialized")
        print(f"Models directory: {config['paths']['models']}")
        print(f"Project path: {self.project_path}")
    
    def query_ollama(self, prompt):
        """Query the local model"""
        cmd = f'ollama run {self.model} "{prompt}"'
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            encoding='utf-8'
        )
        return result.stdout
    
    def analyze_project(self):
        """Analyze Python files in project"""
        py_files = list(self.project_path.glob("**/*.py"))
        print(f"Found {len(py_files)} Python files")
        
        for py_file in py_files[:5]:  # Start with just 5 files
            print(f"Analyzing: {py_file.name}")
            
            with open(py_file, 'r', encoding='utf-8') as f:
                code = f.read()[:1000]  # First 1000 chars for testing
            
            analysis = self.query_ollama(
                f"Briefly analyze this Python code and suggest one improvement:\n{code}"
            )
            
            print(f"Suggestion: {analysis[:200]}...")
            logging.info(f"Analyzed {py_file.name}")
            
            time.sleep(2)  # Don't overwhelm the GPU

if __name__ == "__main__":
    # Allow user to specify project path
    import sys
    project_path = sys.argv[1] if len(sys.argv) > 1 else None
    
    system = AutonomousSystem(project_path)
    system.analyze_project()