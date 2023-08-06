import argparse 
from pathlib import Path
import json
import gzip
import shutil

from typing import TypeAlias, TypedDict
import xml.etree.ElementTree as ET

DEFAULT_TARGET_VERSION = "11.1.5"


AbletonVersion: TypeAlias = str


class AbletonVersionInfo(TypedDict):
    MinorVersion: str
    Creator: str


def load_versions_info() -> dict[AbletonVersion, AbletonVersionInfo]:
    script_folder = Path(__file__).resolve().parent
    with open(script_folder.joinpath("versions_info.json")) as config_file:
        return json.load(config_file)


def load_file_to_convert(filename: str) -> ET:
    with gzip.open(filename, 'rb') as f_in:
        xml_file = Path(filename).with_suffix(".xml")
        with open(xml_file, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
            return ET.parse(xml_file)


def update_tree(
    tree_to_convert: ET,
    target_version: str,
    versions_info: dict[AbletonVersion, AbletonVersionInfo]
) -> ET:
    version_info = versions_info[target_version]
    ableton_tag = tree_to_convert.getroot()
    ableton_attrib = ableton_tag.attrib
    ableton_attrib["MinorVersion"] = version_info["MinorVersion"]
    ableton_attrib["Creator"] = version_info["Creator"]
    ableton_tag.attrib = ableton_attrib
    return tree_to_convert


def save_and_clear(
    filename: str,
    target_version: str,
    tree_to_convert: ET,
):
    path_file = Path(filename)
    with gzip.open(
        path_file.parent.joinpath(
            f"{path_file.stem}-{target_version.replace('.', '-')}.als"
        ), 'wb'
    ) as f_out:
        tree_to_convert.write(f_out, encoding='utf-8', xml_declaration=True)
    Path(filename).with_suffix(".xml").unlink()


def change_version(
    filename: str,
    target_version: str,
) -> None:
    print(f"Hi: {target_version=} {filename=}")
    versions_info = load_versions_info()
    tree_to_convert = load_file_to_convert(filename=filename)
    tree_to_convert = update_tree(
        tree_to_convert=tree_to_convert,
        target_version=target_version,
        versions_info=versions_info,
    )
    save_and_clear(
        filename=filename,
        target_version=target_version,
        tree_to_convert=tree_to_convert,
    )


def main() -> None:
    parser = argparse.ArgumentParser("change_ableton_version")
    parser.add_argument(
        'filename', 
        help="File to convert",
        type=str,
    )
    parser.add_argument(
        "--target_version",
        help="Target ableton version",
        type=str,
        default=DEFAULT_TARGET_VERSION,
    )
    args = parser.parse_args()
    change_version(
        filename=args.filename,
        target_version=args.target_version
    )
