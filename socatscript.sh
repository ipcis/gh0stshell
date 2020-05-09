#!/bin/bash

SOCKDIR=$(mktemp -d)
SOCKF=${SOCKDIR}/usock

# Start tmux, if needed
tmux start

# Create window
#tmux new-window "socat UNIX-LISTEN:${SOCKF},umask=0077 STDIO"
#tmux new "socat UNIX-LISTEN:${SOCKF},umask=0077 STDIO"
tmux new-session -d "socat UNIX-LISTEN:${SOCKF},umask=0077 STDIO"

# Wait for socket
while test ! -e ${SOCKF} ; do sleep 1 ; done

# Use socat to ship data between the unix socket and STDIO.
exec socat STDIO UNIX-CONNECT:${SOCKF}
