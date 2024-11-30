import setuptools
from distutils.core import setup




setup(
    name="telebot-cli",
    version="1.3.0",
    descriptions="Telegram bot to send files",
    author="Mahesh r mesta",
    author_email="maheshmesta98@gmail.com",
    packages=["telebot"],
    entry_points={
        'console_scripts': ['telebot-cli=telebot.entry_v2:run_main']
        },
    install_requires=[
        "python-telegram-bot",
        "argparse",
        "asyncio"
        ]
    )
