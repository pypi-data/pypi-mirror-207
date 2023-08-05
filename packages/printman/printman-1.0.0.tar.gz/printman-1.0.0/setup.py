from setuptools import setup, find_packages

setup(
    name='printman',
    version='1.0.0',
    author='Ayoub Almontaser',
    author_email='',
    description="""A package produced with the help of Chat-GPT to print files through printer IP addresses in the local network. 
    It also has a whatsapp client for receiving files to print.""",
    packages=find_packages(),
    install_requires=[
        'socket',
    ],
)
