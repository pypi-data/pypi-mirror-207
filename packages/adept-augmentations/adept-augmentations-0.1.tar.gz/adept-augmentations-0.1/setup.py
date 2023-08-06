# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['adept_augmentations',
 'adept_augmentations.analyzers',
 'adept_augmentations.augmenters',
 'adept_augmentations.profilers']

package_data = \
{'': ['*']}

install_requires = \
['datasets>=2.5,<3.0', 'pydantic>=1.8,<2.0', 'spacy>=3,<4']

setup_kwargs = {
    'name': 'adept-augmentations',
    'version': '0.1',
    'description': 'A Python library aimed at adeptly, augmenting NLP training data.',
    'long_description': '# Adept Augmentations\n\nWelcome to Adept Augmentations, can be used for creating additional data in Few Shot Named Entity Recognition (NER) setting!\n\nAdept Augmentation is a Python package that provides data augmentation functionalities for NER training data using the `spacy` and `datasets` packages. Currently, we support one augmentor `EntitySwapAugmenter`, however, we plan on [adding some more](#implemented-augmenters).\n\n`EntitySwapAugmenter` takes either a `datasets.Dataset` or a `spacy.tokens.DocBin`. Additionally, it is optional to provide a set of `labels` to be included in the augmentations. It initially created a knowledge base of entities belonging to a certain label. When running `augmenter.augment()` for `N` runs, it then creates `N` new sentences with random swaps of the original entities with an entity of the same corresponding label from the knowledge base.\n\nFor example, assuming that we have knowledge base for PERSONS and LOCATIONS and PRODUCTS. We can then create additional data for the sentence "Momofuko Ando created instant noodles in Osaka." using `augmenter.augment(N=2)`, resulting in "David created instant noodles in Madrid." or "Tom created Adept Augmentations in the Netherlands".\n\nAdept Augmentation works for NER labels using the IOB, IOB2, BIOES and BILUO tagging schemes, as well as labels not following any tagging scheme.\n\n## Usage\n\n### Datasets\n\n```python\nfrom datasets import load_dataset\n\nfrom adept_augmentations import EntitySwapAugmenter\n\ndataset = load_dataset("conll2003", split="train[:3]")\naugmenter = EntitySwapAugmenter(dataset)\naug_dataset = augmenter.augment(N=4)\n\nfor entry in aug_dataset["tokens"]:\n    print(entry)\n\n# [\'EU\', \'rejects\', \'British\', \'call\', \'to\', \'boycott\', \'British\', \'lamb\', \'.\']\n# [\'EU\', \'rejects\', \'German\', \'call\', \'to\', \'boycott\', \'German\', \'lamb\', \'.\']\n# [\'EU\', \'rejects\', \'German\', \'call\', \'to\', \'boycott\', \'British\', \'lamb\', \'.\']\n# [\'Peter\', \'Blackburn\']\n# [\'BRUSSELS\', \'1996-08-22\']\n```\n\n### spaCy\n\n```python\nimport spacy\nfrom spacy.tokens import DocBin\n\nfrom adept_augmentations import EntitySwapAugmenter\n\nnlp = spacy.load("en_core_web_sm")\n\n# Create some example training data\nTRAIN_DATA = [\n    "Apple is looking at buying U.K. startup for $1 billion",\n    "Microsoft acquires GitHub for $7.5 billion",\n]\ndocs = nlp.pipe(TRAIN_DATA)\n\n# Create a new DocBin\ndoc_bin = DocBin(docs=docs)\n\ndoc_bin = EntitySwapAugmenter(doc_bin).augment(4)\nfor doc in doc_bin.get_docs(nlp.vocab):\n    print(doc.text)\n\n# GitHub is looking at buying U.K. startup for $ 7.5 billion\n# Microsoft is looking at buying U.K. startup for $ 1 billion\n# Microsoft is looking at buying U.K. startup for $ 7.5 billion\n# GitHub is looking at buying U.K. startup for $ 1 billion\n# Microsoft acquires Apple for $ 7.5 billion\n# Apple acquires Microsoft for $ 1 billion\n# Microsoft acquires Microsoft for $ 7.5 billion\n# GitHub acquires GitHub for $ 1 billion\n```\n\n## Potential performance gains\nData augmentation can significantly improve model performance in low-data scenarios.\nTo showcase this, we trained a [SpanMarker](https://github.com/tomaarsen/SpanMarkerNER) NER model on\nthe 50, 100, 200, 400 and 800 first [CoNLL03](https://huggingface.co/datasets/conll2003) training samples.\n\nThe augmented dataset is generated like so:\n```python\n# Select N (50, 100, 200, 400 or 800) samples from the gold training dataset\ntrain_dataset = dataset["train"].select(range(N))\n\n# Generate augmented dataset, with 4 * N samples\naugmented_dataset = Augmenter(train_dataset).augment(N=4)\n\n# Combine the original with the augmented to produce the full dataset\n# to produce a dataset 5 times as big as the original\ntrain_dataset = concatenate_datasets([augmented_dataset, train_dataset])\n```\n\nNote that the baseline uses 5 epochs. This way, the training time and steps are identical between the two experiments. All scenarios are executed 5 times,\nand we report means and standard errors.\n\n|       | Original - 5 Epochs | Augmented - 1 Epoch |\n|-------|--|--|\n| N=50  | 0.387 ± 0.042 F1 | **0.484 ± 0.054 F1** |\n| N=100 | 0.585 ± 0.070 F1 | **0.663 ± 0.038 F1** |\n| N=200 | 0.717 ± 0.053 F1 | **0.757 ± 0.025 F1** |\n| N=400 | 0.816 ± 0.017 F1 | **0.826 ± 0.011 F1** |\n| N=800 | 0.859 ± 0.004 F1 | **0.862 ± 0.002 F1** |\n\n(Note: These results are not optimized and do not indicate maximum performances with SpanMarker.)\n\nFrom these results, it is clear that performing data augmentation using `adept_augmentations` can heavily improve performance in low-data settings.\n\n## Implemented Augmenters\n\n- [X] `EntitySwapAugmenter`\n- [ ] `KnowledgeBaseSwapAugmenter`\n- [ ] `CoreferenceSwapAugmenter`\n- [ ] `SyntaticTreeSwapAugmenter`\n\n## Potential integrations\n\nPotentially, we can look into integrations of other augmentations packages that do not preserve gold standard knowledge. Good sources for inspiration are:\n\n- <https://github.com/KennethEnevoldsen/augmenty>\n  - <https://kennethenevoldsen.github.io/augmenty/tutorials/introduction.html>\n- <https://github.com/QData/TextAttack>\n- <https://github.com/infinitylogesh/mutate>\n',
    'author': 'david',
    'author_email': 'david.m.berenstein@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/davidberenstein1957/adept-augmentations',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.12',
}


setup(**setup_kwargs)
