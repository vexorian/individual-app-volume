#!/bin/python3

import subprocess
import sys
import os


SINK_INPUT='Sink Input #'
PROCESS_BINARY="application.process.binary = \""

wanted = sys.argv[1]
volume = sys.argv[2]


#check_output returns byte string
stdoutdata = subprocess.check_output("LANG=EN pactl list sink-inputs", shell=True).decode("utf-8")
sink = None
for line in stdoutdata.splitlines():
    if line.startswith(SINK_INPUT):
        sink = int( line[len(SINK_INPUT) : ] )
    trimmed = line.strip()
    if trimmed.startswith(PROCESS_BINARY):
        binary = trimmed[len(PROCESS_BINARY):-1]
        if binary == wanted:
            os.system( "pactl set-sink-input-volume %d \"%s\"" % (sink, volume) )

    
