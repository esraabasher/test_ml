import mlflow

if __name__ == "__main__":
    # create a new mlflow experiment
    experiment_id = mlflow.create_experiment(
        name="test_mlflow1",
        artifact_location="test_mlflow1_artifacts",
        tags={"env": "dev", "version": "1.0.0"},
    )

    print(experiment_id)