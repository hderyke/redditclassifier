# redditclassifier
These scripts provide a straightforward method to create powerful models that perform binary classification on Reddit posts.

## Language
These scripts are written in Python.

## Dependencies
Dependencies can be found in the requirements.txt folder. Please install all dependencies before using these scripts.


## How it works
The model is trained off of the BERT Large Language Model. BERT is a deep learning model that has given state-of-the-art results on a wide variety of natural language processing tasks. It stands for Bidirectional Encoder Representations for Transformers. It has been pre-trained on Wikipedia and BooksCorpus and requires task-specific fine-tuning.

Here's a step-by-step instruction set for how to create your own model from scratch:

1. Collect data. find subreddits to scrape, along with specific keyworkds that are useful and my reveal posts in the target class
2. Run scraper.py. Plug in subreddits and maunally label each post, either 'target' or 'other'. Data will be appended to data/posts.csv
3. Run trainer.py. Once you have your data correctly labeled, you can run the trainer to create the model.

   And that's it! Once your model is trained you can use it by running classifier.py.

## Getting Started

### Opening project
Start by cloning this repository and moving to the src directory with our scripts:

``` git clone https://github.com/hderyke/redditclassifier.git ```


### Installing dependencies
Ensure you have all the dependendcies needed to run these scripts. Use the  ``` pip ``` command to help.

``` pip install -r requirements.txt ```

Once you have installed the dependencies, you're ready to run the scripts in the ``` src ``` directory.

```cd src```


## Functions

### scraper.py
Collect posts from specified Reddit page and has the user maunally them. Labeled data is appended to the ```data/posts.csv``` file. Uses the Reddit API to get posts- requires the user have their own Reddit API key. Simply run ```python scraper.py```.

### trainer.py
Trains a default BERT classification model on the data in posts.csv. Outputs a working model as well as logs. Simply run ```python trainer.py```.

### classifier.py
Classifier that uses the trained model created by ```trainer.py```. Run the command; ```python classifier.py {subbreddit_name}, {n/o days}``` to get targeted posts from the subbreddit defined in the first argument and the number of days back defined by the second argument.








