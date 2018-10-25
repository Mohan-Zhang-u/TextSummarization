#!/usr/bin/env bash

# a basic interface:

echo "Welcome to the text Summarization Model!"
echo "Please make sure the file you want to summarize is located in my_news folder and the file name does not contains any special character"
echo "Warning: any previous summary and intermediate file will be cleaned up."
read -p "Press enter to continue:"

# trying to clean every remaining intermediate files
rm -rf To_Be_Clean

rm -rf summarizations

# set the path
export CLASSPATH=./stanford-corenlp-full-2018-10-05/stanford-corenlp-3.9.2.jar
export DATA=To_Be_Clean/finished_files

# put all the news you want to summarize in my_news, and the result will be in summarizations

# first, separate news sentences by dot, as did in the CNN dataset https://cs.nyu.edu/~kcho/DMQA/
python separate_sentences.py my_news To_Be_Clean/tokenized_my_news

# now, tokenize it and make jsons by: python make_datafiles.py <your_tokenized_news_dir>
python make_datafiles.py To_Be_Clean/tokenized_my_news

# now, unzip
tar -xvf To_Be_Clean/finished_files/test.tar -C To_Be_Clean/finished_files

# run the model (here model_dir can be either acl or new, as you may select
python decode_full_model.py --path=summarizations --model_dir=pretrained/acl --beam=5 --test

# now, the results should be generated in summarizations/output

# generate refs files to rename the summaries
python make_eval_references.py rename

# rename summaries
python rename_summaries.py --refs_path=To_Be_Clean/finished_files/refs --summarization_path=summarizations/output

#capitalize summaries
python capitalize.py --original_news_path=my_news --summarization_path=summarizations/output

echo "Summarization finished. All summaries are now in summarizations/output folder."