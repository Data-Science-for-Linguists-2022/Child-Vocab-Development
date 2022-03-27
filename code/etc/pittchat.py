import pylangacq
from typing import List, Counter
from collections import Counter

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
             The words to be ignored.
    
    Returns
    List[float] or 0 if no utterance found
    
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
            
    # return 0 if utt_len_list is empty
    return utt_len_list if utt_len_list else 0

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
    List[float] or 0 if no utterance found
    
    Remarks
    - POS_TO_IGNORE (basic list of POS to be ignored) is the same as in
      pylangacq.Reader.mlum, with the addition of '.' and 'None'.
    """
    tok_by_utt = f_reader.tokens(participants=participants, by_utterances=True)
    POS_TO_IGNORE   = ["", "!", "+...", "0", "?", "BEG", '.', None]
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
            
    # return 0 if utt_len_list is empty
    return utt_len_list if utt_len_list else 0

#-------------------------------------------------------------------------------
def get_pos_pro(f_reader, participants='CHI', pos=[], ref_pos=[])-> List[float]:
    """
    Get a list of utterance length by morphemes (MLU-m) for all the utterances
    in the file_reader. 
    
    Parameters
    f_reader : pylangacq.Reader object
               A pylangacq reader object of *one* CHAT file, or a reader of a
               collection of CHAT files indexed to *one* CHAT file.
    participants : str or list[str], optional, default 'CHI' 
                   The participant(s) whose tokens will be extracted from.
    pos : str or list[str], optional, default []
          The target POS of query
    ref_pos : str or list[str], optional, default []
              The reference POS. (i.e., denominator of fraction)
    
    Returns
    List[float] or 0 if no tokens of ref_pos is found
    
    Remarks
    - WORDS_TO_IGNORE (basic list of POS to be ignored) is the same as in
      pylangacq.Reader.ttr .
    - POS_TO_IGNORE (basic list of POS to be ignored) is the same as in
      pylangacq.Reader.mlum, with the addition of '.' and 'None'.
    """
    toks = f_reader.tokens(participants=participants)
    WORDS_TO_IGNORE = ["", "!", "+...", ".", ",", "?", "‡", "„", "0", "CLITIC"]
    POS_TO_IGNORE   = ["", "!", "+...", "0", "?", "BEG", '.', None]
    target_tok_list = [tok.word for tok in toks if
                       (tok.word not in WORDS_TO_IGNORE) and
                       (tok.pos not in POS_TO_IGNORE) and
                       ((not pos) or tok.pos in pos)]
    ref_tok_list    = [tok.word for tok in toks if
                       (tok.word not in WORDS_TO_IGNORE) and
                       (tok.pos not in POS_TO_IGNORE) and
                       ((not ref_pos) or tok.pos in ref_pos)]

    # return 0 if ref_tok_list is empty
    if ref_tok_list:
        return len(set(target_tok_list))/len(set(ref_tok_list))
    else:
        return 0

#-------------------------------------------------------------------------------
def get_wfreq(f_reader, participants='CHI', pos=[]):
    """
    Get a list of utterance length by morphemes (MLU-m) for all the utterances
    in the file_reader. 
    
    Parameters
    f_reader : pylangacq.Reader object
    participants : str or list[str], optional, default 'CHI' 
                   The participant(s) whose tokens will be extracted from.
    pos : str or list[str], optional, default []
          The target POS of query
    
    Returns
    Counter()
    
    Remarks
    - WORDS_TO_IGNORE (basic list of POS to be ignored) is the same as in
      pylangacq.Reader.ttr .
    - POS_TO_IGNORE (basic list of POS to be ignored) is the same as in
      pylangacq.Reader.mlum, with the addition of '.', 'None' and 'n:prop'.
    """
    WORDS_TO_IGNORE = ["", "!", "+...", ".", ",", "?", "‡", "„", "0", "CLITIC"]
    POS_TO_IGNORE   = ["", "!", "+...", "0", "?", "BEG", '.', None, 'n:prop']
    toks = f_reader.tokens(participants=participants)
    tok_list_pos = [tok.word for tok in toks if
                    (tok.word not in WORDS_TO_IGNORE) and
                    (tok.pos not in POS_TO_IGNORE) and
                    ((not pos) or tok.pos in pos)]
    return Counter(tok_list_pos)