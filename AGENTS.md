# AGENTS.md

## Repository identity

- Recommended public repository name: `mlflow-tracking-server`
- Recommended product description: containerized MLflow tracking server deployment for PostgreSQL-backed metadata and optional S3 artifact storage.
- This repository is about deploying and operating MLflow itself, not building a model or agent runtime.

## Agent rules

1. Ground all documentation in the actual files and deployment pattern present in this repository.
2. Do not invent internal infrastructure or hidden services.
3. Treat PostgreSQL credentials, S3 credentials, Railway variables, and server URLs as private.
4. Keep the README focused on why to self-host MLflow, how to deploy it, and how to use it with related projects.
5. When referencing related repositories, describe them as examples or companion projects, not hard dependencies.

## Current repository scope

- containerized MLflow server based on [`Dockerfile`](Dockerfile)
- PostgreSQL-backed metadata store
- optional S3-compatible artifact storage
- Railway deployment guidance
- companion guidance for using this server with agent evaluation and prompt optimization workflows

## Safe cleanup policy

Safe to remove or avoid committing:

- `.env` files
- local MLflow state directories
- local SQLite artifacts
- one-off test outputs

Use caution around:

- deployment commands
- artifact storage configuration
- any example command that may imply real credentials
