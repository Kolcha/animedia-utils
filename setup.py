import setuptools

setuptools.setup(
    name="animedia-utils",
    version="0.1.4",
    author="Nick Korotysh",
    author_email="kolchaprogrammer@list.ru",
    description="download torrents from tt.animedia.tv",
    url="https://github.com/Kolcha/animedia-utils",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    install_requires=['lxml', 'requests'],
    python_requires='>=3.6',
)
