from setuptools import setup,find_packages
from pathlib import Path
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(
    name = "byozdemir-sendmessage",
    version = "0.0.1",
    author = "Byozdemir",
    author_email = "emrenetwork@yandex.com",
    description = ("It's helps you tou send message via populer apps"),
    license = "MIT",
    keywords = "telegram messager,discord messager",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires = ['requests','telepot'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
