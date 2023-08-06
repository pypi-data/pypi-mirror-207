# djungle-rulesengine-client
A client to Djungle Studio rulesengine API


## Tests
This project uses `tox` to run the test suite:
simply run the command `tox` in the root of the repository.

## Release
This project uses `tox` to release a version to PyPI.
Run `tox -e release -- <env>`, where `<env>` is an index identifier in
your `~/.pypirc` file.
