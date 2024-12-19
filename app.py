import streamlit as st
import subprocess
import os
import tempfile

# Function to download video and save it to a temporary directory
def download_video(url, is_playlist, quality, subtitles):
    # Create a temporary directory to save the downloaded video
    temp_dir = tempfile.mkdtemp()

    # Base command for yt-dlp
    cmd = ["yt-dlp", "-o", os.path.join(temp_dir, "%(title)s.%(ext)s")]

    # Add format options for video and audio
    if quality == "144p":
        cmd += ["-f", "bv*[height<=144][ext=mp4]+ba[ext=m4a]/bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]"]
    elif quality == "240p":
        cmd += ["-f", "bv*[height<=240][ext=mp4]+ba[ext=m4a]/bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]"]
    elif quality == "360p":
        cmd += ["-f", "bv*[height<=360][ext=mp4]+ba[ext=m4a]/bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]"]
    elif quality == "480p":
        cmd += ["-f", "bv*[height<=480][ext=mp4]+ba[ext=m4a]/bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]"]
    elif quality == "720p":
        cmd += ["-f", "bv*[height<=720][ext=mp4]+ba[ext=m4a]/bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]"]
    elif quality == "1080p":
        cmd += ["-f", "bv*[height<=1080][ext=mp4]+ba[ext=m4a]/bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]"]
    elif quality == "1440p":
        cmd += ["-f", "bv*[height<=1440][ext=mp4]+ba[ext=m4a]/bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]"]
    elif quality == "2160p":
        cmd += ["-f", "bv*[height<=2160][ext=mp4]+ba[ext=m4a]/bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]"]
    else:
        cmd += ["-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]"]

    # Set output format to mp4
    cmd += ["--merge-output-format", "mp4"]

    # Subtitles options
    if subtitles:
        cmd += ["--write-sub", "--sub-lang", "en", "--embed-subs"]

    # Playlist or single video
    if is_playlist:
        cmd += ["-o", os.path.join(temp_dir, "%(playlist_index)s. %(title)s.%(ext)s")]
    else:
        cmd += ["-o", os.path.join(temp_dir, "%(title)s.%(ext)s")]

    # Add the URL
    cmd.append(url)

    # Execute the command
    subprocess.run(cmd, check=True)

    # Return the path to the downloaded file
    downloaded_file = [f for f in os.listdir(temp_dir) if f.endswith('.mp4') or f.endswith('.mkv') or f.endswith('.webm')][0]
    file_path = os.path.join(temp_dir, downloaded_file)

    return file_path

# Streamlit UI
st.set_page_config(page_title="YouTube Downloader", layout="centered")
st.title("YouTube Video Downloader")

# Input fields
with st.container():
    st.markdown("### Input Video Details")
    url = st.text_input("Enter YouTube URL", key="url_input")
    option = st.selectbox("Download Type", ("Single Video", "Playlist"), key="download_type")
    is_playlist = option == "Playlist"

# Options for quality and subtitles
with st.container():
    st.markdown("### Options")
    quality = st.selectbox(
        "Select Video Quality",
        ["144p", "240p", "360p", "480p", "720p", "1080p", "1440p", "2160p", "Best Available"],
        index=4,
        key="quality_select"
    )
    subtitles = st.checkbox("Add Subtitles", key="subtitles_checkbox")

# Download button
with st.container():
    download_button = st.button("Download", key="download_button")

if download_button:
    if not url:
        st.error("Please provide a valid YouTube URL.")
    else:
        try:
            with st.spinner("Downloading..."):
                # Download video and get the file path
                file_path = download_video(url, is_playlist, quality, subtitles)

                # Provide a download link/button for the user to download the video
                with open(file_path, "rb") as file:
                    st.download_button(
                        label="Download Video",
                        data=file,
                        file_name=os.path.basename(file_path),
                        mime="video/mp4"
                    )

            st.success("Download completed successfully!")
        except subprocess.CalledProcessError:
            st.error("An error occurred during the download. Please check the URL and try again.")
