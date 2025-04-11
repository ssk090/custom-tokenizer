class Encoder:
    def __init__(self):
        # Define the vocabulary: English letters (both lowercase and uppercase) and Hindi characters.
        self.vocabulary = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") + \
                          list("अआइईउऊऋएऐओऔकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसह") + \
                          list("0123456789 ")

    def tokenize(self, input_string):
        """
        Converts the input string into a list of token indices based on the vocabulary.
        If a character is not found in the vocabulary, it returns -1 for that character.
        
        :param input_string: The string to be tokenized.
        :return: A list of token indices.
        """
        tokens = []
        for char in input_string:
            if char in self.vocabulary:
                tokens.append(self.vocabulary.index(char))
            else:
                tokens.append(-1)  # -1 represents an unknown character
        return tokens

    def detokenize(self, tokens):
        """
        Converts a list of token indices back into a string.
        If a token does not correspond to a valid character in the vocabulary, it replaces it with '?'.
        
        :param tokens: A list of token indices.
        :return: The detokenized string.
        """
        result = []
        for token in tokens:
            if 0 <= token < len(self.vocabulary):
                result.append(self.vocabulary[token])
            else:
                result.append('?')
        return ''.join(result)


# Example usage:
if __name__ == "__main__":
    encoder = Encoder()
    
    input_string = "Hello नमस्ते"
    tokens = encoder.tokenize(input_string)
    print("Tokens:", tokens)
    
    output_string = encoder.detokenize(tokens)
    print("Detokenized:", output_string)
