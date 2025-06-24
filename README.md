# Notice:
I am a beginner programmer and the code is not the most robust, I have yet to handle some
bugs and errors. I brought the code to GitHub in hopes to receive feedback on how to better
structure code and packages

## FD-ORGANIZER _(File-Directory Organizer)_
A simple CLI utility that organizes the files of a directory based on a mapping

## Quick Start
I was able to successfully use `fd-organizer` on Python 3.10.X as such this is the minimum
Python version required, although this is likely very restrictive. FD-Organizer uses `poetry` as 
the build-backend. It is recommended to install poetry via `pipx`. Instructions on installing `pipx`
can be found [here](https://pipx.pypa.io/stable/installation/), instructions on installing `poetry` can 
be found [here](https://python-poetry.org/docs/).

After installing `poetry`, clone this repository and install the dependencies of `fd-organizer` 
using `poetry install`. This will also allow for the usage of `fd-organizer` from poetry.

### Quick Start Summmary

```shell
# Install pipx (refer to docs)
# Install poetry (refer to docs)

git clone https://github.com/Kaizen-BT/fd-organizer.git
cd fd-organizer
poetry install
poetry run fd-organizer --help 
```

## Installation Instructions
To install `fd-organizer` it is recommended to install it via `pipx`. Refer [here](#quick-start-summary)
for more information on installing `pipx`

Once `pipx` is installed clone into this repository and install `fd-organizer` using
`pipx install .`

### Installation Summary

```shell
git clone https://github.com/Kaizen-BT/fd-organizer.git
cd fd-organizer
pipx install .
```

## Usage Guide
Once `fd-organizer` is installed and available there are three commands available:

- `default`
- `list-custom`
- `run-custom`

The last two above show the available custom mappers if you created your own. The following
exapnds on creating your own mappers.

## MAPPER (Quick Guide)
A `mapper` is simply a `JSON` file that specifies what files should be stored in which directory.
`Mappers ` are stored in a directory 

```json
{
  "Directory" : [
    ".file_extension",
    ".file_extension" 
  ]
}
```

Where `Directory` is the directory move all files whose file-extensions are specified in the associated array.

An example of a valid mapping shown below:

```json
{
        "Documents": [
            ".pdf",
            ".doc",
            ".docx",
            "."
        ],

        "Audio": [
            ".mp3",
            ".wav",
            ".aic",
            ".flac",
            ".aac",
            ".m4a",
            ".ogg",
            ".pcm"
        ],

        "Videos": [
            ".mp4",
            ".mov",
            ".avi",
            ".mkv",
            ".avchd",
            ".webm"
        ]
    }

```
