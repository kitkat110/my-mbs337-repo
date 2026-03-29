# Homework 08

## About
This directory contains all the files for **Homework 08**, which focuses on DevOps practices for research computing. The goal of this homework is to containerize a minimal Dash web application, demonstrate staging vs. production deployments, automate the development lifecycle with a Makefile, and set up CI/CD pipelines using GitHub Actions.

## Directory Structure
```
my-mbs337-repo/
├── .github/
│   └── workflows/
│       ├── integration-test.yml
│       └── push-to-registry.yml
└── homework08/
    ├── Dockerfile
    ├── Makefile
    ├── app.py
    ├── docker-compose.yml
    ├── docker-compose-staging.yml
    ├── requirements.txt
    └── test/
        └── test_app.py
```

## Summary Workflow
1. Clone repository
2. Start the dashboard using a Makefile target
3. Visit the app in a browser at `http://localhost:8050`
4. Stop the dashboard using a Makefile target

## Starting and Stopping the Dashboard
All commands should be run from inside the `homework08/` directory.

### Production
Start the container (builds first, then runs):
```bash
make compose
```
The dashboard will be available at `http://localhost:8050`

Stop the container:
```bash
make compose-down
```

### Staging
Start the staging container:
```bash
make compose-staging
```
The staging dashboard will be available at `http://localhost:8051`

Stop the staging container:
```bash
make compose-down-staging
```

### Other Makefile Targets
| Target | Description |
|---|---|
| `make build` | Build the Docker image |
| `make run` | Build and run the container directly |
| `make stop` | Stop all running containers |
| `make filter` | List containers exposed on port 8050 |

## Staging vs. Production
| | Staging | Production |
|---|---|---|
| Config file | `docker-compose-staging.yml` | `docker-compose.yml` |
| Port | 8051 | 8050 |
| Purpose | Test changes before release | Serve the stable, released version |

**Staging** is used during active development to verify changes in a containerized environment before promoting them to production. Both environments can run simultaneously since they use separate ports.

## GitHub Actions Workflows
Both workflow files are located in `.github/workflows/` at the root of the repository.

### `integration-test.yml`
**Trigger:** Every push to the repository

Starts the app with Docker Compose, runs `pytest` against `test/test_app.py`, then tears the container down. This catches regressions automatically on every push before code can be merged or deployed.

### `push-to-registry.yml`
**Trigger:** A new Git tag is pushed (e.g. `git tag v1.0.0 && git push --tags`)

Builds the Docker image and pushes it to the GitHub Container Registry (GHCR) tagged with the release version. This automates publishing — tagging a commit is all it takes to release a new versioned image.

## AI Usage
Claude (Anthropic) was used to assist with:
- Writing this README