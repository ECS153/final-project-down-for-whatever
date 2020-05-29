class TimestampedMessage:
    def __init__(self, message: bytes, timestamp: int):
        self.message = message
        self.timestamp = timestamp
    
    def __gt__(self, other):
        return other.timestamp > self.timestamp
    
    def to_bytes(self):
        result = bytearray(self.message)
        result.append(self.timestamp)
        return bytes(result)
    
    def timestamp_in_left_open_interval(self, lower_bound, upper_bound):
        return self.timestamp > lower_bound and upper_bound >= self.timestamp