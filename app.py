import streamlit as st
import subprocess

# st.write(f"Current theme: {st._config.get_option('theme.base')}")

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


# JavaScript to detect the theme
st.markdown("""
    <script>
    window.onload = function() {
        const theme = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
        document.body.setAttribute('data-streamlit-theme', theme);
    }
    </script>
""", unsafe_allow_html=True)

# Footer - dynamically styled
footer_style = """
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            text-align: center;
            padding: 1px 0;
            font-size: 14px;
        }
        .footer[data-streamlit-theme='dark'] {
            background-color: #0E1117;  /* Dark background */
            color: #FAFAFA;  /* White text */
        }
        .footer[data-streamlit-theme='light'] {
            background-color: #f1f1f1;  /* Light background */
            color: #333;  /* Dark text */
        }
        .footer a {
            text-decoration: none;
        }
        /* Email and phone number link color */
        .footer a.email, .footer a.phone {
            color: inherit;  /* Inherit the color from footer (white in dark, dark in light) */
        }
        .footer a:hover {
            text-decoration: underline;
        }
    </style>
"""

# Insert the footer styles
st.markdown(footer_style, unsafe_allow_html=True)

# Footer content
st.markdown("""
    <div class="footer">
        <p>Contact: <a href="mailto:asadsheikh257@gmail.com" class="email">asadsheikh257@gmail.com</a> | Phone: <a href="tel:+923017481916" class="phone">+923017481916</a></p>
    </div>
""", unsafe_allow_html=True)