from psychopy import visual, event, core, data, logging
#%%
#import tools
import time
import os
import pandas as pd
import random
#%%
input_subID = 1
input_runID = 1
input_session = 'pre'
#%%
runID = str(input_runID).zfill(2)
subID = str(input_subID).zfill(3)
sessionID = input_session

#%%
#Initialize the results file
results_dir = os.path.join(current_dir, 'results')
if not os.path.exists(results_dir):
    os.makedirs(results_dir)
resultFile_name = 'sub-' + subID + '_ses-' + sessionID + '_run-' + runID + '.csv'
#%%
# Initialize PsychoPy window
win = visual.Window(
    #set size for test the scripts
    #size=[800, 600],
    color="white",
    units="pix",
    #set full screen to formal experiment
    fullscr=True
)
# Initialize components
intro_text = init_intro(win)
goodbye_text = init_goodbye(win)

# Run the session procedure
session_proc_run()
thisExp.saveAsWideText(filename + '.csv')
thisExp.saveAsPickle(filename)
win.close()
core.quit()