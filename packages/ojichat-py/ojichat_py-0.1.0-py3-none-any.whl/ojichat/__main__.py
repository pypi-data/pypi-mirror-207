from __future__ import annotations

import argparse
import json
import sys
from typing import TYPE_CHECKING

from logzero import LogFormatter, setup_logger

from ojichat import OjichatGenerator, get_github_url, get_license, get_version

if TYPE_CHECKING:
    from .generator.message import OjiMessage

app_version = f"""\
Ojisan Nanchatte (ojichat) command version {get_version()}
Copyright (c) 2023 Charahiro-tan
Released under the MIT License.
{get_github_url()}
"""

usage = f"""\
ojichat.py ver.{get_version()}
おじさんがLINEやメールで送ってきそうな文を生成するコマンド

Usage:
  ojichat [options]
Options:
  -h, --help        ヘルプを表示
  -V, --version     バージョンを表示
  -s, --seed <Any>  シード値を指定する
  -n, --name <Any>  女の子の名前を指定する(-1でランダム)
  -e <number>       絵文字/顔文字の最大連続数 [default: 4]
  -p <level>        句読点挿入頻度レベル [min:0, max:3] [default: 0]
  -q, --quiet       出力を結果のみにします  デバッグモードと併用不可
  -d, --debug       デバッグモード
  --json            結果をJSON形式で返す
std I/O:
  標準入力から入力があった場合、--nameを指定しても標準入力の値に上書きされます
  また、出力は結果のみが標準出力に出力されます
"""

figlet = r"""                _           _
  ___ 😘💗  ___| |__   __ _| |_   _ __  _   _
 / _ \| | |/ __| '_ \ / _` | __| | '_ \| | | |
| (_) | | | (__| | | | (_| | |_  | |_) | |_| |
 \___// |_|\___|_| |_|\__,_|\__💦| .__/ \__, |
    |__/                         |_|    |___/
"""

parser = argparse.ArgumentParser(add_help=False)
parser.add_argument("-h", "--help", action="store_true")
parser.add_argument("-V", "--version", action="store_true")
parser.add_argument("-d", "--debug", action="store_true")
parser.add_argument("-s", "--seed", default=None)
parser.add_argument("-n", "--name", default="")
parser.add_argument("-e", type=int, default=4)
parser.add_argument("-p", type=int, default=0)
parser.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("--json", action="store_true")

args = parser.parse_args()

if args.help is True:
    print(usage)
    sys.exit()
elif args.version is True:
    print(app_version)
    sys.exit()

name = args.name
seed = args.seed
emote = args.e
punc = args.p
loglevel = 20
stdin = False

if name == "-1":
    name = -1

try:
    seed = int(seed)
except Exception:
    try:
        seed = float(seed)
    except Exception:
        pass

if args.debug:
    loglevel = 10

if args.quiet:
    loglevel = 50

if not sys.stdin.isatty():
    name = sys.stdin.readline().rstrip("\n")
    stdin = True
    loglevel = 50

log_format = "%(color)s[%(levelname)1.1s %(asctime)s %(name)s:%(lineno)d]%(end_color)s %(message)s"  # noqa: E501
formatter = LogFormatter(fmt=log_format)
logger = setup_logger(name="ojichat", formatter=formatter, level=loglevel)

for line in figlet.splitlines():
    logger.info(line)
logger.info(f"ojichat.py :  ver. {get_version()}")
logger.info(f"github     :  {get_github_url()}")
logger.info(f"LICENSE    :  {get_license()}")
logger.info("-------------------------------------------------")

ojichat = OjichatGenerator(name, seed, emote, punc)
result: OjiMessage | str = ""
try:
    result = ojichat.generator()
except Exception as e:
    logger.exception(e)
    sys.exit(1)

if result:
    if stdin:
        if args.json:
            sys.stdout.write(json.dumps(result.to_dict(), ensure_ascii=False))
            sys.exit()
        sys.stdout.write(str(result))
        sys.exit()
    logger.info(
        f"name: {result.name}  seed: ({type(result.seed).__name__}) {str(result.seed)}"
    )
    logger.info("Result:")
    if args.json:
        print(json.dumps(result.to_dict(), ensure_ascii=False))
    else:
        print(result.message)
    sys.exit()
else:
    logger.error("なんらかのエラーが発生して生成できませんでした😱💦")
    sys.exit(1)
