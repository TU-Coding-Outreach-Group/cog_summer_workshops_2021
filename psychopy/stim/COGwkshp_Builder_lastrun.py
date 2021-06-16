#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.10),
    on Fri Jun 11 15:54:14 2021
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.10'
expName = 'COGwkshp_Benear'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/susanbenear/Google_Drive/Talks and Posters/Presentations/COG Workshop 2021/stim/COGwkshp_Builder_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Intro"
IntroClock = core.Clock()
introtext = visual.TextStim(win=win, name='introtext',
    text='Welcome to the experiment! \n\nClick the space bar to continue.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
introresponse = keyboard.Keyboard()

# Initialize components for Routine "Encoding"
EncodingClock = core.Clock()
encodingimage = visual.ImageStim(
    win=win,
    name='encodingimage', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
encodingaudio = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='encodingaudio')
encodingaudio.setVolume(1)
encodingtext = visual.TextStim(win=win, name='encodingtext',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.08, wrapWidth=1, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "FactTest"
FactTestClock = core.Clock()
facttestimage = visual.ImageStim(
    win=win,
    name='facttestimage', 
    image='sin', mask=None,
    ori=0, pos=(0, .2), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
factquestiontext = visual.TextStim(win=win, name='factquestiontext',
    text='default text',
    font='Arial',
    pos=(0, -.1), height=0.06, wrapWidth=1.7, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
factACtext = visual.TextStim(win=win, name='factACtext',
    text='default text',
    font='Arial',
    pos=(0, -.3), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
factresponse = keyboard.Keyboard()

# Initialize components for Routine "SourceTest"
SourceTestClock = core.Clock()
sourcetext = visual.TextStim(win=win, name='sourcetext',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
sourceresponse = keyboard.Keyboard()

# Initialize components for Routine "Exit"
ExitClock = core.Clock()
exittext = visual.TextStim(win=win, name='exittext',
    text='Thank you for participating!\n\nClick the space bar to quit.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
exitresponse = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Intro"-------
continueRoutine = True
# update component parameters for each repeat
introresponse.keys = []
introresponse.rt = []
_introresponse_allKeys = []
# keep track of which components have finished
IntroComponents = [introtext, introresponse]
for thisComponent in IntroComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
IntroClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Intro"-------
while continueRoutine:
    # get current time
    t = IntroClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=IntroClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *introtext* updates
    if introtext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        introtext.frameNStart = frameN  # exact frame index
        introtext.tStart = t  # local t and not account for scr refresh
        introtext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(introtext, 'tStartRefresh')  # time at next scr refresh
        introtext.setAutoDraw(True)
    
    # *introresponse* updates
    waitOnFlip = False
    if introresponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        introresponse.frameNStart = frameN  # exact frame index
        introresponse.tStart = t  # local t and not account for scr refresh
        introresponse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(introresponse, 'tStartRefresh')  # time at next scr refresh
        introresponse.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(introresponse.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(introresponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if introresponse.status == STARTED and not waitOnFlip:
        theseKeys = introresponse.getKeys(keyList=['space'], waitRelease=False)
        _introresponse_allKeys.extend(theseKeys)
        if len(_introresponse_allKeys):
            introresponse.keys = _introresponse_allKeys[-1].name  # just the last key pressed
            introresponse.rt = _introresponse_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in IntroComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Intro"-------
for thisComponent in IntroComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('semepistim.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Encoding"-------
    continueRoutine = True
    routineTimer.add(6.000000)
    # update component parameters for each repeat
    encodingimage.setImage(animalimage)
    encodingaudio.setSound(questionaudio, secs=6, hamming=True)
    encodingaudio.setVolume(1, log=False)
    encodingtext.setPos((0, .3))
    encodingtext.setText(animalname)
    # keep track of which components have finished
    EncodingComponents = [encodingimage, encodingaudio, encodingtext]
    for thisComponent in EncodingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    EncodingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Encoding"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = EncodingClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=EncodingClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *encodingimage* updates
        if encodingimage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            encodingimage.frameNStart = frameN  # exact frame index
            encodingimage.tStart = t  # local t and not account for scr refresh
            encodingimage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(encodingimage, 'tStartRefresh')  # time at next scr refresh
            encodingimage.setAutoDraw(True)
        if encodingimage.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > encodingimage.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                encodingimage.tStop = t  # not accounting for scr refresh
                encodingimage.frameNStop = frameN  # exact frame index
                win.timeOnFlip(encodingimage, 'tStopRefresh')  # time at next scr refresh
                encodingimage.setAutoDraw(False)
        # start/stop encodingaudio
        if encodingaudio.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            encodingaudio.frameNStart = frameN  # exact frame index
            encodingaudio.tStart = t  # local t and not account for scr refresh
            encodingaudio.tStartRefresh = tThisFlipGlobal  # on global time
            encodingaudio.play(when=win)  # sync with win flip
        if encodingaudio.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > encodingaudio.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                encodingaudio.tStop = t  # not accounting for scr refresh
                encodingaudio.frameNStop = frameN  # exact frame index
                win.timeOnFlip(encodingaudio, 'tStopRefresh')  # time at next scr refresh
                encodingaudio.stop()
        
        # *encodingtext* updates
        if encodingtext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            encodingtext.frameNStart = frameN  # exact frame index
            encodingtext.tStart = t  # local t and not account for scr refresh
            encodingtext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(encodingtext, 'tStartRefresh')  # time at next scr refresh
            encodingtext.setAutoDraw(True)
        if encodingtext.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > encodingtext.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                encodingtext.tStop = t  # not accounting for scr refresh
                encodingtext.frameNStop = frameN  # exact frame index
                win.timeOnFlip(encodingtext, 'tStopRefresh')  # time at next scr refresh
                encodingtext.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EncodingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Encoding"-------
    for thisComponent in EncodingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    encodingaudio.stop()  # ensure sound has stopped at end of routine
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('semepistim.csv'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "FactTest"-------
    continueRoutine = True
    # update component parameters for each repeat
    facttestimage.setImage(animalimage)
    factquestiontext.setText(question)
    factACtext.setText(lettera + choicea + '\n' + letterb + choiceb)
    factresponse.keys = []
    factresponse.rt = []
    _factresponse_allKeys = []
    # keep track of which components have finished
    FactTestComponents = [facttestimage, factquestiontext, factACtext, factresponse]
    for thisComponent in FactTestComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    FactTestClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "FactTest"-------
    while continueRoutine:
        # get current time
        t = FactTestClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FactTestClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *facttestimage* updates
        if facttestimage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            facttestimage.frameNStart = frameN  # exact frame index
            facttestimage.tStart = t  # local t and not account for scr refresh
            facttestimage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(facttestimage, 'tStartRefresh')  # time at next scr refresh
            facttestimage.setAutoDraw(True)
        
        # *factquestiontext* updates
        if factquestiontext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            factquestiontext.frameNStart = frameN  # exact frame index
            factquestiontext.tStart = t  # local t and not account for scr refresh
            factquestiontext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(factquestiontext, 'tStartRefresh')  # time at next scr refresh
            factquestiontext.setAutoDraw(True)
        
        # *factACtext* updates
        if factACtext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            factACtext.frameNStart = frameN  # exact frame index
            factACtext.tStart = t  # local t and not account for scr refresh
            factACtext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(factACtext, 'tStartRefresh')  # time at next scr refresh
            factACtext.setAutoDraw(True)
        
        # *factresponse* updates
        waitOnFlip = False
        if factresponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            factresponse.frameNStart = frameN  # exact frame index
            factresponse.tStart = t  # local t and not account for scr refresh
            factresponse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(factresponse, 'tStartRefresh')  # time at next scr refresh
            factresponse.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(factresponse.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(factresponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if factresponse.status == STARTED and not waitOnFlip:
            theseKeys = factresponse.getKeys(keyList=['a', 'b'], waitRelease=False)
            _factresponse_allKeys.extend(theseKeys)
            if len(_factresponse_allKeys):
                factresponse.keys = _factresponse_allKeys[-1].name  # just the last key pressed
                factresponse.rt = _factresponse_allKeys[-1].rt
                # was this correct?
                if (factresponse.keys == str(correctanswer)) or (factresponse.keys == correctanswer):
                    factresponse.corr = 1
                else:
                    factresponse.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FactTestComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "FactTest"-------
    for thisComponent in FactTestComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if factresponse.keys in ['', [], None]:  # No response was made
        factresponse.keys = None
        # was no response the correct answer?!
        if str(correctanswer).lower() == 'none':
           factresponse.corr = 1;  # correct non-response
        else:
           factresponse.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('factresponse.keys',factresponse.keys)
    trials_2.addData('factresponse.corr', factresponse.corr)
    if factresponse.keys != None:  # we had a response
        trials_2.addData('factresponse.rt', factresponse.rt)
    trials_2.addData('factresponse.started', factresponse.tStartRefresh)
    trials_2.addData('factresponse.stopped', factresponse.tStopRefresh)
    # the Routine "FactTest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "SourceTest"-------
    continueRoutine = True
    # update component parameters for each repeat
    sourcetext.setText('Did a male or female voice tell you this fact?\n\na. Male \nb. Female')
    sourceresponse.keys = []
    sourceresponse.rt = []
    _sourceresponse_allKeys = []
    # keep track of which components have finished
    SourceTestComponents = [sourcetext, sourceresponse]
    for thisComponent in SourceTestComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    SourceTestClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "SourceTest"-------
    while continueRoutine:
        # get current time
        t = SourceTestClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=SourceTestClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *sourcetext* updates
        if sourcetext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sourcetext.frameNStart = frameN  # exact frame index
            sourcetext.tStart = t  # local t and not account for scr refresh
            sourcetext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sourcetext, 'tStartRefresh')  # time at next scr refresh
            sourcetext.setAutoDraw(True)
        
        # *sourceresponse* updates
        waitOnFlip = False
        if sourceresponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sourceresponse.frameNStart = frameN  # exact frame index
            sourceresponse.tStart = t  # local t and not account for scr refresh
            sourceresponse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sourceresponse, 'tStartRefresh')  # time at next scr refresh
            sourceresponse.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(sourceresponse.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(sourceresponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if sourceresponse.status == STARTED and not waitOnFlip:
            theseKeys = sourceresponse.getKeys(keyList=['a', 'b'], waitRelease=False)
            _sourceresponse_allKeys.extend(theseKeys)
            if len(_sourceresponse_allKeys):
                sourceresponse.keys = _sourceresponse_allKeys[-1].name  # just the last key pressed
                sourceresponse.rt = _sourceresponse_allKeys[-1].rt
                # was this correct?
                if (sourceresponse.keys == str(sourceanswer)) or (sourceresponse.keys == sourceanswer):
                    sourceresponse.corr = 1
                else:
                    sourceresponse.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SourceTestComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "SourceTest"-------
    for thisComponent in SourceTestComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if sourceresponse.keys in ['', [], None]:  # No response was made
        sourceresponse.keys = None
        # was no response the correct answer?!
        if str(sourceanswer).lower() == 'none':
           sourceresponse.corr = 1;  # correct non-response
        else:
           sourceresponse.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('sourceresponse.keys',sourceresponse.keys)
    trials_2.addData('sourceresponse.corr', sourceresponse.corr)
    if sourceresponse.keys != None:  # we had a response
        trials_2.addData('sourceresponse.rt', sourceresponse.rt)
    # the Routine "SourceTest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_2'


# ------Prepare to start Routine "Exit"-------
continueRoutine = True
# update component parameters for each repeat
exitresponse.keys = []
exitresponse.rt = []
_exitresponse_allKeys = []
# keep track of which components have finished
ExitComponents = [exittext, exitresponse]
for thisComponent in ExitComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ExitClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Exit"-------
while continueRoutine:
    # get current time
    t = ExitClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ExitClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *exittext* updates
    if exittext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        exittext.frameNStart = frameN  # exact frame index
        exittext.tStart = t  # local t and not account for scr refresh
        exittext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(exittext, 'tStartRefresh')  # time at next scr refresh
        exittext.setAutoDraw(True)
    
    # *exitresponse* updates
    waitOnFlip = False
    if exitresponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        exitresponse.frameNStart = frameN  # exact frame index
        exitresponse.tStart = t  # local t and not account for scr refresh
        exitresponse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(exitresponse, 'tStartRefresh')  # time at next scr refresh
        exitresponse.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(exitresponse.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(exitresponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if exitresponse.status == STARTED and not waitOnFlip:
        theseKeys = exitresponse.getKeys(keyList=['space'], waitRelease=False)
        _exitresponse_allKeys.extend(theseKeys)
        if len(_exitresponse_allKeys):
            exitresponse.keys = _exitresponse_allKeys[-1].name  # just the last key pressed
            exitresponse.rt = _exitresponse_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ExitComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Exit"-------
for thisComponent in ExitComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Exit" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
