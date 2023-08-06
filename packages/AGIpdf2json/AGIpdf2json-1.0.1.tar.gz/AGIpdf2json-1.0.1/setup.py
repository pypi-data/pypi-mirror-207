from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='AGIpdf2json',
    version='1.0.1',
    packages=find_packages(),
    install_requires=[
        'pdfplumber',
        'click'
    ],
    description='This package can help user parse PDF files into text file and JSON file. Additionally, it can help user parse question-answer pairs into a JSONL document in prompt-completion format, that is supported by OpenAI',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Mayank Monu',
    author_email='mayankmono29@gmail.com',
    entry_points={
        'console_scripts': [
            'AGIpdf2json=AGIPDF2JSON.main:cli',
        ],
    },
)
