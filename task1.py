
import os
import sys
import string

READ_FILENAME = 'content.txt'
READ_MODE = 'r'


WRITE_FILENAME = 'summary_file.txt'
WRITE_MODE = 'w'

line_count = 0
word_count = 0
char_count = 0
sentence_count = 0


ly_ending_dict = {} 
long_word_dict = {} 
ten_long_word_dict = {} 

try:
    article_file = open(READ_FILENAME, READ_MODE) 
    summary_file = open(WRITE_FILENAME, WRITE_MODE) 

    with article_file,summary_file: 
        for line in article_file:
            
            if len(line.split()) == 0:
                continue

            
            sentence = line.split('.\n:')
            sentence_count += len(sentence)

          
            line = line.lower() 
            line = line.translate(line.maketrans("", "", string.punctuation)) 
            line = line.replace("—",'') 

            
            line_count += 1

            
            words = line.split()
            word_count += len(words)

            char_count += sum(len(char) for char in words)

           
            max_len = len(max(words, key=len))

        
            for ly_word in line.split():
                if len(ly_word) == max_len:
                    if ly_word not in long_word_dict:
                        long_word_dict[ly_word] = len(ly_word)
                if ly_word.endswith('ly'):
                    if ly_word in ly_ending_dict:
                        ly_ending_dict[ly_word] += 1
                    else:
                        ly_ending_dict[ly_word] = 1

        summary_file.write(f'Total word count: {word_count}\n')
        summary_file.write(f'Total character count: {char_count}\n')
        summary_file.write(f'The average word length: {(char_count/word_count):.2f}\n')
        summary_file.write(f'The average sentence length: {(word_count/sentence_count):.2f}\n')
        summary_file.write('\n')

        
        summary_file.write('A word distribution of all words ending in “ly”\n')
        for ly_e_word,count in sorted(ly_ending_dict.items()):   
            summary_file.write(f'{ly_e_word}: {count}\n')
        summary_file.write('\n')
        
       
        summary_file.write('A list of top 10 longest words in descending order:\n') 
        ten_long_word_dict = {long_word: count for long_word,count in sorted(long_word_dict.items(),key = lambda x: x[1],reverse = True)}
        for longest_words in sorted(list(ten_long_word_dict)[0:10],reverse = True): 
            summary_file.write(f'{longest_words}, ')


except OSError as error:
    print(f'Unable to open file {READ_FILENAME}. Error message: {error}')
except:
    error = sys.exc_info()[0]
    print(f'Unexpected error: {error}')
finally:
    print('Finally code block executed.')