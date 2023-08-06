import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="geveze",
    version="0.0.1",
    py_modules=['src.twinkle'],
    install_requires=[
        'click==8.1.3',
        'openai==0.27.6'
    ],
    entry_points={
        'console_scripts': [
            'twinkle = src.twinkle:cli',
        ],
    },
    author="Ali Cabukel",
    author_email="acabukel@protonmail.com",
    description="Geveze ChatGPT Examples",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/overenginar/geveze",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
