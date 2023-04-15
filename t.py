import cv2
import os

# Open a video file 
vidcap = cv2.VideoCapture('z.mp4')

# directory to save the frames
outdir = 'C:\\Users\\Abdul Rahman\\Downloads\\time\\New folder' #change or make directory accordingly
if not os.path.exists(outdir):
    os.makedirs(outdir)

# Set the time interval between frames (in seconds) if video is long increase the time so that you can get variety, set to 0 if you want all fps
time_interval = 1

#Dont edit anything beyond this point except name (line 30)

# Set the initial frame count and time
frame_count = 0
time_count = 0

# Read and save the frames as JPEG images
while True:
    success, image = vidcap.read()
    if not success:
        break

    # Only save a frame every time_interval seconds
    time_count += 1
    if time_count >= time_interval * vidcap.get(cv2.CAP_PROP_FPS):
        outfilename = os.path.join(outdir, f"zframeff{frame_count:04d}.jpg") #change the output name to avoid overlapping
        cv2.imwrite(outfilename, image)     # save frame as JPEG file
        print(f'Saved frame {frame_count} to {outfilename}')
        frame_count += 1
        time_count = 0
