# pdf-to-anim
Python script to convert multipage PDF into frame by frame GIF and MP4 files. 

## How to use
- Python only: `python3 main.py <path to pdf to convert> <output location> <frame_duration_ms>`
- Bash: `bash run.sh ./input/test.pdf ./output/test/ 200`
  - This is useful because I run Handbrake afterwards to convert and change encoding for example.

    
### Example:
    `python3 main.py test.pdf ./output/test/ 300`
