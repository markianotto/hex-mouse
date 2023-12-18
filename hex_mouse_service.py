#!/usr/bin/python
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from Xlib import X, display
import json
import time
import math

class StateChangeHandler(FileSystemEventHandler):
   def __init__(self):
      self.display = display.Display()
      self.screen = self.display.screen()
      self.root = self.screen.root
      self.rectangle_windows = []

   def on_modified(self, event):
      if event.src_path == "/tmp/mouse_quad_state":
         self.update_screen()

   def update_screen(self):
      for win in self.rectangle_windows:
         win.destroy()
      self.rectangle_windows.clear()

      try:
         with open("/tmp/mouse_quad_state", "r") as file:
            state = json.load(file)
            x = state["x"]
            y = state["y"]
            width = state["width"]
            height = state["height"]
            draw = state["draw"]
            if not draw:
               print("draw: False -> drawing sacrificial rectangle, exiting...")
               #self.draw_rectangle(10, 10, 50, 50)
               self.display.flush()
               return

      except Exception as e:
         print("Error reading state file:", e)
         return

      hex_centers = []
      for qx in range(0, 3):
         for qy in range(0, 3):
            hex_centers.append((  
               x + math.floor((1+2*qx)*0.16666667*width),
               y + math.floor((1+2*qy)*0.16666667*height),
            ))
      print(f"hex centers: {hex_centers[0]}")
      for center_x, center_y in hex_centers:
         self.draw_rectangle(center_x - 5, center_y - 5, 10, 10)

      self.display.flush()
   def draw_rectangle(self, x, y, width, height):
      rect_window = self.root.create_window(x, y, width, height, 0, X.CopyFromParent, X.InputOutput, X.CopyFromParent, background_pixel=self.display.screen().white_pixel, override_redirect=True)
      rect_window.map()
      self.rectangle_windows.append(rect_window)

if __name__ == "__main__":
   event_handler = StateChangeHandler()
   observer = Observer()
   observer.schedule(event_handler, path='/tmp/', recursive=False)
   observer.start()
   try:
      while True:
         time.sleep(0.25)
   except KeyboardInterrupt:
      observer.stop()
   observer.join()
