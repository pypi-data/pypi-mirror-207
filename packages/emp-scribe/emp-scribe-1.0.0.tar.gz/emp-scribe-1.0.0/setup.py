from setuptools import setup, find_packages

setup(
    name='emp-scribe',
    version='1.0.0',
    author='Ayoub Almontaser',
    author_email='',
    description="""A custo-made tool for automated reporting""",
    packages=find_packages(),
    install_requires=[
        'socket',
    ],
)

