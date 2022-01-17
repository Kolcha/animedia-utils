import setuptools

setuptools.setup(
    name="animedia-utils",
    version="0.2.0",
    author="Nick Korotysh",
    author_email="kolchaprogrammer@list.ru",
    description="download torrents from tt.animedia.tv",
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/Kolcha/animedia-utils",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Internet",
    ],
    license='MIT',
    keywords='anime, torrent-downloader',
    packages=setuptools.find_packages(),
    install_requires=['lxml', 'requests'],
    python_requires='>=3.6',
)
