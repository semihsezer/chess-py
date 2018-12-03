## Getting started

Runtime python 3.6

`python setup.py install`

`python chess.py`


## Tests

`python setup.py test` or `py.test`
`py.test -x` will stop after first failure or customize it `py.test --maxfail=2`

For debugging, insert `pytest.set_trace()` to pytest or simply `pdb.set_trace()` to regular python file. Then:
`py.test --pdb` 