# !/usr/bin/env python
# This Python script allows you to download YouTube videos in either MP4 (video) or MP3 (audio) format.
import os
import sys
import re
import subprocess
import platform
from pathlib import Path


def sanitize_filename(filename):
    """Remove invalid characters from filename"""
    return re.sub(r'[\\/*?:"<>|]', "", filename)


def check_ffmpeg():
    """Check if ffmpeg is available in the system"""
    try:
        # Try to run ffmpeg to check if it's installed
        subprocess.run(['ffmpeg', '-version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
        return True
    except FileNotFoundError:
        return False


def download_youtube(url, format_choice):
    """Download YouTube video in specified format using yt-dlp"""
    try:
        print(f"\nPreparing to download from: {url}")

        # Create downloads directory if it doesn't exist
        if platform.system() == 'Windows':
            downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")
        else:
            downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")

        os.makedirs(downloads_dir, exist_ok=True)

        if format_choice.lower() == 'mp4':
            print("Downloading video in MP4 format...")

            # Command for downloading video in mp4 format
            command = [
                'yt-dlp',
                '-f', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                '-o', os.path.join(downloads_dir, '%(title)s.%(ext)s'),
                '--no-playlist',
                url
            ]

            # Execute the command
            result = subprocess.run(command, capture_output=True, text=True)

            if result.returncode != 0:
                print(f"Error: {result.stderr}")
                return False

            print(f"\nVideo download completed successfully!")
            # Extract filename from output
            for line in result.stdout.split('\n'):
                if "Destination" in line and ".mp4" in line:
                    filename = line.split("Destination: ")[1].strip()
                    print(f"File saved as: {filename}")
                    break

        elif format_choice.lower() == 'mp3':
            print("Downloading audio in MP3 format...")

            # Check if ffmpeg is installed for MP3 conversion
            if not check_ffmpeg():
                print("\nError: ffmpeg is not installed or not in your PATH.")
                print("MP3 conversion requires ffmpeg to be installed.")

                if platform.system() == 'Windows':
                    print("\nTo install ffmpeg on Windows:")
                    print("1. Download from https://ffmpeg.org/download.html")
                    print("2. Extract the files to a folder (e.g., C:\\ffmpeg)")
                    print("3. Add the bin folder to your PATH environment variable")
                    print("   (e.g., C:\\ffmpeg\\bin)")
                    print("4. Restart your command prompt or terminal")
                elif platform.system() == 'Darwin':  # macOS
                    print("\nTo install ffmpeg on macOS using Homebrew:")
                    print("brew install ffmpeg")
                else:  # Linux
                    print("\nTo install ffmpeg on Ubuntu/Debian:")
                    print("sudo apt-get install ffmpeg")
                    print("\nOn Fedora:")
                    print("sudo dnf install ffmpeg")

                return False

            # Command for downloading audio in mp3 format
            command = [
                'yt-dlp',
                '-x',
                '--audio-format', 'mp3',
                '--audio-quality', '0',  # 0 is best
                '-o', os.path.join(downloads_dir, '%(title)s.%(ext)s'),
                '--no-playlist',
                url
            ]

            # Execute the command
            result = subprocess.run(command, capture_output=True, text=True)

            if result.returncode != 0:
                print(f"Error: {result.stderr}")
                return False

            print(f"\nAudio download completed successfully!")
            # Extract filename from output
            for line in result.stdout.split('\n'):
                if "Destination" in line and ".mp3" in line:
                    filename = line.split("Destination: ")[1].strip()
                    print(f"File saved as: {filename}")
                    break

        else:
            print("Invalid format choice. Please choose either 'mp3' or 'mp4'.")
            return False

        return True

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False


def main():
    print("===== YouTube Downloader =====")
    print("This script downloads YouTube videos as MP3 or MP4")
    print("Downloads will be saved to your ~/Downloads directory")

    while True:
        # Get YouTube URL
        url = input("\nEnter YouTube URL (or 'q' to quit): ")

        if url.lower() == 'q':
            print("Exiting program. Goodbye!")
            sys.exit(0)

        # Get format choice
        format_choice = input("Choose format (mp3/mp4): ")

        if format_choice.lower() not in ['mp3', 'mp4']:
            print("Invalid format! Please choose either 'mp3' or 'mp4'.")
            continue

        # Download the video
        success = download_youtube(url, format_choice)

        if success:
            print("\nDownload successful!")
        else:
            print("\nDownload failed. Please check the URL and try again.")

        # Ask if user wants to download another video
        another = input("\nDownload another video? (y/n): ")
        if another.lower() != 'y':
            print("Exiting program. Goodbye!")
            break


if __name__ == "__main__":
    main()
