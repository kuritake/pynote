import sys
import logging
import logging.handlers
import logging.config

#ルートロガーの作成。
_root_logger = logging.getLogger('')

#ログレベル
_root_logger.setLevel(logging.INFO)

#フォーマッターの作成(時刻、ログレベル、モジュール名、関数名、行番号: メッセージ　を出力)
_simpleFormatter = logging.Formatter(
    fmt='%(asctime)s %(levelname)-8s %(module)-10s %(funcName)-10s %(lineno)4s: %(message)s'
)

#コンソール用ハンドラの作成。標準出力へ出力。ログレベル。書式は上記フォーマッター
_consoleHandler = logging.StreamHandler(sys.stdout)
_consoleHandler.setLevel(logging.INFO)
_consoleHandler.setFormatter(_simpleFormatter)

#コンソール用ハンドラをルートロガーに追加
_root_logger.addHandler(_consoleHandler)

#ファイル用ハンドラの作成。ファイル名は logging.log, ログレベル, ファイルサイズ 1MB, バックアップファイル３個まで、エンコーディングは utf-8
_fileHandler = logging.handlers.RotatingFileHandler(
    filename='logfile\\logging.log', maxBytes=1000000, backupCount=3, encoding='utf-8'
)
_fileHandler.setLevel(logging.INFO)
_fileHandler.setFormatter(_simpleFormatter)

#ファイル用ハンドラをルートロガーに追加
_root_logger.addHandler(_fileHandler)
