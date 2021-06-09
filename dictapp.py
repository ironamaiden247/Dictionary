import json
import enchant
import difflib


with open('data.json') as json_dict_file:
    data = json.load(json_dict_file)

# print(type(data))

# Define the function that returns the relevant answers
def return_dict_answer(word):
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data: #in case user enters words like USA or NATO
        return data[word.upper()]
    else:
        # nearest word found and not word found logic
        # nearest word logic
        b = enchant.Broker()
        d = b.request_dict("en_US")
        best_words = []
        best_ratio = 0
        a = set(d.suggest(word))
        for b in a:
            tmp = difflib.SequenceMatcher(None, word, b).ratio()
            if tmp > best_ratio:
                best_words = [b]
                best_ratio = tmp
            elif tmp == best_ratio:
                best_words.append(b)
        print('Did you mean any one of {}?'.format(best_words))
        user_decision = input("Press 'y' for Yes or 'n' for No: ")
        if user_decision == 'y':
            if len(best_words) == 1:
                if word in data:
                    return data[word]
                else:
                    return 'The meaning of the word does not exist in the Thesaurus'
            if len(best_words) > 1:
                a = len(best_words)
                for i in range(1, a+1):
                    print('Press {} for {}'.format(i, best_words[i-1]))
                user_choice = int(input('Your choice: '))
                selected_word = best_words[user_choice - 1]
                if selected_word in data:
                    return data[word]
                else:
                    return 'The word does not exist in the Thesaurus'
        if user_decision == 'n':
            return "We cannot find the mentioned word's meaning. Thank you for using our Thesaurus service"

flag = True

while flag:
    user_input = input('Enter the word: ')
    user_input = user_input.lower()
    output = return_dict_answer(user_input)
    if type(output) == list:
        print('The meaning(s) of the word is: ')
        for meaning in output:
            print('{}'.format(meaning))
    else:
        print('{}'.format(output))
    user_continue = input("Do you wish to continue? 'y' for Yes and 'n' for No: ")
    if user_continue == 'y':
        flag = True
    if user_continue == 'n':
        flag = False



# # Previous code
# user_word = input('Enter the word: ')
#
# for entries in data.items():
#     if entries[0] == user_word:
#         input_word, answers = entries
#         print("The meaning(s) of the entered word '{}' :".format(input_word))
#         for answer in answers:
#             print("{}".format(answer))
#     else:
#     # nearest word logic
#         b = enchant.Broker()
#         d = b.request_dict("en_US")
#         best_words = []
#         best_ratio = 0
#         a = set(d.suggest(user_word))
#         for b in a:
#             tmp = difflib.SequenceMatcher(None, user_word, b).ratio()
#             if tmp > best_ratio:
#                 best_words = [b]
#                 best_ratio = tmp
#             elif tmp == best_ratio:
#                 best_words.append(b)
#         print('Did you mean {}?'.format(best_words[0]))
#         user_decision = input("Press 'y' for Yes or 'n' for No: ")
#         if user_decision == 'y':
#             for entries in data.items():
#                 if entries[0] == best_words[0]:
#                     input_word, answers = entries
#                     print("The meaning(s) of the entered word '{}' :".format(input_word))
#                     for answer in answers:
#                         print("{}".format(answer))
#                 else:
#                     print('Word not present in the Theasaurus!')
#
#         if user_decision == 'n':
#             print('We could not find the suggested word.')
#             print('Thank you for using this Theasaurus')
#             break
#
#
#
#
#
#
