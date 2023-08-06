from __future__ import annotations

import logging
import random
import re
from typing import Literal

import jaconv
from gimei import Gimei
from janome.analyzer import Analyzer
from janome.tokenfilter import CompoundNounFilter

from ..pattern import flex_tags, onara, onara_messages, uniq_tags
from .message import OjiMessage
from .pconfig import PunctuationConfig

logger = logging.getLogger("ojichat")


class OjichatGenerator:
    """おじさんがLINEやメールで送ってきそうな文を生成する"""

    def __init__(
        self,
        name: str | Literal[-1] = "",
        seed: int | float | str | bytes | bytearray | None = None,
        emoji_num: int = 4,
        punc_level: int = 0,
    ) -> None:
        """
        Args:
            name (str, optional): 女の子の名前(オプション)\n
            seed (int | float | str | bytes | bytearray | None, optional): 使用するシード値(オプション)\n
            emoji_num: (int, optional): 絵文字/顔文字の最大連続数(オプション)\n
            punc_level (int, optional): 句読点挿入頻度レベル(0-3)(オプション)
        """  # noqa: E501
        self._name = name
        self._seed = seed

        self._emoji_num = self._check_emoji_num(emoji_num)
        self._punc_level = self._check_punc_level(punc_level)

    def generator(self, reset_on_finish: bool = False) -> OjiMessage:
        """おじさんの文言を生成

        Args:
            reset_on_finish (bool, optional): 完了時に生成に使用したシード値などをリセットするかどうか

        Returns:
            OjiMessage
        """  # noqa: E501

        # 名前が-1だった場合に名前を先に生成してシード値＋名前ランダムを実現する
        if self._name == -1:
            gimei = Gimei("female").name
            first = random.choice(
                [gimei.first.kanji, gimei.first.hiragana, gimei.first.katakana]
            )
            self._name = first

        # シード固定
        if self._seed is None:
            self._seed = random.randint(0, 100000000000)
        random.seed(self._seed)

        logger.debug(
            "[generator](seed)" + f"{type(self._seed).__name__}:{str(self._seed)}"
        )

        # メッセージを選択する
        selected_message = self._select_message()

        # メッセージに含まれるタグを変換
        converted_message = self._convert_tags(selected_message)

        # 句読点レベルに応じて、おじさんのように文中に句読点を適切に挿入する
        result = self._insert_punctuations(converted_message)

        return_msg = OjiMessage(
            str(self._name), self._seed, self._punc_level, self._emoji_num, result
        )

        # fmt: off
        logger.debug(f"[generator](OjiMessage)name       : {return_msg.name}")
        logger.debug(f"[generator](OjiMessage)seed       : ({type(return_msg.seed).__name__}){str(return_msg.seed)}")  # noqa: E501
        logger.debug(f"[generator](OjiMessage)punc_level : {return_msg.punc_level}")
        logger.debug(f"[generator](OjiMessage)emoji_num  : {return_msg.emoji_num}")
        logger.debug(f"[generator](OjiMessage)message    : {return_msg.message}")
        # fmt: on

        if reset_on_finish:
            logger.debug("[generator] Properties reset")
            self.reset()

        return return_msg

    def reset(self) -> None:
        """プロパティをすべて初期値にする"""
        self._name = ""
        self._seed = None
        self._emoji_num = 4
        self._punc_level = 0
        logger.debug("[reset] reset done.")

    def set_props(
        self,
        *,
        name: str | Literal[-1] | None = None,
        seed: int | float | str | bytes | bytearray | None = None,
        emoji_num: int | None = None,
        punc_level: int | None = None,
    ) -> None:
        """プロパティを変更する。すべてオプションでキーワード引数強制です。

        Args:
            name (str | Literal[-1] | None, optional): 女の子の名前(-1で再抽選)
            seed (int | float | str | bytes | bytearray | None, optional): シード値(-1で再抽選)
            emoji_num (int | None, optional): 絵文字/顔文字の最大連続数
            punc_level (int | None, optional):  句読点挿入頻度レベル(0-3)
        """  # noqa: E501
        if name == -1:
            logger.debug("[set_props](name) name reset")
            self._name = name
        elif name is not None:
            logger.debug(f"[set_props](name){name}")
            self._name = name

        if seed == -1:
            logger.debug("[set_props](seed) seed reset")
            self._seed = None
        elif seed is not None:
            logger.debug(f"[set_props](seed){seed}")
            self._seed = seed

        if emoji_num is not None:
            logger.debug(f"[set_props](emoji_num){emoji_num}")
            self._emoji_num = self._check_emoji_num(emoji_num)

        if punc_level is not None:
            logger.debug(f"[set_props](punc_level){punc_level}")
            self._punc_level = self._check_punc_level(punc_level)

    def _select_message(self) -> str:
        """ベースとなるメッセージを選択する

        ランダムに選択されたONARAを元にメッセージを組み立てて返す

        Returns:
            str: メッセージ
        """
        selected_message: str = ""

        # アルゴリズム(ONARA)を無作為に選定
        selected_onara = onara[random.randrange(len(onara))]
        logger.debug("[select_message](selected_onara)" + str(selected_onara))

        # 重複した表現を避けるためのブラックリストを感情ごとに用意
        blacklist: dict[str, set[str]] = {k: set() for k in onara_messages.keys()}

        # アルゴリズム内で表現されたそれぞれの感情に対応した文言を選定
        for oji_e in selected_onara:
            sentences = onara_messages[oji_e]
            while True:
                selected = random.choice(sentences)
                if selected not in blacklist[oji_e]:
                    blacklist[oji_e].add(selected)
                    selected_message += selected
                    break
                # 既にすべての表現を使い切っていたら諦める(多分いらなくない？)
                if len(blacklist[oji_e]) >= len(sentences):
                    selected_message += selected
                    break
            # 挨拶以外の感情に関しては語尾を最大2文字までカタカナに変換するおじさんカタカナ活用を適用する  # noqa: E501
            if oji_e != "GREETING":
                selected_message = self._katakana_katsuyou(
                    selected_message, random.randrange(3)
                )
        logger.debug("[select_message](selected_message)" + selected_message)
        return selected_message

    def _katakana_katsuyou(self, message: str, number: int) -> str:
        """カタカナ活用を適用する

        引数numberの分語尾がひらがなだった場合にカタカナに変換する

        Args:
            message (str): メッセージ\n
            number (int): 変換文字数

        Returns:
            str: カタカナ活用済みメッセージ
        """
        if number == 0:
            return message

        match = re.search(
            r"^(.+)([\u3040-\u309F]{" + str(number) + r"})([^\u3040-\u309F]*)$", message
        )

        if not match:
            return message

        return_message = (
            match.group(1) + jaconv.hira2kata(match.group(2)) + match.group(3)
        )
        logger.debug("[katakana_katsuyou](return_message)" + return_message)
        return return_message

    def _convert_tags(self, message: str) -> str:
        """タグを置換する

        Args:
            message (str): メッセージ

        Returns:
            str: 置換済みメッセージ
        """
        # 乱数の発生回数を揃えるために先に生成しておく
        gimei = Gimei("female").name
        first = random.choice(
            [gimei.first.kanji, gimei.first.hiragana, gimei.first.katakana]
        )
        name_suffix = self._random_name_suffix()

        if "{TARGET_NAME}" in message:
            if self._name:
                # 引数として名前が存在した場合にはそれを使う
                name = str(self._name) + name_suffix
                logger.debug("[convert_tags](self._name)" + name)
                message = message.replace("{TARGET_NAME}", name)
            else:
                # 指定がない場合には gimei から選定
                name = first + name_suffix
                self._name = first
                logger.debug("[convert_tags](Gimei)" + name)
                message = message.replace("{TARGET_NAME}", name)

        # uniq_tags置換
        for k, v in uniq_tags.items():
            tag = "{" + k + "}"
            while tag in message:
                message = message.replace(tag, random.choice(v))
        logger.debug("[convert_tags](uniq_tag replaced)" + message)

        # flex_tags置換
        for k, v in flex_tags.items():
            tag = "{" + k + "}"
            while tag in message:
                num = random.randint(0, self._emoji_num)

                if num == 0:
                    # Ojisan could be seriously
                    message.replace(tag, "。", 1)
                    continue

                words = []
                last_word = ""
                for i in range(num):
                    w = random.choice(v)
                    while w == last_word:
                        w = random.choice(v)
                    last_word = w
                    words.append(w)
                word = "".join(words)
                message = message.replace(tag, word, 1)
        logger.debug("[convert_tags](flex_tags replaced)" + message)
        return message

    def _random_name_suffix(self) -> str:
        """ランダムに敬称(たまに呼び捨て)を返す

        Returns:
            str: 敬称
        """
        n = random.randrange(100)
        if n < 5:
            # たまに呼び捨てにするおじさん
            logger.debug(f'[random_name_suffix]({str(n)})""')
            return ""
        elif n < 20:
            # 時に「◯◯チャン」とカタカナにしてくるのも、おじさんの常套手段だ。
            logger.debug(f'[random_name_suffix]({str(n)})"チャン"')
            return "チャン"
        elif n < 40:
            # 「〇〇チャン」をさらに半角で表現する、そんなおじさんもいる
            logger.debug(f'[random_name_suffix]({str(n)})"ﾁｬﾝ"')
            return "ﾁｬﾝ"
        else:
            # 多くの場合「ちゃん」にする
            logger.debug(f'[random_name_suffix]({str(n)})"ちゃん"')
            return "ちゃん"

    def _insert_punctuations(self, message: str) -> str:
        """句読点挿入頻度レベルに応じ、助詞、助動詞の後に句読点を挿入する

        Args:
            message (str): メッセージ

        Returns:
            str: 句読点挿入済みメッセージ
        """
        if self._punc_level == 0:
            return message

        pconfig = PunctuationConfig.get_pconfig(self._punc_level)
        result: str = ""

        # Pythonでおじさんの文句の形態素解析に使われるかわいそうなライブラリはこちら
        analyzer = Analyzer(token_filters=[CompoundNounFilter()])

        tokens = analyzer.analyze(message)
        for token in tokens:
            if token.part_of_speech.split(",")[0] not in pconfig.target_hinshis:
                result += token.surface
                continue
            if random.randrange(100) <= pconfig.rate:
                result += token.surface + "、"
            else:
                result += token.surface
        return result

    def _check_punc_level(self, level: int) -> int:
        """句読点挿入頻度レベルをチェックして不正な値だった場合にデフォルト(0)を返す

        Args:
            level (int)

        Returns:
            int
        """
        if level < 0 or level > 3 or type(level) is not int:
            logger.warning("[check_punc_level]句読点挿入レベル: " + str(level))
            logger.warning("[check_punc_level]句読点挿入頻度レベル(0～3)が不正です。0に設定しました。")
            return 0
        logger.debug("[check_punc_level](level)" + str(level))
        return level

    def _check_emoji_num(self, num: int) -> int:
        """絵文字/顔文字の最大連続数をチェックして不正な値だった場合にデフォルト(4)を返す

        Args:
            num (int): 絵文字/顔文字の最大連続数

        Returns:
            int
        """
        if num < 0 or type(num) is not int:
            logger.warning("[check_emoji_num]絵文字/顔文字の最大連続数: " + str(num))
            logger.warning("[check_emoji_num]絵文字/顔文字の最大連続数が不正です。4に設定しました。")
            return 4
        logger.debug("[check_emoji_num](num)" + str(num))
        return num
