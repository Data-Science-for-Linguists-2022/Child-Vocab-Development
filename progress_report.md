# Progress Report

## Project creation
- Date: 2/15/2022
- Progress: Project finalized
- Next steps: reading relevant publications, exploring datasets, exploring relevant Python packages

---

# 1st Progress Report

- Date: 2/27/2022
- Current stage: data curation

### Progress

I first explored the structure and the data formats of the target database, CHILDES, and found several tools which I can use to read the CHAT files from the database. I finally decided to use the Python package, `PyLangAcq`, for this project. 

I then intalled the `PyLangAcq` and learned how to use the package to get the data I need. I created a notebook named `data_curation.ipynb` to demonstate how `PyLangAcq` can be used to access information stored in CHAT files and how I can use the information to search for target datasets containing data required for this project. A notebook about `PyLangAcq` was also created as a quick reference ([PyLangAcq_notes.ipynb]()).

In this notebook, I used the Brown Corpus in CHILDES as an example to demonstrate what one can do with `PyLangAcq`. The zip file of the corpus can be found [here](). With this sample corpus, I explored the contents and the data structure of the corpus and the contained CHAT files.  

I found 11 North American English corpora in CHILDES that meet the data needs of the project. I performed a quick statistic analysis to get an idea about the size of the data I am working with, and whether I will need more data for the project. I finally decided that I will primarily work on these CHILDES datasets as the data is already sufficient (5,984,750 tokens and 860,597 utterances). Several data objects storing the data in these corpora were created and pickled for further processing and linguistic analysis. The pickles are stored locally and will not be pushed to GitHub.

