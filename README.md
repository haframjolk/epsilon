# Epsilon

Epsilon is a simple anonymous online voting system with single-use password authentication.

## Prerequisites

Epsilon requires Python and [Poetry](https://python-poetry.org).

## Setup

```sh
git clone https://github.com/haframjolk/epsilon.git
cd epsilon
poetry install
```

## Configuration

Elections are configured using a JSON file placed in the repository root called `config.json`. The file must follow the following format and all options must be specified:

```json
{
    "title": "Election Title", // The title of the election
    "passwords": ["123", "321"], // List of allowed, one-time passwords
    "candidates": ["Foo", "Bar"], // List of the candidates running
    "multiple": false, // Allow voters to vote for multiple candidates?
    "out_filename": "results.json" // Filename to write election results to
}
```

## Running

### Development

```sh
poetry shell
flask run
```

### Production

```sh
poetry shell
gunicorn --bind 0.0.0.0:8080 app:app
```
