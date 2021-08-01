# A Search Engine for StackOverflow

To run this project you need to have Docker installed.

This project goal is to evaluate different ways of performing searches on the StackOverflow database. [View the dataset here](https://www.kaggle.com/stackoverflow/stackoverflow)

We evaluate the performance of our search by searching questions that were marked as duplicated and then verifying if by using the question title we were able to find the duplicate and, if found, which position it was found.

This project has a PDF attached with a full report of the results alongside all the information you need to have to understand how to replicate the findings.

Feel free to extend this repository and use for any purpose. Have fun!

## Running this project locally

The process of running this project consists on a few steps:

1. Downloading the dataset (if you prefer, you can run a smaller dataset like AskUbuntu, for example)
2. Uploading the dataset contents to a MySQL instance (scripts/setup.sh)
3. Migrating the data from MySQL to a searchable format in Elasticsearch (scripts/migrate.sh)
4. Running the embedded python web server (scripts/run.sh)

Keep in mind that in a regular machine this process take hours to index all the results.

## Results

These are the results I found. We evaluated Precision, Recall and F-Measure of each one of the aproaches and how our pre-processing and score calculator approaches influenced the results.

![](comparisons.jpeg?raw=true)