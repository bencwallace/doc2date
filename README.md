# doc2date: A Study in Document Regression

[Document classification](https://en.wikipedia.org/wiki/Document_classification) is a common application of machine learning techniques. Examples include [sentiment analysis](https://en.wikipedia.org/wiki/Sentiment_analysis), the classification of texts into a (typically small) number of moods (such as *positive* and *negative*); as well as authorship attribution in [stylometry](https://en.wikipedia.org/wiki/Stylometry), in which texts are grouped according to their original author,

Unsupersived learning methods have also been applied to the analysis of documents. For instance, [doc2vec](https://arxiv.org/pdf/1405.4053v2.pdf) is a dimensionality reduction technique that extends [word embeddings] to documents.

But what about document *regression*? In this notebook, we investigate the problem of learning the date of a publication from the text contained therein. Since the target space, a range of years, can be viewed as a continuum, this problem presents a natural test case for applying regression techniques to document analysis.

[Read more about it](notebooks/doc2date-00.ipynb)

[Try it out](https://bcwallace.com/doc2date)
