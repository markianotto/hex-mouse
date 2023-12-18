# Hex Mouse
Two scripts for manipulating the mouse cursor's position swiftly.
Hex mouse splits your screen up into 8 equally spaced nodes from which you can choose recursively, in each
iteration getting closer to your target.
Once you are sufficiently close to your target location or sufficiently confused by this recursive approach,
you can enter mouse "nudge" mode, in which 8 of the keyboard keys are bound to move your cursor in 8 directions,
nethack style.

# Requirements
You'll need to be using X11 or replace `python-xlib` with something else to draw the rectangles to screen.
While these scripts can be adjusted for any desktop environment, it is built and tested for the i3
Window Manager.

# How to Run
1. copy the two scripts `hex_mouse.py` and `hex_mouse_service.py` to `/home/$USER/hex_mouse` or the location of your choice.

2. add `i3_config` to your i3 window manager configuration. If you want you can edit the keybindings to better fit to what you're used to. If you installed the two scripts to somewhere else besides `/home/$USER/hex_mouse`, be sure to edit the path to the scripts in `i3_config` accordingly to `/where/ever/you/want/quad_mouse.py`.

3. restart i3 or reload the i3 config.

4. run the `hex_mouse_service.py` in your favorite terminal emulator or install it as a service.

# Default Keybindings
- select one of the 8 quadrants with: `u`, `i`, `o`, `j`, `k`, `l`, `m`, `,` or `.`. 
- move to the desired location with `;`.
- switch to 'nudge' mode with `n`.
- nudge the mouse by 12 pixels using the same keys as for selecting the quadrants: `u`, `i`, `o`, `j`, `k`, `l`, `m`, `,` or `.`.
- in nudge mode: perform a click with `k` or `;`.

# Ideas
This idea can be driven even further by printing the entire keyboard layout onto the screen, with an 
even finer mesh than just a 3 by 3 grid.
Another approach would be to have the user first choose the x-axis position and then the y-axis position
like in chess or that battle ship game.
