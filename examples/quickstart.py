"""
Quick Start Example
Simple example to get you started with YouTube API integration
"""
import os
import sys

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.logger_setup import setup_logger
from src.auth import get_authenticated_service
from src.uploader import YouTubeUploader
from src.channel import YouTubeChannel

# Setup logging
setup_logger()

def main():
    print("\n" + "="*60)
    print("YouTube Video Uploader - Quick Start")
    print("="*60 + "\n")
    
    try:
        # Step 1: Authenticate
        print("🔐 Step 1: Authenticating with YouTube...")
        service = get_authenticated_service()
        print("✅ Authentication successful!\n")
        
        # Step 2: Get channel info
        print("📺 Step 2: Getting your channel information...")
        channel = YouTubeChannel(service)
        channel_info = channel.get_my_channel()
        
        if channel_info:
            print(f"✅ Channel: {channel_info['snippet']['title']}\n")
            
            # Get stats
            stats = channel.get_channel_stats()
            print(f"📊 Channel Stats:")
            print(f"   Subscribers: {stats['subscriber_count']}")
            print(f"   Total Views: {stats['view_count']}")
            print(f"   Total Videos: {stats['video_count']}\n")
        
        # Step 3: Show recent uploads
        print("📹 Step 3: Your recent uploads:")
        recent = channel.get_recent_uploads(3)
        
        if recent:
            for i, video in enumerate(recent, 1):
                print(f"   {i}. {video['title']}")
        else:
            print("   No videos uploaded yet\n")
        
        print("\n" + "="*60)
        print("✅ Quick start completed successfully!")
        print("="*60 + "\n")
        
        print("🚀 Next Steps:")
        print("1. Run: python main.py")
        print("2. Choose option 1 to upload a video")
        print("3. Or explore advanced examples in examples/ folder\n")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\n⚠️  Make sure you've completed setup:")
        print("1. Read SETUP_GUIDE.md")
        print("2. Configure .env file")
        print("3. Place client_secret.json in credentials/ folder\n")

if __name__ == '__main__':
    main()
