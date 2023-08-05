Budo Systems Pytest Suite
=========================

This add-on to the Budo Systems platform creates a standardized test suite
for modules that implement services abstracted in Budo Systems Core
(`project <https://gitlab.com/budosystems/budosystems-core>`_,
`docs <https://budosystems.readthedocs.io/>`_).

This early version only provides a test suite for a ``Repository``.  However, you get 21 ready-to-use tests for free to
validate your implementation of a ``Repository``.

Usage
-----
The assumption here is that you're using this package to add tests for an implementation of a feature for Budo Systems.

Step 1. Installation
~~~~~~~~~~~~~~~~~~~~

From your project environment, first you need to install the package.  There are several options for this.  Here are
but a few examples.

#. Install directly with ``pip``:

    |shell|

    .. code:: sh

        pip install pytest-budosystems

#. Add to ``requirements.txt``, and install using that file:

    |unifile| ``requirements.txt``

    .. code::

        budosystems-core
        pytest-budosystems

    |shell|

    .. code:: sh

        pip install -r requirements.txt

#. Add to ``setup.cfg``, and reinstall your project:

    |unifile| ``setup.cfg``

    .. code:: cfg

        [metadata]
        name = my-budosystems-project
        version = 0.0.2
        description = My implementation of a Budo Systems feature.

        [options]
        python_requires = >= 3.9
        packages = find_namespace:
        package_dir =
            =src

        install_requires =
            budosystems-core
            another-required-package
            something-else-needed

        [options.packages.find]
        where = src

        [options.extras_require]
        test =
            pytest
            pytest-budosystems

    |shell|

    .. code:: sh

        pip install -U -e .

Step 2. Add to your test suite
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To use this test suite to test your implementation of a ``budosystems.storage.repository.Repository``, you'll need to
create a test class that inherits from
``budosystems.xtra.pytest_suite.repository.AbstractTestRepository`` and override a few fixture methods.

The only required fixture method is ``repo_class``.  It's an abstract method with the following specs:

.. code:: python

    @abstractmethod
    @fixture(scope="class")
    def repo_class(self) -> type[Repository]:
        """Returns the class for the implementation of `Repository` being tested."""

Your testing needs may require you to override some other fixture methods.  The two most likely candidates are
``repo_args`` and ``repo_inaccessible``.  Here's how they are defined in ``AbstractTestRepository``

.. code:: python

    @fixture(scope="class")
    def repo_args(self) -> dict[str, Any]:
        """Returns implementation specific arguments to instantiate the implementation of
        `Repository` being tested."""
        return {}

    @fixture(scope="class")
    def repo_inaccessible(self, repo_class: type[Repository]) -> Repository:
        """
        Returns an instance of the implementation of `Repository` with improper connection.
        """
        pytest.skip(f"No 'inaccessible' implementation of {str(repo_class)}")

Minimal Example
+++++++++++++++

A minimal example can be found in the test suite for Budo Systems Core:

|unifile| ``test_dict_repository.py``

.. code:: python

    from pytest import fixture
    from budosystems.xtra.pytest_suite.repository import AbstractTestRepository
    from budosystems.storage.repository import Repository
    from budosystems.storage.dict_repository import DictRepository

    class TestDictRepository(AbstractTestRepository):

        @fixture(scope="class")
        def repo_class(self) -> type[Repository]:
            return DictRepository

A More Complex Example
++++++++++++++++++++++

An example that overrides all the methods listed above can be found in the test suite for Budo Systems SQLite Storage:

|unifile| ``test_repository.py``

.. code:: python

    from pytest import fixture
    import sqlite3
    from typing import Any

    from budosystems.xtra.pytest_suite.repository import AbstractTestRepository
    from budosystems.storage.repository import Repository
    from budosystems.xtra.sqlite3_storage.repository import SQLite3Repository

    class TestSQLite3Repository(AbstractTestRepository):

        @fixture(scope="class")
        def repo_class(self) -> type[Repository]:
            return SQLite3Repository

        @fixture(scope="class")
        def repo_args(self) -> dict[str, Any]:
            return {"con": sqlite3.connect(":memory:")}

        @fixture(scope="class")
        def repo_inaccessible(self, repo_class: type[Repository]) -> Repository:
            con = sqlite3.connect(":memory:")
            repo = repo_class(con=con)
            con.close()
            return repo

Step 3. Test!
~~~~~~~~~~~~~

Run ``pytest`` and get your results.

.. |unishell| unicode:: U+1f41a
.. |unifile| unicode:: U+1f4dd
.. |shell| replace:: |unishell| shell
