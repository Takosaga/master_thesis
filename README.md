# Evaluating the Consistency of Explainable AI Methods in Hate Speech Detection on Social Media Platforms

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         master_thesis and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── enviroment.yml   <- The requirements file for reproducing the analysis environment
│                         
│
├── setup.cfg          <- Configuration file for flake8
│
└── master_thesis   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes master_thesis a Python module
    │
    └── config.py               <- Store useful variables and configuration
```

--------

## Notebook Use in Thesis

### Section 1.1

[Eligible and Included studies from literature search](https://www.zotero.org/groups/5798956/gamez_master_thesis)

![image](https://github.com/user-attachments/assets/bc3285ec-59e1-4c7c-948f-c1598d9f91fe)

Notebook 01 was used for analysis on the eligible studies, but was reduced to the 13 included studies about hate speech.

### Section 2.1 

Notebook 02, 03, and 04 were used to understand the datasets

Notebook 05 was to understanding and preparing how to align datasets

Notebook 06 merged datasets

### Section 2.2

Notebook 07 for EDA

### Section 2.3

Notebook 08 and 09 was understanding the models and for original experiment that was not used in this thesis. 09 contains the performance of the CardiffNLP and Facebook models. 

### Section 2.5

Notebook 10c is the final code used on Google Colab to gather experiment data

### Section 3.1

Notebook 11b and 11c were the single samples 

### Section 3.2 and 3.3

Notebook 11 contains aggregated data from experiment results

