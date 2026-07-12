class AIApplicationError(Exception):
    pass
class APIConnectionTimeoutError(AIApplicationError):
    pass
class ProviderRateLimitError(AIApplicationError):
    pass