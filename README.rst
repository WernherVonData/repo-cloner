repo-cloner
=====

Open source repository cloner.

- Github: https://github.com/danpeczek/repo-cloner

repo-cloner is a python utility to clone multiple repositories at once without bothering
to do it manual. Tool reads the information about your repositories and clone them into current
directory.

+-------------------------+
| **develop**             |
+=========================+
| |Build Status Develop|  |
+-------------------------+

Setup
=====

Currently the tool is available only on test pypi repository.

.. code-block:: bash

    $ pip install -i https://test.pypi.org/simple/ repo-cloner==0.0.4

Now try to run repo-cloner:

.. code-block:: bash

    $ repo-cloner -h
    Usage: repo-cloner [--help][-h][--repo_file][-rf]
    --help, -h: prints this message
    --repo_file, -rf: .yml file with list of repositories to clone

License
-------

`MIT LICENSE <./LICENSE>`__

.. |Build Status Develop| image:: https://ci.conan.io/buildStatus/icon?job=ConanTestSuite/develop
   :target: https://api.travis-ci.com/danpeczek/repo-cloner.svg?branch=main