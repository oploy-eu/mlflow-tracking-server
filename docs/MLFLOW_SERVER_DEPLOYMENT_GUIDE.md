# MLflow Server Deployment Guide

## Goal

Run MLflow as a hosted tracking server with:

- PostgreSQL for experiment metadata
- optional S3-compatible object storage for artifacts
- a clean browser-accessible web UI

## Why hosted MLflow instead of local-only MLflow

Hosted MLflow is useful when:

- local SQLite becomes limiting for richer experiment data
- artifacts become too large or messy on the local machine
- you want a central UI across multiple repositories
- you need persistent prompt, run, trace, and evaluation history

## Recommended deployment ingredients

### Required

- MLflow server container
- PostgreSQL database

### Recommended

- S3-compatible artifact bucket

## Environment variables

```env
BACKEND_STORE_URI=postgresql://postgres:your-password@your-host:5432/railway
BACKEND_S3=s3://mlflow-artifacts/
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_DEFAULT_REGION=
```

## Current container behavior

The current startup command is configured in [`Dockerfile`](../Dockerfile) and launches MLflow with:

- `--backend-store-uri $BACKEND_STORE_URI`
- `--default-artifact-root ${BACKEND_S3:-$BACKEND_s3}`
- `--host 0.0.0.0`
- `--port 8080`

## Persistent artifacts recommendation

Without S3-style storage, artifacts written to `/app/mlruns` are ephemeral and may disappear on restart or redeploy.

For production-like usage, configure object storage from the start.

## Railway note

If you want to keep costs lower when MLflow is not actively needed, the service can be paused operationally by changing the start behavior, for example using a sleep-based custom command such as `sleep infinity` while idle.
