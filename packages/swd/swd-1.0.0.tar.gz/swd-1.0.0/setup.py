from setuptools import setup, find_packages

def readme():
  with open('README.md', 'r') as f:
    return f.read()

setup(
  name='swd',
  version='1.0.0',
  author='modsdownloader',
  author_email='nikitasss_2000@mail.ru',
  description='Simple Steam Workshop Downloader. Powered by MODSDOWNLOADER.COM',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/DyadyushkaDyadya/swd',
  packages=find_packages(),
  install_requires=['requests>=2.25.1'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License'
  ],
  keywords=[
    'steam workshop downloader',
    'swd',
    'mods downloader',
    'api'
  ],
  project_urls={
    'Documentation': 'https://github.com/DyadyushkaDyadya/swd#readme'
  },
  python_requires='>=3.7'
)