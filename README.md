# redditclassifier
These scripts provide a straightforward method to create powerful models that perform binary classification on Reddit post

## Language:

These scripts are written in Python.

## Dependencies:
Dependencies can be found in the requirements.txt folder. Please install all dependencies before using these scriots
...

## How it works:
The model is trained off of the BERT Large Language Model. BERT is a deep learning model that has given state-of-the-art results on a wide variety of natural language processing tasks. It stands for Bidirectional Encoder Representations for Transformers. It has been pre-trained on Wikipedia and BooksCorpus and requires task-specific fine-tuning.

Here's a step-by-step instruction set for how to create your own model from scratch:

1. Collect data. find subreddits to scrape, along with specific keyworkds that are useful and my reveal posts in the target class
2. Run scraper.py. Plug in subreddits and maunally label each post, either 'target' or 'other'. Data will be appended to data/posts.csv
3. Run trainer.py. Once you have your data correctly labeled, you can run the trainer to create the model.

   And that's it! Once your model is trained you can use it by running classifier.py.

...
