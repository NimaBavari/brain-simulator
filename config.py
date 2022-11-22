import os

DECAY_DIFF_PER_SEC = 1.97e-9  # Based on an annual 6% decay level
RADIUS_REL_SIZE = 0.03

REDIS_CLIENT_PARAMS = {"host": "localhost", "port": 6379, "db": 0}
OUTPUT_WEBSOCKET_HOST = os.getenv("output_websocket_host", "localhost")
OUTPUT_WEBSOCKET_PORT = os.getenv("output_websocket_port", 8767)
