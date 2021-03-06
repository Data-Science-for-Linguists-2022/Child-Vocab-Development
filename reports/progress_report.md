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

I then intalled the `PyLangAcq` and learned how to use the package to get the data I need. I created a notebook named [`data_curation.ipynb`](https://github.com/Data-Science-for-Linguists-2022/Child-Vocab-Development/blob/main/code/data_curation.ipynb) to demonstate how `PyLangAcq` can be used to access information stored in CHAT files and how I can use the information to search for target datasets containing data required for this project. A notebook about `PyLangAcq` was also created as a quick reference ([`PyLangAcq_notes.ipynb`](https://github.com/Data-Science-for-Linguists-2022/Child-Vocab-Development/blob/main/code/etc/PyLangAcq_notes.ipynb)).

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

- Date: 3/24/2022
- Current stage: data cleaning/ integration and exploratory analysis
- Next step: linguistic analysis

## Progress

I integrated the data I currated in [`data_curation.ipynb`](https://github.com/Data-Science-for-Linguists-2022/Child-Vocab-Development/blob/main/code/data_curation.ipynb)(script type: `NEW CONTINUING`) by merging some of the labels defining the CHAT files in the dataset. This process was documented in [`data_preprocessing.ipynb`](https://github.com/Data-Science-for-Linguists-2022/Child-Vocab-Development/blob/main/code/data_preprocessing.ipynb). In addition, I also cleaned the data by removing files recorded in less naturalistic situations (e.g., book reading and elicited data). More details can also be found in [`data_preprocessing.ipynb`](https://github.com/Data-Science-for-Linguists-2022/Child-Vocab-Development/blob/main/code/data_preprocessing.ipynb).

For exploratory analysis ([`exploratory_analysis.ipynb`](https://github.com/Data-Science-for-Linguists-2022/Child-Vocab-Development/blob/main/code/exploratory_analysis.ipynb))(script type: `NEW CONTINUING`), I tried `pylangacq`'s default methods for a few linguistic measurements (e.g. mean length of utterance by morpheme, MLU-M), but I found a few limitations that may not suit my project. For example, I could not choose what punctuations or which word classes/parts of speech (POSs) to include or exclude in my analysis. Therefore, I wrote three functions to get the same measurements with more options. These functions measure MLU, TTR or word frequency with the option to select POSs to analyze. In addition, I also wrote a function to convert the default age format (in year-month-day) to age in months. This will come in handy later when I need to analyze vocabulary development by age. 

Besides data processing and data analysis, I also reorganized my repo and updated my [`README.md`](https://github.com/Data-Science-for-Linguists-2022/Child-Vocab-Development/blob/main/README.md) file to help visitors to navigate my repo.

## Sharing plan

I will use the same license as planned for the non-code parts of the project: Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported (**CC BY-NC-SA 3.0**) license. For details, see [`last progress report`](#1st-Progress-Report) or [`LICENSE-non_code.md`](https://github.com/Data-Science-for-Linguists-2022/Child-Vocab-Development/blob/main/LICENSE-non_code.md).

The rest of the project is licensed under GNU General Public License Version 3 (GPLv3). See [`LICENSE.md`](https://github.com/Data-Science-for-Linguists-2022/Child-Vocab-Development/blob/main/LICENSE.md) for more information.

# 3rd Progress Report

- Date: 4/12/2022
- Current stage: Linguistic analysis
- Next step: More linguistic analysis on all files; statistics

## Progress

In the last stage, I explored the data by checking whether differences between children of different background can be observed after data processing ([`exploratory_analysis.ipynb`](https://github.com/Data-Science-for-Linguists-2022/Child-Vocab-Development/blob/main/code/exploratory_analysis.ipynb))(script type: `EXISTING`). Specifically, I looked at the mean length of utterance (MLU), which is a common metric to measure vocabulary development in children. In this stage, I decided to dig a bit deeper into the data by analyzing the lexical semantic networks, which are supposed to be more informative about vocabulary development and acquisition. After doing some literature research, I decided to construct semantic networks based on word similarity derived from word vectors based on `ConceptNet-Numberbatch`.

I also tried out different Python packages and decided to do my analysis mainly with the `Gensim` and `NetworkX` packages. In this stage, I only perform analysis on one file, but I developed a pipeline which can easily be expanded to other files in the dataset (see [`vocabulary_analysis.ipynb`](https://github.com/Data-Science-for-Linguists-2022/Child-Vocab-Development/blob/main/code/vocabulary_analysis.ipynb) (script type: `NEW CONTINUING`)). This include a custom function and a general procedure to construct a semantic network from a list of words. I was looking for a suitable similarity threshold in literature and decided to use 0.19 as the threshold, although more testing will probably be needed. I recognized some problems in building semantic networks (such as the threshold problem and out-of-vocabulary problem), which I may need to address them in the next step depending on how they would affect my analysis.

