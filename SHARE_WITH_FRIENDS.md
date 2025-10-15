# Autonomous AI Coding Setup - Windows

## Requirements
- Windows 10/11 64-bit
- NVIDIA GPU with 8GB+ VRAM (RTX 3060 minimum, RTX 4090/5090 recommended)
- 50GB free space on any drive
- Python 3.10+

## Quick Install (5 minutes)

1. **Download this folder to any drive** (C:, D:, G:, etc.)

2. **Run PowerShell as Administrator and execute:**
```powershell
# Change G: to your preferred drive
cd G:\
git clone [your-repo-url] AI_Coding
cd AI_Coding
python setup_autonomous_coding.py --drive G
```

3. **Start the system:**
   - Double-click `START_AI_CODING.bat`
   - Or run: `python autonomous_system.py "C:\path\to\your\project"`

## What Gets Installed Where

- **Program files** (small): C:\Program Files\Ollama
- **Everything else** (large): G:\AI_Coding\
  - Models: G:\AI_Coding\models\ (20-30GB)
  - Your projects: G:\AI_Coding\projects\
  - Databases: G:\AI_Coding\data\
  - Logs: G:\AI_Coding\logs\

## Models Included

- **DeepSeek-Coder 33B**: Best for complex tasks (uses ~20GB)
- **DeepSeek-Coder 6.7B**: Fast for simple tasks (uses ~4GB)

## Costs

- **Electricity**: ~$3/day running 24/7
- **API costs**: $0 (everything runs locally)
- **Cloud equivalent**: Would cost $100-300/day

## Troubleshooting

If Ollama doesn't see your GPU:
1. Update NVIDIA drivers: https://www.nvidia.com/drivers
2. Restart Ollama: Services → Ollama → Restart

## Customization

Edit `setup_config.json` to:
- Change model choices
- Adjust paths
- Add new tools