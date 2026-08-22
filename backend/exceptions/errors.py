"""Custom Exception Classes for NexaMusic"""


class NexaMusicException(Exception):
    """Base exception for NexaMusic"""
    pass


class ConfigurationError(NexaMusicException):
    """Raised when configuration is invalid"""
    pass


class ProviderError(NexaMusicException):
    """Raised when provider fails"""
    pass


class ProviderNotFoundError(ProviderError):
    """Raised when provider is not found"""
    pass


class DownloadError(NexaMusicException):
    """Raised when download fails"""
    pass


class TrackNotFoundError(DownloadError):
    """Raised when track is not found"""
    pass


class InvalidTrackError(DownloadError):
    """Raised when track data is invalid"""
    pass


class MetadataError(NexaMusicException):
    """Raised when metadata operation fails"""
    pass


class MetadataNotFoundError(MetadataError):
    """Raised when metadata is not found"""
    pass


class LyricsError(NexaMusicException):
    """Raised when lyrics operation fails"""
    pass


class LyricsNotFoundError(LyricsError):
    """Raised when lyrics are not found"""
    pass


class FileOperationError(NexaMusicException):
    """Raised when file operation fails"""
    pass


class DirectoryError(FileOperationError):
    """Raised when directory operation fails"""
    pass


class InvalidPathError(FileOperationError):
    """Raised when path is invalid"""
    pass


class ValidationError(NexaMusicException):
    """Raised when validation fails"""
    pass


class InvalidFormatError(ValidationError):
    """Raised when format is invalid"""
    pass


class InvalidQualityError(ValidationError):
    """Raised when quality is invalid"""
    pass


class QueueError(NexaMusicException):
    """Raised when queue operation fails"""
    pass


class QueueFullError(QueueError):
    """Raised when queue is full"""
    pass


class TaskNotFoundError(QueueError):
    """Raised when task is not found"""
    pass


class NetworkError(NexaMusicException):
    """Raised when network operation fails"""
    pass


class TimeoutError(NetworkError):
    """Raised when operation times out"""
    pass


class APIError(NexaMusicException):
    """Raised when API call fails"""
    pass


class WebSocketError(NexaMusicException):
    """Raised when WebSocket operation fails"""
    pass
