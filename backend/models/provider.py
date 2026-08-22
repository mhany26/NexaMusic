"""Provider Data Models"""
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List
from enum import Enum


class ProviderType(str, Enum):
    """Provider type enumeration"""
    LOCAL = "local"
    SPOTIFY = "spotify"
    YOUTUBE = "youtube"
    SOUNDCLOUD = "soundcloud"
    APPLE_MUSIC = "apple_music"
    TIDAL = "tidal"


class ProviderStatus(str, Enum):
    """Provider status enumeration"""
    ACTIVE = "active"
    INACTIVE = "inactive"
    ERROR = "error"
    RATE_LIMITED = "rate_limited"


class ProviderConfig(BaseModel):
    """Provider configuration model"""
    type: ProviderType
    enabled: bool = True
    priority: int = Field(default=0, ge=0, description="Provider priority for search")
    api_key: Optional[str] = None
    secret_key: Optional[str] = None
    endpoint: Optional[str] = None
    timeout: int = Field(default=30, ge=5, description="Request timeout in seconds")
    retry_attempts: int = Field(default=3, ge=1, le=10)
    retry_delay: int = Field(default=1, ge=1, description="Retry delay in seconds")
    extra_config: Dict[str, Any] = Field(default_factory=dict)
    
    class Config:
        json_schema_extra = {
            "example": {
                "type": "local",
                "enabled": True,
                "priority": 1,
                "timeout": 30,
                "retry_attempts": 3
            }
        }


class ProviderCapabilities(BaseModel):
    """Provider capabilities model"""
    search: bool = True
    stream: bool = True
    download: bool = False
    metadata: bool = True
    lyrics: bool = False
    artwork: bool = True
    playlist: bool = False
    recommendations: bool = False
    
    class Config:
        json_schema_extra = {
            "example": {
                "search": True,
                "stream": True,
                "download": False,
                "metadata": True,
                "lyrics": False,
                "artwork": True,
                "playlist": False,
                "recommendations": False
            }
        }


class ProviderInfo(BaseModel):
    """Provider information model"""
    type: ProviderType
    name: str
    version: str
    status: ProviderStatus
    capabilities: ProviderCapabilities
    supported_formats: List[str] = Field(default_factory=lambda: ["mp3"])
    rate_limit: Optional[int] = None  # requests per minute
    last_error: Optional[str] = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "type": "local",
                "name": "Local Music Provider",
                "version": "1.0.0",
                "status": "active",
                "capabilities": {
                    "search": True,
                    "stream": False,
                    "download": True,
                    "metadata": True
                },
                "supported_formats": ["mp3", "flac", "wav"]
            }
        }


class ProviderHealthCheck(BaseModel):
    """Provider health check model"""
    provider: ProviderType
    status: ProviderStatus
    response_time: float  # milliseconds
    success_rate: float = Field(..., ge=0.0, le=1.0)
    last_checked: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "provider": "local",
                "status": "active",
                "response_time": 25.5,
                "success_rate": 0.99,
                "last_checked": "2024-01-01T00:00:00"
            }
        }


class AuthCredentials(BaseModel):
    """Authentication credentials model"""
    provider: ProviderType
    username: Optional[str] = None
    password: Optional[str] = None
    api_key: Optional[str] = None
    refresh_token: Optional[str] = None
    access_token: Optional[str] = None
    expires_at: Optional[str] = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "provider": "spotify",
                "api_key": "xxx_api_key_xxx",
                "access_token": "xxx_access_token_xxx"
            }
        }


class ProviderStats(BaseModel):
    """Provider statistics model"""
    provider: ProviderType
    total_requests: int = 0
    successful_requests: int = 0
    failed_requests: int = 0
    rate_limit_hits: int = 0
    avg_response_time: float = 0.0  # milliseconds
    
    @property
    def success_rate(self) -> float:
        """Calculate success rate"""
        if self.total_requests == 0:
            return 0.0
        return self.successful_requests / self.total_requests
    
    class Config:
        json_schema_extra = {
            "example": {
                "provider": "local",
                "total_requests": 100,
                "successful_requests": 99,
                "failed_requests": 1,
                "rate_limit_hits": 0,
                "avg_response_time": 25.5
            }
        }
