"""Backend Configuration Management"""
from pydantic_settings import BaseSettings
from pathlib import Path
from typing import Optional


class Settings(BaseSettings):
    """Application Settings"""
    
    # Server Configuration
    backend_host: str = "127.0.0.1"
    backend_port: int = 8000
    debug: bool = True
    
    # Path Configuration
    download_dir: str = "./downloads"
    temp_dir: str = "./temp"
    log_file: str = "./logs/nexamusic.log"
    
    # Download Settings
    max_concurrent_downloads: int = 3
    default_format: str = "mp3"
    default_quality: int = 320
    
    # Metadata Settings
    embed_metadata: bool = True
    download_artwork: bool = True
    download_lyrics: bool = True
    
    # Folder Organization
    folder_template: str = "{artist}/{album}/{track_number} - {title}"
    
    # Logging
    log_level: str = "INFO"
    
    class Config:
        env_file = ".env"
        case_sensitive = False
    
    @property
    def download_path(self) -> Path:
        """Get download directory path"""
        path = Path(self.download_dir)
        path.mkdir(parents=True, exist_ok=True)
        return path
    
    @property
    def temp_path(self) -> Path:
        """Get temp directory path"""
        path = Path(self.temp_dir)
        path.mkdir(parents=True, exist_ok=True)
        return path
    
    @property
    def log_path(self) -> Path:
        """Get log directory path"""
        path = Path(self.log_file).parent
        path.mkdir(parents=True, exist_ok=True)
        return path


# Global settings instance
settings = Settings()
