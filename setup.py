from distutils.core import setup
setup(
  name = 'bea_data',
  packages = ['bea_data'],
  version = '0.1',
  license='MIT',
  description = 'A python library that interacts with the Burea of Econmic Analysis API',
  author = 'Aaron Finocchiaro',
  author_email = 'afinny10@gmail.com',
  url = 'https://github.com/a-finocchiaro/bea_project',
  download_url = 'https://github.com/a-finocchiaro/bea_project/archive/v_01.tar.gz',
  keywords = ['Pandas', 'Economic', 'Analysis', 'Bureau'],
  install_requires=[
          'pandas',
          'requests',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)