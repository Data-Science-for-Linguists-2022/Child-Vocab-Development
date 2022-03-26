import pylangacq
from typing import List
import collections

#-------------------------------------------------------------------------------

def get_age_m(ymd) -> float:
    """
    Convert age from year-month-day tuple to age in months.
    
    Parameters
    ymd : tuple
          A tuple of three integers, e.g. (1, 0, 15) for 1 year and 15 days.
    
    Returns
    float
    """    
    age_m = ymd[0]*12 + ymd[1] + round(ymd[2]/30,1)
    return age_m

#-------------------------------------------------------------------------------

def utt_len_w(f_reader, participants='CHI', ignore=[]) -> List[float]:
    """
    Get a list of utterance length by words (MLU-w) for all the utterances
    in the file_reader. 
    
    Parameters
    f_reader : pylangacq.Reader object
               A pylangacq reader object of *one* CHAT file, or a reader of a
               collection of CHAT files indexed to *one* CHAT file.
    participants : str or list[str], optional, default 'CHI' 
                   The participant(s) whose tokens will be extracted from.
    ignore : str or list[str], optional, default []
             The POS to be ignored.
    
    Returns
    List[float] 
    
    Remarks
    - WORDS_TO_IGNORE (basic list of words to be ignored) is the same as in
      pylangacq.Reader.mluw .
    """
    tok_by_utt = f_reader.tokens(participants=participants, by_utterances=True)
    WORDS_TO_IGNORE = ["", "!", "+...", ".", ",", "?", "‡", "„", "0", "CLITIC"]
    WORDS_TO_IGNORE.extend(ignore)  # add user-defined list
    utt_len_list = []
    for utt in tok_by_utt:
        n_word = 0
        for tok in utt:
            if (tok.word not in WORDS_TO_IGNORE):
                n_word += 1
        if n_word > 0:  # exclude 0-length utterances (differs from pylangacq)
            utt_len_list.append(n_word)
    return utt_len_list

#-------------------------------------------------------------------------------

def utt_len_m(f_reader, participants='CHI', ignore=[]) -> List[float]:
    """
    Get a list of utterance length by morphemes (MLU-m) for all the utterances
    in the file_reader. 
    
    Parameters
    f_reader : pylangacq.Reader object
               A pylangacq reader object of *one* CHAT file, or a reader of a
               collection of CHAT files indexed to *one* CHAT file.
    participants : str or list[str], optional, default 'CHI' 
                   The participant(s) whose tokens will be extracted from.
    ignore : str or list[str], optional, default []
             The POS to be ignored.
    
    Returns
    List[float]
    
    Remarks
    - POS_TO_IGNORE (basic list of POS to be ignored) is the same as in
      pylangacq.Reader.mlum .
    """
    tok_by_utt = f_reader.tokens(participants=participants, by_utterances=True)
    POS_TO_IGNORE = ["", "!", "+...", "0", "?", "BEG"]
    POS_TO_IGNORE.extend(ignore)  # add user-defined list
    utt_len_list = []
    for utt in tok_by_utt:
        n_mor = 0
        for tok in utt:
            if (tok.pos not in POS_TO_IGNORE):
                n_mor += 1
                if type(tok.mor) == str:
                    n_mor += tok.mor.count('-')
                    n_mor += tok.mor.count('~')
        if n_mor > 0:
            utt_len_list.append(n_mor)
    return utt_len_list