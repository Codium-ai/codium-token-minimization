import argparse

import tiktoken

from src.code_minification import minify_code
from src.code_tabification import tabify_code

parser = argparse.ArgumentParser(description='Code token minimization')
parser.add_argument('--example_file_location', default='example_code/bank_mini_class.py', type=str)


def main():
    args = parser.parse_args()

    # calculate the code tokens. note that gpt-2 and gpt-3 use the same tokenizer
    encoder = tiktoken.get_encoding('gpt2')

    # base code
    code = open(args.example_file_location).read()
    num_tokens_base_code = len(encoder.encode(code))

    # tabified code
    options = {'tab_spaces': 4, 'remove_newlines': True, 'remove_trailing_spaces': True}
    code_tabified = tabify_code(code, **options)
    num_tokens_tabified_code = len(encoder.encode(code_tabified))

    # tabified and minimized code
    options = {'combine_imports': True, 'remove_annotations': True, 'remove_pass': True,
               'convert_posargs_to_args': False, 'rename_locals': False, 'rename_globals': False, 'hoist_literals': False}
    code_tabified_and_minimized = minify_code(code_tabified, **options)
    num_tokens_tabified_and_minimized_code = len(encoder.encode(code_tabified_and_minimized))

    # printing code
    print(f"####################")
    print(f"Base code:\n{code}")
    print(f"####################")
    print(f"Tabified code:\n{code_tabified}")
    print(f"####################")
    print(f"Tabified and minimized code:\n{code_tabified_and_minimized}")
    print(f"####################")

    # printing number of tokens
    print(f"\nNumber of tokens in base code: {num_tokens_base_code}")
    print(f"Number of tokens in tabified code: {num_tokens_tabified_code}")
    print(f"Number of tokens in tabified and minimized code: {num_tokens_tabified_and_minimized_code}")


if __name__ == '__main__':
    main()
