#!/bin/bash

RESOURCES='./resources'
notify-send --icon=checkbox,terminal 'Waka Time Notification' 'Daemon started'
aplay -q $RESOURCES/start.wav