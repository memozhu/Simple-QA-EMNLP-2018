from lib.text_encoders.static_tokenizer_encoder import StaticTokenizerEncoder


class CharacterEncoder(StaticTokenizerEncoder):

    def __init__(self, *args, **kwargs):
        if 'tokenize' in kwargs:
            raise TypeError('CharacterEncoder defines a tokenize callable per character')
        super().__init__(*args, **kwargs, tokenize=(lambda s: s.split('')))

    def decode(self, tensor):
        tokens = [self.itos[index] for index in tensor]
        return ''.join(tokens)
