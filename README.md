[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![non-code license](https://img.shields.io/badge/License_(non--code)-CC_BY--NC--SA_3.0-orange)](https://creativecommons.org/licenses/by-nc-sa/3.0/)
![GitHub last commit](https://img.shields.io/github/last-commit/Data-Science-for-Linguists-2022/Child-Vocab-Development)
![GitHub repo size](https://img.shields.io/github/repo-size/Data-Science-for-Linguists-2022/Child-Vocab-Development)

# Analysis of lexical semantic network growth in children from different socio-economic backgrounds  

Man Ho Wong (m.wong@pitt.edu), University of Pittsburgh  
April 24, 2022

## Thank you for visiting this project!

This project aims to investigate the relationship between early vocabulary development in children from different socio-economic backgrounds and their mother's child-directed speech (CDS). Lexical semantic networks for the child speech (CS) and the CDS were constructed from individual files in a dataset collected from CHILDES (see [Data sources](#data-sources)). For the original project plan, please see [`project_plan.md`](https://github.com/Data-Science-for-Linguists-2022/Child-Vocab-Development/blob/main/project_plan.md). [`progress_report.md`](https://github.com/Data-Science-for-Linguists-2022/Child-Vocab-Development/blob/main/reports/progress_report.md) documents the development of this project and [`progress_presentation.pdf`](progress_presentation.pdf) summarized the progress at the end of the semester. 

**The final report can be found [here](https://github.com/Data-Science-for-Linguists-2022/Child-Vocab-Development/blob/main/reports/final_report.md).**

The guestbook for the project can be found [Here](https://github.com/Data-Science-for-Linguists-2022/Class-Lounge/blob/main/guestbooks/guestbook_manho.md).

# Table of contents

- [1 Repo directory](#1-repo-directory)
- [2 Data processing and analysis](#2-data-processing-and-analysis)
- [3 Running the code](#3-running-the-code)
  - [Requirements](#requirements)
  - [Data](#data)
- [4 About](#4-about)
  - [Data sources](#data-sources)
  - [Python package `PyLangAcq`](#python-package-pylangacq)
  - [Licenses](#licenses)
  - [Acknowledgment](#acknowledgment)

# 1 Repo directory

```
./
 |---code/                           # code for data processing/analysis
 |   |---etc/
 |   |   |---PyLangAcq_notes.ipynb
 |   |   |---pittchat.py
 |   |
 |   |---data_curation.ipynb
 |   |---data_preprocessing.ipynb
 |   |---exploratory_analysis.ipynb
 |   |---pylangacq_license.txt
 |   |---vocabulary_analysis.ipynb
 |
 |---data/                           # processed and unprocessed data
 |   |---data_samples/               # data samples
 |
 |---reports/                        # reports and presentation
 |   |---images/                     # images used in the final report
 |   |---final_report.md
 |   |---progress_report.md
 |   |---progress_presentation.pdf
 |
 |---.gitignore
 |---LICENSE.md
 |---project_plan.md
 |---README.md                       # YOU ARE HERE
```

# 2 Data processing and analysis

The following scripts form the pipeline for data processing and analysis. Each generates the data required by the next script. They should be executed in the same sequence as listed:

1. [`data_curation.ipynb`](https://github.com/Data-Science-for-Linguists-2022/Child-Vocab-Development/blob/main/code/data_curation.ipynb) ([nbviewer](https://nbviewer.org/github/Data-Science-for-Linguists-2022/Child-Vocab-Development/blob/main/code/data_curation.ipynb)) curates datasets from CHILDES needed for this project.
2. [`data_preprocessing.ipynb`](https://github.com/Data-Science-for-Linguists-2022/Child-Vocab-Development/blob/main/code/data_preprocessing.ipynb) ([nbviewer](https://nbviewer.org/github/Data-Science-for-Linguists-2022/Child-Vocab-Development/blob/main/code/data_preprocessing.ipynb)) integrates datasets curated and cleans the data before analysis.
3. [`exploratory_analysis.ipynb`](https://github.com/Data-Science-for-Linguists-2022/Child-Vocab-Development/blob/main/code/exploratory_analysis.ipynb) ([nbviewer](https://nbviewer.org/github/Data-Science-for-Linguists-2022/Child-Vocab-Development/blob/main/code/exploratory_analysis.ipynb)) explores what kinds of linguistic analysis can be done with the curated data.
4. [`vocabulary_analysis.ipynb`](https://github.com/Data-Science-for-Linguists-2022/Child-Vocab-Development/blob/main/code/vocabulary_analysis.ipynb) ([nbviewer](https://nbviewer.org/github/Data-Science-for-Linguists-2022/Child-Vocab-Development/blob/main/code/vocabulary_analysis.ipynb)) examines the characteristics of semantic networks in children of different SES group.

# 3 Running the code

The code is written in Python 3.9.7. For easy sharing, scripts are organized into Jupyter notebooks (see above).

*Viewing*: You can view the notebooks either on GitHub or on [nbviewer.org](https:/./nbviewer.org/).

*Running*: To run the code, you will need a [Jupyter Notebook interface](https://docs.jupyter.org/en/latest/install.html). You can also run the code on [Google Colab](https://colab.research.google.com/). 

Below is a list of required libraries and packages that are not included in the Python Standard Library, as well as the version tested in this project:

- Gensim (4.1.2)
- Matplotlib (3.4.3)
- NumPy (1.20.3)
- Pandas (1.3.4)
- [PyLangAcq](https://pylangacq.org/) (0.16.0)
- NLTK (3.6.5)
- NetworkX (2.6.3)
- scikit-learn (0.24.2)
- Tqdm (4.62.3) (*Optional*, for showing progress bar during running)

# 4 About

## Data sources

The corpus data used in this project was downloaded from the CHILDES database:  
> MacWhinney, B. (2000). The CHILDES Project: Tools for analyzing talk. Third Edition. Mahwah, NJ: Lawrence Erlbaum Associates.

See this [page](https://talkbank.org/share/citation.html) for more information.

This project also used data containing semantic vectors from [ConceptNet Numberbatch 19.08](https://github.com/commonsense/conceptnet-numberbatch), by
Luminoso Technologies, Inc. You may redistribute or modify the
data under a compatible Share-Alike license.

## Python package `PyLangAcq`

The following Python package was used in this project for processing CHAT files:
> Lee, Jackson L., Ross Burkholder, Gallagher B. Flinn, and Emily R. Coppess. 2016. Working with CHAT transcripts in Python. Technical report TR-2016-02, Department of Computer Science, University of Chicago.  
> Github repo: https://github.com/jacksonllee/pylangacq

The package is licensed under the MIT License. See [`pylangacq_license.txt`](https://github.com/Data-Science-for-Linguists-2022/Child-Vocab-Development/blob/main/code/pylangacq_license.txt) for more information.

## Licenses

The non-code parts of the project are licensed under Attribution-NonCommercial-ShareAlike 3.0 Unported (CC BY-NC-SA 3.0). See [`LICENSE-non_code.md`](https://github.com/Data-Science-for-Linguists-2022/Child-Vocab-Development/blob/main/LICENSE-non_code.md) for more information.  
The rest of the project is licensed under GNU General Public License Version 3 (GPLv3). See [`LICENSE.md`](https://github.com/Data-Science-for-Linguists-2022/Child-Vocab-Development/blob/main/LICENSE.md) for more information.

## Acknowledgment

I would like to thank my instructors and fellow students of the course [Data Science for Linguists](https://naraehan.github.io/Data-Science-for-Linguists-2022/) for their help and valuable inputs. I would also like to express my special thanks to Prof. Na-Rae Han for helping me to review the course [Introduction to Computational Linguistics](https://sites.pitt.edu/~naraehan/ling1330/), which I missed last semester due to other commitments. Both courses helped me to devlop better computational thinking to work with large linguistic data.