import redis

from config import REDIS_CLIENT_PARAMS

from .utils import event_feeder, freq_feeder

redis_client = redis.StrictRedis(**REDIS_CLIENT_PARAMS)

__all__ = ["event_feeder", "freq_feeder", "redis_client"]
