# Project Plan

Man Ho Wong | m.wong@pitt.edu | Feb 1st, 2022

**Working title:**

Relationship between vocabulary development and child-directed speech

**Summary:**

Vocabulary development of a child has been linked to mother's educational background and socio-economic status. For example, children from families of higher socio-economic status have been shown to have larger vocabulary size in early ages. The goal of this project is to study the relationship between vocabulary development and child-directed speech (CDS) among native American English speakers. Ideally, I would be able to use the knowledge we learn from American English speakers to predict if there is any similar relationship in other languages. Because of time constraints, the last goal may not be achieved before the end of the semester. Nevertheless, the findings of this project will hopefully provide some helpful preliminary data for future study.

# Data

The data required for this project should be free and licensed in the public domain. At the moment, I have found two online datasets consist of the information I will need and have fairly large sample size:
- For age of acquisition, Wordbank ([website](http://wordbank.stanford.edu/)) provides the age of production for approximately 400 words in the CDI categories;
- For child-directed speech, CHILDES ([website](https://childes.talkbank.org/)) provides transcripts of mother-child interaction in different environments.

For data pre-processing and clean-up, I will need to look for a subset of data in both datasets to match the words produced by children and the age of children. I will need to create a vocabulary of child-directed speech by e.g. using Python's NLTK word tokenization. As Na-Rae suggested, there are existing Python packages avaible for well-known database like CHILDES. Originally, I planned to re-annotate the word categories in these datasets myself to fit my study purposes, but I decided to follow Lindsey and Sean's advice to reduce the number of datasets I need to deal with. Hopefully, I will have more time to focus on the analysis part.

For more details about data processing, see the part "Timeline" below.

# Analysis

To understand better how exactly child's family background contribute to vocabulary development, I will compare the frequency of words in child-directed speech and the age of acquisition for the corresponding words in American English. If information about child's family background is not available in CHILDES, or different measures are used in Wordbank and CHILDES, I will look for sex different instead. I will also compare such a relationship in different word categories, such as MacArthur-Bates Communicative Development Inventory (CDI) categories, synatactic categories and/or morphologically inflected word forms. To characterize CDS, I will measure word/sentence length, TTR and MLU (if possible). I will also compare the word frequency distribution of CDS and that of American English. Ideally, I would like to build a predictive model (likely a regression model, but this depends on the data) of age of acquisition (AoA) of a given word based on word categories. Finally, if enough samples are available and time is allowed, I would like to use the model to predict vocabulary development in other languages. My hypothesis is that, similar relationship should maintain across languages in normally developed children.

Finally, as Lindsey suggested, difference in poverty rate (and other differences among cultures/societies) may also contribute the the difference in vocabulary development of Children within a society, I will pay attention on this and see if my data will reflect this. 

# Presentation

The project will be made available to the public on GitHub. It will be presented in Jupyter Notebook mainly.

# Timeline (tentative)

| Stage | Objective | Target completion date |
|---|---|---|
| **Data Curation** | Identify relevant sub-dataset in Wordbank and related publications | 2/20/2022 |
|  | Identify relevant sub-dataset in CHILDES: age- and sex-matched  child-directed speech from all control groups | 2/20/2022 |
|  | Identify additional data required for linguistic Analysis,  e.g. English word frequency distribution, CDI word list | 2/20/2022 |
|  | Check license info and download data; if not available for public use,  contact copyright owners or look for alternative data source | 2/21/2022 |
|  | Explore raw data format/structure and decide on suitable  data structure for data preprocessing | 2/21/2022 |
|  | Convert data to Python data structure (will most likely use `Pandas`) | 2/22/2022 |
|  | 1st progress report | 2/24/2022 |
| **Data preprocessing** | Exploratory Data Analysis (ongoing) | N.A. |
|  | Data cleaning and transformation (e.g. clean missing data,  word tokenization of child-directed speech, annotation) | 3/6/2022 |
|  | Data integration (integrate datasets by using same data types,  format and annotation; matching age, sex and other factors;  normalizing data if necessary.) | 3/20/2022 |
|  | 2nd progress report | 3/22/2022 |
| **Linguistic Analysis** | TBD (will be updated after first/second stage). Available packages: | TBD |
|  | https://www.nltk.org/howto/childes.html |  |
|  | https://pylangacq.org/ |  |
| **(Model building, TBD)** | 3rd progress report | 4/12/2022 |
| **Presentation and report** | Oral presentation | 4/14-4/21/2022   |
|  | Final report | TBD |

# acknowledgment

I would like to thank Prof. Na-Rae Han, Lindsey Rojtas and Sean Steinle for their help with the development of this project.