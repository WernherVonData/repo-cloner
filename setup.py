import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(name='repo-cloner',
                 version='0.0.1',
                 description='Python utility for cloning repositories',
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 author='Daniel Peczek',
                 author_email='danpeczek@gmail.com',
                 url='https://github.com/danpeczek/repo-cloner',
                 project_urls={
                     "Bug Tracker": "https://github.com/danpeczek/repo-cloner/issues",
                 },
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
                 ],
                 package_dir={"": "repo_cloner"},
                 packages=setuptools.find_packages(where="repo_cloner"),
                 python_requires=">=3.6"
                 )
