import fasttext

from .text_preprocessing import TextPreprocessor


class MessageCategorizer:
    def __init__(self, preprocessing_pipe=None):
        # load model (just 2mb)
        self.model = fasttext.load_model('project/ml/storage/message_categorizer/fasttext.ftz')

        # create text preprocessor with pipeline config
        self.preprocessor = TextPreprocessor(preprocessing_pipe)

    def predict_proba(self, x):
        print(1, x)
        x = self.preprocessor.preprocess(x)
        print(2, x)
        return list(self.model.predict(x, k=3)[1])
