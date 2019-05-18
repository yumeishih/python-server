
### conda
```sh
$ conda info -e
$ conda create -n [NAME] python=3.6
$ source activate [NAME]
$ source deactivate
```

### pip

```sh
$ pip install [moduleName]
$ pip uninstall [moduleName]
$ pip search [moduleName]
```

Save modules name and version into a txt file.

```sh
$ pip freeze > requirements.txt
```
Install from the record.
```sh
$ pip install -r requirements.txt
```