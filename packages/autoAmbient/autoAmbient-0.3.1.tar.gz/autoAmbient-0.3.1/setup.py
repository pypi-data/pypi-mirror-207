from setuptools import setup

setup(
    name="autoAmbient",
    version="0.3.1",
    packages=["ambient", "ambient.tolls", "ambient.models"],
    entry_points={
        "console_scripts": [
            "getFile=ambient.getFile:main",
            "createTagsFile=ambient.createTagsFile:main",
            "createAmbient=ambient.createAutoAmbient:main",
        ],
    },
)
