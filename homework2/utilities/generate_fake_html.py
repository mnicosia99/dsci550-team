import os
import json
import requests
import tensorflow as tf
import numpy as np
import sys
import feedparser
import time
from datetime import datetime, timedelta
import requests
import base64
from working.fakedata import create_authors, get_random_school, get_random_department, get_date
from ttp import ttp

sys.path.append('../')
from lm.modeling import GroverConfig, sample
from sample.encoder import get_encoder, _tokenize_article_pieces, extract_generated_target
import random

def generate_html_from_article_text(article_title, article_text, author_list, publish_date, university, department, image_url=None, caption = ""):    
    # parse the article text
    p = ttp.Parser()
    result = p.parse(article_text)
    article_text = result.html
    image = None
    
    #  split article on newlines
    lines = article_text.split("\n")
   
    new_lines = []
    for line in lines:
        new_lines.append(line)
    
    #  add paragraph between each new line
    article_text = "<p>".join(new_lines)
    
    print(article_text)
    
    # if an image url exists, add it to the returned html
    # <figure>
    #    <img src="http://mnicosia.tech/images/samples_5_100.png"/>
    #    <figcaption>Fig.1 - Trulli, Puglia, Italy.</figcaption>
    # </figure>
    if image_url is not None:
        image = "<figure><img src=\"" + image_url + "\"/><figcaption>" + caption + "</figcaption></figure>"
    
    #  create html from article text

    # body { margin: 20px; text-align: center; } h1 {color: green; } img { float: left; margin: 5px; } p { text-align: justify; font-size: 25px; }
    # <div class="square"><div> <img src="https://media.geeksforgeeks.org/wp-content/uploads/20190808143838/logsm.png" alt="Longtail boat in Thailand"></div><p></p></div>
    
    style = " hr.solid { border-top: 3px solid #bbb;} figure { display: inline-block; border: 0px dotted gray; margin: 20px;text-align: center; } figure img { vertical-align: top; }"
    article_title = "<h1>" + article_title + "</h1>\n"
    authors = "<p>Authors: "
    for author in author_list:
        authors += author + " "
    authors += "</p>\n"
    publish_date = "Published Date: " + publish_date + "<br/>\n"
    university = "<p>" + university + "</p>\n"
    department = department + "<br/>\n"
    abstract = ""
    # abstract = "<h3>Abstract</h3>\n<p>" + article_summary + "</p>\n"
    sep = "<hr class=\"solid\">\n"
    body = article_title + authors + publish_date + sep + university + department + sep + abstract + "<br/><br/>" + article_text
    article_html = "<html><head><style>" + style + "</style></head><body>" + body + image + "</body></html>"
 
    # return the article as html
    return article_html

def generate_article_attribute(sess, encoder, tokens, probs, article, target='article'):

    # Tokenize the raw article text from sample grover encoder
    article_pieces = _tokenize_article_pieces(encoder, article)

    # Grab the article elements the model careas about - domain, date, title, etc.
    context_formatted = []
    for key in ['domain', 'date', 'authors', 'title', 'article']:
        if key != target:
            context_formatted.extend(article_pieces.pop(key, []))

    # Start formatting the tokens in the way the model expects them, starting with
    # which article attribute we want to generate.
    context_formatted.append(encoder.__dict__['begin_{}'.format(target)])
    # Tell the model which special tokens (such as the end token) aren't part of the text
    ignore_ids_np = np.array(encoder.special_tokens_onehot)
    ignore_ids_np[encoder.__dict__['end_{}'.format(target)]] = 0

    # We are only going to generate one article attribute with a fixed
    # top_ps cut-off of 95%. This simple example isn't processing in batches.
    gens = []
    article['top_ps'] = [0.95]

    # Run the input through the TensorFlow model and grab the generated output
    tokens_out, probs_out = sess.run(
        [tokens, probs],
        feed_dict={
            # Pass real values for the inputs that the
            # model needs to be able to run.
            initial_context: [context_formatted],
            eos_token: encoder.__dict__['end_{}'.format(target)],
            ignore_ids: ignore_ids_np,
            p_for_topp: np.array([0.95]),
        }
    )

    # The model is done! Grab the results it generated and format the results into normal text.
    for t_i, p_i in zip(tokens_out, probs_out):
        extraction = extract_generated_target(output_tokens=t_i, encoder=encoder, target=target)
        gens.append(extraction['extraction'])

    # Return the generated text.
    return gens[-1]

