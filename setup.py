from distutils.core import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name='repo-cloner',
      version='0.0.1',
      description='Python utility for cloning repositories',
      author='Daniel Peczek',
      author_email='danpeczek@gmail.com',
      packages=['repo_cloner'],
      url='https://github.com/danpeczek/repo-cloner',
      # To provide executable scripts, use entry points in preference to the
      # "scripts" keyword. Entry points provide cross-platform support and allow
      # pip to create the appropriate form of executable for the target platform.
      entry_points={
            'console_scripts': [
                  'repo_cloner=repo_cloner.repo_cloner:main'
            ]
      },
      classifiers=[
            'Environment :: Console',
            'Intended Audience :: Developers',
            'Operating System :: Linux',
            'Programming Language :: Python',
            'Topic :: Communications :: Github',
            'Topic :: Communications :: Email',
            'Topic :: Software Development :: Bug Tracking'
      ]
)
