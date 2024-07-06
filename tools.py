# Function to update attributes
def setAttrib(attr, value):
    trialAttributes[attr] = value
def getAttrib(attr):
    return trialAttributes[attr]
# Function to initialize text display defaults
def InitTextDisplayDefaults(win, text_content=""):
    text_display = visual.TextStim(
        win=win,
        text=text_content,
        pos=(0, 0),  # Center position
        color="black",  # Foreground color
        colorSpace='rgb',
        height=18,  # Font size
        wrapWidth=win.size[0],  # Word wrap width set to window width
        font="Courier New",  # Font name
        bold=True,  # Font bold
        italic=False,  # Font italic
        alignHoriz="center",  # Horizontal alignment
        alignVert="center"  # Vertical alignment
    )
    return text_display

def InitSlideImageDefaults(win, image_path):
    # Check if image path is None or empty
    if not image_path:
        return None
    # Create an ImageStim with default properties
    theSlideImage = visual.ImageStim(
        win=win,
        image=image_path,
        size=None,  # Preserve original size by default
        units='pix',  # You can adjust this based on your requirement
        interpolate=True  # Enable interpolation for better quality
    )
    # Set additional properties equivalent to E-Prime defaults
    theSlideImage.mirror = False  # Equivalent to MirrorLeftRight and MirrorUpDown being "No"
    return theSlideImage
def init_intro(win):
    intro_text = visual.TextStim(win, text="Welcome to the experiment. Press a key to continue...", pos=(0, 0), color="black")
    return intro_text
def init_goodbye(win):
    goodbye_text = visual.TextStim(win, text="Thank you for participating. Press a key to exit...", pos=(0, 0), color="black")
    return goodbye_text
def run_intro(intro_text):
    intro_text.draw()
    win.flip()
    keys = event.waitKeys(keyList=["s"], clearEvents=True)
    return keys
def run_goodbye(goodbye_text):
    goodbye_text.draw()
    win.flip()
    event.waitKeys()
def run_runs(runID):
    current_dir = os.getcwd()
    stimList_name = 'run-' + str(runID) + '.csv'
    stimList_dir = os.path.join(current_dir, 'experiment_design', 'stim_lists', stimList_name)
    stimList = pd.read_csv(stimList_dir)
    for index, row in stimList.iterrows():
        trialAttributes = row.to_dict()
        # Define stimuli
        fixation_start = visual.TextStim(win, text='+', height=0.1)
        warning = visual.ImageStim(win, image=getAttrib('TargetFilePath') + 'symbolstarbig.bmp', pos=(0, getAttrib('CuePositionY')))
        warning2 = visual.ImageStim(win, image=getAttrib('TargetFilePath') + 'symbolstarbig.bmp', pos=(0, getAttrib('CuePositionY2')))
        fixation_middle = visual.TextStim(win, text='+', height=0.1)
        target = visual.ImageStim(win, image=getAttrib('TargetFilePath') + getAttrib('TargetImage') + '.bmp', pos=(0, getAttrib('TargetPosition')))
        fixation_end = visual.TextStim(win, text='+', height=0.1)
        # Start routine for fixation start
        fixation_start.draw()
        win.flip()
        core.wait(getAttrib('DurationOfFixation') / 1000)
        # Update onset attributes (dummy values for illustration)
        setAttrib('SlideFixationStart.OnsetDelay', 0)
        setAttrib('SlideFixationStart.OnsetTime', core.getTime())
        setAttrib('SlideFixationStart.DurationError', 0)
        # Start routine for warning
        warning.draw()
        warning2.draw()
        win.flip()
        core.wait(getAttrib('IntervalBetweenCueAndTarget') / 1000)
        # Start routine for fixation middle
        fixation_middle.draw()
        win.flip()
        core.wait(getAttrib('IntervalBetweenCueAndTarget') / 1000)
        # Start routine for target
        target.draw()
        win.flip()
        keys = event.waitKeys(maxWait=getAttrib('DurationOfTarget') / 1000, keyList=['space'], timeStamped=True)
        # Update target response attributes
        if keys:
            key, rt = keys[0]
            setAttrib('SlideTarget.RT', rt)
            setAttrib('SlideTarget.RESP', key)
            setAttrib('SlideTarget.ACC', 1 if key == getAttrib('CorrectAnswer') else 0)
        else:
            setAttrib('SlideTarget.RT', None)
            setAttrib('SlideTarget.RESP', None)
            setAttrib('SlideTarget.ACC', 0)

        # Provide feedback (dummy feedback)
        #feedback_text = "ACC=%s, RESP=%s, RT=%s" % (getAttrib('SlideTarget.ACC'), getAttrib('SlideTarget.RESP'), getAttrib('SlideTarget.RT'))
        #feedback = visual.TextStim(win, text=feedback_text)
        #feedback.draw()
        #win.flip()
        #core.wait(1)  # Display feedback for 1 second
        # Adjust fixation end duration
        if getAttrib('SlideTarget.RT'):
            setAttrib('DurationOfFixationEnd', getAttrib('DurationOfFixationEnd') - getAttrib('DurationOfFixation') + (2000 - getAttrib('SlideTarget.RT')) + 1000 - 40)
        else:
            setAttrib('DurationOfFixationEnd', getAttrib('DurationOfFixationEnd') - getAttrib('DurationOfFixation') + 1000 - 40)
        pass
        # Start routine for fixation end
        fixation_end.draw()
        win.flip()
        core.wait(getAttrib('DurationOfFixationEnd') / 1000)
    thisExp.addData('SlideTarget.RT', getAttrib('SlideTarget.RT'))
    thisExp.addData('SlideTarget.ACC', getAttrib('SlideTarget.ACC'))
    thisExp.addData('SlideTarget.RESP', getAttrib('SlideTarget.RESP'))
    thisExp.nextEntry()
def session_proc_run():
    logging.console.setLevel(logging.DATA)  # Set the logging level to DATA
    # Run Intro
    run_intro(intro_text)
    # Run IFISBlockList equivalent
    run_block(block)
    # Run Goodbye
    run_goodbye(goodbye_text)
    # Log the context (for the sake of this example, we'll log a simple message)
    logging.log(level=logging.DATA, msg="Session completed")



# Create and initialize the text display
startInstruction_display = InitTextDisplayDefaults(win, text_content=startInstruction_Text)
# Drawing the stimulus
startInstruction_display.draw()
# Flip the window to update the display
win.flip()
# Wait for a key press to end
event.waitKeys(keyList=['s'])