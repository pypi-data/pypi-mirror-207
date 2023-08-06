"""Contains the class that converts XML scripture files into JSON files."""

from __future__ import annotations

import json
import os
from contextlib import suppress
from logging import warning
from typing import Any

from pythonbible import Book
from pythonbible import Version
from pythonbible import get_book_chapter_verse
from pythonbible import get_book_number
from pythonbible.verses import VERSE_IDS

from pythonbible_parser.bible_parser import BibleParser
from pythonbible_parser.errors import InvalidBibleParserError
from pythonbible_parser.osis.old_osis_parser import OldOSISParser

CURRENT_FOLDER: str = os.path.dirname(os.path.realpath(__file__))
DATA_FOLDER: str = os.path.join(CURRENT_FOLDER, "data")


class JSONConverter:
    """Convert XML scripture files into faster verse and book title JSON files."""

    def __init__(
        self: JSONConverter,
        parser: BibleParser,
        **kwargs: Any | None,
    ) -> None:
        """
        Initialize with a BibleParser and optional data folder and list of verse ids.

        If no data folder is specified, the data folder in the same directory
        as this class will be used. If no verse ids are specified, the list of
        all verse ids will be used.

        :param parser: BibleParser instance with version
        :param kwargs: optional "data_folder" and "verse_ids"
        """
        self.parser: BibleParser = parser
        self.data_folder: str = kwargs.get("data_folder", DATA_FOLDER)
        self.verse_ids: list[int] = kwargs.get("verse_ids", VERSE_IDS)
        self.books: dict[int, tuple[str, str]] = {}
        self.verses: dict[int, str] = {}

    def generate_book_file(self: JSONConverter) -> None:
        """
        Generate the book title JSON file for the given version.

        :return: None
        """
        self._validate_parser()
        self._get_books()
        _print_file(self.data_folder, self.parser.version, "books.json", self.books)

    def generate_verse_file(self: JSONConverter) -> None:
        """
        Generate the verse text JSON file for the given version.

        :return: None
        """
        self._validate_parser()
        self._get_verses()
        _print_file(self.data_folder, self.parser.version, "verses.json", self.verses)

    def _validate_parser(self: JSONConverter) -> None:
        if self.parser is None:
            raise InvalidBibleParserError("Parser instance is None.")

        if not isinstance(self.parser, OldOSISParser):
            raise InvalidBibleParserError("Parser instance is not a valid type.")

    def _get_books(self: JSONConverter) -> None:
        for verse_id in self.verse_ids:
            book_id: int = get_book_number(verse_id)

            if book_id in self.books:
                continue

            book: Book
            book, _, _ = get_book_chapter_verse(verse_id)

            if book:
                long_book_title: str = self.parser.get_book_title(book)
                short_book_title: str = self.parser.get_short_book_title(book)
                self.books[book_id] = (long_book_title, short_book_title)

    def _get_verses(self: JSONConverter) -> None:
        for verse_id in self.verse_ids:
            verse_text: str = self.parser.verse_text(
                verse_id,
                include_verse_number=False,
            )

            if verse_text is None or not verse_text.strip():
                warning(f"Verse {verse_id} is empty.")

            self.verses[verse_id] = verse_text


def _print_file(
    data_folder: str,
    version: Version,
    filename: str,
    data_dictionary: dict,
) -> None:
    version_folder: str = os.path.join(data_folder, version.value.lower())

    _make_sure_directory_exists(data_folder)
    _make_sure_directory_exists(version_folder)

    with open(
        os.path.join(version_folder, filename),
        "w",
        encoding="utf-8",
    ) as json_file:
        json.dump(data_dictionary, json_file)


def _make_sure_directory_exists(directory: str) -> None:
    with suppress(FileExistsError):
        os.makedirs(directory)
