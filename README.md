# Core

## About

The core repository contains types and chunkers shared by multiple services. Types are always imported while chunkers are an optional import.

## To import to a service

Edit `pyproject.toml` under Poetry dependencies:

`[tool.poetry.dependencies]`

Default import (types only):

`chunkwise-core = { git = "https://github.com/Chunkwise/chunkwise_core.git" }`

Import types and chunkers:

`chunkwise-core = { git = "https://github.com/Chunkwise/chunkwise_core.git", extras = ["chunkers"] }`

## To add to `requirements.txt` for a Docker image

Default:

`chunkwise-core @ git+https://github.com/Chunkwise/chunkwise_core.git`

With chunkers:

`chunkwise-core[chunkers] @ git+https://github.com/Chunkwise/chunkwise_core.git`
