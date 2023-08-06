from setuptools import setup, find_packages

setup(
    name="ms_mailbox_reader",
    version="1.0.1",
    packages=find_packages(),
    install_requires=[
        "pywin32"
    ],
    author="Daniel Van Houten",
    author_email="",
    description="A simple package for parsing email content stored locally in Outlook from a Microsoft Exchange Server.",
    url="https://github.com/daniel-van-houten/ms-mailbox-reader",
)
