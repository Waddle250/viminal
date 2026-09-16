import curses
import cv2

timestamp = 0
curses.start_color()

def playVideo(stdscr, video, width, height):
  global timestamp
  capturedVideo = cv2.VideoCapture(video)
  success, frame = capturedVideo.read()
  maxFrames = capturedVideo.get(cv2.CAP_PROP_FRAME_COUNT)
  cv2.resize(frame, (width, height))
  stdscr.clear()
  
  x = 0
  y = 0

  #loop that renders each frame
  for f in range(maxFrames):
    for y in range(height):
      try:
        for x in range(width):
          cap.set(cv2.CAP_PROP_POS_FRAMES, timestamp-1)
          pixelColor = frame[y, x]
          b, g, r = BGRColor
          curses.init_color(1, r, g, b)
          stdscr.addstr(y, x, '██')
      except null:
        return 1
    timestamp += 1
    print(timestamp)

  stdscr.clear()
  print(f"Video finished successfully at {str(timestamp)}")
  return
  

