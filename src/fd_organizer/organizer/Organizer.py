from pathlib import Path
from shutil import move
from typing import Iterator

# My Package Imports
from fd_organizer.mapper import Mapper, BaseMapper
from fd_organizer.mixins  import LoggingMixin


class Organizer(LoggingMixin):
    """
    A simple class that operates by organizing a snapshot of a directories contents
    """

    def __init__(self, dir: Path | str, verbose: bool = False) -> None:
        """Instantiate  our organizer at the specified path

        Args:
            dir (Path | str): Path of the directory to organize
            verbose (boolean, optional): Determines if operations are printed  to the console. Defaults to False.
        """

        self._verbose: bool = verbose
        self._path: Path = dir if isinstance(dir, Path) else Path(dir)
        self.initialize_logger(self._verbose, self._path)  # Logger initialized

    @property
    def target_directory(self) -> Path:
        """Returns the directory the organizer is instantiated on

        Returns:
            Path: Path to the directory being organized
        """

        return self._path.absolute()

    @property
    def files(self) -> Iterator[Path]:
        """Returns an iterable containing only the FILES within the target directory

        Returns:
            Iterator[Path]: Iterable of FILES inside the target directory
        """

        return filter(lambda x: x.is_file(), self.target_directory.iterdir())

    @property
    def folders(self) -> Iterator[Path]:
        """Returns an iterable containing only the FOLDERS within the target directory

        Returns:
            Iterator[Path]: Iterable of FOLDERS inside the target directory
        """

        return filter(lambda x: x.is_file(), self.target_directory.iterdir())

    def move(self, src: Path, dest_folder: Path | str) -> None:
        """Utility method to move a file from the src directory to a folder within the target directory

        Args:
            src (Path): The file to move
            dest_folder (Path | str): Directory to move file to
        """

        destination: Path = self.target_directory / dest_folder / src.name

        if not destination.parent.exists():
            destination.parent.mkdir()  # Target_Dir -> Parent -> File
            # Log directory creation
            self.log(f"{destination.parent} created")

        move(src, destination)  # NOTE: Metadata not preserved when moved
        # Log movement
        self.log(f"Moved {src.name} to {destination.parent.name}")

    def organize(self, mapping: type[Mapper] = BaseMapper) -> None:
        """Organizes the directory based on the specified mapping

        Args:
            mapping (type[Mapper], optional): Mapper that dictates what files to move and to which directories. Defaults to BaseMapper.
        """

        for file_ in self.files:
            if target_dir := mapping[file_.suffix.lower()]:

                self.move(
                    file_.absolute(),
                    target_dir
                )  # Move our file to the folder specified by the mapping

    def __repr__(self) -> str:
        return f"Organizer({self.target_directory}, {self._verbose})"

    def __str__(self) -> str:
        return self.__repr__()
