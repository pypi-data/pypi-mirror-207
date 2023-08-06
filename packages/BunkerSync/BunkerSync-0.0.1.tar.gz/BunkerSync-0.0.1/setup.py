from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(
    name = 'BunkerSync',
    version = '0.0.1',
    author = 'Luai Okasha',
    author_email = 'LuaiOkasha@gmail.com',
    license = 'Apache License 2.0',
    description = 'Internal-External git repositories synchronization tool',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/okashaluai/BunkerSync',
    py_modules = ['BunkerSync', 'Deletion_Filter', 'Sync_Filter', 'Synchronizer', 'Sync_Pool', 'utils'],
    package_dir = {'': 'src'},
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.11',
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: Apache Software License", 
        "Operating System :: OS Independent",
    ],
    entry_points = '''
        [console_script]
        BunkerSync=BunkerSync:cli
    '''
)
