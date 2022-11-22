#!/bin/bash
cd $(dirname "$SCRIPT")
if [ ! -d "$(dirname '$SCRIPT')/simenv" ]
then
    echo "Creating virtualenv..."
    python3 -m venv simenv

    echo "Activating virtualenv..."
    source simenv/bin/activate
elif [ -z $VIRTUAL_ENV ]
then
    echo "Activating detected virtualenv..."
    source simenv/bin/activate
fi

echo "Installing requirements..."
simenv/bin/pip install -r requirements.txt

echo "Build is complete."

read -p "Enter output host (skip for localhost): " output_websocket_host
[ -z "$output_websocket_host" ] && output_websocket_host="localhost"
export output_websocket_host

read -p "Enter output port (skip for 8767): " output_websocket_port
[ -z "$output_websocket_port" ] && output_websocket_port=8767
export output_websocket_port

simenv/bin/python server.py
