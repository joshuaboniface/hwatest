# A CPU and Hardware Acceleration (GPU) tester for Jellyfin

<p align="center">
<a href="https://github.com/joshuaboniface/hwatest"><img alt="License" src="https://img.shields.io/github/license/joshuaboniface/hwatest"/></a>
<a href="https://github.com/psf/black"><img alt="Code style: Black" src="https://img.shields.io/badge/code%20style-black-000000.svg"/></a>
</p>

HWA Tester (`hwatest`) is a Python 3 CPU and Hardware Acceleration (GPU) tester for Jellyfin.

This program runs a series of standardized tests to determine how video transcoding will perform on your hardware, with the goal being to provide a maximum number of simultaneous streams that can be expected to perform adequately (i.e. at at least 1x realtime transcode speed).

It will run through several possible transcoding methods using Jellyfin's FFmpeg binary build, including CPU software transcoding, nVidia NVENC, Intel QSV, and AMD AMF, and report the results of any compatible method(s), along with anonymous system hardware information in a standardized format.

To perform the test, the program will download four standardized test files totalling 641 MB from the Jellyfin mirror (credit to jell.yfish.us for the original files and www.larmoire.info for the active mirror we could clone). The location of these temporary files is set by the "--videos" option.

The results will be output in JSON format to the output path, either stdout (the default) or the path specified by the "--output" option. You can then share your results to https://hwa.jellyfin.org to help us build a database of available hardware and how well it will perform.

*NOTE:* Obtaining hardware info requires the "lshw" program. Please install it before running HWA Tester. On Debian/Ubuntu/derivatives it can be installed with "sudo apt install lshw". For other Linux distributions, consult your local package manager database.

*NOTE:* For nVidia consumer GPUs, ensure you have applied the driver unlock patch to raise the simultaneous stream limit, or you will get erroneous (very low) numbers of simultaneous streams in your results.

*WARNING:* This benchmark will be quite stressful on your system and will take a very long time to run, especially on lower-end hardware. Ensure you run it on a lightly-loaded system and do not perform any heavy workloads, including streaming videos in Jellyfin, while the test is running, to avoid compromising the results. It is recommended to run the test overnight.

## Operating System & FFmpeg Support

Currently, only Linux, and specifically only any distribution that packages Jellyfin FFmpeg, is supported, in order to ensure consistency of test results. The distribution is recorded, along with the FFmpeg binary used, and invalid results discarded on the eventual database.

## Installing `hwatest`

To install `hwatest`, clone this repository somewhere on your system. You can then either:

* Run the script directly: `hwatest/hwatest.py`

* Install the Python package with PIP: `pip install .`

  *NOTE:* Later sections assume this method (running the installed `hwatest` command)

## Running The Benchmark

Before running the benchmark, ensure you understand the requirements and implications (above, or shown with the `hwatest --help` option) before continuing.

```
$ hwatest --help
```

Once you are ready to run the test, set the options if they differ from the defaults below, run the program, and observe the results. For uploading results, ensure you set the `--output` option to a file.

```
$ hwatest --output results.json
```

If you get any errors, correct them and retry. Specifically if you have multiple GPUs, you will be asked to specify which one to test with the `--gpu` option.

```
$ hwatest --output results.json --gpu 0
```

## Command-line Options

```
  --ffmpeg FILE       Path to the Jellyfin FFmpeg binary.  [default: /usr/lib/jellyfin-ffmpeg/ffmpeg]
  --videos DIRECTORY  Directory to store temporary video files.  [default: ~/hwatest; required]
  --output FILE       Path to the output JSON file ('-' for stdout).  [default: -]
  --gpu INTEGER       The specific GPU to test in a multi-GPU system.
  --debug             Enable additional debug output.
  -h, --help          Show the help message and exit.
```
