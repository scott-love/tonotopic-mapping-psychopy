#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Sun Nov  6 22:57:38 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '4'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

import random
import numpy as np


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'broad'  # from the Builder filename that created this script
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
    originPath='/Users/slove/GDrive/projects/SheepVoicefMRI/stim-code/broadband-sparse-testing/Broadband_tonotopy.py',
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
    size=[2560, 1440], fullscr=True, screen=0, 
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

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "setup"
setupClock = core.Clock()
frequencies = np.arange(125,8000)

dx = 4/7875
X  = np.arange(-2, 2, dx)
Y  = np.exp(-X ** 2)
Y /= (dx * Y).sum()
CY = np.cumsum(Y * dx)
CY = CY/sum(CY)

nsoundblocks = 16
nblocksTotal = 65
nbeepsblock = 88

band = ['low','high']
sband = np.repeat("silence",nbeepsblock)
hband = np.repeat("high",nbeepsblock)
lband = np.repeat("low",nbeepsblock)
svolume = np.ones(nbeepsblock)*0
lvolume = np.ones(nbeepsblock)*1
hvolume = np.ones(nbeepsblock)*1

tones = np.ones(nbeepsblock)*100
bands = sband
volumes = svolume

# Initialize components for Routine "sync"
syncClock = core.Clock()
starttext = visual.TextStim(win=win, name='starttext',
    text='Press “s” to start',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "start_TR"
start_TRClock = core.Clock()
sound_1 = sound.Sound('A', secs=1.42, stereo=True, hamming=True,
    name='sound_1')
sound_1.setVolume(0.0)

# Initialize components for Routine "play_tone"
play_toneClock = core.Clock()
count=0
Tones = sound.Sound('A', secs=0.075, stereo=True, hamming=True,
    name='Tones')
Tones.setVolume(1.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "setup"-------
continueRoutine = True
# update component parameters for each repeat
for i in range (1,nsoundblocks+1):
  random.shuffle(band)

  if band[0] == 'low':
    tones = np.hstack((tones, np.random.choice(frequencies,nbeepsblock,p=CY[::-1])))
    bands = np.hstack((bands,lband))
    volumes = np.hstack((volumes,lvolume))
    tones = np.hstack((tones, np.ones(nbeepsblock)*100))
    bands = np.hstack((bands,sband))
    volumes = np.hstack((volumes,svolume))
    tones = np.hstack((tones, np.random.choice(frequencies,nbeepsblock,p=CY)))
    bands = np.hstack((bands,hband))
    volumes = np.hstack((volumes,hvolume))
    tones = np.hstack((tones, np.ones(nbeepsblock)*100))
    bands = np.hstack((bands,sband))
    volumes = np.hstack((volumes,svolume))
  else:
    tones = np.hstack((tones, np.random.choice(frequencies,nbeepsblock,p=CY)))
    bands = np.hstack((bands,hband))
    volumes = np.hstack((volumes,hvolume))
    tones = np.hstack((tones, np.ones(nbeepsblock)*100))
    bands = np.hstack((bands,sband))
    volumes = np.hstack((volumes,svolume))
    tones = np.hstack((tones, np.random.choice(frequencies,nbeepsblock,p=CY[::-1])))
    bands = np.hstack((bands,lband))
    volumes = np.hstack((volumes,lvolume))
    tones = np.hstack((tones, np.ones(nbeepsblock)*100))
    bands = np.hstack((bands,sband))
    volumes = np.hstack((volumes,svolume))
# keep track of which components have finished
setupComponents = []
for thisComponent in setupComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
setupClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "setup"-------
while continueRoutine:
    # get current time
    t = setupClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=setupClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in setupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "setup"-------
for thisComponent in setupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
#thisExp.addData('volume', volumes)
#thisExp.addData('tones', tones)
#thisExp.addData('band', bands)
# the Routine "setup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
blocks = data.TrialHandler(nReps=nblocksTotal, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='blocks')
thisExp.addLoop(blocks)  # add the loop to the experiment
thisBlock = blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for thisBlock in blocks:
    currentLoop = blocks
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "sync"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    syncComponents = [starttext, key_resp]
    for thisComponent in syncComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    syncClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "sync"-------
    while continueRoutine:
        # get current time
        t = syncClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=syncClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *starttext* updates
        if starttext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            starttext.frameNStart = frameN  # exact frame index
            starttext.tStart = t  # local t and not account for scr refresh
            starttext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(starttext, 'tStartRefresh')  # time at next scr refresh
            starttext.setAutoDraw(True)
        
        # *key_resp* updates
        if key_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            key_resp.clock.reset()  # now t=0
            key_resp.clearEvents(eventType='keyboard')
        if key_resp.status == STARTED:
            theseKeys = key_resp.getKeys(keyList=['s'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in syncComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "sync"-------
    for thisComponent in syncComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    blocks.addData('starttext.started', starttext.tStartRefresh)
    blocks.addData('starttext.stopped', starttext.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    blocks.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        blocks.addData('key_resp.rt', key_resp.rt)
    blocks.addData('key_resp.started', key_resp.tStart)
    blocks.addData('key_resp.stopped', key_resp.tStop)
    # the Routine "sync" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "start_TR"-------
    continueRoutine = True
    routineTimer.add(1.420000)
    # update component parameters for each repeat
    sound_1.setSound('A', secs=1.42, hamming=True)
    sound_1.setVolume(0.0, log=False)
    # keep track of which components have finished
    start_TRComponents = [sound_1]
    for thisComponent in start_TRComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    start_TRClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "start_TR"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = start_TRClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=start_TRClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_1
        if sound_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.tStart = t  # local t and not account for scr refresh
            sound_1.tStartRefresh = tThisFlipGlobal  # on global time
            sound_1.play(when=win)  # sync with win flip
        if sound_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_1.tStartRefresh + 1.42-frameTolerance:
                # keep track of stop time/frame for later
                sound_1.tStop = t  # not accounting for scr refresh
                sound_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_1, 'tStopRefresh')  # time at next scr refresh
                sound_1.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in start_TRComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "start_TR"-------
    for thisComponent in start_TRComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_1.stop()  # ensure sound has stopped at end of routine
    blocks.addData('sound_1.started', sound_1.tStartRefresh)
    blocks.addData('sound_1.stopped', sound_1.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=nbeepsblock, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
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
        
        # ------Prepare to start Routine "play_tone"-------
        continueRoutine = True
        routineTimer.add(0.100000)
        # update component parameters for each repeat
        current_volumes=volumes[count]
        current_tones=tones[count]
        current_bands=bands[count]
        Tones.setSound(current_tones, secs=0.075, hamming=True)
        Tones.setVolume(current_volumes, log=False)
        # keep track of which components have finished
        play_toneComponents = [Tones]
        for thisComponent in play_toneComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        play_toneClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "play_tone"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = play_toneClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=play_toneClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # start/stop Tones
            if Tones.status == NOT_STARTED and tThisFlip >= 0.025-frameTolerance:
                # keep track of start time/frame for later
                Tones.frameNStart = frameN  # exact frame index
                Tones.tStart = t  # local t and not account for scr refresh
                Tones.tStartRefresh = tThisFlipGlobal  # on global time
                Tones.play(when=win)  # sync with win flip
            if Tones.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Tones.tStartRefresh + 0.075-frameTolerance:
                    # keep track of stop time/frame for later
                    Tones.tStop = t  # not accounting for scr refresh
                    Tones.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Tones, 'tStopRefresh')  # time at next scr refresh
                    Tones.stop()
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in play_toneComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "play_tone"-------
        for thisComponent in play_toneComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        if count==nblocksTotal*nbeepsblock:
            count=0
        else: count+=1
        
        
        thisExp.addData('volume', current_volumes)
        thisExp.addData('tones', current_tones)
        thisExp.addData('band', current_bands)
        Tones.stop()  # ensure sound has stopped at end of routine
        trials.addData('Tones.started', Tones.tStartRefresh)
        trials.addData('Tones.stopped', Tones.tStopRefresh)
        thisExp.nextEntry()
        
    # completed nbeepsblock repeats of 'trials'
    
# completed nblocksTotal repeats of 'blocks'


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
