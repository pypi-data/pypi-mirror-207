from text2vec import Similarity, SimilarityType,EmbeddingType,EncoderType

'''models
BERT: 
shibing624/text2vec-base-chinese: 用CoSENT方法训练，基于MacBERT在中文STS-B数据训练得到，并在中文STS-B测试集评估达到SOTA
sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2: 用SBERT训练，是paraphrase-MiniLM-L12-v2模型的多语言版本，支持中文、英文等
hfl/chinese-macbert-base: 
uer/roberta-medium-wwm-chinese-cluecorpussmall
hfl/chinese-roberta-wwm-ext
Langboat/mengzi-bert-base
WMD: 
w2v-light-tencent-chinese
'''

class SimilarityUtils:
    def __init__(self,type="sbert"):
        sbert_models = [
            'bert-base-chinese',
            'hfl/chinese-macbert-base',
            'hfl/chinese-roberta-wwm-ext'
        ]

        cosent_models = [
            'hfl/chinese-macbert-base',
            'Langboat/mengzi-bert-base',
            'bert-base-chinese',
            'hfl/chinese-roberta-wwm-ext'
        ]

        w2v_models = [
            'w2v-light-tencent-chinese'
        ]

        if type=="sbert":
            self.used_model=sbert_models
        if type=="cosent":
            self.used_model=cosent_models
        if type=="w2v":
            self.used_model=w2v_models
        self.dict_models={}
        for model_path in self.used_model:
            if type=="sbert":
                sim_model = Similarity(
                    model_name_or_path=model_path,
                    similarity_type=SimilarityType.COSINE,
                    embedding_type=EmbeddingType.BERT,
                    encoder_type=EncoderType.MEAN
                )
                self.dict_models[model_path] = sim_model
            if type=="cosent":
                sim_model = Similarity(
                    model_name_or_path=model_path,
                    similarity_type=SimilarityType.COSINE,
                    embedding_type=EmbeddingType.BERT,
                    encoder_type=EncoderType.MEAN
                )
                self.dict_models[model_path] = sim_model
            if type=="w2v":
                sim_model = Similarity(
                    model_name_or_path=model_path,
                    similarity_type=SimilarityType.WMD,
                    embedding_type=EmbeddingType.WORD2VEC,
                  #  encoder_type=EncoderType.MEAN
                )
                self.dict_models[model_path] = sim_model

    def get_similarity(self,s1,s2):
        list_model=[]
        for k in self.dict_models:
            score=self.dict_models[k].get_score(s1,s2)
            list_model.append({
                "model":k,
                "score":score
            })
        return list_model

