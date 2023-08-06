from setuptools import find_packages, setup

setup(
    author = "pinktoxin",
    author_email = "pinktoxindev@gmail.com",
    name="subtitlfy",
    version="0.1.0",
    url="https://github.com/somatosensory/subtitlfy",
    description="subtitlfy - add subtitles to video",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "numpy",
        "opencv-python",
        "typing"
    ],
    entry_points={
        "console_scripts": [
            "subtitlfy = subtitlfy.cli:main",
        ],
    }
)
