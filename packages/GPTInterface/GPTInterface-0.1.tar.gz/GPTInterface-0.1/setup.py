from setuptools import setup, find_packages

setup(
    name='GPTInterface',
    version='0.1',
    author='Michael Nefiodovas',
    author_email='michael@nef.net.au',
    packages=find_packages(),
    url='https://github.com/MouseAndKeyboard/GPTInterface',
    license='LICENSE.txt',
    description='A simple interface to OpenAI\'s GPT-3 API.',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=[
        "openai", 
        "tiktoken"
    ],
)
