#!/bin/bash
cd $(dirname "$SCRIPT")
if [[ -z $VIRTUAL_ENV ]]
then
    echo "Activating detected virtualenv..."
    source simenv/bin/activate
fi

read -p "Enter output host (skip for localhost): " output_websocket_host
[ -z "$output_websocket_host" ] && output_websocket_host="localhost"

read -p "Enter output port (skip for 8767): " output_websocket_port
[ -z "$output_websocket_port" ] && output_websocket_port=8767

simenv/bin/python -m websockets "ws://$output_websocket_host:$output_websocket_port/"
