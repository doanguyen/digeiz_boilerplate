# A boilerplate project for python packages

A boilerplate project to use when bootstrapping new Python 3 projects.
Copy the source code (no need to fork it), tweak the ``setup.py`` file to suit your needs and start doing things.

## Features

* Test automation and environment provisioning using [Tox](https://tox.readthedocs.io)
* Static code analysis using [Flake8](http://flake8.pycqa.org/en/latest/)
* Unit testing using [ pytest ](https://docs.pytest.org/en/latest/)
* Enforced code coverage threshold using [ coverage ](https://coverage.readthedocs.io)
* Dependencies pinned to the major version, allowing for backwards-compatible updates when upstream
* Licensed under [CC0 Public Domain Dedication](http://creativecommons.org/publicdomain/zero/1.0/),
  you can copy/paste anything and not worry about a thing, not even giving original authors attribution.

## Usage

*Remember only to follow those instructions after editing the source code to bootstrap your new
project.*

### Run the application

```shell
pipenv install
pipenv shell
flask db upgrade
flask run
```

### Run test suite

```shell
pipenv run pytest
```

### License Notice
Python Project Boilerplate - A boilerplate project for python packages

Written in 2020 by Francesco Perna

To the extent possible under law, the author(s) have dedicated all copyright
and related and neighboring rights to this software to the public domain
worldwide. This software is distributed without any warranty.

You should have received a copy of the CC0 Public Domain Dedication along
with this software. If not, see <http://creativecommons.org/publicdomain/zero/1.0/>.
