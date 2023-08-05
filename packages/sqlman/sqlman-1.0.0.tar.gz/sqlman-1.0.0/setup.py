from setuptools import setup, find_packages

setup(
    name='sqlman',
    version='1.0.0',
    author='Ayoub Almontaser',
    author_email='',
    description="""A package produced with the help of Chat-GPT to connect python to sql server.""",
    packages=find_packages(),
    install_requires=[
        'socket',
    ],
)

