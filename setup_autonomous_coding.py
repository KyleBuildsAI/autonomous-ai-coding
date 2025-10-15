# setup_autonomous_coding.py
import os
import json
import subprocess
import sys
from pathlib import Path

class AutonomousCodingSetup:
    def __init__(self, base_path="G:\\AI_Coding"):
        self.base_path = Path(base_path)
        self.config_file = self.base_path / "setup_config.json"
        
        # Load or create config
        if self.config_file.exists():
            with open(self.config_file, 'r') as f:
                self.config = json.load(f)
        else:
            self.create_default_config()
    
    def create_default_config(self):
        """Create default configuration"""
        self.config = {
            "paths": {
                "base_dir": str(self.base_path),
                "models": str(self.base_path / "models"),
                "projects": str(self.base_path / "projects"),
                "chroma_db": str(self.base_path / "data" / "chroma_db"),
                "logs": str(self.base_path / "logs"),
                "swe_agent": str(self.base_path / "tools" / "SWE-agent"),
                "tabby_data": str(self.base_path / "data" / "tabby")
            },
            "models": {
                "primary": "deepseek-coder:33b-instruct-q4_K_M",
                "secondary": "deepseek-coder:6.7b-instruct"
            }
        }
        
        # Create all directories
        for path in self.config["paths"].values():
            Path(path).mkdir(parents=True, exist_ok=True)
        
        # Save config
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=2)
    
    def setup_ollama(self):
        """Setup Ollama with G drive storage"""
        print("Setting up Ollama...")
        
        # Set environment variable
        os.environ["OLLAMA_MODELS"] = self.config["paths"]["models"]
        
        # Check if Ollama is installed
        try:
            subprocess.run(["ollama", "--version"], check=True, capture_output=True)
            print("✓ Ollama is installed")
        except:
            print("Installing Ollama...")
            subprocess.run(["winget", "install", "Ollama.Ollama"], check=True)
        
        # Pull models
        for model_name in self.config["models"].values():
            print(f"Pulling {model_name}...")
            subprocess.run(["ollama", "pull", model_name], check=True)
            print(f"✓ {model_name} ready")
    
    def setup_python_env(self):
        """Setup Python virtual environment"""
        print("Setting up Python environment...")
        
        venv_path = self.base_path / "venv"
        if not venv_path.exists():
            subprocess.run([sys.executable, "-m", "venv", str(venv_path)], check=True)
        
        # Install packages
        pip_path = venv_path / "Scripts" / "pip.exe"
        packages = [
            "langchain", "chromadb", "sentence-transformers",
            "torch", "ollama", "requests", "schedule", "gitpython"
        ]
        
        for package in packages:
            print(f"Installing {package}...")
            subprocess.run([str(pip_path), "install", package], check=True)
        
        print("✓ Python environment ready")
    
    def create_launcher(self):
        """Create a simple launcher script"""
        launcher_content = f'''@echo off
echo Starting Autonomous Coding System...
echo =====================================

:: Set environment variables
set OLLAMA_MODELS={self.config["paths"]["models"]}
set PYTHONPATH={self.base_path}

:: Activate virtual environment
call {self.base_path}\\venv\\Scripts\\activate.bat

:: Start the system
python {self.base_path}\\autonomous_system.py

pause
'''
        
        launcher_path = self.base_path / "START_AI_CODING.bat"
        with open(launcher_path, 'w') as f:
            f.write(launcher_content)
        
        print(f"✓ Launcher created: {launcher_path}")
    
    def run_setup(self):
        """Run complete setup"""
        print("=== Autonomous Coding Setup ===")
        print(f"Base directory: {self.base_path}")
        print("================================\n")
        
        self.setup_ollama()
        self.setup_python_env()
        self.create_launcher()
        
        print("\n=== Setup Complete! ===")
        print(f"1. Your AI coding system is installed at: {self.base_path}")
        print(f"2. Models are stored at: {self.config['paths']['models']}")
        print(f"3. To start, run: {self.base_path}\\START_AI_CODING.bat")

if __name__ == "__main__":
    # Check if user wants a different drive
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--drive", default="G", help="Drive letter to install on")
    args = parser.parse_args()
    
    base_path = f"{args.drive}:\\AI_Coding"
    setup = AutonomousCodingSetup(base_path)
    setup.run_setup()