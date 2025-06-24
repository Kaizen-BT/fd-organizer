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

```bash
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

```bash
git clone https://github.com/Kaizen-BT/fd-organizer.git
cd fd-organizer
pipx install .
```

## Usage Guide
Once `fd-organizer` is installed and available there are three commands available:

- `default`
- `list-custom`
- `run-custom`

### `default`
Using the `default` command in `fd-organizer` will organize a given directory based
on the default mapping.

Syntax:
```bash
fd-organizer default [--verbose|--no-verbose] DIRECTORY
```

### `list-custom`
Running the `list-custom` command simple shows the custom mappings you have created in
a neat format 

Syntax:
```bash
fd-organizer list-custom
```

### `run-custom`
Using the `run-custom` command requires a custom `mapper` (refer to [Adding Customizations](#adding-customizations)
for details on how to create your own `mapppers`) but is otherwise identical to the `default` command

Syntax:
```bash
fd-organizer run-custom --custom-mapper CUSTOM-MAPPER [--verbose|--no-verbose] DIRECTORY
```

The last two above show the available custom mappers if you created your own. The following
exapnds on creating your own mappers.

## Adding Customizations

### Mapper

`Mappers` are used by `fd-organizer` to determine which directories hold what files.

They are simply `JSON` files that follow a a specific format. `Mappers` are to be stored
in a sub-directory in the users `HOME`. The directory is up to the user but must be set as
the value to the environmental variable `FD_JSON_DIR`, i.e: `FD_JSON_DIR` is a sub-directory 
inside the user's `HOME`. 

> **Note: I am working on implementing a helper command to set the value of `FD_JSON_DIR`, but
can be done manually for now**

The following is the format that every mapper must follow:

```json
{
  "Directory" : [
    ".file_extension",
    ".file_extension" 
  ]
}
```

Where `Directory` is the directory move all files whose file-extensions are specified in the associated array.

An example of a valid mapping shown below and is the `Mapping` used when running `fd-organizer` using the
`default` command:

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
