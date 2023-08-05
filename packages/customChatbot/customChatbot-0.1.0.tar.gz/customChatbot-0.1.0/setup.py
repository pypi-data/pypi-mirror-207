from setuptools import find_packages, setup
setup(
    name='customChatbot',
    packages=find_packages(include=['customGPT']),
    version='0.1.0',
    description='It is a custom GPT-3 bot that can be used to answer questions based on a custom dataset',
    author='Me',
)
