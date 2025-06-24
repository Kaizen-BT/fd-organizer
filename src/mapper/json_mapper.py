import json
from pathlib import Path
from mapper import Mapper


def mapper_decoding(
    decoded: dict[str, list[str]]
) -> dict[str, tuple[str, ...]]:
    """Checks if the JSON loaded is in the appropriate format

    Args:
        decoded (dict[str, list[str]]): The decoded JSON

    Raises:
        json.JSONDecodeError: Raises an error if the format is not implemented in the JSON file

    Returns:
        dict[str, tuple[str,...]]: The mapper equivalent of the JSON
    """
    
    mapper_equivalent: dict[str, tuple[str, ...]] = {}

    for dir in decoded:
        extension_list: list[str] = decoded[dir]

        if isinstance(extension_list, list):
            extension_tuple: tuple[str, ...] = tuple(extension_list)
            mapper_equivalent[dir] = extension_tuple
        else:
            raise json.JSONDecodeError("Error", "Error", 0)

    return mapper_equivalent


class JSONMapper(Mapper):

    @classmethod
    def parse_json(cls, json_path: Path):
        """Creates a mapper from the provided JSON

        Args:
            json_path (Path): The path to a mapping in JSON format
        """

        try:
            with open(json_path, "r") as json_file:
                cls.mapping = json.load(json_file, object_hook=mapper_decoding)
        except json.JSONDecodeError:
            print("JSON is invalid... check formatting please")
        except FileNotFoundError:
            print(f"{json_path.absolute()} not found")