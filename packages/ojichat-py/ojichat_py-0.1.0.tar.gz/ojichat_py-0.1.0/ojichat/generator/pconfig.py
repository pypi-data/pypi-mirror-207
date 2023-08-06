from __future__ import annotations


class PunctuationConfig:
    """句読点挿入の設定"""

    def __init__(self, target_hinshis: list[str], rate: int) -> None:
        """
        Args:
            target_hinshis (list[str]): 句読点を後方に挿入する形態素の品詞\n
            rate (int): 句読点を挿入する確率(百分率)
        """
        self.target_hinshis = target_hinshis
        self.rate = rate

    @classmethod
    def get_pconfig(cls, level: int) -> PunctuationConfig:
        """PunctuationConfigを返すメソッド

        句読点挿入頻度レベルに応じたクラスを返します

        Args:
            level (int): 句読点挿入頻度レベル(0-3)

        Returns:
            PunctuationConfig
        """
        if level == 1:
            return cls(["助動詞"], 30)
        elif level == 2:
            return cls(["助動詞", "助詞"], 60)
        elif level == 3:
            return cls(["助動詞", "助詞"], 100)

        return cls([], 0)
