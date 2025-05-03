# YouTube Downloader - Usage Instructions

## Overview
This Python script allows you to download YouTube videos in either MP4 (video) or MP3 (audio) format. It uses the `yt-dlp` library which is more reliable and regularly maintained than alternatives.

## Requirements
- Python 3.6 or higher
- yt-dlp library
- ffmpeg (for MP3 conversion)

## Installation

### 1. Install Python
If you don't have Python installed, download and install it from [python.org](https://www.python.org/downloads/).

### 2. Install Required Packages
Open a terminal/command prompt and run:

```bash
# Install yt-dlp
pip install yt-dlp

# Install ffmpeg (required for MP3 conversion)
# On Ubuntu/Debian:
sudo apt-get install ffmpeg

# On macOS (using Homebrew):
# brew install ffmpeg

# On Windows (Detailed):
# 1. Go to the official FFmpeg download page: https://ffmpeg.org/download.html
# 2. Under the Windows logo, click one of the recommended build links (e.g., from gyan.dev or BtbN).
# 3. Download the latest "release" build (usually a .zip file).
# 4. Extract the downloaded .zip file to a location on your computer, for example, `C:\ffmpeg`.
# 5. Add the `bin` directory inside the extracted folder (e.g., `C:\ffmpeg\bin`) to your system's PATH environment variable.
#    - Search for "Environment Variables" in the Windows search bar and select "Edit the system environment variables".
#    - Click the "Environment Variables..." button.
#    - Under "System variables" (or "User variables" for just your account), find the `Path` variable, select it, and click "Edit...".
#    - Click "New" and paste the full path to the `bin` directory (e.g., `C:\ffmpeg\bin`).
#    - Click "OK" on all windows to save the changes.
# 6. Close and reopen any command prompt or terminal windows for the changes to take effect.
# 7. You can verify the installation by opening a new command prompt and typing `ffmpeg -version`.
```

### 3. Download the Script
Save the `youtube_downloader.py` script to your computer.

## How to Use

1. Open a terminal/command prompt
2. Navigate to the directory containing the script
3. Make the script executable (Linux/macOS only):
   ```bash
   chmod +x youtube_downloader.py
   ```
4. Run the script:
   ```bash
   python youtube_downloader.py
   ```
   or on Linux/macOS:
   ```bash
   ./youtube_downloader.py
   ```

5. Follow the prompts:
   - Enter the YouTube URL when prompted
   - Choose the format (mp3 or mp4)
   - The download will begin automatically
   - Files are saved to your ~/Downloads directory

6. After download completes, you can choose to download another video or quit

## Features
- Downloads YouTube videos in highest available quality
- Converts videos to MP3 format if audio-only is desired
- Sanitizes filenames to remove invalid characters
- Creates a Downloads directory if it doesn't exist
- Provides detailed progress information

## Troubleshooting
- If you encounter errors, ensure you have the latest version of yt-dlp:
  ```bash
  pip install --upgrade yt-dlp
  ```
- For MP3 downloads, make sure ffmpeg is properly installed
- If a download fails, check your internet connection and verify the YouTube URL is correct

## Notes
- This script is for personal use only
- Please respect copyright and YouTube's terms of service
- Some videos may be restricted and cannot be downloaded
