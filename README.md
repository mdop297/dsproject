# dsproject

## Workflows --ML Pipeline

1. Data Ingestion
2. Data Validation
3. Data Transformation
4. Model Trainer
5. Model Evaluation

## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py


## Config management
In this project I use python-box (ConfigBox) to read yaml file and get values in this file instead of using hydra to manage configuration as the complex project. I will have some comparation with these two library later.

## Type checking 
Using @ensure_anotations from ensure library instead of using hydra