# Analysis of lexical semantic network growth in children from different socio-economic backgrounds

by Man Ho Wong, University of Pittsburgh  
May 1st, 2022

---

# 1 Introduction and project development

Mother's educational background and socio-economic status (SES) have been shown to influence early vocabulary development in children. For example, vocabulary size of children from families of higher SES have been shown to be larger than that of children from families of lower SES at the same age during early development. To goal of this project is to understand better how exactly the vocabulary development differs among children of different SES group, and how it is affected by the mother's child-directed speech (CDS).

Originally, the project started quite amibitiously: I was planning to use data from two online databases, CHILDES (see next section) and WordBank. Since the tokens in WordBank are included in the MacArthur-Bates Communicative Development Inventory (MB-CDI) used in many studies to evaluate a child's vocabulary size, I planned to integrate the data from two databases by matching the tokens in CHILDES to those in WordBank, which would allow me to estimate the vocabulary size in each child in CHILDES. However, I realized that I would probably have no enough time for this project to integrate the two databases as it involves annotating thousands of files, not too mentioned that most files in CHILDES would not have enough words to represent a child's CDI-vocabulary. Therefore, I decided to use only CHILDES for this project and changed my analysis plan accordingly.

In the original project plan, I planned to quantify the CDI-vocabulary size in each child, as well as comparing the frequency of words in the mother's CDS and the age of acquisition (AOA) for the corresponding words. I planned to characterize the child speech (CS) and the CDS by using word count-based metrics, such as the mean length of utterance (MLU), type-to-token ratio (TTR), noun-to-verb ratio (NTVR) and word frequency by lexcial categories However, since information about the CDI word list and AOA for the words are not available in CHILDES, I decided to change my analysis focus from word count-based metrics to lexical semantic network analysis.

Lexical semantic network analysis focuses on word-word relationships. Differences in semantic networks have been found in children of various developmental conditions, such as typically devloped children and later talkers. However, there are no studies look at effects of SES on semantic network during development. I took this project as a chance to explore the potential of studying the effects of SES with semantic network analysis. In this project, I demonstrated how semantic network analysis can be performed with data combined from different previous studies. I also showed that semantic network analysis may provide a possible way to analyze a child's vocabulary development with only a subset of the child's vocabulary.

For reference, the original project plan can be found [here]().

---

# 2 Data sourcing

