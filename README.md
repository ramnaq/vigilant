# Vigilant

A poor programming language.

## Setup

### Requirements

Python 3.9 and its dependencies, defined in `requirements.txt`:

- `ply`, for lexing the input file.

### Install

It's recommended to use a virtual environment such as `venv`. To initialize
`venv`, run

```bash
$ python3 -m venv .venv
$ source .venv/bin/activate
```

Either using or not a virtual env, to install dependencies, run

```bash
$ pip install -r requirements.txt
```

## Run

This project includes three programs as example, `example<1,2,3>.lcc`.
To run all of them, execute

```bash
$ make all
```

To run each one execute

```bash
$ make ex1
$ make ex2
$ make ex3
```

The "raw command" can also be used instead, it's quite simple:

```bash
$ python main.py your_program.py
```
