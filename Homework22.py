
class WordsFinder:
        def __init__(self, *list_file):

            self.list_file = list_file

        def get_all_words(self):

            all_words = {}

            file_names = list(self.list_file)

            for elem in file_names:

                names_ = elem

                with (open(names_, 'r') as file):

                    data_1 = file.read().lower()
                    data_2 = data_1.replace(',','').replace('.', '') \
                            .replace('=', '').replace("'", '').replace('!', '') \
                            .replace('?', '').replace(';', '').replace(':', '') \
                            .replace(' - ', '').split()


                    all_words[names_] = data_2

            return all_words


        def count(self, word_user):

            all_words = self.get_all_words()
            data_4 = []
            count_words = {}

            for names, words in all_words.items():
                data_3 = words
                for i in data_3:
                    if i == word_user:
                        data_4.append(i)
                        count_words[names] = len(data_4)
            return count_words

        def find(self, word_user):

            all_words = self.get_all_words()
            find_words = {}

            for names, words in all_words.items():
                data_6 = words
                if word_user in data_6:
                    data_7 = data_6.index(word_user) + 1
                    find_words[names] = data_7
            return find_words







finder2 = WordsFinder('test_file.txt', 'test_file_2.txt')
print(finder2.get_all_words())
print(finder2.find('text'))
print(finder2.count('task'))