The data curation process of the project is documanted in [`data_curation.ipynb`](https://github.com/Data-Science-for-Linguists-2022/Child-Vocab-Development/blob/main/code/data_curation.ipynb). 

## 2.1 CHILDES

Data used in this project was downloaded from the online speech database, Child Language Data Exchange System (CHILDES). 
>MacWhinney, B. (2000). The CHILDES Project: Tools for analyzing talk. Third Edition. Mahwah, NJ: Lawrence Erlbaum Associates.

CHILDES is the child language component of TalkBank maintained by Brian MacWhinney at Carnegie Mellon University, Pittsburgh, USA. It is a multilingual database containing corpora with transcriptions, audio recordings and/or video recordings of child speech (CS) and child-directed speech (CDS) at different developmental stages. The recording transcripts in the database are stored in CHAT formats. ([Example](https://childes.talkbank.org/access/Eng-NA/Brown.html)). CHILDES is licensed under Creative Commons License (CC BY-NC-SA 3.0).

## 2.2 PyLangAcq package

The python package PyLangAcq was used to read CHAT files as suggested by Prof. Na-Rae Han. See [`data_curation.ipynb`](https://github.com/Data-Science-for-Linguists-2022/Child-Vocab-Development/blob/main/code/data_curation.ipynb) for demonstration.

## 2.3 Corpora used in this project

There are 47 North American English corpora in CHILDES (see TalkBank's [browsable database](https://sla.talkbank.org/TBB/childes); also listed in `data/data_samples/childes/eng_NA_corpus_list.csv`). For this project, I collected the transcipts for both the CS and the associated CDS from the following 13 corpora in CHILDES: Bates, Bernstein, Brown, Clark, Demetras2, Gleason, HSLLD, Hall, Hicks, Nelson, NewmanRatner, Post and VanHouten.

## 2.4 Data search strategy

Dataset curation was documented in [`data_curation.ipynb`](https://github.com/Data-Science-for-Linguists-2022/Child-Vocab-Development/blob/main/code/data_curation.ipynb). Briefly, I screened for suitable CHAT files in three phases. In the first first phase, I narrowed down the scope of search by identifying the relevant corpora fitting a set of basic criteria:
- Participants: data includes child or mother
- Child information: data contains child age, sex and socioeconomic status (SES) information
- Mother information: data contains socioeconomic status (SES), education information
For efficiency, not all files were read and screened:  Handling all corpora at once as one PyLangAcq `Reader` object is not memory-efficient, but reading each single CHAT file into individual `Reader`s does not allow parallelized reading and parsing and thus it is less efficient. Therefore, instead of reading all corpora at once or reading each CHAT file one by one,  CHAT files in each corpus were read and evaluated parallelly each time. As long as there was a CHAT file in a corpus meeting the above criteria, the corpus would be included in the next phase  (because CHAT files belonging to the same corpus are supposed to come from the same study contain similar header information).

In the first phase, the 13 corpora mentioned previously were identified. These corpora were then downloaded to local drive. In the second phase, all CHAT files in the identified corpora were screened and only those matching the above criteria were kept. In addition to the previous criteria, I also narrowed the age range of the child participants down to 6 years old. In the third phase, the curated dataset was refined through out the data processing pipeline. The CHAT files matching the search criteria were indexed by their header information which was stored in a DataFrame called `data_idx`. `data_idx` was pickled and stored locally for further data processing and analysis later. The list of corpora identified were also pickled as a list `search_result` for quicker re-run of the search if needed.

To organize the header information stored in each CHAT file in `data_idx`, I created the following variables for different attributes of a CHAT file: 
- `mot_edu`: mother's education level 
- `group`: child's developmental group, e.g. typically developed
- `ses`: child's SES (socioeconomic status; same as mother's)
- `situation`: situation of recording (e.g. play session)
- `activities`: activities during recording (e.g. Toy play)
- `study_type`: type of study (e.g. longitudinal study)

### Data before cleaning and processing

The figure below shows the composition of the curated dataset before data preprocessing.

![data_composition_unprocessed.svg](images/data_composition_unprocessed.svg)

The figure below shows the demographics of the child participants in the dataset before data preprocessing. Note that child participants involved in longitudinal studies may have multiple files in the dataset. Those file were recorded at different time and thus were treated as separate files in this project.

![child_demgph_unprocessed.svg](images/child_demgph_unprocessed.svg)

As shown above in the participant demographics, different corpora use different sets of labels and definitions for the same variable (e.g. mother's education). Besides, there are files that were not needed (e.g. children in groups other than typically development). Therefore, the dataset curated in were cleaned and preprocessed before analysis.

---

# 3 Data cleaning

The curated dataset was further processed in [`data_preprocessing.ipynb`](https://github.com/Data-Science-for-Linguists-2022/Child-Vocab-Development/blob/main/code/data_preprocessing.ipynb) to prepare the data for linguistic analysis later.

The figure below shows the demographics of the child participants in the dataset after data preprocessing.

![child_demgph_processed.svg](images/child_demgph_processed.svg)

In summary, the following changes were made to the index of the dataset (`data_idx`):
1. Similar `mot_edu` labels in `data_idx` were merged and changed to custom labels.
2. All entries in `data_idx` were labeled as `TD` for `group`.
3. Similar `SES` labels were merged and changed to three classes: `WC` (working class), `MC` (middle class) and `UC` (upper class).
4. Unknown labels were marked as `unspecified`.
5. Entries collected from children of adolescent mothers were dropped.
6. Entries containing recordings from less naturalistic situations or maternal interviews (without CDS) were dropped.
7. A unique child ID was created for each entry.

After data preprocessing, 972 entries were dropped and there are 1639 remaining entries. The processed dataset was indexed by a DataFrame called `data_idx_processed`.

---

# 4 Exploratory data analysis

The quality of the processed dataset was evaluated in [`exploratory_analysis.ipynb`](https://github.com/Data-Science-for-Linguists-2022/Child-Vocab-Development/blob/main/code/exploratory_analysis.ipynb) Besides, the limitations the dataset were also identified for further data cleaning. The objectives of this section are summarized as follow: 
1. To identify the tools available for measuring MLU:
    - Assess the tools available in the `PyLangAcq` package and identify their limitations
    - Develop custom functions specifically designed for this project
2. To evaluate the quality and limitations of the processed dataset with MLU:
    - Is the sample size sufficient?
    - Is the sample distribution balanced so that fair comparison between different groups can be made?
    - Can we really combine different corpora?

## 4.1 Evaluating dataset with MLU

A common way to measure a child's linguistic productivity is to look at the child's mean length of utterance (MLU). In General, MLU increases with age during early development. It can be measured by morphemes (MLU-m) or by words (MLU-w):  
`MLU-m = number of morphemes / number of utterances`

The accuracy of MLU depends on the overall quality of the data, which relies on: 
- correctly parsed speech
- Sample size (total number of utterances)

Therefore, by measuring MLU, we can assess whether the quality of the processed dataset is high enough for the study of vocabulary development: we should see an increase in MLU during development. Besides, if there is any effect of socio-economic status (SES) on vocabulary development, it should also be reflected by differences in MLU among different SES groups.

MLU can be computed with the MLU functions in the `PyLangAcq` package. However, they have a few limitations which make them unsuited for this project. For example, these functions count the punctuation period (.) as a word or empty string (e.g., the annotation for the punctuation period; some corpora also annotate gestures or actions) as a morpheme. Consequently, utterances with no words but just punctuation would be included in the calculation of the mean. Besides, the `PyLangAcq` functions only return average values: you cannot get the distribution of utterance length, nor the median length (MdLU) or other MLU variants such as MLU5-w (mean length of five longest utterances by words).

To overcome the limitations of `PyLangAcq` functions, I developed similar custom functions for this project. The functions are stored in [`./etc/pittchat.py`](https://github.com/Data-Science-for-Linguists-2022/Child-Vocab-Development/blob/main/code/etc/pittchat.py).

## 4.2 Comparing MLU-m between childen of different SES

I first compared the MLU-m between children of different SES (upper class UC, middle class MC and working class WC). MLU-w was not measured as MLU-m was sufficient to reveal the effects of SES.

![mlu_all_ages.svg](images/mlu_all_ages.svg)

The figure above shows that MLU increases with age regardless of the child's SES. This suggests that the age effect on MLU was preserved in the dataset after preprocessing - the quality of the dataset was sufficient to reveal the age effect. If we compare the overall trends of MLU between different SES groups, we can also find a possible effect of SES on MLU: within the same age range, UC has the highest MLU and WC has the lowest.

While the quality of the dataset is high enough to reveal developmental changes, however, the dataset has a very imbalanced sample distribution for different SES groups.

![age_dist_by_ses.svg](images/age_dist_by_ses.svg)

As shown in the histogram, most of the samples (i.e. CHAT files) for WC have age above 40 months, while there are much fewer samples for UC. For fair comparison, the following analysis will focus on the range of **20 to 42 months** where WC and MC have similar sample distribution and where most UC samples are included. This is also the age range when the difference in vocabulary size among children of different SES was observed in other studies.

Note that some age groups seem to have an unusually large sample size. These samples could possibly come from corpora where participant age was well-matched, or from repeated recordings of the same individual participants.

## 4.3 Checking effects of recording length on MLU

One thing we need to consider when combining different datasets is that, data samples may have different lengths of recording. This will affect the values of MLU: For example, samples with short duration only provide a "cross-sectional" view of a participant's linguistic productivity, and therefore the measured MLU may not reflect the overall linguistic productivity of the participant. To check whether the length of recording has an impact on the measurement of MLU and thus distorting the observed age or SES effect on vocabulary development, I measured three additional variants of MLU:
- **MLU100-m**: MLU-m of first 100 utterances
- **MLU5-m**: MLU-m of first 5 utterances
- **VLU-m**: Variance of utterance length by morpheme

![mlu_variants.svg](images/mlu_variants.svg)

As shown in the figure above, same effects of age and SES can be observed in all the four variants of MLU, although the degree of effects might be different with different measurements. This demonstrates that, with suitable analysis, it is possible to uncover the effects of age and SES on vocabulary development even the dataset contains samples of different recording lengths. 

To summarize, this section demonstrated that the quality of the processed datasset was sufficient for further analysis by showing that MLU increases during development and SES likely has an effect on MLU. Looking at the sample distribution by participant's age, I decided to focus on the age range of 20 to 42 months for further analysis. With different variants of MLU, I also showed the effects of age and SES on vocabulary development can be uncovered even the dataset consists of samples of different recording lengths. Together, the above observations show that it is possible to use a dataset combined from different studies to investigate the effects of SES on early vocabulary development.

---

# 5 Vocabulary analysis

This section is documented in [`vocabulary_analysis.ipynb`](https://github.com/Data-Science-for-Linguists-2022/Child-Vocab-Development/blob/main/code/vocabulary_analysis.ipynb).

## 5.1 Vocabulary as a lexical semantic network

Currently, many studies on early vocabulary development rely on quantifying vocabulary growth by token or morpheme counting, such as the mean length of utterance as we have discussed in the last section, or vocabulary size by number of words. To the best of my knowledge, no study has investigated the word-word relationships during development in children of different SES groups. This section aims to explore the potential of analyzing the word-word relationships in different SES groups with semantic network analysis.

## 5.2 Getting word embeddings from ConceptNet

Relationships between words in a lexicon can be represented by how similar they are in their semantic meanings. There are many metrics to measure word-to-word similarity. In general, these metrics can be derived from two different sources: human-annotated datasets (e.g. WordNet), or word associations learned by machine algorithms (e.g. word2vec). Both sources have their pros and cons for different applications. In this project, I used machine-generated word associations for the calculation of word-to-word similarity because it is more flexible (e.g. getting different word associations by using different training data) than human-annotated datasets and is probably less prone to human biases (depending on training data). Besides, human-annotated datasets are based on formal taxonomies of words and such knowledge is unlikely to be present in a young child's world.

There are two main types of machine-learning models to generate word associations, count-based and prediction-based models. In this project, word similarity were computed from word embeddings based on a semantic network called **ConceptNet**, which is a network built by both count-based and prediction-based models. The most unique feature about ConceptNet is that, unlike other semantic networks, it is concept-based rather than word-based (though nodes are still represented by words or phrases). For mapping word relations in a young child's lexicon where word meanings are closely related to the concepts that they are acquiring at the same time, this concept-based feature probably makes ConceptNet more suitable for this project than word embeddings derived from other models.

## 5.3 Pipeline for constructing lexical semantic network

Below are the steps of the pipeline used for constructing lexical semantic network from each participant's word list in each CHAT file. This pipeline were applied to all CHAT files in the dataset.
1. Extract tokens from a CHAT file
2. Import ConceptNet-Numberbatch word vectors
3. Map each word in the word list to its word vector
4. Compute pairwise word similarity (cosine similarity) from word vectors
5. Construct a semantic network using cosine similarities as the weights of edges

Due to time constraints and computing resources, I did not train my own model to get the word vectors. Instead, I used a pre-trained dataset, ConceptNet-Numberbatch, to get the word vectors. It can be download from their official GitHub. In this project, I used the Gensim package to process word vectors. The figure below shows the word vectors generated from a file in the 'Eve' dataset of the Brown Corpus.

![eve_vectors.svg](images/eve_vectors.svg)

To construct a semantic network, we need to know the word similarity between every possible pair of words. As far as I know, Gensim can only compute cosine similarity between a pair of words one at a time. Therefore, I used a Scikit-learn function called `pairwise.cosine_similarity`, to compute the pairwise cosine similarity. A matrix of cosine similarities was generated from the word vectors in each CHAT file. As an example, the following figure shows the cosine similarity matrix generated from the 'Eve' dataset.

![eve_sim_mat.svg](images/eve_sim_mat.svg)

In a semantic network, words are the nodes and they can be linked by edges representing word similarity. For this project, I chose to work with the NetworkX library because of its ease of use in Python and a large collection of algorithms for network analysis.

For the similarity threshold ($\varepsilon$), I will use the value 0.19 as suggested by 
>Amatuni and Bergelson (2017). Semantic Networks Generated from Early Linguistic Input. BioRxiv 157701; doi: https://doi.org/10.1101/157701.

Below is a semantic network constructed with NetworkX from the 'Eve' dataset shown previously:

![eve_network.svg](images/eve_network.svg)

Note that a child may produce "words" that not found in their native language as creating new words are very common among young children. Such words may not be found in ConceptNet and this may generate errors. This is generally referred as an out-of-vocabulary (OOV) problem. To handle these words, I simply removed them from the list, although it may be neccessary to develop a better strategy to handle OOV words in the future.

## 5.4 Semantic network analysis

### Characterizing semantic network

In the following analysis, I quantified the network properties of each semantic network with the following common metrics:
- number of nodes
- number of edges
- average degree (K)
- average shortest path length (L)
- average local clustering coefficient (C)

The number of nodes gives us an idea about the size of a semantic network. The other metrics tell us about the overall connectivity of the network. In addition, L and C also allow us to quantify global and local connectivity of the network.

One thing we should consider when computing L and C is that, some semantic networks may contain disconnected components. For example, in Eve's semantic network, there are two disconnected components:

![net_components.svg](images/net_components.svg)

Depending on the sizes (here: number of nodes) of a network's components, the value of C can vary a lot. Therefore, I also looked at C of the largest component (C<sub>0</sub>) in addition to the whole network's C. Besides, L cannot be computed from networks containing disconnected components because there are no paths between nodes of different components. Therefore, I only computed the L for the largest component (L<sub>0</sub>).

### Effects of semantic network size on network properties

As discussed in the last notebook, the curated dataset contains samples of different recording lengths. Therefore, semantic networks constructed from different samples were expected to have different sizes in terms of node number. For fair comparison, we should limit our analysis to networks of similar size. To examine how the network size influences the measurement of other network properties, I inspected the interaction between node number and L<sub>0</sub> , as well as between node number and C<sub>0</sub> .

![effects_node_number.svg](images/effects_node_number.svg)

The figure above shows an interesting non-linear interaction between node number and L<sub>0</sub> or C<sub>0</sub> : L<sub>0</sub> increases as the network grows in size while C<sub>0</sub> decreases, but both values stop changing and become stable when the network size reaches at around 50 nodes, suggesting that global and local connectivity are stabilized when the network grows to a certain size. This is itself an intriguing phenomenon worth further investigation in the future. Nevertheless, I am focusing on comparing semantic networks across different SES groups in this project.

Note that I did not look at all network properties available as I found that some of them are closely related with each other. For example, node number is directly proportional to the average degree, k:

![k_vs_n.svg](images/k_vs_n.svg)

Since the values of L<sub>0</sub> and C<sub>0</sub> become relatively unaffected by node number in semantic networks containing more than 50 nodes, I only included these networks in the analysis.

Four network properties were analyzed here:
- Average degree, K
- Average shortest path length (largest component), L<sub>0</sub>
- Average local clustering coefficient, C
- Average local clustering coefficient (largest component), C<sub>0</sub>

![net_prop_cs.svg](images/net_prop_cs.svg)

For semantic networks in the CS, SES seems to specifically affect only the average degree but not other network properties: the average degree increases during development in MC and UC children, but not in WC children. As noted earlier, node number (i.e. number of words in the semantic network) is directly proportional to the average degree. Therefore, higher average degree indicates larger vocabulary size. This observation agrees with the larger vocabulary size observed in UC children in other studies.

The unchanged L and C during development show that global and local connectivity of a growing semantic network is very stable regardless of the SES, suggesting that the small-world characteristic of semantic networks is preserved during development.

The results here also demonstrate that the average degree of a semantic network could be used as a proxy for vocabulary size, despite each network in the dataset only contains a subset of the child's vocabulary. Measuring average degree of a child's semantic network is potentially more efficient and naturalistic than measuring a child's vocabulary size through parent reporting using standardized word list such as the MacArthur-Bates Communicative Development Inventory (MB-CDI) used in most studies on early vocabulary development. It would be helpful in the future to further study the possibility of using average degree as a proxy for vocabulary size.

For semantic networks in the mother's CDS, the network properties seems to be minimally influenced by SES. Specifically, the difference in average degree between MC and WC mothers is not as obvious as what we observed in children. Unfortunately, the sample size for UC was not sufficient to see any effects of SES. 

![net_prop_cds.svg](images/net_prop_cds.svg)

To see if there is any correlation between the effects of SES on CS and CDS, only files containing both CS and CDS were included in the analysis. Since the sample size was not big enough to study the correlation in different age groups separately, I looked at the overall correlation in all samples regardless of age.

![net_prop_cs_vs_cds.svg](images/net_prop_cs_vs_cds.svg)

Two observations can be made from the above figure: First, the interaction between CS and CDS may be different in MC and WC. In general, K for CS is higher in MC than in WC within the same range of K for CDS, while C, C<sub>0</sub> and L<sub>0</sub> for CS is lower in MC than in WC. Second, there is a positive relationship between CS and CDS, though the relationship seems to be weaker in WC for K. These observations suggest that the overall network connectivity of CS is likely modulated by that of CDS and the degree of modulation differs between MC and WC.

---

# 6 Summary

This project performed simple network analysis on the dataset by first constructing lexical semantic networks from individual CHAT files in the dataset. The following observations were made from the semantic networks in CS and CDS:
- The average shortest path length (L) and average local clustering coefficient (C) do not change with node number in networks containing more than 50 nodes, suggesting that the global and local network connectivity of a semantic network are fairly stable even when new nodes are added to the network.
- L and C also do not change during development, suggesting that the global and local network connectivity are stable over time during early vocabulary development.
- The average degree (K) could potentially be used as a proxy for vocabulary size in the assessment of early vocabulary growth.
- The overall network connectivity of CS is likely modulated by that of CDS.

Due to time constraints, the above observations were not tested statistically. Besides, the sample size may not be sufficient to draw conclusions from the observations. The inherently small size of semantic networks in children also makes it impossible to perform some common types of network analysis, such as the degree distribution. Nevertheless, despite the limitations of the dataset, this project demonstrated the possibility of studying early vocabulary development with semantic network analysis using a combined source of data.



