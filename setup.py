from distutils.core import setup

setup(name='repo-cloner',
      version='0.0.1',
      description='Python utility for cloning repositories',
      author='Daniel Peczek',
      author_email='danpeczek@gmail.com',
      packages=['repo_cloner'],
      # To provide executable scripts, use entry points in preference to the
      # "scripts" keyword. Entry points provide cross-platform support and allow
      # pip to create the appropriate form of executable for the target platform.
      entry_points={
            'console_scripts': [
                  'repo_cloner=repo_cloner.repo_cloner:main'
            ]
      }
)
