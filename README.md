# Analytics Team Project Template

## Project Description
This project provides a structured template for data science and machine learning projects, ensuring best practices for organizing code, data, and documentation. It includes modular components for data loading, preprocessing, model training, and evaluation, and is built to streamline collaboration and reproducibility.

## Authors
- Samuel Pérez Hurtado
- Analytics Team

## Project structure

```bash
├── {{cookiecutter.project_slug}}/
│   ├── data/
│   │   ├── models/
│   │   │   ├── .gitkeep
│   │   ├── processed/
│   │   │   ├── .gitkeep
│   │   ├── raw/
│   │   │   ├── .gitkeep
│   │   ├── README.md
│   ├── docs/
│   │   ├── data/
│   │   │   ├── models.md
│   │   │   ├── processed.md
│   │   │   ├── raw.md
│   │   ├── iac/
│   │   │   ├── docker.md
│   │   │   ├── gitlab-ci.md
│   │   │   ├── terraform.md
│   │   ├── notebooks/
│   │   │   ├── data_exploration.md
│   │   │   ├── data_preprocessing.md
│   │   │   ├── model_training.md
│   │   ├── src/
│   │   │   ├── data_loading.md
│   │   │   ├── data_preprocessing.md
│   │   │   ├── model.md
│   │   │   ├── train.md
│   │   ├── tests/
│   │   │   ├── test_data_loading.md
│   │   │   ├── test_model.md
│   │   ├── config.py
│   │   ├── index.rst
│   │   ├── make.bat
│   │   ├── Makefile
│   ├── iac/
│   │   ├── docker/
│   │   │   ├── Dockerfile
│   │   ├── gitlab-ci/
│   │   │   ├── .gitlab-ci.yml
│   │   ├── terraform/
│   │   │   ├── main.tf
│   │   │   ├── outputs.tf
│   │   │   ├── variables.tf
│   │   ├── README.md
│   ├── notebooks/
│   │   ├── 0.0-{{ cookiecutter.project_slug }}-data_exploration.ipynb
│   │   ├── 0.1-{{ cookiecutter.project_slug }}-data_preprocessing.ipynb
│   │   ├── 0.2-{{ cookiecutter.project_slug }}-model_training.ipynb
│   │   ├── README.md
│   ├── src/
│   │   ├── 1.1-{{ cookiecutter.project_slug }}-data_loading.py
│   │   ├── 1.2-{{ cookiecutter.project_slug }}-data_preprocessing.py
│   │   ├── 1.3-{{ cookiecutter.project_slug }}-model.py
│   │   ├── 1.4-{{ cookiecutter.project_slug }}-train.py
│   │   ├── README.md
│   ├── tests/
│   │   ├── 2.1-{{ cookiecutter.project_slug }}-test_data_loading.py
│   │   ├── 2.2-{{ cookiecutter.project_slug }}-test_model.py
│   │   ├── README.md
│   ├── .editorconfig
│   ├── README.md
│   ├── requirements.txt
│   ├── setup_env.bat
│   ├── setup_env.sh
│   ├── hooks/
│   │   ├── post_gen_project.py
│   ├── cookiecutter.json
```

## How to clone this template using cookiecutter?

1. Install `cookiecutter` in your local machine by running the following command:
    ```bash
    pip install cookiecutter
    ```

2. Run the command to copy the template and answer the questions such as project name, author, and version:
    ```bash
    cookiecutter https://github.com/fountain-forward/cookiecutter-template
    ```

## How to generate the documentation in PDF format?

Generate the documentation with Sphinx running the following commands:

- For Unix systems (MacOS and Linux):
  ```bash
  cd docs/
  make html && make pdf
  ```
- For Windows systems run:
  ```cmd
  cd docs/
  .\make.bat html
  .\make.bat pdf
  ```