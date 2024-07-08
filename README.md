Convert from the e-prime fMRI version ([Fan et al., 2005](.md file add link)).
Changes including:
  * simplify the instruction
    - in original e-prime version:
      - "Welcome to Attention Experiment\nPress a button to continue. \n\nPress and hold all 5 buttons to contact Technologist."
      - " \nInstruction\n\nPlease press left point finger when the cental arrowhead points left and press right pointing finger when the central arrowhead poin" &_ 
				"ts right.\n\n\nPress any button if you are ready.. "
    - in current version:
      - "Please press left point finger when the cental arrowhead points left \n \nand press right pointing finger when the central arrowhead poin right"
  * using norm (Normalized) as the representation units to avoid changes across different screens.
| field | original e-prime version | current version |
|:-----------------|:-----------------|:-----------------|
| win size | (640, 480) | full screen |
| intro text size | 16 | 0.08 |
| fixation text size | 18 | 0.08 |
| text font | Arial & Bold | DejaVu Sans [the default of python] |
| cue image size| 0.25 | (0.00002 * win_width, 0.000035 * win_height) |
| target image size | 0.25 | (win_width * 0.00025, win_height * 0.0006) |
