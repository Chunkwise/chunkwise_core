# Chunkwise core

## About

This core repository contains shared types, chunkers, and utility functions used across multiple Chunkwise services.

### What's included

- **Types**: Shared data types for chunks, chunker configurations, and evaluation metrics
- **Chunkers**: Document chunker implementations
- **Utils**: Currently contains a document normalisation function for stable chunking

## To import to a service

Edit `pyproject.toml` under Poetry dependencies:

`[tool.poetry.dependencies]`

Default import (types and utils):

`chunkwise-core = { git = "https://github.com/Chunkwise/chunkwise_core.git" }`

Import types, utils, and chunkers:

`chunkwise-core = { git = "https://github.com/Chunkwise/chunkwise_core.git", extras = ["chunkers"] }`

## To add to `requirements.txt` for a Docker image

Default:

`chunkwise-core @ git+https://github.com/Chunkwise/chunkwise_core.git`

With chunkers:

`chunkwise-core[chunkers] @ git+https://github.com/Chunkwise/chunkwise_core.git`
