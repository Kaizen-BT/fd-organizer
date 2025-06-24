from fd_organizer.mapper import Mapper


class BaseMapper(Mapper):
    """Default mapper to use if not specified"""

    mapping = {
        "Documents": (
            ".pdf",
            ".doc",
            ".docx",
            "."
        ),

        "Audio": (
            ".mp3",
            ".wav",
            ".aic",
            ".flac",
            ".aac",
            ".m4a",
            ".ogg",
            ".pcm"
        ),

        "Videos": (
            ".mp4",
            ".mov",
            ".avi",
            ".mkv",
            ".avchd",
            ".webm"
        )
    }
