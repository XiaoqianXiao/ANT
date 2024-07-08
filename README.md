Convert from the e-prime fMRI version ([Fan et al., 2005](.md file add link)).
Changes including:
  * simplify the instruction
    - in original e-prime version:
      "Welcome to Attention Experiment\nPress a button to continue. \n\nPress and hold all 5 buttons to contact Technologist."
      " \nInstruction\n\nPlease press left point finger when the cental arrowhead points left and press right pointing finger when the central arrowhead poin" &_ 
				"ts right.\n\n\nPress any button if you are ready.. "
    - in current version:
      "Please press left point finger when the cental arrowhead points left \n \nand press right pointing finger when the central arrowhead poin right"
  * using norm (Normalized) as the representation units to avoid changes across different screens.
    - in original e-prime version:
      win size: size=(640, 480)
      intro text size: 16
      fixation text size: 18
      text font: Arial & Bold
      cue image size: full
      target image size: full
    - in current version:
      win size: full screen
      intro text size: 0.08
      fixation text size: 0.08
      text font: DejaVu Sans [the default of python]
      cue image size: size=(0.00002 * win_width, 0.000035 * win_height)
      target image size: size=(win_width * 0.00025, win_height * 0.0006)
