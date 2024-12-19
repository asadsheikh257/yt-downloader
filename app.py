import streamlit as st
import subprocess

def download_video(url, is_playlist, quality, subtitles):
    # Base command
    cmd = ["yt-dlp"]

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
        cmd += ["-o", "%(playlist_index)s. %(title)s.%(ext)s"]
    else:
        cmd += ["-o", "%(title)s.%(ext)s"]

    # Add the URL
    cmd.append(url)

    # Execute the command
    subprocess.run(cmd, check=True)

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
                download_video(url, is_playlist, quality, subtitles)
            st.success("Download completed successfully!")
        except subprocess.CalledProcessError:
            st.error("An error occurred during the download. Please check the URL and try again.")



# Footer
st.markdown("""
        <style>
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #0E1117;  /* Dark background */
            text-align: center;
            padding: 1px 0;
            font-size: 14px;
            color: #FAFAFA;  /* White text color for high contrast */
        }
        .footer a {
            color: #FAFAFA;  /* Light purple color for links */
            text-decoration: none;
        }
        .footer a:hover {
            text-decoration: underline;
        }
    </style>
    <div class="footer">
        <p>Contact: <a href="mailto:asadsheikh257@gmail.com">asadsheikh257@gmail.com</a> | Phone: +923017481916</p>
    </div>
""", unsafe_allow_html=True)