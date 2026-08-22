# Backend - Core Application
backend/
├── __init__.py
├── main.py
├── config.py
├── api/
│   ├── __init__.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── search.py
│   │   ├── download.py
│   │   ├── metadata.py
│   │   └── lyrics.py
│   └── websocket.py
├── providers/
│   ├── __init__.py
│   ├── base.py
│   ├── music_provider.py
│   ├── metadata_provider.py
│   ├── lyrics_provider.py
│   └── registry.py
├── providers_impl/
│   ├── __init__.py
│   └── local/
│       ├── __init__.py
│       └── provider.py
├── downloader/
│   ├── __init__.py
│   ├── manager.py
│   ├── queue.py
│   ├── task.py
│   └── progress.py
├── metadata/
│   ├── __init__.py
│   ├── parser.py
│   ├── editor.py
│   └── artwork.py
├── lyrics/
│   ├── __init__.py
│   ├── manager.py
│   └── parser.py
├── models/
│   ├── __init__.py
│   ├── track.py
│   ├── album.py
│   ├── playlist.py
│   ├── download.py
│   ├── artist.py
│   ├── artwork.py
│   ├── lyrics.py
│   ├── provider.py
│   └── settings.py
├── exceptions/
│   ├── __init__.py
│   └── errors.py
├── utils/
│   ├── __init__.py
│   ├── files.py
│   ├── strings.py
│   ├── hashes.py
│   ├── validation.py
│   └── formatting.py
└── logging_config.py

# Frontend
frontend/
├── index.html
├── css/
│   ├── main.css
│   ├── components.css
│   └── responsive.css
└── js/
    ├── app.js
    ├── api.js
    ├── downloads.js
    ├── search.js
    └── ui.js

# Directories
downloads/
temp/

# Configuration
.env.example
README.md
