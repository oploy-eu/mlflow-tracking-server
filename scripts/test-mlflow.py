"""
Quick MLflow connectivity and logging test.

Usage:
    python scripts/test-mlflow.py
    python scripts/test-mlflow.py --uri http://localhost:8080
    python scripts/test-mlflow.py --uri https://your-mlflow-server.example.com
"""

from __future__ import annotations

import argparse
import sys
import time


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Quick MLflow connectivity test")
    parser.add_argument(
        "--uri",
        default="http://localhost:8080",
        help="MLflow tracking URI (default: http://localhost:8080)",
    )
    parser.add_argument(
        "--experiment",
        default="mlflow-test",
        help="Experiment name to use (default: mlflow-test)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    print(f"\n{'━' * 55}")
    print("  MLflow Test")
    print(f"{'━' * 55}")
    print(f"  Tracking URI : {args.uri}")
    print(f"  Experiment   : {args.experiment}")
    print(f"{'━' * 55}\n")

    try:
        import requests

        resp = requests.get(f"{args.uri.rstrip('/')}/health", timeout=5)
        resp.raise_for_status()
        print(f"✅ Server is reachable ({args.uri})\n")
    except Exception as exc:
        print(f"❌ Server is NOT reachable ({args.uri})")
        print(f"   Error: {exc}")
        sys.exit(1)

    try:
        import mlflow

        mlflow.set_tracking_uri(args.uri)
        mlflow.set_experiment(args.experiment)

        with mlflow.start_run(run_name="setup-test") as run:
            mlflow.log_param("test_param", "hello-mlflow")
            mlflow.log_metric("setup_success", 1.0)
            mlflow.log_metric("timestamp", time.time())
            mlflow.log_text(
                f"MLflow test completed successfully.\nURI: {args.uri}",
                "welcome.txt",
            )

            print("✅ Run completed successfully!")
            print(f"   Run ID      : {run.info.run_id}")
            print(f"   Experiment  : {run.info.experiment_id}")
            print(
                f"\n   View it at  : {args.uri}/#/experiments/{run.info.experiment_id}/runs/{run.info.run_id}"
            )
    except ImportError:
        print("❌ MLflow SDK is not installed.")
        print("   Install it: pip install mlflow")
        sys.exit(1)
    except Exception as exc:
        print(f"❌ MLflow run failed: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
