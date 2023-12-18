#!/usr/bin/python
import json
import math
import subprocess
import sys

def trafo(x:int) -> int:
   return x*2*0.16666667

def update_state(cmd, state_file="/tmp/mouse_quad_state"):
   try:
      with open(state_file, "r") as file:
         state = json.load(file)
   except FileNotFoundError:
      state = {"x": 0, "y": 0, "width": 1920, "height": 1080, "draw": True}

   #new_width = state["width"] // 2
   #new_height = state["height"] // 2
   x = state["x"]
   y = state["y"]
   w = state["width"]
   h = state["height"]
   print(f"x:{x};y:{y};w:{w};h:{h}")

   vv = 12
   if cmd[0] == 'n':
      if   cmd[1] == '7':
         move_mouse_rel(-vv, -vv)
      elif cmd[1] == '8':
         move_mouse_rel(0, -vv)
      elif cmd[1] == '9':
         move_mouse_rel(vv, -vv)
      elif cmd[1] == '4':
         move_mouse_rel(-vv, 0)
      elif cmd[1] == '5':
         mouse_click()
      elif cmd[1] == '6':
         move_mouse_rel(vv, 0)
      elif cmd[1] == '1':
         move_mouse_rel(-vv, vv)
      elif cmd[1] == '2':
         move_mouse_rel(0, vv)
      elif cmd[1] == '3':
         move_mouse_rel(vv, vv)
      return
   
   if cmd == 'init':
      state = {"x": 0, "y": 0, "width": 1920, "height": 1080, "draw": True}
   elif cmd == 'quit':
      state = {"x": 0, "y": 0, "width": 1920, "height": 1080, "draw": False}
   elif cmd == 'move': # exit
      move_mouse(x+w//2, y+h//2)
      state.update({"x": 0, "y": 0, "width": 1920, "height": 1080, "draw": False})
   elif cmd == 'click':
      mouse_click()
   elif cmd == '7': # Top left
      state.update({
         "x": x + math.floor(w*trafo(0)),
         "y": y + math.floor(h*trafo(0)),
         "width": math.floor(w*0.333333),
         "height": math.floor(h*0.333333),
         "draw": True
      })
   elif cmd == '8': # Top Middle
      state.update({
         "x": x + math.floor(w*trafo(1)),
         "y": y + math.floor(h*trafo(0)),
         "width": math.floor(w*0.333333),
         "height": math.floor(h*0.333333),
         "draw": True
      })
   elif cmd == '9': # Top Right
      state.update({
         "x": x + math.floor(w*trafo(2)),
         "y": y + math.floor(h*trafo(0)),
         "width": math.floor(w*0.333333),
         "height": math.floor(h*0.333333),
         "draw": True
      })
   elif cmd == '4': # Top left
      state.update({
         "x": x + math.floor(w*trafo(0)),
         "y": y + math.floor(h*trafo(1)),
         "width": math.floor(w*0.333333),
         "height": math.floor(h*0.333333),
         "draw": True
      })
   elif cmd == '5': # Top left
      state.update({
         "x": x + math.floor(w*trafo(1)),
         "y": y + math.floor(h*trafo(1)),
         "width": math.floor(w*0.333333),
         "height": math.floor(h*0.333333),
         "draw": True
      })
   elif cmd == '6': # Top left
      state.update({
         "x": x + math.floor(w*trafo(2)),
         "y": y + math.floor(h*trafo(1)),
         "width": math.floor(w*0.333333),
         "height": math.floor(h*0.333333),
         "draw": True
      })
   elif cmd == '1': # Top left
      state.update({
         "x": x + math.floor(w*trafo(0)),
         "y": y + math.floor(h*trafo(2)),
         "width": math.floor(w*0.333333),
         "height": math.floor(h*0.333333),
         "draw": True
      })
   elif cmd == '2': # Top left
      state.update({
         "x": x + math.floor(w*trafo(1)),
         "y": y + math.floor(h*trafo(2)),
         "width": math.floor(w*0.333333),
         "height": math.floor(h*0.333333),
         "draw": True
      })
   elif cmd == '3': # Top left
      state.update({
         "x": x + math.floor(w*trafo(2)),
         "y": y + math.floor(h*trafo(2)),
         "width": math.floor(w*0.333333),
         "height": math.floor(h*0.333333),
         "draw": True
      })

   # elif cmd == 'l':  # Top-right quadrant
   #    state.update({"x": state["x"] + new_width, "width": new_width, "height": new_height, "draw": True})
   # elif cmd == 'j':  # Bottom-left quadrant
   #    state.update({"y": state["y"] + new_height, "width": new_width, "height": new_height, "draw": True})
   # elif cmd == 'k':  # Bottom-right quadrant
   #    state.update({"x": state["x"] + new_width, "y": state["y"] + new_height, "width": new_width, "height": new_height, "draw": True})
   # elif cmd == 'u': # exit
   #    move_mouse(state["x"] + state["width"] // 2, state["y"] + state["height"] // 2)
   #    state.update({"x": 0, "y": 0, "width": 1920, "height": 1080, "draw": False})

   with open(state_file, "w") as file:
      json.dump(state, file)

def move_mouse(x, y):
   subprocess.run(["xdotool", "mousemove", str(x), str(y)])

def move_mouse_rel(x, y):
   subprocess.run(["xdotool", "mousemove_relative", "--", str(x), str(y)])

def mouse_click():
   subprocess.run(["xdotool", "click", "1"])

if __name__ == "__main__":
   key_input = sys.argv[1]
   update_state(key_input)
