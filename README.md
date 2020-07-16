# Cookiecutter Archimedes

_The boilerplate setup for any Archimedes Energy Modelling project._

## Usage

Standalone:

```sh
cookiecutter https://git.optimeering.no/archimedes/cookiecutter-archimedes
```

In Python:

```py
from cookiecutter.main import cookiecutter

cookiecutter(
    "https://git.optimeering.no/archimedes/archimedes-cookiecutter.git",
    extra_context={
        "project_name": "Testproject",
        "examples": False,
        "author_name": "N.N.",
        "description": "No description",
    },
    no_input=True
)
```

This repo is used by the Arhcimedes CLI (when calling `arhcimedes new ...`).
See the codebase for the [Archimedes Python Client](https://git.optimeering.no/archimedes/archimedes-python-client).