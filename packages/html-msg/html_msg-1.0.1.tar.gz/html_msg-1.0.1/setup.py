from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()



setup_args = dict(
    name='html_msg',
    version='1.0.1',
    description='This tool allows to create HTML message via simple methods, \
        even if you dont now HTML',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n',
    license='MIT',
    packages=find_packages(),
    author='Sirakan Bagdasarian',
    author_email='bsirak@bk.ru',
    keywords=['HTML', 'Message'],
    #url='https://github.com/',
    #download_url='https://pypi.org/project/'
)

install_requires = [
    'IPython',
    'pandas'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)