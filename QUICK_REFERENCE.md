# YouTube Video Uploader - Quick Reference

Cheat sheet untuk quick access ke commands dan features.

## 🚀 Quick Start

```bash
# 1. Setup
git clone https://github.com/antonobekasi/youtube-video-uploader.git
cd youtube-video-uploader
python -m venv venv
source venv/bin/activate  # venv\Scripts\activate on Windows
pip install -r requirements.txt

# 2. Configure
cp .env.example .env
# Edit .env with your credentials

# 3. Place credentials
cp ~/Downloads/client_secret.json credentials/

# 4. Run
python main.py
```

---

## 📋 Commands

### Main Application
```bash
python main.py                    # Interactive menu
```

### Examples
```bash
python examples/quickstart.py     # Quick start
python examples/advanced_upload.py --example batch    # Batch upload
python examples/advanced_upload.py --example stats    # Get stats
python examples/advanced_upload.py --example update   # Update metadata
```

### Debugging
```bash
tail -f logs/youtube_uploader.log # View logs
rm credentials/youtube_credentials.pickle  # Clear cache
rm credentials/client_secret.json && python main.py  # Re-setup
```

---

## 🔧 Configuration

### .env Variables
```env
# Required
YOUTUBE_CLIENT_ID=your_id.apps.googleusercontent.com
YOUTUBE_CLIENT_SECRET=your_secret

# Optional
YOUTUBE_REDIRECT_URI=http://localhost:8080/
VIDEO_TITLE=My Video
VIDEO_DESCRIPTION=Description
VIDEO_TAGS=tag1,tag2
VIDEO_CATEGORY=22
VIDEO_PRIVACY_STATUS=private
LOG_LEVEL=INFO
```

### Privacy Status Values
- `private` - Only you
- `unlisted` - Link only
- `public` - Everyone

### Category IDs
| 1 | 10 | 15 | 17 | 18 | 20 | 22 | 24 | 25 | 27 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Film | Music | Pets | Sports | Shorts | Gaming | Blogs | Entertainment | News | Education |

---

## 💻 API Usage

### Simple Upload
```python
from src.auth import get_authenticated_service
from src.uploader import YouTubeUploader

service = get_authenticated_service()
uploader = YouTubeUploader(service)

result = uploader.upload_video(
    video_path='video.mp4',
    title='My Video',
    privacy_status='private'
)

print(result['url'])  # https://youtube.com/watch?v=...
```

### Get Channel Info
```python
from src.channel import YouTubeChannel

channel = YouTubeChannel(service)
info = channel.get_my_channel()
stats = channel.get_channel_stats()
recent = channel.get_recent_uploads(10)
```

### Batch Upload
```python
videos = [
    {'path': 'video1.mp4', 'title': 'Video 1'},
    {'path': 'video2.mp4', 'title': 'Video 2'}
]

for video in videos:
    uploader.upload_video(video_path=video['path'], 
                          title=video['title'])
```

---

## 📂 File Structure
```
youtube-video-uploader/
├── config/youtube_config.py     # Config
├── src/
│   ├── auth.py                 # OAuth
│   ├── uploader.py             # Upload
│   ├── channel.py              # Channel info
│   └── logger_setup.py         # Logging
├── examples/
│   ├── quickstart.py           # Quick start
│   └── advanced_upload.py      # Advanced
├── credentials/                # Credentials (auto-created)
├── videos/                     # Video files
├── logs/                       # Log files
├── main.py                     # Main app
├── .env.example                # Template
├── README.md                   # Full docs
└── requirements.txt            # Dependencies
```

---

## 🐛 Common Issues

| Issue | Solution |
|-------|----------|
| `client_secret.json` not found | Place file in `credentials/` folder |
| Invalid credentials | Re-download from Google Cloud Console |
| Redirect URI mismatch | Set `YOUTUBE_REDIRECT_URI=http://localhost:8080/` |
| Video stuck uploading | Check connection, try smaller file |
| Permission denied | `chmod 755 credentials/` |
| Module not found | `pip install -r requirements.txt` |
| .env not loaded | Spaces in .env file? Check format |
| Video upload error | Check file format (MP4/AVI/MOV) |

---

## 📚 Documentation

- **README.md** - Full documentation (Indonesian)
- **SETUP_GUIDE.md** - Step-by-step setup
- **API_REFERENCE.md** - Complete API docs
- **PROJECT_STRUCTURE.md** - Project structure
- **TROUBLESHOOTING.md** - Troubleshooting guide
- **QUICK_REFERENCE.md** - This file

---

## 🔗 Links

- [YouTube Data API v3](https://developers.google.com/youtube/v3)
- [OAuth 2.0 Guide](https://developers.google.com/identity/protocols/oauth2)
- [Google Cloud Console](https://console.cloud.google.com/)
- [YouTube Studio](https://studio.youtube.com/)

---

## 📞 Support

1. Check **TROUBLESHOOTING.md**
2. Review logs: `tail -f logs/youtube_uploader.log`
3. Read **API_REFERENCE.md**
4. Check **SETUP_GUIDE.md**

---

**Happy uploading! 🎬**
