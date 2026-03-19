FROM ghcr.io/mlflow/mlflow:v3.10.1-full

CMD ["sh", "-c", "mlflow server --host 0.0.0.0 --port 8080 --backend-store-uri $BACKEND_STORE_URI --default-artifact-root ${BACKEND_S3:-$BACKEND_s3} --allowed-hosts \"*\" --cors-allowed-origins \"*\""]

