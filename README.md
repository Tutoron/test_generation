# capstone
This version incorporated NLTK (http://www.nltk.org/), which is a sophisticated python NLP library. I use sent_tokenize() function, which uses a pre-trained English model to automatically extract sentences from a given text.

In order to use NLTK, you need to install NLTK at http://www.nltk.org/install.html.

After that, you need to download the Punkt model. In interactive Python console, type:

import nltk

nltk.download('punkt')

If you run into certificate verify failed issue, check this link: https://stackoverflow.com/questions/41348621/ssl-error-downloading-nltk-data
