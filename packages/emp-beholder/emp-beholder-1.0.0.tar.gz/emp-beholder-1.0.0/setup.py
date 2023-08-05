from setuptools import setup, find_packages

setup(
    name='emp-beholder',
    version='1.0.0',
    author='Ayoub Almontaser',
    author_email='',
    description="""A for recording the screen during tests.""",
    packages=find_packages(),
    install_requires=[
        'socket',
    ],
)

