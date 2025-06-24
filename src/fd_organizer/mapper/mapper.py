
from typing import cast


class MapperMeta(type):

    def __getitem__(cls, extension: str) -> str | None:
        """Return the associated directory"""
        mapper_cls = cast("Mapper", cls)
        return mapper_cls.get_linked_directory(extension)


class Mapper(metaclass=MapperMeta):
    """Base class to extend if we wish to create our own mappings"""

    mapping: dict[str, tuple[str, ...]] = {}

    @classmethod
    def get_mapping(cls) -> dict[str, tuple[str, ...]]:
        """Returns the mapping to use

        Returns:
            dict[str, tuple[str]]: Directory name -> File types
        """
        return cls.mapping

    @classmethod
    def _get_reverse_mapping(cls) -> dict[str, str]:
        """Returns the mapping but with the extensions mapped to the directory

        Returns:
            dict[str, str]: File types -> Directory name
        """

        rev_mapping = {}

        for directory in cls.get_mapping():
            for extension in cls.get_mapping().get(directory, ""):
                rev_mapping.update({extension: directory})

        return rev_mapping

    @classmethod
    def get_linked_directory(cls, extension: str) -> str | None:
        """Returns the directory storing the files of specified extension

        Args:
            extension (str): File extension

        Returns:
            str | None: Storing directory
        """

        return cls._get_reverse_mapping().get(extension, None)
