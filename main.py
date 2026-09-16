import curses
import cv2

timestamp = 0

def playVideo(stdscr, video, width, height):
  global timestamp
  capturedVideo = cv2.VideoCapture(video)
  success, frame = capturedVideo.read
  stdscr.clear()
  
  x = 0
  y = 0

  #loop that renders each frame
  
  for y in range(height):
    try:
      for x in range(width):
        stdscr.addstr(y, x, '#')
  timestamp += 1

  stdscr.clear()
  print(f"Video finished successfully at {str(timestamp)}")
  

