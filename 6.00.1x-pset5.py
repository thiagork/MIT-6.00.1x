# MIT 6.00.1x
# Problem Set 5
# Caesar Cipher Program

import string


def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load.

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list


def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'


class Message(object):

    def __init__(self, text):
        '''
        Initializes a Message object

        text (string): the message's text
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class

        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class

        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        has 52 keys of all the uppercase letters and all the lowercase
        letters.

        shift (integer): the amount by which to shift every letter of the
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to
                 another letter (string).
        '''
        # Line bellow broken to comply with pep8
        shiftedLowercase = list(string.ascii_lowercase[shift:] +
                                string.ascii_lowercase[:shift])
        # Line bellow broken to comply with pep8
        shiftedUppercase = list(string.ascii_uppercase[shift:] +
                                string.ascii_uppercase[:shift])
        # Line bellow broken to comply with pep8
        shiftedAlphabet = shiftedLowercase + shiftedUppercase
        return dict(zip(string.ascii_letters, shiftedAlphabet))

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift.

        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        # Line bellow broken to comply with pep8
        return ''.join([self.build_shift_dict(shift)[x] if x in
                        string.ascii_letters else x for x in self.message_text
                        ])


class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object.

        text (string): the message's text
        shift (integer): the shift associated with this message
        '''
        Message.__init__(self, text)
        self.shift = shift
        self.encrypting_dict = Message.build_shift_dict(self, shift)
        self.message_text_encrypted = Message.apply_shift(self, shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class

        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class

        Returns: a COPY of self.encrypting_dict
        '''
        return dict(self.encrypting_dict)

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class

        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other
        attributes determined by shift (ie. self.encrypting_dict and
        message_text_encrypted).

        shift (integer): the new shift that should be associated with
        this message. 0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object

        text (string): the message's text
        '''
        Message.__init__(self, text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. The "best" one is defined as the shift that
        creates the maximum number of real words when apply_shift(shift) is
        used on the message text.

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        countValidWords = 0
        bestShiftValue = 0
        for i in range(27):
            decryptWordsList = self.apply_shift(i).split()
            # Line bellow broken to comply with pep8
            countValidWords = ([1 for x in decryptWordsList if
                                is_word(self.valid_words, x)]).count(1)
            if countValidWords > bestShiftValue:
                bestShiftValue = i
        return (bestShiftValue, self.apply_shift(bestShiftValue))


def decrypt_story():
    '''
    This function simply decrypts the previously encrypted story
    inside story.txt
    '''
    story = get_story_string()
    encryptedStory = CiphertextMessage(story)
    decryptedStory = encryptedStory.decrypt_message()
    return decryptedStory

print(decrypt_story())
