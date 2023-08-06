from __future__ import annotations

from typing import Any


class OjiMessage:
    """おじさんのメッセージとプロパティが含まれたクラス"""

    def __init__(
        self, name: str, seed: Any, punc_level: int, emoji_num: int, message: str
    ) -> None:
        """
        Args:
            name (str): 女の子の名前\n
            seed (Any): 使用されたシード値\n
            punc_level (int): 句読点挿入頻度レベル\n
            emoji_num (int): 絵文字/顔文字の最大連続数\n
            message (str): Ojichat😘
        """
        self._name = name
        self._seed = seed
        self._punc_level = punc_level
        self._emoji_num = emoji_num
        self._message = message

    def __str__(self) -> str:
        return self._message

    def to_dict(self) -> dict:
        return {
            "name": self._name,
            "seed": self._seed,
            "punc_level": self._punc_level,
            "emoji_num": self._emoji_num,
            "message": self._message,
        }

    @property
    def name(self) -> str:
        """女の子の名前"""
        return self._name

    @property
    def seed(self) -> int:
        """使用されたシード値"""
        return self._seed

    @property
    def punc_level(self) -> int:
        """句読点挿入頻度レベル"""
        return self._punc_level

    @property
    def emoji_num(self) -> int:
        """絵文字/顔文字の最大連続数"""
        return self._emoji_num

    @property
    def message(self) -> str:
        """Ojichat😘"""
        return self._message
