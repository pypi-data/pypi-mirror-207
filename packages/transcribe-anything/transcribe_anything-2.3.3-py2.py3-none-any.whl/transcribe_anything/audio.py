"""
    Fetches audio and handles transcoding it for it.
"""


import sys
import tempfile
import subprocess
import os
import static_ffmpeg  # type: ignore

_PROCESS_TIMEOUT = 4 * 60 * 60


def _ytdlp_download(url: str, outdir: str) -> str:
    """Downloads a file using ytdlp."""
    os.makedirs(outdir, exist_ok=True)
    # remove all files in the directory
    for file in os.listdir(outdir):
        os.remove(os.path.join(outdir, file))
    cmd = f'yt-dlp --no-check-certificate {url} -o "out.%(ext)s"'
    print(f"Running:\n  {cmd}")
    subprocess.run(
        cmd,
        shell=True,
        cwd=outdir,
        check=True,
        timeout=_PROCESS_TIMEOUT,
        universal_newlines=True,
    )
    new_files = os.listdir(outdir)
    assert len(new_files) == 1, f"Expected 1 file, got {new_files}"
    downloaded_file = os.path.join(outdir, new_files[0])
    assert os.path.exists(downloaded_file), f"The expected file {downloaded_file} doesn't exist"
    return downloaded_file


def _convert_to_mp3(inpath: str, outpath: str, speech_normalization: bool = False) -> None:
    """Converts a file to mp3."""
    cmd_audio_filter = ""
    if speech_normalization:
        cmd_audio_filter = "-filter:a speechnorm=e=12.5:r=0.00001:l=1"
    cmd = f'ffmpeg -y -i "{inpath}" {cmd_audio_filter} -acodec libmp3lame "{outpath}"'
    print(f"Running:\n  {cmd}")
    try:
        subprocess.run(cmd, shell=True, check=True, capture_output=True, timeout=_PROCESS_TIMEOUT)
    except subprocess.CalledProcessError as exc:
        print(f"Failed to run {cmd} with error {exc}")
        print(f"stdout: {exc.stdout}")
        print(f"stderr: {exc.stderr}")
        raise
    assert os.path.exists(outpath), f"The expected file {outpath} doesn't exist"


def fetch_audio(url_or_file: str, out_mp3: str) -> None:
    """Fetches from the internet or from a local file and outputs a wav file."""
    assert out_mp3.endswith(".mp3")
    static_ffmpeg.add_paths()  # pylint: disable=no-member
    if url_or_file.startswith("http") or url_or_file.startswith("ftp"):
        with tempfile.TemporaryDirectory() as tmpdir:
            print(f"Using temporary directory {tmpdir}")
            downloaded_file = _ytdlp_download(url_or_file, os.path.abspath(tmpdir))
            print("Downloaded file: ", downloaded_file)
            _convert_to_mp3(downloaded_file, out_mp3, speech_normalization=True)
        sys.stderr.write("Downloading complete.\n")
        assert os.path.exists(out_mp3), f"The expected file {out_mp3} doesn't exist"
    else:
        assert os.path.isfile(url_or_file)
        cmd = f'ffmpeg -i "{url_or_file}" -acodec libmp3lame "{out_mp3}"'
        sys.stderr.write(f"Running:\n  {cmd}\n")
        subprocess.run(cmd, shell=True, check=True, capture_output=True, timeout=_PROCESS_TIMEOUT)
        assert os.path.exists(out_mp3), f"The expected file {out_mp3} doesn't exist"


def unit_test() -> None:
    """Runs the program."""
    url = "https://www.youtube.com/watch?v=8Wg8f2g_GQY"
    fetch_audio(url, "out.mp3")


if __name__ == "__main__":
    unit_test()
