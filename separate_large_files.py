import os
import sys
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='separate large articles into several smaller articles that contains several paragraphs of it so that the summarization has a better performance. ')
    parser.add_argument('--target_file', required=True, help='path to target file that to be separated')
    parser.add_argument('--storage_location', required=True, help='path to store the separated files')
    parser.add_argument('--num_of_sent', required=True, help='number of paragraphs per article')