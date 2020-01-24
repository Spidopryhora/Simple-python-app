import random as rnd
import string
import sys

def create_matrix(x_elements, y_elements):
    """ This function create matrix of random latin lowercase letters

    Parameters:
    x_elements (int): Number of rows

    y_elements (int): Number of columns
    
    Returns:
    matrix (list): matrix

    """

    matrix = []
    i = 0
    while i < x_elements:
        matrix.append([rnd.choice(string.ascii_lowercase) for j in range(y_elements)])
        i += 1
    
    for element in matrix:
        print (*element)

    return matrix

def find_the_words(dict_file, matrix):
    """ This function look for words from dictionary in file in the matrix of random 
    latin lowercase letters

    Parameters:
    dict_file (string): File name

    matrix (list): Two dimesion list of random latin lowercase letters
    
    Returns:
    final_word_list (list): List of words from dict_file that matched in matrix

    """
    try:
        f = open(dict_file, 'r')
    except IOError:
        print('Dictionary file does not exist')
    else:
        list_of_the_words = f.read().split()

    string_rows_list = []
    final_word_list = []

    for row in matrix:
        string_rows_list.append(''.join(row))
    
    
    for word in list_of_the_words:
        for row in string_rows_list:
            if not(row.find(word) == -1):
                final_word_list.append(word)                
                break

    return final_word_list
    

def main():
    if len(sys.argv) != 3:
        print('usage: python wordsearch.py rows columns')
        sys.exit(1)

    rows = sys.argv[1]
    columns = sys.argv[2]
    try:
        matrix = create_matrix(int(rows),int(columns))
    except ValueError:
        print('Please enter number of rows and columns using space as separator')
    else:
        print(find_the_words('words.txt', matrix))
    sys.exit(1)

if __name__ == '__main__':
    main()