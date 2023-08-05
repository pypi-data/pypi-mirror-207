## DeepSim
This toolkit provides deep learning-based similarity utilities. 

### Example

```python
'''models for type
BERT: 
shibing624/text2vec-base-chinese
sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
hfl/chinese-macbert-base: 
uer/roberta-medium-wwm-chinese-cluecorpussmall
hfl/chinese-roberta-wwm-ext
Langboat/mengzi-bert-base
WMD: 
w2v-light-tencent-chinese
'''
from deepsim import *
sim_utils=SimilarityUtils(type='w2v')
list_r=sim_utils.get_similarity('I like you!','I love you!')
print(list_r)

```

### License
The `deepsim` project is provided by [Donghua Chen](https://github.com/dhchenx). 
