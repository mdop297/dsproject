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

## project structure

```plaintext
.
├── config
│   └── config.yaml
├── Dockerfile
├── .github
│   └── workflows
├── .gitignore
├── LICENSE
├── main.py
├── params.yaml
├── README.md
├── requirements.txt
├── research
│   ├── 1_data_ingestion.ipynb
│   ├── 2_data_validation.ipynb
│   ├── 3_data_transformation.ipynb
│   ├── 4_model_trainer.ipynb
│   └── research.ipynb
├── schema.py
├── schema.yaml
├── setup.py
├── src
│   └── dsproject
│       ├── components
│       │   ├── data_ingestion.py
│       │   ├── data_transformation.py
│       │   ├── data_validation.py
│       │   ├── __init__.py
│       │   └── model_trainer.py
│       ├── config
│       │   ├── configurations.py
│       │   └── __init__.py
│       ├── constants
│       │   └── __init__.py
│       ├── entity
│       │   ├── config_entity.py
│       │   └── __init__.py
│       ├── __init__.py
│       ├── pipeline
│       │   ├── data_ingestion_pipeline.py
│       │   ├── data_transformation_pipeline.py
│       │   ├── data_validation_pipeline.py
│       │   ├── __init__.py
│       │   └── model_trainer_pipeline.py
│       └── utils
│           ├── common.py
│           └── __init__.py
├── template.py
└── templates
    └── index.html
```    

## Config management
In this project I use python-box (ConfigBox) to read yaml file and get values in this file instead of using hydra to manage configuration as the complex project. I will have some comparation with these two library later.

## Type checking 
Using @ensure_anotations from ensure library instead of using hydra