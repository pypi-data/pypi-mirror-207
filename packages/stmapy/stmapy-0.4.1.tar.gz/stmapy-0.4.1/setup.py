import setuptools
from setup_qt import build_qt

with open("README.md", "r") as fh:
    long_description = fh.read()

__version__ = None
with open("stmapy/_version.py") as o:
    exec(o.read())
assert __version__ is not None

setuptools.setup(
    name="stmapy",
    version="0.4.1",
    authors="Loïc Huder, Florie Mesple",
    author_email="loic.huder@gmail.com, florie.mesple@gmail.com",
    description="Scanning tunneling microscopy analysis in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/lateqs/stmapy",
    packages=setuptools.find_packages(),
    package_data={
        'stmapy': [
            '*.ui',
            '*.qrc',
            'languages/*.ts',
            'languages/*.qm',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Visualization",
        "Environment :: X11 Applications :: Qt",
    ],
    install_requires=["numpy", "scipy>=0.17", "matplotlib>=2.0", "pyqt5"],
    tests_require=["h5py"],
    python_requires=">=3.6",
    entry_points={
    "console_scripts": ["stmapy = stmapy.main:main",],
    'gui_scripts': [
            'stmapy=stmapy.__main__:main',
        ],
    },
    cmdclass={
        'build_qt': build_qt,
    },
)
