from setuptools import setup, find_packages

setup(
    name='emp-taskman',
    version='1.0.0',
    author='Ayoub Almontaser',
    author_email='',
    description="""A package produced with the help of Chat-GPT to manage external processes.""",
    packages=find_packages(),
    install_requires=[
        'socket',
    ],
)

