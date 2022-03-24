[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![non-code license](https://img.shields.io/badge/License_(non--code)-CC_BY--NC--SA_3.0-orange)](https://creativecommons.org/licenses/by-nc-sa/3.0/)
![GitHub last commit](https://img.shields.io/github/last-commit/Data-Science-for-Linguists-2022/Child-Vocab-Development)
![GitHub repo size](https://img.shields.io/github/repo-size/Data-Science-for-Linguists-2022/Child-Vocab-Development)

# Child-Vocab-Development

Man Ho Wong  
Updated: March 24, 2022

## Thank you for visiting this project!

This readme file helps you to navigate this repo.  
For project overview, please see [project_plan.md](https://github.com/Data-Science-for-Linguists-2022/Child-Vocab-Development/blob/main/project_plan.md).

## Table of contents
- [Repo directory](#repo-directory)
- [Data processing and analysis](#data-processing-and-analysis)
- [Reports](#reports)
- [Running the codes](#running-the-codes)
  - [Requirements](#requirements)
  - [Data](#data)
- [About](#about)
  - [Data source](#data-source)
  - [Acknowledgment](#acknowledgment)
  - [License](#license)

# Repo directory

```
./
 |---codes/                          # codes for data processing/analysis
 |   |---etc/                        # e.g. pylangacq notes
 |   |---data_curation.ipynb
 |   |---data_preprocessing.ipynb
 |   |---exploratory_analysis.ipynb
 |          
 |---data_samples/                   # data samples for testing the codes
 |
 |---reports/                        # reports, presentations
 |   |---images/
 |   |---progress_report.md
 |
 |---.gitignore
 |---LICENSE.md
 |---project_plan.md
 |---README.md                       # You are here
```

# Data processing and analysis

The following scripts form the pipeline for data processing and analysis. Each generates the data required by the next script. They should be executed in the same sequence as listed:

1. [`data_curation.ipynb`]() curates datasets from CHILDES needed for this project.
2. [`data_preprocessing.ipynb`]() integrates datasets curated and cleans the data before analysis.
3. [`exploratory_analysis.ipynb`]() explores what kinds of linguistic analysis can be done with the curated data.
4. [`linguistic_analysis.ipynb`](#) *Under development*

# Reports

- [`progress_report.md`](#) documents the development of this project.
- [`final_report.*`](#) *Under development*
- [`presentation.*`](#) *Under development*


# Running the codes
Coming soon :-)

## Requirements
Coming soon :-)

## Data
Coming soon :-)

# About

## Data source
The data used in this project was downloaded from the CHILDES database:  
> MacWhinney, B. (2000). The CHILDES Project: Tools for analyzing talk. Third Edition. Mahwah, NJ: Lawrence Erlbaum Associates.

## Acknowledgment
Coming soon :-)

See this [page](https://talkbank.org/share/citation.html) for more information.

## Licenses

The non-code parts of this project are licensed under Attribution-NonCommercial-ShareAlike 3.0 Unported (CC BY-NC-SA 3.0). See [`LICENSE-non_code.md`](https://github.com/Data-Science-for-Linguists-2022/Child-Vocab-Development/blob/main/LICENSE-non_code.md) for more information.  
The rest of this project is licensed under GNU General Public License Version 3 (GPLv3). See [`LICENSE.md`](https://github.com/Data-Science-for-Linguists-2022/Child-Vocab-Development/blob/main/LICENSE.md) for more information.