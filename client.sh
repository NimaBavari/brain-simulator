#!/bin/bash
cd $(dirname "$SCRIPT")
if [[ -z $VIRTUAL_ENV ]]
then
    echo "Activating detected virtualenv..."
    source simenv/bin/activate
fi

simenv/bin/python -m websockets "ws://$output_websocket_host:$output_websocket_port/"
