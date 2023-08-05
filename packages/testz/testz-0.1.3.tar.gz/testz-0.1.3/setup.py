from setuptools import setup

with open("./README.md", "r", encoding="utf-8") as e:
    long_description = e.read()
setup(
    name="testz",
    version="0.1.3",
    author="Dxsxsx",
    author_email="psdd@pm.me",
    description="Web Boilerplate for Flet Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dxsxsx",
    packages=["testz"],
    install_requires=["click"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": ["pc=testz.pc:main"],
    },
    keywords=["python web template", "web application", "development"],
)

#pip install -U ./test_click
#pip uninstall testz