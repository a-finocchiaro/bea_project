from distutils.core import setup
setup(
  name = 'pyBea',         # How you named your package folder (MyLib)
  packages = ['bea_data'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A python library that interacts with the Burea of Econmic Analysis API',   # Give a short description about your library
  author = 'Aaron Finocchiaro',                   # Type in your name
  author_email = 'afinny10@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/a-finocchiaro/pybea',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/a-finocchiaro/pybea/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['Pandas', 'Economic', 'Analysis', 'Bureau'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'pandas',
          'requests',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)