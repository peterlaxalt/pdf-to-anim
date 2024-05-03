# pdf-to-gif
Python script to convert multipage PDF into multi-GIF files. 

# Setup
This script uses Python 2.7 and Wand (based on ImageMagick).

    brew install python
    pip install Wand

# How to use
## Single file

    python3 main.py <path to pdf to convert> <output location> <frame_duration_ms>
    
Example:
    python3 main.py stone_creek.pdf ./output/stone_creek/ 300
