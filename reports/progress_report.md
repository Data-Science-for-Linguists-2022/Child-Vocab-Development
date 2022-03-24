# Progress Report

Man Ho Wong | m.wong@pitt.edu | Feb 27th, 2022

## Project creation
- Date: 2/15/2022
- Progress: Project finalized
- Next steps: reading relevant publications, exploring datasets, exploring relevant Python packages

---

# 1st Progress Report

- Date: 2/27/2022
- Current stage: data curation
- Next step: data preprocessing (e.g. data cleaning)

## Progress

I first explored the structure and the data formats of the target database, [CHILDES](https://childes.talkbank.org/), and found several tools which I can use to read the CHAT files from the database. I finally decided to use the Python package, `PyLangAcq` ([website](https://pylangacq.org/)), for this project. 

I then intalled the `PyLangAcq` and learned how to use the package to get the data I need. I created a notebook named [data_curation.ipynb](https://github.com/Data-Science-for-Linguists-2022/Child-Vocab-Development/blob/main/codes/data_curation.ipynb) to demonstate how `PyLangAcq` can be used to access information stored in CHAT files and how I can use the information to search for target datasets containing data required for this project. A notebook about `PyLangAcq` was also created as a quick reference ([PyLangAcq_notes.ipynb](https://github.com/Data-Science-for-Linguists-2022/Child-Vocab-Development/blob/main/codes/etc/PyLangAcq_notes.ipynb)).

In this notebook, I used the Brown Corpus in CHILDES ([download link](https://childes.talkbank.org/data/Eng-NA/Brown.zip)) as an example to demonstrate what one can do with `PyLangAcq`. The zip file of the corpus can be found in [this folder](https://github.com/Data-Science-for-Linguists-2022/Child-Vocab-Development/tree/main/data_samples/childes). With this sample corpus, I explored the contents and the data structure of the corpus and the contained CHAT files.  

From CHILDES's website, I found 47 North American English corpora which I could potentially use for this project (the list of corpora is stored as a csv file; a sample list can be found in [this folder](https://github.com/Data-Science-for-Linguists-2022/Child-Vocab-Development/tree/main/data_samples/childes). Among these corpora, I found 11 North American English corpora in CHILDES that meet the data needs of the project. I performed a quick statistic analysis to get an idea about the size of the data I am working with, and whether I will need more data for the project. I finally decided that I will primarily work on these CHILDES datasets as the data is already sufficient (5,984,750 tokens and 860,597 utterances). Several data objects storing the data in these corpora were created and pickled for further processing and linguistic analysis. The pickles are stored locally and will not be pushed to GitHub.

### Citation requirements
Since I am using more than six corpora from CHILDES, I do not need to cite each corpus separately, but instead, just need to cite the database (i.e. CHILDES):  
MacWhinney, B. (2000). The CHILDES Project: Tools for analyzing talk. Third Edition. Mahwah, NJ: Lawrence Erlbaum Associates.


More rules about citation can be found [here](https://talkbank.org/share/citation.html).

## Sharing plan

Since the original data was published under Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported (**CC BY-NC-SA 3.0**) license, I am required to share my work under the same license.

See [this page](https://creativecommons.org/licenses/by-nc-sa/3.0/) for more information.

# 2nd Progress Report

- Date: 4/24/2022
- Current stage: data cleaning/ integration and exploratory analysis
- Next step: linguistic analysis

## Progress

- data integration

- data cleaning

- exploratory analysis
    - MLU
    - TTR
    - Word frequency
    - self-defined functions

- etc.
    - Reorganized directory

- Next step
