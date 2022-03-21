# Epsilon

Epsilon is a simple anonymous online voting system with single-use password authentication.

## Prerequisites

Epsilon requires Python 3.9 or later and [Poetry](https://python-poetry.org).

## Setup

```sh
git clone https://github.com/haframjolk/epsilon.git
cd epsilon
poetry install
```

## Configuration

Elections are configured using a JSON file placed in the repository root called `config.json`. The file must follow the following format and all options must be specified:

```js
{
    "title": "Election Title", // The title of the election
    "passwords": ["123", "321"], // List of allowed, one-time passwords
    "candidates": ["Foo", "Bar"], // List of the candidates running
    "max_candidates": 1, // Maximum number of candidates a voter can vote for (-1 for no limit)
    "out_filename": "results.json" // Filename to write election results to
}
```

## Running

### Development

```sh
poetry run flask run
```

### Production

```sh
poetry run ./serve.py
```

For production use I recommend setting up a reverse proxy using Apache or nginx and serving requests to Epsilon at <http://127.0.0.1:8080>.

Votes are written to the results file when the election ends. To end the election, simply stop the Epsilon process by pressing <kbd>CTRL</kbd>+<kbd>C</kbd>.
