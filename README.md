# Evaluating the Consistency of Explainable AI Methods in Hate Speech Detection on Social Media Platforms

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

[Kanban Board](https://github.com/users/Takosaga/projects/3)

## Project Overview

This repository contains the complete codebase, data processing, and analysis for my master's thesis on evaluating the consistency of Explainable Artificial Intelligence (XAI) methods when applied to hate speech detection models. As social media platforms increasingly rely on AI systems to detect and moderate harmful content at scale, the need for transparent and reliable explanations of these automated decisions becomes critical. This research addresses a significant gap in the field by systematically evaluating how consistent XAI methods are when explaining hate speech detection models.

The research specifically focuses on comparing two popular post-hoc explanation techniques: Local Interpretable Model-agnostic Explanations (LIME) and SHapley Additive exPlanations (SHAP). By applying quantitative and qualitative evaluation methodologies, this project provides insights into the consistency of these explanation methods in the context of hate speech detection.

### Data Processing and Analysis

The project aggregates multiple hate speech datasets (HateXplain, MLMA, and Measuring Hate Speech) from various social media platforms including Twitter, YouTube, Reddit, and Gab. This approach ensures diverse representation of hate speech instances across different contexts. Data processing included standardization of annotation formats, normalization of target group categorizations, and creation of consistent labeling schemes.

Exploratory data analysis provides insights into class distributions, platform representation, and target demographics, establishing a solid foundation for subsequent modeling and evaluation.

### Model Selection and XAI Implementation

![image](https://github.com/user-attachments/assets/6a7e2c41-7de5-4a69-886b-61aebaff5cc1)

![image](https://github.com/user-attachments/assets/5ecd5ca4-d1a6-4964-a610-dd03967ed895)


The research utilizes the CardiffNLP model, a RoBERTa-based architecture specifically fine-tuned for hate speech detection. This state-of-the-art transformer model serves as the base classifier for which explanations are generated and evaluated.

The implementation includes:

- Integration of LIME and SHAP explanation frameworks with the transformer-based model
- Development of a controlled experimental setup to isolate the effect of stochasticity on explanation consistency
- Implementation of stratified sampling to ensure evaluation across diverse prediction scenarios
- Application of multiple consistency metrics including Jaccard Similarity, Spearman Correlation, and Kendall Tau-b


### Visualization and Evaluation

![image](https://github.com/user-attachments/assets/a1826f97-95fb-4ecb-b750-75e522b97969)

![image](https://github.com/user-attachments/assets/71e022b6-ce6a-41e8-9c29-adfe56582fb1)

The project features comprehensive visualization techniques to represent explanation consistency, including:

- Heatmap visualizations of word importance attributions
- Consistency matrices showing agreement between multiple explanation runs
- Comparative visualizations of LIME and SHAP explanations across different prediction outcomes

These visualizations not only support the quantitative findings but also provide intuitive understanding of explanation behavior for different types of content and model predictions.

## Key Findings

The research yielded the following findings regarding XAI consistency in hate speech detection:

- SHAP generally provides more consistent explanations than LIME across multiple runs, confirming the initial research hypothesis
- Explanation consistency varies across different prediction scenarios for LIME (true positives, true negatives, false positives, false negatives)

## Technical Skills Demonstrated

This project demonstrates proficiency in numerous technical skills valuable in data science and AI development roles:

- **Explainable AI**: Integration and evaluation of state-of-the-art explanation techniques for black-box models
- **Data Analysis**: Comprehensive exploratory data analysis and statistical evaluation of results
- **Data Visualization**: Creation of informative and intuitive visualizations to communicate complex findings
- **Research Methodology**: Design and implementation of rigorous experimental protocols to test specific hypotheses
- **Python Programming**: Extensive use of Python and relevant libraries (Transformers, LIME, SHAP, pandas, matplotlib)

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

01 was used for analysis on the eligible studies, but was reduced to the 13 included studies about hate speech.

### Section 2.1 

02, 03, and 04 were used to understand the datasets

05 was to understanding and preparing how to align datasets

06 merged datasets

### Section 2.2

07 for EDA

### Section 2.3

08 and 09 was understanding the models and for original experiment that was not used in this thesis. 09 contains the performance of the CardiffNLP and Facebook models. 

### Section 2.5

10c is the final code used on Google Colab to gather experiment data

### Section 3.1

11b and 11c were the single samples 

### Section 3.2 and 3.3

11 contains aggregated data from experiment results

## Reproduction and Extension

To reproduce the results or extend this research:

1. Clone this repository
2. Install the required dependencies using the provided `environment.yml` file
3. Follow the notebooks in sequential order to process data, train models, and generate explanations
4. Explore the evaluation metrics and visualization tools to analyze explanation consistency

The modular design of this project makes it straightforward to extend with additional datasets, models, or XAI methods.

## Future Directions

This research opens several avenues for future work:

- Evaluation of additional XAI methods beyond LIME and SHAP
- Investigation of consistency across different model architectures and training regimes
- Development of more robust explanation methods specifically designed for content moderation
- Integration of user studies to evaluate the practical utility of explanations for content moderators
