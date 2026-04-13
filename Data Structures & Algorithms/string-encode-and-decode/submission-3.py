class Solution:

    def encode(self, strs: List[str]) -> str:
        # We need to transform the list into a single string that 
        # could be transformed back into the list
        
        # A naive approach is to transform each char into his
        # numeric representation, delimit each numeric rep with ','
        # and each single string with a arbitrary representation such as ';'
    
        encoded = ''

        if not strs:
            return encoded

        for s in strs:
            for c in s:
                encoded = encoded + str(ord(c))
                encoded = encoded + ','
            encoded = encoded + ';'
                
        return encoded


    def decode(self, s: str) -> List[str]:
        # To decode the naive encoding we can split() method
        if not s:
            return []

        encoded_strs = s.split(';')

        decoded_strs = []

        if len(encoded_strs) == 0:
            return []

        for encoded in encoded_strs[:-1]:
            decode = ""
            encoded_chars = encoded.split(',')

            for c in encoded_chars:
                if c.isnumeric():
                    decode = decode + chr(int(c))
            
            decoded_strs.append(decode)

        return decoded_strs