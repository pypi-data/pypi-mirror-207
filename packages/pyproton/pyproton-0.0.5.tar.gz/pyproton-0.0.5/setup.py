import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyproton",
    version="0.0.5",
    author="Aaron Stopher",
    packages=setuptools.find_packages(include=["pyproton"]),
    description="Minimal wrapper implementation of the linux protonvpn-cli",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aastopher/pyproton",
    project_urls={
        "Bug Tracker": "https://github.com/aastopher/pyproton/issues",
    },
    keywords=['vpn', 'proton vpn', 'proton', 'wrapper', 'cli'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires=">=3.9",
)
