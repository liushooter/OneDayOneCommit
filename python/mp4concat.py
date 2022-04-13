# https://gist.github.com/mwouts/115956d3fc7ece55cbce483a7a5148bd

import subprocess
import tempfile
import click

@click.command()
@click.argument("inputs", nargs=-1)
@click.option("--output", nargs=1, help="The result of the concatenation")
def mp4concat(inputs, output):
    """Concatenate MP4 files into a MP4 file without re-encoding"""
    assert output.lower().endswith(
        ".mp4"
    ), f"The destination file {output} should have a .mp4 extension"

    intermediate_ts_files = [tempfile.mktemp() for i in inputs]
    for input_file, intermediate_ts_file in zip(inputs, intermediate_ts_files):
        assert input_file.lower().endswith(
            ".mp4"
        ), f"The input file {output} should have a .mp4 extension"
        process = subprocess.Popen(
            [
                "ffmpeg",
                "-i",
                input_file,
                "-c",
                "copy",
                "-bsf:v",
                "h264_mp4toannexb",
                "-f",
                "mpegts",
                intermediate_ts_file,
            ]
        )
        process.communicate()

    process = subprocess.Popen(
        [
            "ffmpeg",
            "-i",
            "concat:" + "|".join(intermediate_ts_files),
            "-c",
            "copy",
            "-bsf:a",
            "aac_adtstoasc",
            output,
        ]
    )

    process.communicate()


if __name__ == "__main__":
    mp4concat()
