from __future__ import print_function, division
from wand.image import Image, Color
import sys
import os.path
import imageio
import numpy as np

# os.environ["IMAGEIO_FFMPEG_EXE"] = "/usr/bin/ffmpeg"
import moviepy.editor as mp

from PIL import Image as PILImage

'''
PDF to GIF/MP4 converter
by Peter Laxalt
'''

################################################################################

frames_directory = "frames/"

def createFrames(argv):

    # informative, but simplistic, error message
    if not len(argv) == 3:
        print("ERROR: You must provide three arguments.")
        print("Usage: python main.py [path to pdf to convert] [output location] [frame_duration]")
        sys.exit(1)

    # set up all our arguments
    converting_file = argv[0]
    output_location = argv[1]

    print("\033[92m" + "[INFO] Currently converting file: ", converting_file)

    # generate a subdirectory for the gifs to live in
    subdirectory = os.path.join(output_location, frames_directory)
    makeDir(output_location)
    makeDir(subdirectory)

    with Image(filename = converting_file, resolution = 200) as pdf:
        print("\033[92m" + "[INFO] Reading file: ", converting_file)

        # give info on what we're doing
        print("\033[92m" + "[INFO] Saving " + str(len(pdf.sequence)) + " pages, [width=" +
            str(pdf.width) + ", height=" + str(pdf.height) + "]")

        # loop through each page in the PDF
        for page in pdf.sequence:
            print("\033[92m" + "[INFO] Currently on page:", page.index + 1)
            # initialize an image of the right size
            converted = Image(width = page.width, height=page.height, background='#fff')
            # copy in the page of the PDF to this image
            converted.composite(page, top=0, left=0)
            # save the image as a png
            converted.format = "png"
            savepath = os.path.join(subdirectory, str(page.index + 1) + ".png")
            converted.save(filename=savepath)

################################################################################

def mergeImagesToGif(folder_path, gif_path, duration):
    print("\033[92m" + "[INFO] mergeImagesToGif initializing")
    print("\033[92m" + "[INFO] folder_path:", folder_path)
    print("\033[92m" + "[INFO] gif_path:", gif_path)
    print("\033[92m" + "[INFO] duration:", duration)
    print("\033[92m" + "os.listdir(folder_path):", sorted(os.listdir(folder_path)))
    images = []

    for filename in os.listdir(folder_path):
        print("\033[92m" + "[INFO] Checking file: " + filename)
        file_path = os.path.join(folder_path, filename)

        images.append(imageio.imread(file_path))
        

    if os.path.exists(gif_path):
      print("\033[92m" + "[INFO] Replacing gif: " + gif_path)
      os.remove(gif_path)  # Remove existing GIF file if present


    print("\033[92m" + "[INFO] Outputting gif: " + gif_path)
    imageio.mimsave(gif_path, images, duration = duration)

################################################################################

def gifToMp4(path): 
    print("\033[92m" + "[INFO] gifToMp4 initializing")
    print("\033[92m" + "[INFO] path", path)
    print("\033[92m" + "[INFO] os.path.splitext(path)[0]+'.mp4'", os.path.splitext(path)[0]+'.mp4')

    clip = mp.VideoFileClip((path))
    clip.write_videofile(os.path.splitext(path)[0]+'.mp4')

################################################################################

# simple function to make a directory if it doesn't exist
def makeDir(directory):
    if not os.path.exists(directory):
        try:
            os.mkdir(directory)
            print("\033[92m" + "[INFO] Made directory: " + directory)
        except Exception:
            print("\033[91m" + "[ERROR] Couldn't make directory: " + directory)
            sys.exit(3)
    else:
        print("\033[93m" + "[WARN] Directory already exists: " + directory)

################################################################################

if __name__ == "__main__":
    combined_frame_dir = "".join((sys.argv[2], frames_directory))
    combined_gif_dir = "".join((sys.argv[2], "output.gif"))

    # print("sys.argv[1:]", sys.argv[1:])
    # print("sys.argv[1]", sys.argv[1])
    # print("sys.argv[2]", sys.argv[2])
    # print("sys.argv[3]", sys.argv[3])
    print("\033[92m" + "[INFO] combined_frame_dir", combined_frame_dir)
    print("\033[92m" + "[INFO] combined_gif_dir", combined_gif_dir)

    # imageio.help("gif")

    # createFrames(sys.argv[1:])
    # mergeImagesToGif(combined_frame_dir, combined_gif_dir, int(sys.argv[3]))
    gifToMp4(combined_gif_dir)
    print("\033[95m" + "CONVERSION COMPLETE")
