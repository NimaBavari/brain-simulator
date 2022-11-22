# Human Brain Simulator

_by Nima Bavari_

Human brain Autostore-Autoload Simulator. I devised an accumulative small-precision decay automaton as my data pipeline, and used Redis cache for autostore and autoload. The simulator broadcasts the stream of autoload results over a websocket channel.

## Idea

I'd like to thank my good friend Amin Fouladi, MEng, who told me about the above autostore-autoload mechanism of the human brain and asked me to make a simulation based on this mechanism. According to Amin, human brain saves the event and the frequency of its wave at the time of the event to the back (i.e., permanent) memory every time an "event" occurs. Simultaneous to that, based on the current frequency of its wave, the brain also continuously brings to the front (i.e., temporary) memory the event associated with that frequency. But there's a twist: frequencies saved in the back memory decay over time! This means that the autostore-autoload mechanism of the human brain is a _continuous_ retrieval system, not just a discrete one (e.g., key-value pairs, relational, etc.).

### Mechanism

* Back (permanent) memory: Redis cache
* Front (temporary) memory: Websocket (output channel)
* Reality: feeders

## Usage

Run `./run.sh` to spin up the server.

Run `./client.sh` (only when the server is also running) to listen to the stream of temporary memories.

## TODO

* learning & reaction (calibration mechanism)
* simple front-end (a place to see the output)
