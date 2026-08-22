"""Track Data Models"""
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class TrackMetadata(BaseModel):
    """Track metadata model"""
    title: str
    artist: str
    album: Optional[str] = None
    album_artist: Optional[str] = None
    duration: int  # seconds
    year: Optional[int] = None
    genre: Optional[str] = None
    track_number: Optional[int] = None
    total_tracks: Optional[int] = None
    artwork_url: Optional[str] = None
    lyrics: Optional[str] = None
    isrc: Optional[str] = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "title": "Bohemian Rhapsody",
                "artist": "Queen",
                "album": "A Night at the Opera",
                "duration": 354,
                "year": 1975,
                "genre": "Rock",
                "track_number": 11
            }
        }


class Track(BaseModel):
    """Track information model"""
    id: str = Field(..., description="Unique track identifier")
    provider: str = Field(..., description="Source provider (e.g., 'local', 'spotify')")
    metadata: TrackMetadata
    url: Optional[str] = None
    file_path: Optional[str] = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": "track_123",
                "provider": "local",
                "metadata": {
                    "title": "Bohemian Rhapsody",
                    "artist": "Queen",
                    "album": "A Night at the Opera",
                    "duration": 354
                }
            }
        }


class TrackSearchQuery(BaseModel):
    """Track search query model"""
    query: str = Field(..., min_length=1, description="Search query")
    providers: Optional[List[str]] = Field(default=None, description="Specific providers to search")
    limit: int = Field(default=10, ge=1, le=100, description="Maximum results")
    offset: int = Field(default=0, ge=0, description="Result offset")
    
    class Config:
        json_schema_extra = {
            "example": {
                "query": "Bohemian Rhapsody",
                "providers": ["local", "spotify"],
                "limit": 20
            }
        }


class TrackSearchResult(BaseModel):
    """Track search result model"""
    tracks: List[Track]
    total: int = Field(..., description="Total number of results")
    query: str
    provider: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "tracks": [],
                "total": 1,
                "query": "Bohemian Rhapsody",
                "provider": "local"
            }
        }


class TrackDownloadOptions(BaseModel):
    """Track download options model"""
    format: str = Field(default="mp3", description="Audio format")
    quality: int = Field(default=320, ge=64, le=320, description="Bitrate in kbps")
    embed_metadata: bool = Field(default=True, description="Embed metadata in file")
    download_artwork: bool = Field(default=True, description="Download and embed artwork")
    download_lyrics: bool = Field(default=True, description="Download and embed lyrics")
    folder_template: Optional[str] = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "format": "mp3",
                "quality": 320,
                "embed_metadata": True,
                "download_artwork": True,
                "download_lyrics": True,
                "folder_template": "{artist}/{album}/{track_number} - {title}"
            }
        }


class TrackDownloadRequest(BaseModel):
    """Track download request model"""
    track_id: str
    provider: str
    options: TrackDownloadOptions = Field(default_factory=TrackDownloadOptions)
    
    class Config:
        json_schema_extra = {
            "example": {
                "track_id": "track_123",
                "provider": "local",
                "options": {
                    "format": "mp3",
                    "quality": 320
                }
            }
        }


class DownloadStatus(BaseModel):
    """Download status model"""
    task_id: str
    track_id: str
    status: str = Field(..., description="Status: pending, downloading, completed, failed")
    progress: float = Field(default=0.0, ge=0.0, le=100.0, description="Progress percentage")
    file_path: Optional[str] = None
    error: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    
    class Config:
        json_schema_extra = {
            "example": {
                "task_id": "task_123",
                "track_id": "track_123",
                "status": "downloading",
                "progress": 45.5,
                "created_at": "2024-01-01T00:00:00",
                "updated_at": "2024-01-01T00:05:00"
            }
        }
