# Job Agent Backend MLflow Guide

This document captures the main MLflow workflow patterns previously documented inside [`job-agent-backend`](job-agent-backend), but reframes them as companion guidance for a hosted MLflow server.

## What the companion backend uses MLflow for

The agent backend uses MLflow for:

- production tracing
- prompt registry workflows
- evaluation datasets
- scorer and judge logic
- baseline evaluation
- prompt optimization

## Practical workflow sequence

Recommended order:

1. create an experiment
2. register prompt and dataset assets
3. run a baseline evaluation
4. review traces and metrics
5. optimize prompt candidates
6. validate before promotion

## Why a hosted server matters in this workflow

This workflow benefits from a hosted MLflow server because it provides:

- durable metadata in PostgreSQL
- a shared UI for reviewing traces and runs
- cleaner prompt and dataset lifecycle management
- less local artifact clutter

## Key concepts to carry into related projects

### Prompt registry

Use prompt registry when you want:

- versioned prompt history
- aliases such as `baseline`, `candidate`, and `production`
- reproducible comparisons between prompt versions

### Datasets

Use curated datasets so optimization is driven by repeatable evaluation cases instead of ad hoc manual testing.

### Scorers and judges

Use a mix of:

- code-based scorers for deterministic checks
- LLM judges for higher-level quality checks

### Baseline before optimization

Always establish a baseline first so prompt changes can be compared against a known state.

## Included example utility

The repository includes a generic MLflow connectivity test in [`scripts/test-mlflow.py`](../scripts/test-mlflow.py).

That script is useful for:

- testing server reachability
- checking whether runs can be logged successfully
- validating that the deployed MLflow server is usable before connecting companion application repositories
