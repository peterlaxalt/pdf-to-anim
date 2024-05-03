echo "🚀 Initializing... "
python3 main.py $1 $2 $3
handbrakecli -i ./output/test/output_original.mp4 -o ./output/test/output_h264.mp4  -e x264