def create_fake(article, sess, encoder, tokens, probs, count):
    print(f"Building article from headline '{article['title']}'")
    # generate fake text based on the original paper
    article['text'] = generate_article_attribute(sess, encoder, tokens, probs, article, target="article")
    # Generate a fake title that fits the generated paper text
    article['title'] = generate_article_attribute(sess, encoder, tokens, probs, article, target="title")
    # Generate a fake abstract that fits the generated paper text
    # article['summary'] = generate_article_attribute(sess, encoder, tokens, probs, article, target="title")

    article_title = article['title']
    article_text = article['text']
    
    # <img src="http://mnicosia.tech/images/samples_5_100.png"/>
    article_image_url = "http://mnicosia.tech/images/samples_5_" + str(count) + ".png"
    # article_summary = article['summary']

    authors = create_authors()
    university = get_random_school()
    department = get_random_department()
    publish_date = get_date(365 * 2, 365 * 8)
    # caption = TODO
    caption = "Test Caption"
    article_text = generate_html_from_article_text(
        article_title, article_text, authors, publish_date, university, department, article_image_url, caption)

    print(f" - Generated fake article titled '{article_title}'")
    article_title = article_title.replace(" ", "-")
    filename = "/content/gdrive/My Drive/Articles/generated_fake-" + str(count) + ".html"
    with open(filename, 'w' ) as f:
        f.write(article_text)
    count += 1
    
model_type = "mega"

model_dir = os.path.join('/content/gdrive/MyDrive/grover-fork2/grover/models', model_type)
if not os.path.exists(model_dir):
    os.makedirs(model_dir)

for ext in ['data-00000-of-00001', 'index', 'meta']:
    r = requests.get(f'https://storage.googleapis.com/grover-models/{model_type}/model.ckpt.{ext}', stream=True)
    with open(os.path.join(model_dir, f'model.ckpt.{ext}'), 'wb') as f:
        file_size = int(r.headers["content-length"])
        if file_size < 1000:
            raise ValueError("File doesn't exist? idk")
        chunk_size = 1000
        for chunk in r.iter_content(chunk_size=chunk_size):
            f.write(chunk)
    print(f"Just downloaded {model_type}/model.ckpt.{ext}!", flush=True)
    
articles = list()

for filename in os.listdir("/content/gdrive/MyDrive/grover-fork2/grover/working/inputs/json"):
    fn = os.path.join("/content/gdrive/MyDrive/grover-fork2/grover/working/inputs/json/", filename)
    # checking if it is a file
    if os.path.isfile(fn) and ".jsonl" not in fn:
        try:
            f = open(fn)
            article = json.load(f)
            articles.append(article)
        except:
            print("unable to parse json file " + fn)    
        finally:
            f.close()

# Load the pre-trained "huge" Grover model with 1.5 billion params
model_config_fn = '/content/gdrive/MyDrive/grover-fork2/grover/lm/configs/mega.json'
model_ckpt = '/content/gdrive/MyDrive/grover-fork2/grover/models/mega/model.ckpt'
encoder = get_encoder()
news_config = GroverConfig.from_json_file(model_config_fn)

# Set up TensorFlow session to make predictions
tf_config = tf.ConfigProto(allow_soft_placement=True)

with tf.Session(config=tf_config, graph=tf.Graph()) as sess:
    # Create the placehodler TensorFlow input variables needed to feed data to Grover model
    # to make new predictions.
    initial_context = tf.placeholder(tf.int32, [1, None])
    p_for_topp = tf.placeholder(tf.float32, [1])
    eos_token = tf.placeholder(tf.int32, [])
    ignore_ids = tf.placeholder(tf.bool, [news_config.vocab_size])

    # Load the model config to get it set up to match the pre-trained model weights
    tokens, probs = sample(
        news_config=news_config,
        initial_context=initial_context,
        eos_token=eos_token,
        ignore_ids=ignore_ids,
        p_for_topp=p_for_topp,
        do_topk=False
    )

    # Restore the pre-trained Grover 'huge' model weights
    saver = tf.train.Saver()
    saver.restore(sess, model_ckpt)

    fakes_made = 0
    paper_index = 0
    # process each research paper to make fake papers
    for article in articles:
        paper_index += 1
        #  create first
        create_fake(article, sess, encoder, tokens, probs, fakes_made)
        fakes_made += 1
        #  create second
        create_fake(article, sess, encoder, tokens, probs, fakes_made)
        fakes_made += 1
        if paper_index < 104:
            #  for first 104 articles create third
            continue
        # create third
        create_fake(article, sess, encoder, tokens, probs, fakes_made)
        fakes_made += 1
        