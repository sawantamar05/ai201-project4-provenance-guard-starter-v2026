# Criteria run — after

- Produced by `run_eval.py::main` and `run_eval.py::trial_result`.
- Five original criteria; three real HTTP trials each. Full capture: part2_eval_after.json.
- No request is silently retried. A 429 differs from a required 400/413/415.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Limit false accusations | At most 1/10 sourced human passages labeled AI in every trial | 0/10 AI flags; 10/10 valid | 0/10 AI flags; 10/10 valid | 0/10 AI flags; 10/10 valid | MET |
| 2. Separate contrasting inputs | Four-AI median minus first-four-human median >= 0.20 in every trial | median gap 0.247 | median gap 0.247 | median gap 0.247 | MET |
| 3. Cover all labels and scores | Actual human/unsure/ai labels and all 10,001 scores mapped; 0.51 differs from 0.95 | 3/3 labels; 10001 scores | 3/3 labels; 10001 scores | 3/3 labels; 10001 scores | MET |
| 4. Preserve usable appeals | 10/10 exact appeals, immutable decisions, fresh-process status, no rescoring; unknown ID404 | 10/10 appeals; persistence True | 10/10 appeals; persistence True | 10/10 appeals; persistence True | MET |
| 5. Reject bad input before scoring | All 18 validation groups return specified JSON400/404/413/415; no success events | 36/37 exact responses; 18/18 groups | 26/37 exact responses; 18/18 groups | 26/37 exact responses; 18/18 groups | MISSED |

## Actual output, trial 1

### Criterion 1

Produced by `run_eval.py::trial_result` (false_positives).

```json
{
  "trial": 1,
  "criterion": 1,
  "kind": "false_positives",
  "cases": [
    {
      "method": "POST",
      "url": "http://127.0.0.1:5054/submit",
      "request_json": {
        "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
        "creator_id": "eval-after-c1-t1-human-01"
      },
      "status_code": 200,
      "content_type": "application/json",
      "response_json": {
        "combined_score": 0.6593,
        "confidence": 0.6593,
        "content_id": "51450dcb-09a1-43ce-84ce-0419f521b5a8",
        "creator_id": "eval-after-c1-t1-human-01",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.6922,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.5,
          "punctuation_density": 0.016286644951140065,
          "punctuation_simplicity": 0.8642779587404994,
          "repetition": 0.34976525821596255,
          "sentence_count": 2,
          "sentence_length_spread": 0.352112676056338,
          "style_score": 0.5278,
          "type_token_ratio": 0.6901408450704225,
          "word_count": 71
        },
        "style_score": 0.5278,
        "text_length": 377,
        "timestamp": "2026-11-08T21:53:15+00:00"
      },
      "elapsed_ms": 69.86,
      "input_id": "human-01",
      "input_provenance": {
        "id": "human-01",
        "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
        "source_url": "https://www.gutenberg.org/cache/epub/1342/pg1342.txt",
        "author": "Jane Austen",
        "title": "Pride and Prejudice",
        "publication_year": 1813,
        "location": "Chapter I, first two paragraphs",
        "genre": "literary fiction",
        "provenance": "Exact public-domain excerpt from the Project Gutenberg edition of Austen's published novel, verified against the linked primary text on 2026-10-30. Whitespace normalized."
      }
    },
    {
      "method": "POST",
      "url": "http://127.0.0.1:5054/submit",
      "request_json": {
        "text": "There was no possibility of taking a walk that day. We had been wandering, indeed, in the leafless shrubbery an hour in the morning; but since dinner (Mrs. Reed, when there was no company, dined early) the cold winter wind had brought with it clouds so sombre, and a rain so penetrating, that further outdoor exercise was now out of the question. I was glad of it: I never liked long walks, especially on chilly afternoons: dreadful to me was the coming home in the raw twilight, with nipped fingers and toes, and a heart saddened by the chidings of Bessie, the nurse, and humbled by the consciousness of my physical inferiority to Eliza, John, and Georgiana Reed.",
        "creator_id": "eval-after-c1-t1-human-02"
      },
      "status_code": 200,
      "content_type": "application/json",
      "response_json": {
        "combined_score": 0.4608,
        "confidence": 0.4608,
        "content_id": "331adb6d-9ae9-4c14-9bf9-2b723b112e22",
        "creator_id": "eval-after-c1-t1-human-02",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.4863,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.2554540936099331,
          "punctuation_density": 0.04021937842778794,
          "punctuation_simplicity": 0.6648385131017671,
          "repetition": 0.3276836158192091,
          "sentence_count": 4,
          "sentence_length_spread": 0.5956367251120536,
          "style_score": 0.359,
          "type_token_ratio": 0.7033898305084746,
          "word_count": 118
        },
        "style_score": 0.359,
        "text_length": 664,
        "timestamp": "2026-11-08T21:53:15+00:00"
      },
      "elapsed_ms": 72.1,
      "input_id": "human-02",
      "input_provenance": {
        "id": "human-02",
        "text": "There was no possibility of taking a walk that day. We had been wandering, indeed, in the leafless shrubbery an hour in the morning; but since dinner (Mrs. Reed, when there was no company, dined early) the cold winter wind had brought with it clouds so sombre, and a rain so penetrating, that further outdoor exercise was now out of the question. I was glad of it: I never liked long walks, especially on chilly afternoons: dreadful to me was the coming home in the raw twilight, with nipped fingers and toes, and a heart saddened by the chidings of Bessie, the nurse, and humbled by the consciousness of my physical inferiority to Eliza, John, and Georgiana Reed.",
        "source_url": "https://www.gutenberg.org/cache/epub/1260/pg1260.txt",
        "author": "Charlotte Bront\u00eb",
        "title": "Jane Eyre: An Autobiography",
        "publication_year": 1847,
        "location": "Chapter I, first two paragraphs",
        "genre": "first-person literary fiction",
        "provenance": "Exact public-domain excerpt from the Project Gutenberg edition of Bront\u00eb's published novel, verified against the linked primary text on 2026-10-30. Whitespace normalized."
      }
    },
    {
      "method": "POST",
      "url": "http://127.0.0.1:5054/submit",
      "request_json": {
        "text": "Call me Ishmael. Some years ago\u2014never mind how long precisely\u2014having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world. It is a way I have of driving off the spleen and regulating the circulation. Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral I meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people\u2019s hats off\u2014then, I account it high time to get to sea as soon as I can.",
        "creator_id": "eval-after-c1-t1-human-03"
      },
      "status_code": 200,
      "content_type": "application/json",
      "response_json": {
        "combined_score": 0.3358,
        "confidence": 0.3358,
        "content_id": "843427f4-2332-40c9-979b-5b15906cca41",
        "creator_id": "eval-after-c1-t1-human-03",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.3532,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.0,
          "punctuation_density": 0.027522935779816515,
          "punctuation_simplicity": 0.7706422018348624,
          "repetition": 0.37356321839080464,
          "sentence_count": 4,
          "sentence_length_spread": 0.8882105351861661,
          "style_score": 0.2662,
          "type_token_ratio": 0.6758620689655173,
          "word_count": 145
        },
        "style_score": 0.2662,
        "text_length": 795,
        "timestamp": "2026-11-08T21:53:15+00:00"
      },
      "elapsed_ms": 78.36,
      "input_id": "human-03",
      "input_provenance": {
        "id": "human-03",
        "text": "Call me Ishmael. Some years ago\u2014never mind how long precisely\u2014having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world. It is a way I have of driving off the spleen and regulating the circulation. Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral I meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people\u2019s hats off\u2014then, I account it high time to get to sea as soon as I can.",
        "source_url": "https://www.gutenberg.org/cache/epub/2701/pg2701.txt",
        "author": "Herman Melville",
        "title": "Moby Dick; Or, The Whale",
        "publication_year": 1851,
        "location": "Chapter 1, Loomings, opening through 'as soon as I can.'",
        "genre": "first-person literary fiction",
        "provenance": "Exact public-domain excerpt from the Project Gutenberg edition of Melville's published novel, verified against the linked primary text on 2026-10-30. Whitespace normalized."
      }
    },
    {
      "method": "POST",
      "url": "http://127.0.0.1:5054/submit",
      "request_json": {
        "text": "You don\u2019t know about me without you have read a book by the name of The Adventures of Tom Sawyer; but that ain\u2019t no matter. That book was made by Mr. Mark Twain, and he told the truth, mainly. There was things which he stretched, but mainly he told the truth. That is nothing. I never seen anybody but lied one time or another, without it was Aunt Polly, or the widow, or maybe Mary. Aunt Polly\u2014Tom\u2019s Aunt Polly, she is\u2014and Mary, and the Widow Douglas is all told about in that book, which is mostly a true book, with some stretchers, as I said before.",
        "creator_id": "eval-after-c1-t1-human-04"
      },
      "status_code": 200,
      "content_type": "application/json",
      "response_json": {
        "combined_score": 0.3954,
        "confidence": 0.3954,
        "content_id": "86bd2d93-97c8-4f53-9be4-144ae57126fe",
        "creator_id": "eval-after-c1-t1-human-04",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.4097,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.16602391043278608,
          "punctuation_density": 0.053691275167785234,
          "punctuation_simplicity": 0.5525727069351231,
          "repetition": 0.48148148148148145,
          "sentence_count": 7,
          "sentence_length_spread": 0.6671808716537712,
          "style_score": 0.338,
          "type_token_ratio": 0.6111111111111112,
          "word_count": 108
        },
        "style_score": 0.338,
        "text_length": 552,
        "timestamp": "2026-11-08T21:53:15+00:00"
      },
      "elapsed_ms": 62.18,
      "input_id": "human-04",
      "input_provenance": {
        "id": "human-04",
        "text": "You don\u2019t know about me without you have read a book by the name of The Adventures of Tom Sawyer; but that ain\u2019t no matter. That book was made by Mr. Mark Twain, and he told the truth, mainly. There was things which he stretched, but mainly he told the truth. That is nothing. I never seen anybody but lied one time or another, without it was Aunt Polly, or the widow, or maybe Mary. Aunt Polly\u2014Tom\u2019s Aunt Polly, she is\u2014and Mary, and the Widow Douglas is all told about in that book, which is mostly a true book, with some stretchers, as I said before.",
        "source_url": "https://www.gutenberg.org/cache/epub/76/pg76.txt",
        "author": "Mark Twain",
        "title": "Adventures of Huckleberry Finn",
        "publication_year": 1884,
        "location": "Chapter I, first paragraph",
        "genre": "first-person dialect fiction",
        "provenance": "Exact public-domain excerpt from the Project Gutenberg edition of Twain's published novel, verified against the linked primary text on 2026-10-30. Whitespace normalized. First UK publication was 1884; US publication followed in 1885."
      }
    },
    {
      "method": "POST",
      "url": "http://127.0.0.1:5054/submit",
      "request_json": {
        "text": "When I wrote the following pages, or rather the bulk of them, I lived alone, in the woods, a mile from any neighbor, in a house which I had built myself, on the shore of Walden Pond, in Concord, Massachusetts, and earned my living by the labor of my hands only. I lived there two years and two months. At present I am a sojourner in civilized life again.",
        "creator_id": "eval-after-c1-t1-human-05"
      },
      "status_code": 200,
      "content_type": "application/json",
      "response_json": {
        "combined_score": 0.6497,
        "confidence": 0.6497,
        "content_id": "70e13c84-8309-413e-a20b-e853c01b4a68",
        "creator_id": "eval-after-c1-t1-human-05",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.7577,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.0,
          "punctuation_density": 0.04195804195804196,
          "punctuation_simplicity": 0.6503496503496503,
          "repetition": 0.29227053140096626,
          "sentence_count": 3,
          "sentence_length_spread": 0.8615573303015565,
          "style_score": 0.2178,
          "type_token_ratio": 0.7246376811594203,
          "word_count": 69
        },
        "style_score": 0.2178,
        "text_length": 354,
        "timestamp": "2026-11-08T21:53:15+00:00"
      },
      "elapsed_ms": 43.59,
      "input_id": "human-05",
      "input_provenance": {
        "id": "human-05",
        "text": "When I wrote the following pages, or rather the bulk of them, I lived alone, in the woods, a mile from any neighbor, in a house which I had built myself, on the shore of Walden Pond, in Concord, Massachusetts, and earned my living by the labor of my hands only. I lived there two years and two months. At present I am a sojourner in civilized life again.",
        "source_url": "https://www.gutenberg.org/cache/epub/205/pg205.txt",
        "author": "Henry David Thoreau",
        "title": "Walden",
        "publication_year": 1854,
        "location": "Economy, first paragraph",
        "genre": "first-person nonfiction",
        "provenance": "Exact public-domain excerpt from Walden in the Project Gutenberg volume Walden, and On The Duty Of Civil Disobedience, verified against the linked primary text on 2026-10-30. Whitespace normalized."
      }
    },
    {
      "method": "POST",
      "url": "http://127.0.0.1:5054/submit",
      "request_json": {
        "text": "You will rejoice to hear that no disaster has accompanied the commencement of an enterprise which you have regarded with such evil forebodings. I arrived here yesterday, and my first task is to assure my dear sister of my welfare and increasing confidence in the success of my undertaking. I am already far north of London, and as I walk in the streets of Petersburgh, I feel a cold northern breeze play upon my cheeks, which braces my nerves and fills me with delight. Do you understand this feeling?",
        "creator_id": "eval-after-c1-t1-human-06"
      },
      "status_code": 200,
      "content_type": "application/json",
      "response_json": {
        "combined_score": 0.5545,
        "confidence": 0.5545,
        "content_id": "bcbc1050-fb0f-49bd-979e-b025dff8758a",
        "creator_id": "eval-after-c1-t1-human-06",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.5829,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.38795621995783924,
          "punctuation_density": 0.01937046004842615,
          "punctuation_simplicity": 0.8385794995964487,
          "repetition": 0.2640449438202247,
          "sentence_count": 4,
          "sentence_length_spread": 0.48963502403372866,
          "style_score": 0.4409,
          "type_token_ratio": 0.7415730337078652,
          "word_count": 89
        },
        "style_score": 0.4409,
        "text_length": 501,
        "timestamp": "2026-11-08T21:53:15+00:00"
      },
      "elapsed_ms": 48.68,
      "input_id": "human-06",
      "input_provenance": {
        "id": "human-06",
        "text": "You will rejoice to hear that no disaster has accompanied the commencement of an enterprise which you have regarded with such evil forebodings. I arrived here yesterday, and my first task is to assure my dear sister of my welfare and increasing confidence in the success of my undertaking. I am already far north of London, and as I walk in the streets of Petersburgh, I feel a cold northern breeze play upon my cheeks, which braces my nerves and fills me with delight. Do you understand this feeling?",
        "source_url": "https://www.gutenberg.org/cache/epub/84/pg84.txt",
        "author": "Mary Wollstonecraft Shelley",
        "title": "Frankenstein; or, The Modern Prometheus",
        "publication_year": 1818,
        "location": "Letter 1, opening through 'Do you understand this feeling?'",
        "genre": "epistolary literary fiction",
        "provenance": "Exact public-domain excerpt from the Project Gutenberg text of Shelley's novel, verified against the linked primary text on 2026-10-30. The work first appeared in 1818 and was revised in 1831; this is a transcription from the linked edition, not a claim that it is the 1818 wording. Whitespace normalized."
      }
    },
    {
      "method": "POST",
      "url": "http://127.0.0.1:5054/submit",
      "request_json": {
        "text": "Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, \u201cand what is the use of a book,\u201d thought Alice \u201cwithout pictures or conversations?\u201d So she was considering in her own mind (as well as she could, for the hot day made her feel very sleepy and stupid), whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her.",
        "creator_id": "eval-after-c1-t1-human-07"
      },
      "status_code": 200,
      "content_type": "application/json",
      "response_json": {
        "combined_score": 0.5606,
        "confidence": 0.5606,
        "content_id": "6f35cefd-8572-4370-8399-8d5b1c34218c",
        "creator_id": "eval-after-c1-t1-human-07",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.5745,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.5,
          "punctuation_density": 0.035343035343035345,
          "punctuation_simplicity": 0.7054747054747055,
          "repetition": 0.3790560471976401,
          "sentence_count": 2,
          "sentence_length_spread": 0.008849557522123894,
          "style_score": 0.5048,
          "type_token_ratio": 0.672566371681416,
          "word_count": 113
        },
        "style_score": 0.5048,
        "text_length": 592,
        "timestamp": "2026-11-08T21:53:15+00:00"
      },
      "elapsed_ms": 58.32,
      "input_id": "human-07",
      "input_provenance": {
        "id": "human-07",
        "text": "Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, \u201cand what is the use of a book,\u201d thought Alice \u201cwithout pictures or conversations?\u201d So she was considering in her own mind (as well as she could, for the hot day made her feel very sleepy and stupid), whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her.",
        "source_url": "https://www.gutenberg.org/cache/epub/11/pg11.txt",
        "author": "Lewis Carroll",
        "title": "Alice's Adventures in Wonderland",
        "publication_year": 1865,
        "location": "Chapter I, Down the Rabbit-Hole, first two paragraphs",
        "genre": "literary fiction",
        "provenance": "Exact public-domain excerpt from the Project Gutenberg edition of Carroll's published novel, verified against the linked primary text on 2026-10-30. Whitespace normalized."
      }
    },
    {
      "method": "POST",
      "url": "http://127.0.0.1:5054/submit",
      "request_json": {
        "text": "When on board H.M.S. \u2018Beagle,\u2019 as naturalist, I was much struck with certain facts in the distribution of the inhabitants of South America, and in the geological relations of the present to the past inhabitants of that continent. These facts seemed to me to throw some light on the origin of species\u2014that mystery of mysteries, as it has been called by one of our greatest philosophers. On my return home, it occurred to me, in 1837, that something might perhaps be made out on this question by patiently accumulating and reflecting on all sorts of facts which could possibly have any bearing on it.",
        "creator_id": "eval-after-c1-t1-human-08"
      },
      "status_code": 200,
      "content_type": "application/json",
      "response_json": {
        "combined_score": 0.5581,
        "confidence": 0.5581,
        "content_id": "df4e4b97-3d98-469b-ad02-88765beb6278",
        "creator_id": "eval-after-c1-t1-human-08",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.5825,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.420697370644045,
          "punctuation_density": 0.03232323232323232,
          "punctuation_simplicity": 0.7306397306397306,
          "repetition": 0.3473520249221185,
          "sentence_count": 4,
          "sentence_length_spread": 0.46344210348476406,
          "style_score": 0.4607,
          "type_token_ratio": 0.6915887850467289,
          "word_count": 107
        },
        "style_score": 0.4607,
        "text_length": 598,
        "timestamp": "2026-11-08T21:53:15+00:00"
      },
      "elapsed_ms": 53.47,
      "input_id": "human-08",
      "input_provenance": {
        "id": "human-08",
        "text": "When on board H.M.S. \u2018Beagle,\u2019 as naturalist, I was much struck with certain facts in the distribution of the inhabitants of South America, and in the geological relations of the present to the past inhabitants of that continent. These facts seemed to me to throw some light on the origin of species\u2014that mystery of mysteries, as it has been called by one of our greatest philosophers. On my return home, it occurred to me, in 1837, that something might perhaps be made out on this question by patiently accumulating and reflecting on all sorts of facts which could possibly have any bearing on it.",
        "source_url": "https://www.gutenberg.org/cache/epub/1228/pg1228.txt",
        "author": "Charles Darwin",
        "title": "On the Origin of Species By Means of Natural Selection",
        "publication_year": 1859,
        "location": "Introduction, first three sentences",
        "genre": "formal scientific nonfiction",
        "provenance": "Exact public-domain excerpt from the Project Gutenberg edition of Darwin's published work, verified against the linked primary text on 2026-10-30. Whitespace normalized."
      }
    },
    {
      "method": "POST",
      "url": "http://127.0.0.1:5054/submit",
      "request_json": {
        "text": "The produce of industry is what it adds to the subject or materials upon which it is employed. In proportion as the value of this produce is great or small, so will likewise be the profits of the employer. But it is only for the sake of profit that any man employs a capital in the support of industry; and he will always, therefore, endeavour to employ it in the support of that industry of which the produce is likely to be of the greatest value, or to exchange for the greatest quantity either of money or of other goods.",
        "creator_id": "eval-after-c1-t1-human-09"
      },
      "status_code": 200,
      "content_type": "application/json",
      "response_json": {
        "combined_score": 0.7081,
        "confidence": 0.7081,
        "content_id": "8e4775a9-d72c-482f-b972-531d35df6483",
        "creator_id": "eval-after-c1-t1-human-09",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.7648,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.26494047860054226,
          "punctuation_density": 0.018823529411764704,
          "punctuation_simplicity": 0.8431372549019608,
          "repetition": 0.6,
          "sentence_count": 3,
          "sentence_length_spread": 0.5880476171195662,
          "style_score": 0.4811,
          "type_token_ratio": 0.54,
          "word_count": 100
        },
        "style_score": 0.4811,
        "text_length": 524,
        "timestamp": "2026-11-08T21:53:15+00:00"
      },
      "elapsed_ms": 49.19,
      "input_id": "human-09",
      "input_provenance": {
        "id": "human-09",
        "text": "The produce of industry is what it adds to the subject or materials upon which it is employed. In proportion as the value of this produce is great or small, so will likewise be the profits of the employer. But it is only for the sake of profit that any man employs a capital in the support of industry; and he will always, therefore, endeavour to employ it in the support of that industry of which the produce is likely to be of the greatest value, or to exchange for the greatest quantity either of money or of other goods.",
        "source_url": "https://www.gutenberg.org/cache/epub/3300/pg3300.txt",
        "author": "Adam Smith",
        "title": "An Inquiry into the Nature and Causes of the Wealth of Nations",
        "publication_year": 1776,
        "location": "Book IV, Chapter II, paragraph beginning 'The produce of industry'",
        "genre": "formal economic nonfiction",
        "provenance": "Exact public-domain excerpt from the Project Gutenberg edition of Smith's published work, verified against the linked primary text on 2026-10-30. Whitespace normalized."
      }
    },
    {
      "method": "POST",
      "url": "http://127.0.0.1:5054/submit",
      "request_json": {
        "text": "My elder brothers were all put apprentices to different trades. I was put to the grammar-school at eight years of age, my father intending to devote me, as the tithe[13] of his sons, to the service of the Church. My early readiness in learning to read (which must have been very early, as I do not remember when I could not read), and the opinion of all his friends, that I should certainly make a good scholar, encouraged him in this purpose of his. My uncle Benjamin, too, approved of it, and proposed to give me all his short-hand volumes of sermons, I suppose as a stock to set up with, if I would learn his character.[14]",
        "creator_id": "eval-after-c1-t1-human-10"
      },
      "status_code": 200,
      "content_type": "application/json",
      "response_json": {
        "combined_score": 0.5475,
        "confidence": 0.5475,
        "content_id": "5ca3eaf8-27d6-45af-87a9-0449ae23b3bd",
        "creator_id": "eval-after-c1-t1-human-10",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.566,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.4729379744287563,
          "punctuation_density": 0.047058823529411764,
          "punctuation_simplicity": 0.607843137254902,
          "repetition": 0.3842975206611571,
          "sentence_count": 4,
          "sentence_length_spread": 0.421649620456995,
          "style_score": 0.4733,
          "type_token_ratio": 0.6694214876033058,
          "word_count": 121
        },
        "style_score": 0.4733,
        "text_length": 626,
        "timestamp": "2026-11-08T21:53:15+00:00"
      },
      "elapsed_ms": 61.16,
      "input_id": "human-10",
      "input_provenance": {
        "id": "human-10",
        "text": "My elder brothers were all put apprentices to different trades. I was put to the grammar-school at eight years of age, my father intending to devote me, as the tithe[13] of his sons, to the service of the Church. My early readiness in learning to read (which must have been very early, as I do not remember when I could not read), and the opinion of all his friends, that I should certainly make a good scholar, encouraged him in this purpose of his. My uncle Benjamin, too, approved of it, and proposed to give me all his short-hand volumes of sermons, I suppose as a stock to set up with, if I would learn his character.[14]",
        "source_url": "https://www.gutenberg.org/cache/epub/20203/pg20203.txt",
        "author": "Benjamin Franklin",
        "title": "Autobiography of Benjamin Franklin",
        "publication_year": 1791,
        "location": "Passage beginning 'My elder brothers were all put apprentices', first four sentences",
        "genre": "first-person autobiographical nonfiction",
        "provenance": "Exact public-domain excerpt from the Project Gutenberg transcription of the 1916 English edition (1922 printing), verified against the linked primary text on 2026-10-30. The memoir was composed in 1771\u20131790 and initially published in French in 1791. The linked edition states that its text follows Bigelow's nineteenth-century editions. Edition footnote markers retained; whitespace normalized."
      }
    }
  ],
  "flagged_ids": [],
  "valid_count": 10,
  "summary": "0/10 AI flags; 10/10 valid",
  "passed": true,
  "verdict": "MET"
}
```

### Criterion 2

Produced by `run_eval.py::trial_result` (score_spread).

```json
{
  "trial": 1,
  "criterion": 2,
  "kind": "score_spread",
  "cases": [
    {
      "method": "POST",
      "url": "http://127.0.0.1:5054/submit",
      "request_json": {
        "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
        "creator_id": "eval-after-c2-t1-human-01"
      },
      "status_code": 200,
      "content_type": "application/json",
      "response_json": {
        "combined_score": 0.6593,
        "confidence": 0.6593,
        "content_id": "8d520d39-1760-4a4b-8aae-74e0c1094aea",
        "creator_id": "eval-after-c2-t1-human-01",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.6922,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.5,
          "punctuation_density": 0.016286644951140065,
          "punctuation_simplicity": 0.8642779587404994,
          "repetition": 0.34976525821596255,
          "sentence_count": 2,
          "sentence_length_spread": 0.352112676056338,
          "style_score": 0.5278,
          "type_token_ratio": 0.6901408450704225,
          "word_count": 71
        },
        "style_score": 0.5278,
        "text_length": 377,
        "timestamp": "2026-11-08T21:53:15+00:00"
      },
      "elapsed_ms": 41.36,
      "input_id": "human-01",
      "input_provenance": {
        "id": "human-01",
        "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
        "source_url": "https://www.gutenberg.org/cache/epub/1342/pg1342.txt",
        "author": "Jane Austen",
        "title": "Pride and Prejudice",
        "publication_year": 1813,
        "location": "Chapter I, first two paragraphs",
        "genre": "literary fiction",
        "provenance": "Exact public-domain excerpt from the Project Gutenberg edition of Austen's published novel, verified against the linked primary text on 2026-10-30. Whitespace normalized."
      }
    },
    {
      "method": "POST",
      "url": "http://127.0.0.1:5054/submit",
      "request_json": {
        "text": "There was no possibility of taking a walk that day. We had been wandering, indeed, in the leafless shrubbery an hour in the morning; but since dinner (Mrs. Reed, when there was no company, dined early) the cold winter wind had brought with it clouds so sombre, and a rain so penetrating, that further outdoor exercise was now out of the question. I was glad of it: I never liked long walks, especially on chilly afternoons: dreadful to me was the coming home in the raw twilight, with nipped fingers and toes, and a heart saddened by the chidings of Bessie, the nurse, and humbled by the consciousness of my physical inferiority to Eliza, John, and Georgiana Reed.",
        "creator_id": "eval-after-c2-t1-human-02"
      },
      "status_code": 200,
      "content_type": "application/json",
      "response_json": {
        "combined_score": 0.4608,
        "confidence": 0.4608,
        "content_id": "2add6a7a-d295-4559-aa87-d8bba72553eb",
        "creator_id": "eval-after-c2-t1-human-02",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.4863,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.2554540936099331,
          "punctuation_density": 0.04021937842778794,
          "punctuation_simplicity": 0.6648385131017671,
          "repetition": 0.3276836158192091,
          "sentence_count": 4,
          "sentence_length_spread": 0.5956367251120536,
          "style_score": 0.359,
          "type_token_ratio": 0.7033898305084746,
          "word_count": 118
        },
        "style_score": 0.359,
        "text_length": 664,
        "timestamp": "2026-11-08T21:53:15+00:00"
      },
      "elapsed_ms": 63.72,
      "input_id": "human-02",
      "input_provenance": {
        "id": "human-02",
        "text": "There was no possibility of taking a walk that day. We had been wandering, indeed, in the leafless shrubbery an hour in the morning; but since dinner (Mrs. Reed, when there was no company, dined early) the cold winter wind had brought with it clouds so sombre, and a rain so penetrating, that further outdoor exercise was now out of the question. I was glad of it: I never liked long walks, especially on chilly afternoons: dreadful to me was the coming home in the raw twilight, with nipped fingers and toes, and a heart saddened by the chidings of Bessie, the nurse, and humbled by the consciousness of my physical inferiority to Eliza, John, and Georgiana Reed.",
        "source_url": "https://www.gutenberg.org/cache/epub/1260/pg1260.txt",
        "author": "Charlotte Bront\u00eb",
        "title": "Jane Eyre: An Autobiography",
        "publication_year": 1847,
        "location": "Chapter I, first two paragraphs",
        "genre": "first-person literary fiction",
        "provenance": "Exact public-domain excerpt from the Project Gutenberg edition of Bront\u00eb's published novel, verified against the linked primary text on 2026-10-30. Whitespace normalized."
      }
    },
    {
      "method": "POST",
      "url": "http://127.0.0.1:5054/submit",
      "request_json": {
        "text": "Call me Ishmael. Some years ago\u2014never mind how long precisely\u2014having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world. It is a way I have of driving off the spleen and regulating the circulation. Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral I meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people\u2019s hats off\u2014then, I account it high time to get to sea as soon as I can.",
        "creator_id": "eval-after-c2-t1-human-03"
      },
      "status_code": 200,
      "content_type": "application/json",
      "response_json": {
        "combined_score": 0.3358,
        "confidence": 0.3358,
        "content_id": "16bb95f1-8b23-44d5-b91e-aafefd5f3a53",
        "creator_id": "eval-after-c2-t1-human-03",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.3532,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.0,
          "punctuation_density": 0.027522935779816515,
          "punctuation_simplicity": 0.7706422018348624,
          "repetition": 0.37356321839080464,
          "sentence_count": 4,
          "sentence_length_spread": 0.8882105351861661,
          "style_score": 0.2662,
          "type_token_ratio": 0.6758620689655173,
          "word_count": 145
        },
        "style_score": 0.2662,
        "text_length": 795,
        "timestamp": "2026-11-08T21:53:16+00:00"
      },
      "elapsed_ms": 69.49,
      "input_id": "human-03",
      "input_provenance": {
        "id": "human-03",
        "text": "Call me Ishmael. Some years ago\u2014never mind how long precisely\u2014having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world. It is a way I have of driving off the spleen and regulating the circulation. Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral I meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people\u2019s hats off\u2014then, I account it high time to get to sea as soon as I can.",
        "source_url": "https://www.gutenberg.org/cache/epub/2701/pg2701.txt",
        "author": "Herman Melville",
        "title": "Moby Dick; Or, The Whale",
        "publication_year": 1851,
        "location": "Chapter 1, Loomings, opening through 'as soon as I can.'",
        "genre": "first-person literary fiction",
        "provenance": "Exact public-domain excerpt from the Project Gutenberg edition of Melville's published novel, verified against the linked primary text on 2026-10-30. Whitespace normalized."
      }
    },
    {
      "method": "POST",
      "url": "http://127.0.0.1:5054/submit",
      "request_json": {
        "text": "You don\u2019t know about me without you have read a book by the name of The Adventures of Tom Sawyer; but that ain\u2019t no matter. That book was made by Mr. Mark Twain, and he told the truth, mainly. There was things which he stretched, but mainly he told the truth. That is nothing. I never seen anybody but lied one time or another, without it was Aunt Polly, or the widow, or maybe Mary. Aunt Polly\u2014Tom\u2019s Aunt Polly, she is\u2014and Mary, and the Widow Douglas is all told about in that book, which is mostly a true book, with some stretchers, as I said before.",
        "creator_id": "eval-after-c2-t1-human-04"
      },
      "status_code": 200,
      "content_type": "application/json",
      "response_json": {
        "combined_score": 0.3954,
        "confidence": 0.3954,
        "content_id": "daa1301c-4a58-4d9c-8786-02507850f440",
        "creator_id": "eval-after-c2-t1-human-04",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.4097,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.16602391043278608,
          "punctuation_density": 0.053691275167785234,
          "punctuation_simplicity": 0.5525727069351231,
          "repetition": 0.48148148148148145,
          "sentence_count": 7,
          "sentence_length_spread": 0.6671808716537712,
          "style_score": 0.338,
          "type_token_ratio": 0.6111111111111112,
          "word_count": 108
        },
        "style_score": 0.338,
        "text_length": 552,
        "timestamp": "2026-11-08T21:53:16+00:00"
      },
      "elapsed_ms": 59.1,
      "input_id": "human-04",
      "input_provenance": {
        "id": "human-04",
        "text": "You don\u2019t know about me without you have read a book by the name of The Adventures of Tom Sawyer; but that ain\u2019t no matter. That book was made by Mr. Mark Twain, and he told the truth, mainly. There was things which he stretched, but mainly he told the truth. That is nothing. I never seen anybody but lied one time or another, without it was Aunt Polly, or the widow, or maybe Mary. Aunt Polly\u2014Tom\u2019s Aunt Polly, she is\u2014and Mary, and the Widow Douglas is all told about in that book, which is mostly a true book, with some stretchers, as I said before.",
        "source_url": "https://www.gutenberg.org/cache/epub/76/pg76.txt",
        "author": "Mark Twain",
        "title": "Adventures of Huckleberry Finn",
        "publication_year": 1884,
        "location": "Chapter I, first paragraph",
        "genre": "first-person dialect fiction",
        "provenance": "Exact public-domain excerpt from the Project Gutenberg edition of Twain's published novel, verified against the linked primary text on 2026-10-30. Whitespace normalized. First UK publication was 1884; US publication followed in 1885."
      }
    },
    {
      "method": "POST",
      "url": "http://127.0.0.1:5054/submit",
      "request_json": {
        "text": "Effective communication is essential for building a productive and collaborative workplace. By establishing clear expectations and encouraging open dialogue, organizations can ensure that every team member understands their responsibilities. Regular feedback helps employees identify opportunities for improvement while reinforcing successful habits. In addition, consistent documentation allows important information to remain accessible as projects evolve. Managers should create an environment where questions are welcomed and different perspectives are respected. This approach supports accountability, reduces misunderstandings, and strengthens trust across departments. Ultimately, investing in thoughtful communication practices enables teams to work more efficiently and achieve sustainable results together.",
        "creator_id": "eval-after-c2-t1-ai-01"
      },
      "status_code": 200,
      "content_type": "application/json",
      "response_json": {
        "combined_score": 0.6086,
        "confidence": 0.6086,
        "content_id": "d7526ea8-a718-4aa9-ba6d-e818367016ce",
        "creator_id": "eval-after-c2-t1-ai-01",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.6223,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.7627491255431172,
          "punctuation_density": 0.016643550624133148,
          "punctuation_simplicity": 0.8613037447988905,
          "repetition": 0.0,
          "sentence_count": 7,
          "sentence_length_spread": 0.18980069956550624,
          "style_score": 0.5536,
          "type_token_ratio": 0.90625,
          "word_count": 96
        },
        "style_score": 0.5536,
        "text_length": 816,
        "timestamp": "2026-11-08T21:53:16+00:00"
      },
      "elapsed_ms": 51.71,
      "input_id": "ai-01",
      "input_provenance": {
        "id": "ai-01",
        "text": "Effective communication is essential for building a productive and collaborative workplace. By establishing clear expectations and encouraging open dialogue, organizations can ensure that every team member understands their responsibilities. Regular feedback helps employees identify opportunities for improvement while reinforcing successful habits. In addition, consistent documentation allows important information to remain accessible as projects evolve. Managers should create an environment where questions are welcomed and different perspectives are respected. This approach supports accountability, reduces misunderstandings, and strengthens trust across departments. Ultimately, investing in thoughtful communication practices enables teams to work more efficiently and achieve sustainable results together.",
        "origin": "AI-generated by Codex for development",
        "provenance": "Generated before detector evaluation on 2026-10-30. Original synthetic workplace advice; not independently human-authored or copied from a source.",
        "generation_prompt": "Write a polished, approximately 100-word paragraph of ordinary workplace communication advice."
      }
    },
    {
      "method": "POST",
      "url": "http://127.0.0.1:5054/submit",
      "request_json": {
        "text": "A successful morning routine begins with a clear and achievable plan. Start by choosing a consistent time to wake up each day. Next, drink a glass of water and prepare a simple breakfast. Set aside a few minutes to review your most important tasks. Keep your workspace organized so that necessary materials are easy to find. Limit unnecessary notifications during periods that require your full attention. Take short breaks to maintain focus and prevent mental fatigue. Review your progress at the end of each working session. Small, consistent improvements can make daily responsibilities easier to manage over time.",
        "creator_id": "eval-after-c2-t1-ai-02"
      },
      "status_code": 200,
      "content_type": "application/json",
      "response_json": {
        "combined_score": 0.6668,
        "confidence": 0.6668,
        "content_id": "6240db55-f541-49d4-9902-ac413338b7f5",
        "creator_id": "eval-after-c2-t1-ai-02",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.6649,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.9153922247358316,
          "punctuation_density": 0.021153846153846155,
          "punctuation_simplicity": 0.8237179487179487,
          "repetition": 0.1734693877551021,
          "sentence_count": 9,
          "sentence_length_spread": 0.06768622021133469,
          "style_score": 0.6745,
          "type_token_ratio": 0.7959183673469388,
          "word_count": 98
        },
        "style_score": 0.6745,
        "text_length": 617,
        "timestamp": "2026-11-08T21:53:16+00:00"
      },
      "elapsed_ms": 49.56,
      "input_id": "ai-02",
      "input_provenance": {
        "id": "ai-02",
        "text": "A successful morning routine begins with a clear and achievable plan. Start by choosing a consistent time to wake up each day. Next, drink a glass of water and prepare a simple breakfast. Set aside a few minutes to review your most important tasks. Keep your workspace organized so that necessary materials are easy to find. Limit unnecessary notifications during periods that require your full attention. Take short breaks to maintain focus and prevent mental fatigue. Review your progress at the end of each working session. Small, consistent improvements can make daily responsibilities easier to manage over time.",
        "origin": "AI-generated by Codex for development",
        "provenance": "Generated before detector evaluation on 2026-10-30. Original synthetic routine advice with deliberately regular sentence structure.",
        "generation_prompt": "Write approximately 100 words of routine advice using plain sentences of fairly consistent length."
      }
    },
    {
      "method": "POST",
      "url": "http://127.0.0.1:5054/submit",
      "request_json": {
        "text": "The team reviews the project plan before starting each task. The team checks the project goals before starting each task. The team shares the project notes before starting each task. The team updates the project schedule before starting each task. The team reviews the project budget before starting each task. The team checks the project records before starting each task. The team shares the project results before starting each task. The team updates the project report before starting each task.",
        "creator_id": "eval-after-c2-t1-ai-03"
      },
      "status_code": 200,
      "content_type": "application/json",
      "response_json": {
        "combined_score": 0.9615,
        "confidence": 0.9615,
        "content_id": "5896602e-a7a0-448b-a49e-1312c59d5c4c",
        "creator_id": "eval-after-c2-t1-ai-03",
        "detector_model": "gpt2",
        "guess": "ai",
        "label": "This writing shows patterns often found in AI-generated text. This estimate can be wrong and is not proof of AI use. You can request a review.",
        "model_score": 0.9598,
        "status": "decided",
        "style_metrics": {
          "evenness": 1.0,
          "punctuation_density": 0.01904761904761905,
          "punctuation_simplicity": 0.8412698412698413,
          "repetition": 1.0,
          "sentence_count": 8,
          "sentence_length_spread": 0.0,
          "style_score": 0.9683,
          "type_token_ratio": 0.2375,
          "word_count": 80
        },
        "style_score": 0.9683,
        "text_length": 499,
        "timestamp": "2026-11-08T21:53:16+00:00"
      },
      "elapsed_ms": 44.93,
      "input_id": "ai-03",
      "input_provenance": {
        "id": "ai-03",
        "text": "The team reviews the project plan before starting each task. The team checks the project goals before starting each task. The team shares the project notes before starting each task. The team updates the project schedule before starting each task. The team reviews the project budget before starting each task. The team checks the project records before starting each task. The team shares the project results before starting each task. The team updates the project report before starting each task.",
        "origin": "AI-generated by Codex for development",
        "provenance": "Generated before detector evaluation on 2026-10-30. Deliberately repetitive synthetic prose for exercising the stylometry signal; not representative of typical AI writing.",
        "generation_prompt": "Write eight ordinary project-management sentences with the same grammatical pattern and closely matched length."
      }
    },
    {
      "method": "POST",
      "url": "http://127.0.0.1:5054/submit",
      "request_json": {
        "text": "Rain gardens provide a practical way to manage stormwater while supporting healthy urban environments. These shallow planted areas collect runoff from roofs, sidewalks, and driveways, allowing water to soak gradually into the ground. Native plants help stabilize the soil and provide food and shelter for local wildlife. Because rain gardens slow the movement of water, they can also reduce the amount of sediment reaching nearby streams. Successful installation requires attention to drainage, soil conditions, and the distance from building foundations. With appropriate planning and routine maintenance, a rain garden can become an attractive and useful feature of a neighborhood.",
        "creator_id": "eval-after-c2-t1-ai-04"
      },
      "status_code": 200,
      "content_type": "application/json",
      "response_json": {
        "combined_score": 0.6834,
        "confidence": 0.6834,
        "content_id": "672b4ddb-3c38-4664-80dd-d7503eed3f4f",
        "creator_id": "eval-after-c2-t1-ai-04",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.6956,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.8106060606060606,
          "punctuation_density": 0.022222222222222223,
          "punctuation_simplicity": 0.8148148148148148,
          "repetition": 0.22053872053872067,
          "sentence_count": 6,
          "sentence_length_spread": 0.15151515151515152,
          "style_score": 0.6344,
          "type_token_ratio": 0.7676767676767676,
          "word_count": 99
        },
        "style_score": 0.6344,
        "text_length": 683,
        "timestamp": "2026-11-08T21:53:16+00:00"
      },
      "elapsed_ms": 52.87,
      "input_id": "ai-04",
      "input_provenance": {
        "id": "ai-04",
        "text": "Rain gardens provide a practical way to manage stormwater while supporting healthy urban environments. These shallow planted areas collect runoff from roofs, sidewalks, and driveways, allowing water to soak gradually into the ground. Native plants help stabilize the soil and provide food and shelter for local wildlife. Because rain gardens slow the movement of water, they can also reduce the amount of sediment reaching nearby streams. Successful installation requires attention to drainage, soil conditions, and the distance from building foundations. With appropriate planning and routine maintenance, a rain garden can become an attractive and useful feature of a neighborhood.",
        "origin": "AI-generated by Codex for development",
        "provenance": "Generated before detector evaluation on 2026-10-30. Original synthetic general explainer; not a sourced human passage.",
        "generation_prompt": "Write an approximately 100-word informational paragraph explaining rain gardens in a polished general-audience style."
      }
    }
  ],
  "human_median": 0.4281,
  "ai_median": 0.6751,
  "gap": 0.247,
  "summary": "median gap 0.247",
  "passed": true,
  "verdict": "MET"
}
```

### Criterion 3

Produced by `run_eval.py::trial_result` (label_coverage).

```json
{
  "trial": 1,
  "criterion": 3,
  "kind": "label_coverage",
  "cases": [
    {
      "method": "POST",
      "url": "http://127.0.0.1:5054/submit",
      "request_json": {
        "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
        "creator_id": "eval-after-c3-t1-human-01"
      },
      "status_code": 200,
      "content_type": "application/json",
      "response_json": {
        "combined_score": 0.6593,
        "confidence": 0.6593,
        "content_id": "bd890b89-3c52-4158-b7aa-d15e3859e621",
        "creator_id": "eval-after-c3-t1-human-01",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.6922,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.5,
          "punctuation_density": 0.016286644951140065,
          "punctuation_simplicity": 0.8642779587404994,
          "repetition": 0.34976525821596255,
          "sentence_count": 2,
          "sentence_length_spread": 0.352112676056338,
          "style_score": 0.5278,
          "type_token_ratio": 0.6901408450704225,
          "word_count": 71
        },
        "style_score": 0.5278,
        "text_length": 377,
        "timestamp": "2026-11-08T21:53:16+00:00"
      },
      "elapsed_ms": 40.29,
      "input_id": "human-01",
      "input_provenance": {
        "id": "human-01",
        "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
        "source_url": "https://www.gutenberg.org/cache/epub/1342/pg1342.txt",
        "author": "Jane Austen",
        "title": "Pride and Prejudice",
        "publication_year": 1813,
        "location": "Chapter I, first two paragraphs",
        "genre": "literary fiction",
        "provenance": "Exact public-domain excerpt from the Project Gutenberg edition of Austen's published novel, verified against the linked primary text on 2026-10-30. Whitespace normalized."
      }
    },
    {
      "method": "POST",
      "url": "http://127.0.0.1:5054/submit",
      "request_json": {
        "text": "There was no possibility of taking a walk that day. We had been wandering, indeed, in the leafless shrubbery an hour in the morning; but since dinner (Mrs. Reed, when there was no company, dined early) the cold winter wind had brought with it clouds so sombre, and a rain so penetrating, that further outdoor exercise was now out of the question. I was glad of it: I never liked long walks, especially on chilly afternoons: dreadful to me was the coming home in the raw twilight, with nipped fingers and toes, and a heart saddened by the chidings of Bessie, the nurse, and humbled by the consciousness of my physical inferiority to Eliza, John, and Georgiana Reed.",
        "creator_id": "eval-after-c3-t1-human-02"
      },
      "status_code": 200,
      "content_type": "application/json",
      "response_json": {
        "combined_score": 0.4608,
        "confidence": 0.4608,
        "content_id": "79018bf0-7875-4d6e-885b-7dbae0a84dcf",
        "creator_id": "eval-after-c3-t1-human-02",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.4863,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.2554540936099331,
          "punctuation_density": 0.04021937842778794,
          "punctuation_simplicity": 0.6648385131017671,
          "repetition": 0.3276836158192091,
          "sentence_count": 4,
          "sentence_length_spread": 0.5956367251120536,
          "style_score": 0.359,
          "type_token_ratio": 0.7033898305084746,
          "word_count": 118
        },
        "style_score": 0.359,
        "text_length": 664,
        "timestamp": "2026-11-08T21:53:16+00:00"
      },
      "elapsed_ms": 63.18,
      "input_id": "human-02",
      "input_provenance": {
        "id": "human-02",
        "text": "There was no possibility of taking a walk that day. We had been wandering, indeed, in the leafless shrubbery an hour in the morning; but since dinner (Mrs. Reed, when there was no company, dined early) the cold winter wind had brought with it clouds so sombre, and a rain so penetrating, that further outdoor exercise was now out of the question. I was glad of it: I never liked long walks, especially on chilly afternoons: dreadful to me was the coming home in the raw twilight, with nipped fingers and toes, and a heart saddened by the chidings of Bessie, the nurse, and humbled by the consciousness of my physical inferiority to Eliza, John, and Georgiana Reed.",
        "source_url": "https://www.gutenberg.org/cache/epub/1260/pg1260.txt",
        "author": "Charlotte Bront\u00eb",
        "title": "Jane Eyre: An Autobiography",
        "publication_year": 1847,
        "location": "Chapter I, first two paragraphs",
        "genre": "first-person literary fiction",
        "provenance": "Exact public-domain excerpt from the Project Gutenberg edition of Bront\u00eb's published novel, verified against the linked primary text on 2026-10-30. Whitespace normalized."
      }
    },
    {
      "method": "POST",
      "url": "http://127.0.0.1:5054/submit",
      "request_json": {
        "text": "Call me Ishmael. Some years ago\u2014never mind how long precisely\u2014having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world. It is a way I have of driving off the spleen and regulating the circulation. Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral I meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people\u2019s hats off\u2014then, I account it high time to get to sea as soon as I can.",
        "creator_id": "eval-after-c3-t1-human-03"
      },
      "status_code": 200,
      "content_type": "application/json",
      "response_json": {
        "combined_score": 0.3358,
        "confidence": 0.3358,
        "content_id": "9fce5b9a-df32-429a-a4eb-6b0512568880",
        "creator_id": "eval-after-c3-t1-human-03",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.3532,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.0,
          "punctuation_density": 0.027522935779816515,
          "punctuation_simplicity": 0.7706422018348624,
          "repetition": 0.37356321839080464,
          "sentence_count": 4,
          "sentence_length_spread": 0.8882105351861661,
          "style_score": 0.2662,
          "type_token_ratio": 0.6758620689655173,
          "word_count": 145
        },
        "style_score": 0.2662,
        "text_length": 795,
        "timestamp": "2026-11-08T21:53:16+00:00"
      },
      "elapsed_ms": 68.66,
      "input_id": "human-03",
      "input_provenance": {
        "id": "human-03",
        "text": "Call me Ishmael. Some years ago\u2014never mind how long precisely\u2014having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world. It is a way I have of driving off the spleen and regulating the circulation. Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral I meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people\u2019s hats off\u2014then, I account it high time to get to sea as soon as I can.",
        "source_url": "https://www.gutenberg.org/cache/epub/2701/pg2701.txt",
        "author": "Herman Melville",
        "title": "Moby Dick; Or, The Whale",
        "publication_year": 1851,
        "location": "Chapter 1, Loomings, opening through 'as soon as I can.'",
        "genre": "first-person literary fiction",
        "provenance": "Exact public-domain excerpt from the Project Gutenberg edition of Melville's published novel, verified against the linked primary text on 2026-10-30. Whitespace normalized."
      }
    },
    {
      "method": "POST",
      "url": "http://127.0.0.1:5054/submit",
      "request_json": {
        "text": "You don\u2019t know about me without you have read a book by the name of The Adventures of Tom Sawyer; but that ain\u2019t no matter. That book was made by Mr. Mark Twain, and he told the truth, mainly. There was things which he stretched, but mainly he told the truth. That is nothing. I never seen anybody but lied one time or another, without it was Aunt Polly, or the widow, or maybe Mary. Aunt Polly\u2014Tom\u2019s Aunt Polly, she is\u2014and Mary, and the Widow Douglas is all told about in that book, which is mostly a true book, with some stretchers, as I said before.",
        "creator_id": "eval-after-c3-t1-human-04"
      },
      "status_code": 200,
      "content_type": "application/json",
      "response_json": {
        "combined_score": 0.3954,
        "confidence": 0.3954,
        "content_id": "8884f26e-ac78-4774-80c7-602ecebf8679",
        "creator_id": "eval-after-c3-t1-human-04",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.4097,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.16602391043278608,
          "punctuation_density": 0.053691275167785234,
          "punctuation_simplicity": 0.5525727069351231,
          "repetition": 0.48148148148148145,
          "sentence_count": 7,
          "sentence_length_spread": 0.6671808716537712,
          "style_score": 0.338,
          "type_token_ratio": 0.6111111111111112,
          "word_count": 108
        },
        "style_score": 0.338,
        "text_length": 552,
        "timestamp": "2026-11-08T21:53:16+00:00"
      },
      "elapsed_ms": 59.17,
      "input_id": "human-04",
      "input_provenance": {
        "id": "human-04",
        "text": "You don\u2019t know about me without you have read a book by the name of The Adventures of Tom Sawyer; but that ain\u2019t no matter. That book was made by Mr. Mark Twain, and he told the truth, mainly. There was things which he stretched, but mainly he told the truth. That is nothing. I never seen anybody but lied one time or another, without it was Aunt Polly, or the widow, or maybe Mary. Aunt Polly\u2014Tom\u2019s Aunt Polly, she is\u2014and Mary, and the Widow Douglas is all told about in that book, which is mostly a true book, with some stretchers, as I said before.",
        "source_url": "https://www.gutenberg.org/cache/epub/76/pg76.txt",
        "author": "Mark Twain",
        "title": "Adventures of Huckleberry Finn",
        "publication_year": 1884,
        "location": "Chapter I, first paragraph",
        "genre": "first-person dialect fiction",
        "provenance": "Exact public-domain excerpt from the Project Gutenberg edition of Twain's published novel, verified against the linked primary text on 2026-10-30. Whitespace normalized. First UK publication was 1884; US publication followed in 1885."
      }
    },
    {
      "method": "POST",
      "url": "http://127.0.0.1:5054/submit",
      "request_json": {
        "text": "When I wrote the following pages, or rather the bulk of them, I lived alone, in the woods, a mile from any neighbor, in a house which I had built myself, on the shore of Walden Pond, in Concord, Massachusetts, and earned my living by the labor of my hands only. I lived there two years and two months. At present I am a sojourner in civilized life again.",
        "creator_id": "eval-after-c3-t1-human-05"
      },
      "status_code": 200,
      "content_type": "application/json",
      "response_json": {
        "combined_score": 0.6497,
        "confidence": 0.6497,
        "content_id": "25e8a07c-9b5a-4025-a8ac-b337a1bf7537",
        "creator_id": "eval-after-c3-t1-human-05",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.7577,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.0,
          "punctuation_density": 0.04195804195804196,
          "punctuation_simplicity": 0.6503496503496503,
          "repetition": 0.29227053140096626,
          "sentence_count": 3,
          "sentence_length_spread": 0.8615573303015565,
          "style_score": 0.2178,
          "type_token_ratio": 0.7246376811594203,
          "word_count": 69
        },
        "style_score": 0.2178,
        "text_length": 354,
        "timestamp": "2026-11-08T21:53:16+00:00"
      },
      "elapsed_ms": 43.18,
      "input_id": "human-05",
      "input_provenance": {
        "id": "human-05",
        "text": "When I wrote the following pages, or rather the bulk of them, I lived alone, in the woods, a mile from any neighbor, in a house which I had built myself, on the shore of Walden Pond, in Concord, Massachusetts, and earned my living by the labor of my hands only. I lived there two years and two months. At present I am a sojourner in civilized life again.",
        "source_url": "https://www.gutenberg.org/cache/epub/205/pg205.txt",
        "author": "Henry David Thoreau",
        "title": "Walden",
        "publication_year": 1854,
        "location": "Economy, first paragraph",
        "genre": "first-person nonfiction",
        "provenance": "Exact public-domain excerpt from Walden in the Project Gutenberg volume Walden, and On The Duty Of Civil Disobedience, verified against the linked primary text on 2026-10-30. Whitespace normalized."
      }
    },
    {
      "method": "POST",
      "url": "http://127.0.0.1:5054/submit",
      "request_json": {
        "text": "You will rejoice to hear that no disaster has accompanied the commencement of an enterprise which you have regarded with such evil forebodings. I arrived here yesterday, and my first task is to assure my dear sister of my welfare and increasing confidence in the success of my undertaking. I am already far north of London, and as I walk in the streets of Petersburgh, I feel a cold northern breeze play upon my cheeks, which braces my nerves and fills me with delight. Do you understand this feeling?",
        "creator_id": "eval-after-c3-t1-human-06"
      },
      "status_code": 200,
      "content_type": "application/json",
      "response_json": {
        "combined_score": 0.5545,
        "confidence": 0.5545,
        "content_id": "2e3dc93f-91ef-4cc4-8b73-6dd1e57df023",
        "creator_id": "eval-after-c3-t1-human-06",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.5829,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.38795621995783924,
          "punctuation_density": 0.01937046004842615,
          "punctuation_simplicity": 0.8385794995964487,
          "repetition": 0.2640449438202247,
          "sentence_count": 4,
          "sentence_length_spread": 0.48963502403372866,
          "style_score": 0.4409,
          "type_token_ratio": 0.7415730337078652,
          "word_count": 89
        },
        "style_score": 0.4409,
        "text_length": 501,
        "timestamp": "2026-11-08T21:53:16+00:00"
      },
      "elapsed_ms": 48.73,
      "input_id": "human-06",
      "input_provenance": {
        "id": "human-06",
        "text": "You will rejoice to hear that no disaster has accompanied the commencement of an enterprise which you have regarded with such evil forebodings. I arrived here yesterday, and my first task is to assure my dear sister of my welfare and increasing confidence in the success of my undertaking. I am already far north of London, and as I walk in the streets of Petersburgh, I feel a cold northern breeze play upon my cheeks, which braces my nerves and fills me with delight. Do you understand this feeling?",
        "source_url": "https://www.gutenberg.org/cache/epub/84/pg84.txt",
        "author": "Mary Wollstonecraft Shelley",
        "title": "Frankenstein; or, The Modern Prometheus",
        "publication_year": 1818,
        "location": "Letter 1, opening through 'Do you understand this feeling?'",
        "genre": "epistolary literary fiction",
        "provenance": "Exact public-domain excerpt from the Project Gutenberg text of Shelley's novel, verified against the linked primary text on 2026-10-30. The work first appeared in 1818 and was revised in 1831; this is a transcription from the linked edition, not a claim that it is the 1818 wording. Whitespace normalized."
      }
    },
    {
      "method": "POST",
      "url": "http://127.0.0.1:5054/submit",
      "request_json": {
        "text": "Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, \u201cand what is the use of a book,\u201d thought Alice \u201cwithout pictures or conversations?\u201d So she was considering in her own mind (as well as she could, for the hot day made her feel very sleepy and stupid), whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her.",
        "creator_id": "eval-after-c3-t1-human-07"
      },
      "status_code": 200,
      "content_type": "application/json",
      "response_json": {
        "combined_score": 0.5606,
        "confidence": 0.5606,
        "content_id": "04e690c2-e042-4806-8bc7-cd7a1fa38613",
        "creator_id": "eval-after-c3-t1-human-07",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.5745,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.5,
          "punctuation_density": 0.035343035343035345,
          "punctuation_simplicity": 0.7054747054747055,
          "repetition": 0.3790560471976401,
          "sentence_count": 2,
          "sentence_length_spread": 0.008849557522123894,
          "style_score": 0.5048,
          "type_token_ratio": 0.672566371681416,
          "word_count": 113
        },
        "style_score": 0.5048,
        "text_length": 592,
        "timestamp": "2026-11-08T21:53:16+00:00"
      },
      "elapsed_ms": 58.21,
      "input_id": "human-07",
      "input_provenance": {
        "id": "human-07",
        "text": "Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, \u201cand what is the use of a book,\u201d thought Alice \u201cwithout pictures or conversations?\u201d So she was considering in her own mind (as well as she could, for the hot day made her feel very sleepy and stupid), whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her.",
        "source_url": "https://www.gutenberg.org/cache/epub/11/pg11.txt",
        "author": "Lewis Carroll",
        "title": "Alice's Adventures in Wonderland",
        "publication_year": 1865,
        "location": "Chapter I, Down the Rabbit-Hole, first two paragraphs",
        "genre": "literary fiction",
        "provenance": "Exact public-domain excerpt from the Project Gutenberg edition of Carroll's published novel, verified against the linked primary text on 2026-10-30. Whitespace normalized."
      }
    },
    {
      "method": "POST",
      "url": "http://127.0.0.1:5054/submit",
      "request_json": {
        "text": "When on board H.M.S. \u2018Beagle,\u2019 as naturalist, I was much struck with certain facts in the distribution of the inhabitants of South America, and in the geological relations of the present to the past inhabitants of that continent. These facts seemed to me to throw some light on the origin of species\u2014that mystery of mysteries, as it has been called by one of our greatest philosophers. On my return home, it occurred to me, in 1837, that something might perhaps be made out on this question by patiently accumulating and reflecting on all sorts of facts which could possibly have any bearing on it.",
        "creator_id": "eval-after-c3-t1-human-08"
      },
      "status_code": 200,
      "content_type": "application/json",
      "response_json": {
        "combined_score": 0.5581,
        "confidence": 0.5581,
        "content_id": "919ded2e-f866-4a26-9e5a-5008d2dc6f88",
        "creator_id": "eval-after-c3-t1-human-08",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.5825,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.420697370644045,
          "punctuation_density": 0.03232323232323232,
          "punctuation_simplicity": 0.7306397306397306,
          "repetition": 0.3473520249221185,
          "sentence_count": 4,
          "sentence_length_spread": 0.46344210348476406,
          "style_score": 0.4607,
          "type_token_ratio": 0.6915887850467289,
          "word_count": 107
        },
        "style_score": 0.4607,
        "text_length": 598,
        "timestamp": "2026-11-08T21:53:16+00:00"
      },
      "elapsed_ms": 53.31,
      "input_id": "human-08",
      "input_provenance": {
        "id": "human-08",
        "text": "When on board H.M.S. \u2018Beagle,\u2019 as naturalist, I was much struck with certain facts in the distribution of the inhabitants of South America, and in the geological relations of the present to the past inhabitants of that continent. These facts seemed to me to throw some light on the origin of species\u2014that mystery of mysteries, as it has been called by one of our greatest philosophers. On my return home, it occurred to me, in 1837, that something might perhaps be made out on this question by patiently accumulating and reflecting on all sorts of facts which could possibly have any bearing on it.",
        "source_url": "https://www.gutenberg.org/cache/epub/1228/pg1228.txt",
        "author": "Charles Darwin",
        "title": "On the Origin of Species By Means of Natural Selection",
        "publication_year": 1859,
        "location": "Introduction, first three sentences",
        "genre": "formal scientific nonfiction",
        "provenance": "Exact public-domain excerpt from the Project Gutenberg edition of Darwin's published work, verified against the linked primary text on 2026-10-30. Whitespace normalized."
      }
    },
    {
      "method": "POST",
      "url": "http://127.0.0.1:5054/submit",
      "request_json": {
        "text": "The produce of industry is what it adds to the subject or materials upon which it is employed. In proportion as the value of this produce is great or small, so will likewise be the profits of the employer. But it is only for the sake of profit that any man employs a capital in the support of industry; and he will always, therefore, endeavour to employ it in the support of that industry of which the produce is likely to be of the greatest value, or to exchange for the greatest quantity either of money or of other goods.",
        "creator_id": "eval-after-c3-t1-human-09"
      },
      "status_code": 200,
      "content_type": "application/json",
      "response_json": {
        "combined_score": 0.7081,
        "confidence": 0.7081,
        "content_id": "8c5f5a11-3c7d-4201-95b8-6d6f4f436ebf",
        "creator_id": "eval-after-c3-t1-human-09",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.7648,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.26494047860054226,
          "punctuation_density": 0.018823529411764704,
          "punctuation_simplicity": 0.8431372549019608,
          "repetition": 0.6,
          "sentence_count": 3,
          "sentence_length_spread": 0.5880476171195662,
          "style_score": 0.4811,
          "type_token_ratio": 0.54,
          "word_count": 100
        },
        "style_score": 0.4811,
        "text_length": 524,
        "timestamp": "2026-11-08T21:53:16+00:00"
      },
      "elapsed_ms": 49.56,
      "input_id": "human-09",
      "input_provenance": {
        "id": "human-09",
        "text": "The produce of industry is what it adds to the subject or materials upon which it is employed. In proportion as the value of this produce is great or small, so will likewise be the profits of the employer. But it is only for the sake of profit that any man employs a capital in the support of industry; and he will always, therefore, endeavour to employ it in the support of that industry of which the produce is likely to be of the greatest value, or to exchange for the greatest quantity either of money or of other goods.",
        "source_url": "https://www.gutenberg.org/cache/epub/3300/pg3300.txt",
        "author": "Adam Smith",
        "title": "An Inquiry into the Nature and Causes of the Wealth of Nations",
        "publication_year": 1776,
        "location": "Book IV, Chapter II, paragraph beginning 'The produce of industry'",
        "genre": "formal economic nonfiction",
        "provenance": "Exact public-domain excerpt from the Project Gutenberg edition of Smith's published work, verified against the linked primary text on 2026-10-30. Whitespace normalized."
      }
    },
    {
      "method": "POST",
      "url": "http://127.0.0.1:5054/submit",
      "request_json": {
        "text": "My elder brothers were all put apprentices to different trades. I was put to the grammar-school at eight years of age, my father intending to devote me, as the tithe[13] of his sons, to the service of the Church. My early readiness in learning to read (which must have been very early, as I do not remember when I could not read), and the opinion of all his friends, that I should certainly make a good scholar, encouraged him in this purpose of his. My uncle Benjamin, too, approved of it, and proposed to give me all his short-hand volumes of sermons, I suppose as a stock to set up with, if I would learn his character.[14]",
        "creator_id": "eval-after-c3-t1-human-10"
      },
      "status_code": 200,
      "content_type": "application/json",
      "response_json": {
        "combined_score": 0.5475,
        "confidence": 0.5475,
        "content_id": "4fc47716-5217-4173-9f39-c3e85e55d9fb",
        "creator_id": "eval-after-c3-t1-human-10",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.566,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.4729379744287563,
          "punctuation_density": 0.047058823529411764,
          "punctuation_simplicity": 0.607843137254902,
          "repetition": 0.3842975206611571,
          "sentence_count": 4,
          "sentence_length_spread": 0.421649620456995,
          "style_score": 0.4733,
          "type_token_ratio": 0.6694214876033058,
          "word_count": 121
        },
        "style_score": 0.4733,
        "text_length": 626,
        "timestamp": "2026-11-08T21:53:16+00:00"
      },
      "elapsed_ms": 60.93,
      "input_id": "human-10",
      "input_provenance": {
        "id": "human-10",
        "text": "My elder brothers were all put apprentices to different trades. I was put to the grammar-school at eight years of age, my father intending to devote me, as the tithe[13] of his sons, to the service of the Church. My early readiness in learning to read (which must have been very early, as I do not remember when I could not read), and the opinion of all his friends, that I should certainly make a good scholar, encouraged him in this purpose of his. My uncle Benjamin, too, approved of it, and proposed to give me all his short-hand volumes of sermons, I suppose as a stock to set up with, if I would learn his character.[14]",
        "source_url": "https://www.gutenberg.org/cache/epub/20203/pg20203.txt",
        "author": "Benjamin Franklin",
        "title": "Autobiography of Benjamin Franklin",
        "publication_year": 1791,
        "location": "Passage beginning 'My elder brothers were all put apprentices', first four sentences",
        "genre": "first-person autobiographical nonfiction",
        "provenance": "Exact public-domain excerpt from the Project Gutenberg transcription of the 1916 English edition (1922 printing), verified against the linked primary text on 2026-10-30. The memoir was composed in 1771\u20131790 and initially published in French in 1791. The linked edition states that its text follows Bigelow's nineteenth-century editions. Edition footnote markers retained; whitespace normalized."
      }
    },
    {
      "method": "POST",
      "url": "http://127.0.0.1:5054/submit",
      "request_json": {
        "text": "Effective communication is essential for building a productive and collaborative workplace. By establishing clear expectations and encouraging open dialogue, organizations can ensure that every team member understands their responsibilities. Regular feedback helps employees identify opportunities for improvement while reinforcing successful habits. In addition, consistent documentation allows important information to remain accessible as projects evolve. Managers should create an environment where questions are welcomed and different perspectives are respected. This approach supports accountability, reduces misunderstandings, and strengthens trust across departments. Ultimately, investing in thoughtful communication practices enables teams to work more efficiently and achieve sustainable results together.",
        "creator_id": "eval-after-c3-t1-ai-01"
      },
      "status_code": 200,
      "content_type": "application/json",
      "response_json": {
        "combined_score": 0.6086,
        "confidence": 0.6086,
        "content_id": "5eaa9ba5-cee6-43ed-b43d-5bd55a58242e",
        "creator_id": "eval-after-c3-t1-ai-01",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.6223,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.7627491255431172,
          "punctuation_density": 0.016643550624133148,
          "punctuation_simplicity": 0.8613037447988905,
          "repetition": 0.0,
          "sentence_count": 7,
          "sentence_length_spread": 0.18980069956550624,
          "style_score": 0.5536,
          "type_token_ratio": 0.90625,
          "word_count": 96
        },
        "style_score": 0.5536,
        "text_length": 816,
        "timestamp": "2026-11-08T21:53:16+00:00"
      },
      "elapsed_ms": 49.47,
      "input_id": "ai-01",
      "input_provenance": {
        "id": "ai-01",
        "text": "Effective communication is essential for building a productive and collaborative workplace. By establishing clear expectations and encouraging open dialogue, organizations can ensure that every team member understands their responsibilities. Regular feedback helps employees identify opportunities for improvement while reinforcing successful habits. In addition, consistent documentation allows important information to remain accessible as projects evolve. Managers should create an environment where questions are welcomed and different perspectives are respected. This approach supports accountability, reduces misunderstandings, and strengthens trust across departments. Ultimately, investing in thoughtful communication practices enables teams to work more efficiently and achieve sustainable results together.",
        "origin": "AI-generated by Codex for development",
        "provenance": "Generated before detector evaluation on 2026-10-30. Original synthetic workplace advice; not independently human-authored or copied from a source.",
        "generation_prompt": "Write a polished, approximately 100-word paragraph of ordinary workplace communication advice."
      }
    },
    {
      "method": "POST",
      "url": "http://127.0.0.1:5054/submit",
      "request_json": {
        "text": "A successful morning routine begins with a clear and achievable plan. Start by choosing a consistent time to wake up each day. Next, drink a glass of water and prepare a simple breakfast. Set aside a few minutes to review your most important tasks. Keep your workspace organized so that necessary materials are easy to find. Limit unnecessary notifications during periods that require your full attention. Take short breaks to maintain focus and prevent mental fatigue. Review your progress at the end of each working session. Small, consistent improvements can make daily responsibilities easier to manage over time.",
        "creator_id": "eval-after-c3-t1-ai-02"
      },
      "status_code": 200,
      "content_type": "application/json",
      "response_json": {
        "combined_score": 0.6668,
        "confidence": 0.6668,
        "content_id": "e149cc35-47c2-408c-bfc7-c0426f67f953",
        "creator_id": "eval-after-c3-t1-ai-02",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.6649,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.9153922247358316,
          "punctuation_density": 0.021153846153846155,
          "punctuation_simplicity": 0.8237179487179487,
          "repetition": 0.1734693877551021,
          "sentence_count": 9,
          "sentence_length_spread": 0.06768622021133469,
          "style_score": 0.6745,
          "type_token_ratio": 0.7959183673469388,
          "word_count": 98
        },
        "style_score": 0.6745,
        "text_length": 617,
        "timestamp": "2026-11-08T21:53:16+00:00"
      },
      "elapsed_ms": 49.68,
      "input_id": "ai-02",
      "input_provenance": {
        "id": "ai-02",
        "text": "A successful morning routine begins with a clear and achievable plan. Start by choosing a consistent time to wake up each day. Next, drink a glass of water and prepare a simple breakfast. Set aside a few minutes to review your most important tasks. Keep your workspace organized so that necessary materials are easy to find. Limit unnecessary notifications during periods that require your full attention. Take short breaks to maintain focus and prevent mental fatigue. Review your progress at the end of each working session. Small, consistent improvements can make daily responsibilities easier to manage over time.",
        "origin": "AI-generated by Codex for development",
        "provenance": "Generated before detector evaluation on 2026-10-30. Original synthetic routine advice with deliberately regular sentence structure.",
        "generation_prompt": "Write approximately 100 words of routine advice using plain sentences of fairly consistent length."
      }
    },
    {
      "method": "POST",
      "url": "http://127.0.0.1:5054/submit",
      "request_json": {
        "text": "The team reviews the project plan before starting each task. The team checks the project goals before starting each task. The team shares the project notes before starting each task. The team updates the project schedule before starting each task. The team reviews the project budget before starting each task. The team checks the project records before starting each task. The team shares the project results before starting each task. The team updates the project report before starting each task.",
        "creator_id": "eval-after-c3-t1-ai-03"
      },
      "status_code": 200,
      "content_type": "application/json",
      "response_json": {
        "combined_score": 0.9615,
        "confidence": 0.9615,
        "content_id": "f167d99a-0947-4e6c-971a-4ee08b060f1b",
        "creator_id": "eval-after-c3-t1-ai-03",
        "detector_model": "gpt2",
        "guess": "ai",
        "label": "This writing shows patterns often found in AI-generated text. This estimate can be wrong and is not proof of AI use. You can request a review.",
        "model_score": 0.9598,
        "status": "decided",
        "style_metrics": {
          "evenness": 1.0,
          "punctuation_density": 0.01904761904761905,
          "punctuation_simplicity": 0.8412698412698413,
          "repetition": 1.0,
          "sentence_count": 8,
          "sentence_length_spread": 0.0,
          "style_score": 0.9683,
          "type_token_ratio": 0.2375,
          "word_count": 80
        },
        "style_score": 0.9683,
        "text_length": 499,
        "timestamp": "2026-11-08T21:53:16+00:00"
      },
      "elapsed_ms": 43.71,
      "input_id": "ai-03",
      "input_provenance": {
        "id": "ai-03",
        "text": "The team reviews the project plan before starting each task. The team checks the project goals before starting each task. The team shares the project notes before starting each task. The team updates the project schedule before starting each task. The team reviews the project budget before starting each task. The team checks the project records before starting each task. The team shares the project results before starting each task. The team updates the project report before starting each task.",
        "origin": "AI-generated by Codex for development",
        "provenance": "Generated before detector evaluation on 2026-10-30. Deliberately repetitive synthetic prose for exercising the stylometry signal; not representative of typical AI writing.",
        "generation_prompt": "Write eight ordinary project-management sentences with the same grammatical pattern and closely matched length."
      }
    },
    {
      "method": "POST",
      "url": "http://127.0.0.1:5054/submit",
      "request_json": {
        "text": "Rain gardens provide a practical way to manage stormwater while supporting healthy urban environments. These shallow planted areas collect runoff from roofs, sidewalks, and driveways, allowing water to soak gradually into the ground. Native plants help stabilize the soil and provide food and shelter for local wildlife. Because rain gardens slow the movement of water, they can also reduce the amount of sediment reaching nearby streams. Successful installation requires attention to drainage, soil conditions, and the distance from building foundations. With appropriate planning and routine maintenance, a rain garden can become an attractive and useful feature of a neighborhood.",
        "creator_id": "eval-after-c3-t1-ai-04"
      },
      "status_code": 200,
      "content_type": "application/json",
      "response_json": {
        "combined_score": 0.6834,
        "confidence": 0.6834,
        "content_id": "ec4d32b3-9556-41bd-97ee-62e8e16dff73",
        "creator_id": "eval-after-c3-t1-ai-04",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.6956,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.8106060606060606,
          "punctuation_density": 0.022222222222222223,
          "punctuation_simplicity": 0.8148148148148148,
          "repetition": 0.22053872053872067,
          "sentence_count": 6,
          "sentence_length_spread": 0.15151515151515152,
          "style_score": 0.6344,
          "type_token_ratio": 0.7676767676767676,
          "word_count": 99
        },
        "style_score": 0.6344,
        "text_length": 683,
        "timestamp": "2026-11-08T21:53:17+00:00"
      },
      "elapsed_ms": 52.09,
      "input_id": "ai-04",
      "input_provenance": {
        "id": "ai-04",
        "text": "Rain gardens provide a practical way to manage stormwater while supporting healthy urban environments. These shallow planted areas collect runoff from roofs, sidewalks, and driveways, allowing water to soak gradually into the ground. Native plants help stabilize the soil and provide food and shelter for local wildlife. Because rain gardens slow the movement of water, they can also reduce the amount of sediment reaching nearby streams. Successful installation requires attention to drainage, soil conditions, and the distance from building foundations. With appropriate planning and routine maintenance, a rain garden can become an attractive and useful feature of a neighborhood.",
        "origin": "AI-generated by Codex for development",
        "provenance": "Generated before detector evaluation on 2026-10-30. Original synthetic general explainer; not a sourced human passage.",
        "generation_prompt": "Write an approximately 100-word informational paragraph explaining rain gardens in a polished general-audience style."
      }
    },
    {
      "method": "POST",
      "url": "http://127.0.0.1:5054/submit",
      "request_json": {
        "text": "The produce of industry is what it adds to the subject or materials upon which it is employed. In proportion as the value of this produce is great or small, so will likewise be the profits of the employer. But it is only for the sake of profit that any man employs a capital in the support of industry; and he will always, therefore, endeavour to employ it in the support of that industry of which the produce is likely to be of the greatest value, or to exchange for the greatest quantity either of money or of other goods.",
        "creator_id": "eval-after-c3-t1-calibration-formal-human"
      },
      "status_code": 200,
      "content_type": "application/json",
      "response_json": {
        "combined_score": 0.7081,
        "confidence": 0.7081,
        "content_id": "a6f49e36-75d2-4aab-bc76-cab15e5337ed",
        "creator_id": "eval-after-c3-t1-calibration-formal-human",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.7648,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.26494047860054226,
          "punctuation_density": 0.018823529411764704,
          "punctuation_simplicity": 0.8431372549019608,
          "repetition": 0.6,
          "sentence_count": 3,
          "sentence_length_spread": 0.5880476171195662,
          "style_score": 0.4811,
          "type_token_ratio": 0.54,
          "word_count": 100
        },
        "style_score": 0.4811,
        "text_length": 524,
        "timestamp": "2026-11-08T21:53:17+00:00"
      },
      "elapsed_ms": 49.2,
      "input_id": "calibration-formal-human",
      "input_provenance": {
        "id": "calibration-formal-human",
        "role": "formal human writing",
        "reference_id": "human-09",
        "text": "The produce of industry is what it adds to the subject or materials upon which it is employed. In proportion as the value of this produce is great or small, so will likewise be the profits of the employer. But it is only for the sake of profit that any man employs a capital in the support of industry; and he will always, therefore, endeavour to employ it in the support of that industry of which the produce is likely to be of the greatest value, or to exchange for the greatest quantity either of money or of other goods.",
        "source_url": "https://www.gutenberg.org/cache/epub/3300/pg3300.txt",
        "author": "Adam Smith",
        "title": "An Inquiry into the Nature and Causes of the Wealth of Nations",
        "publication_year": 1776,
        "provenance": "Same sourced passage as human-09, reused to make the formal-human demonstration explicit. Excluded from metric group counts."
      }
    },
    {
      "method": "POST",
      "url": "http://127.0.0.1:5054/submit",
      "request_json": {
        "text": "Effective communication is essential for building a productive and collaborative workplace. By establishing clear expectations and encouraging open dialogue, organizations can ensure that every team member understands their responsibilities. Regular feedback helps employees identify opportunities for improvement while reinforcing successful habits. In addition, consistent documentation allows important information to remain accessible as projects evolve. Managers should create an environment where questions are welcomed and different perspectives are respected. This approach supports accountability, reduces misunderstandings, and strengthens trust across departments. Ultimately, investing in thoughtful communication practices enables teams to work more efficiently and achieve sustainable results together.",
        "creator_id": "eval-after-c3-t1-calibration-original-ai"
      },
      "status_code": 200,
      "content_type": "application/json",
      "response_json": {
        "combined_score": 0.6086,
        "confidence": 0.6086,
        "content_id": "a810e80f-2885-48cb-ae55-b03092975027",
        "creator_id": "eval-after-c3-t1-calibration-original-ai",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.6223,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.7627491255431172,
          "punctuation_density": 0.016643550624133148,
          "punctuation_simplicity": 0.8613037447988905,
          "repetition": 0.0,
          "sentence_count": 7,
          "sentence_length_spread": 0.18980069956550624,
          "style_score": 0.5536,
          "type_token_ratio": 0.90625,
          "word_count": 96
        },
        "style_score": 0.5536,
        "text_length": 816,
        "timestamp": "2026-11-08T21:53:17+00:00"
      },
      "elapsed_ms": 49.81,
      "input_id": "calibration-original-ai",
      "input_provenance": {
        "id": "calibration-original-ai",
        "role": "original AI writing",
        "reference_id": "ai-01",
        "text": "Effective communication is essential for building a productive and collaborative workplace. By establishing clear expectations and encouraging open dialogue, organizations can ensure that every team member understands their responsibilities. Regular feedback helps employees identify opportunities for improvement while reinforcing successful habits. In addition, consistent documentation allows important information to remain accessible as projects evolve. Managers should create an environment where questions are welcomed and different perspectives are respected. This approach supports accountability, reduces misunderstandings, and strengthens trust across departments. Ultimately, investing in thoughtful communication practices enables teams to work more efficiently and achieve sustainable results together.",
        "origin": "AI-generated by Codex for development",
        "provenance": "Same generated passage as ai-01. Excluded from metric group counts."
      }
    },
    {
      "method": "POST",
      "url": "http://127.0.0.1:5054/submit",
      "request_json": {
        "text": "Clear communication makes it easier for a team to get useful work done. By establishing clear expectations and encouraging open dialogue, organizations can ensure that every team member understands their responsibilities. Regular feedback helps employees identify opportunities for improvement while reinforcing successful habits. In addition, consistent documentation allows important information to remain accessible as projects evolve. Managers should create an environment where questions are welcomed and different perspectives are respected. This approach supports accountability, reduces misunderstandings, and strengthens trust across departments. For a small team, a short written update can be a good place to start.",
        "creator_id": "eval-after-c3-t1-calibration-edited-ai"
      },
      "status_code": 200,
      "content_type": "application/json",
      "response_json": {
        "combined_score": 0.6225,
        "confidence": 0.6225,
        "content_id": "acbe1b0f-8c08-46cf-962f-6c863354341a",
        "creator_id": "eval-after-c3-t1-calibration-edited-ai",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.6295,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.8068698310652171,
          "punctuation_density": 0.01901743264659271,
          "punctuation_simplicity": 0.8415213946117274,
          "repetition": 0.07638888888888899,
          "sentence_count": 7,
          "sentence_length_spread": 0.15450413514782632,
          "style_score": 0.5947,
          "type_token_ratio": 0.8541666666666666,
          "word_count": 96
        },
        "style_score": 0.5947,
        "text_length": 726,
        "timestamp": "2026-11-08T21:53:17+00:00"
      },
      "elapsed_ms": 49.63,
      "input_id": "calibration-edited-ai",
      "input_provenance": {
        "id": "calibration-edited-ai",
        "role": "lightly edited AI writing",
        "reference_id": "ai-01",
        "text": "Clear communication makes it easier for a team to get useful work done. By establishing clear expectations and encouraging open dialogue, organizations can ensure that every team member understands their responsibilities. Regular feedback helps employees identify opportunities for improvement while reinforcing successful habits. In addition, consistent documentation allows important information to remain accessible as projects evolve. Managers should create an environment where questions are welcomed and different perspectives are respected. This approach supports accountability, reduces misunderstandings, and strengthens trust across departments. For a small team, a short written update can be a good place to start.",
        "origin": "AI-generated by Codex for development; first and last sentences subsequently rewritten by Codex",
        "provenance": "A lightly edited version of ai-01 created before evaluation. Both generation and edits were AI-produced; this is not a human-edited AI sample. Excluded from metric group counts."
      }
    },
    {
      "method": "POST",
      "url": "http://127.0.0.1:5054/submit",
      "request_json": {
        "text": "The meeting starts at nine tomorrow. Please bring the latest notes and leave a little time for questions. We can decide the next steps after everyone has had a chance to speak.",
        "creator_id": "eval-after-c3-t1-calibration-short-uncertain"
      },
      "status_code": 200,
      "content_type": "application/json",
      "response_json": {
        "combined_score": 0.4621,
        "confidence": 0.4621,
        "content_id": "93074c33-b7dd-4668-9b15-693f07410f8e",
        "creator_id": "eval-after-c3-t1-calibration-short-uncertain",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.461,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.6016391005005637,
          "punctuation_density": 0.020689655172413793,
          "punctuation_simplicity": 0.8275862068965517,
          "repetition": 0.0,
          "sentence_count": 3,
          "sentence_length_spread": 0.3186887195995491,
          "style_score": 0.4663,
          "type_token_ratio": 0.90625,
          "word_count": 32
        },
        "style_score": 0.4663,
        "text_length": 176,
        "timestamp": "2026-11-08T21:53:17+00:00"
      },
      "elapsed_ms": 29.82,
      "input_id": "calibration-short-uncertain",
      "input_provenance": {
        "id": "calibration-short-uncertain",
        "role": "short ambiguous demonstration candidate",
        "text": "The meeting starts at nine tomorrow. Please bring the latest notes and leave a little time for questions. We can decide the next steps after everyone has had a chance to speak.",
        "origin": "AI-generated by Codex for development",
        "provenance": "Short ordinary prose generated before evaluation as a candidate for demonstrating uncertainty. Its role does not assert a detector result or human authorship. Excluded from metric group counts."
      }
    },
    {
      "method": "POST",
      "url": "http://127.0.0.1:5054/submit",
      "request_json": {
        "text": "\u2019Twas brillig, and the slithy toves\n    Did gyre and gimble in the wabe;\nAll mimsy were the borogoves,\n    And the mome raths outgrabe.\n\u201cBeware the Jabberwock, my son!\n    The jaws that bite, the claws that catch!\nBeware the Jubjub bird, and shun\n    The frumious Bandersnatch!\u201d\nHe took his vorpal sword in hand:\n    Long time the manxome foe he sought\u2014\nSo rested he by the Tumtum tree,\n    And stood awhile in thought.\nAnd as in uffish thought he stood,\n    The Jabberwock, with eyes of flame,\nCame whiffling through the tulgey wood,\n    And burbled as it came!\nOne, two! One, two! And through and through\n    The vorpal blade went snicker-snack!\nHe left it dead, and with its head\n    He went galumphing back.\n\u201cAnd hast thou slain the Jabberwock?\n    Come to my arms, my beamish boy!\nO frabjous day! Callooh! Callay!\u201d\n    He chortled in his joy.\n\u2019Twas brillig, and the slithy toves\n    Did gyre and gimble in the wabe;\nAll mimsy were the borogoves,\n    And the mome raths outgrabe.",
        "creator_id": "eval-after-c3-t1-label-demo-jabberwocky"
      },
      "status_code": 200,
      "content_type": "application/json",
      "response_json": {
        "combined_score": 0.5472,
        "confidence": 0.5472,
        "content_id": "622ce8ed-ba77-4f04-8a0e-c10429421492",
        "creator_id": "eval-after-c3-t1-label-demo-jabberwocky",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.6137,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.0,
          "punctuation_density": 0.05774278215223097,
          "punctuation_simplicity": 0.5188101487314085,
          "repetition": 0.5918163672654692,
          "sentence_count": 17,
          "sentence_length_spread": 0.8596934062200292,
          "style_score": 0.2813,
          "type_token_ratio": 0.5449101796407185,
          "word_count": 167
        },
        "style_score": 0.2813,
        "text_length": 983,
        "timestamp": "2026-11-08T21:53:17+00:00"
      },
      "elapsed_ms": 141.07,
      "input_id": "label-demo-jabberwocky",
      "input_provenance": {
        "id": "label-demo-jabberwocky",
        "text": "\u2019Twas brillig, and the slithy toves\n    Did gyre and gimble in the wabe;\nAll mimsy were the borogoves,\n    And the mome raths outgrabe.\n\u201cBeware the Jabberwock, my son!\n    The jaws that bite, the claws that catch!\nBeware the Jubjub bird, and shun\n    The frumious Bandersnatch!\u201d\nHe took his vorpal sword in hand:\n    Long time the manxome foe he sought\u2014\nSo rested he by the Tumtum tree,\n    And stood awhile in thought.\nAnd as in uffish thought he stood,\n    The Jabberwock, with eyes of flame,\nCame whiffling through the tulgey wood,\n    And burbled as it came!\nOne, two! One, two! And through and through\n    The vorpal blade went snicker-snack!\nHe left it dead, and with its head\n    He went galumphing back.\n\u201cAnd hast thou slain the Jabberwock?\n    Come to my arms, my beamish boy!\nO frabjous day! Callooh! Callay!\u201d\n    He chortled in his joy.\n\u2019Twas brillig, and the slithy toves\n    Did gyre and gimble in the wabe;\nAll mimsy were the borogoves,\n    And the mome raths outgrabe.",
        "author": "Lewis Carroll",
        "title": "Jabberwocky, Through the Looking-Glass",
        "publication_year": 1871,
        "source_url": "https://www.gutenberg.org/cache/epub/12/pg12-images.html",
        "provenance": "Sourced human-written public-domain poem. Selected after the initial fixed-corpus evaluation to demonstrate label reachability; excluded from false-positive and median-gap groups."
      }
    },
    {
      "method": "POST",
      "url": "http://127.0.0.1:5054/submit",
      "request_json": {
        "text": "Clank! Tessellated moonwort crumpled beneath Inez's vermilion galoshes; meanwhile, a xylophagous cartographer annotated the cistern's palimpsest with persimmon ink, cataloguing quincunxes, antimony flecks, frosted fulcra, and a thoroughly uncooperative aardvark named Sprocket, whose left whisker twitched whenever the barometer hiccupped. Why? Upstairs, zephyrs rattled through a cabinet of mislabelled astrolabes\u2014each drawer exhaled bergamot, each latch muttered differently, and somewhere behind the wainscot a velvet-furred mechanic counted backwards in an extinct dialect. Hush.",
        "creator_id": "eval-after-c3-t1-label-demo-synthetic-rare-prose"
      },
      "status_code": 200,
      "content_type": "application/json",
      "response_json": {
        "combined_score": 0.1628,
        "confidence": 0.1628,
        "content_id": "dc6ef482-3c40-4f08-9def-f5888a930ece",
        "creator_id": "eval-after-c3-t1-label-demo-synthetic-rare-prose",
        "detector_model": "gpt2",
        "guess": "human",
        "label": "This writing looks more consistent with human writing. This estimate does not verify who wrote it.",
        "model_score": 0.169,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.0,
          "punctuation_density": 0.037109375,
          "punctuation_simplicity": 0.6907552083333333,
          "repetition": 0.0,
          "sentence_count": 5,
          "sentence_length_spread": 1.151744635279055,
          "style_score": 0.1382,
          "type_token_ratio": 0.9054054054054054,
          "word_count": 74
        },
        "style_score": 0.1382,
        "text_length": 583,
        "timestamp": "2026-11-08T21:53:17+00:00"
      },
      "elapsed_ms": 64.39,
      "input_id": "label-demo-synthetic-rare-prose",
      "input_provenance": {
        "id": "label-demo-synthetic-rare-prose",
        "text": "Clank! Tessellated moonwort crumpled beneath Inez's vermilion galoshes; meanwhile, a xylophagous cartographer annotated the cistern's palimpsest with persimmon ink, cataloguing quincunxes, antimony flecks, frosted fulcra, and a thoroughly uncooperative aardvark named Sprocket, whose left whisker twitched whenever the barometer hiccupped. Why? Upstairs, zephyrs rattled through a cabinet of mislabelled astrolabes\u2014each drawer exhaled bergamot, each latch muttered differently, and somewhere behind the wainscot a velvet-furred mechanic counted backwards in an extinct dialect. Hush.",
        "origin": "AI-generated by Codex for a label-reachability stress demonstration",
        "provenance": "Deliberately uncommon vocabulary, varied sentence lengths, and punctuation. Generated after initial results; excluded from all false-positive and separation metric groups. A human label on this AI-generated fixture is an evasion example, not a correct authorship decision."
      }
    }
  ],
  "actual_labels": [
    "ai",
    "human",
    "unsure"
  ],
  "score_sweep": {
    "scores_checked": 10001,
    "counts": {
      "human": 2501,
      "unsure": 5499,
      "ai": 2001
    },
    "boundary_guesses": {
      "0.0": "human",
      "0.25": "human",
      "0.2501": "unsure",
      "0.51": "unsure",
      "0.7999": "unsure",
      "0.8": "ai",
      "0.95": "ai",
      "1.0": "ai"
    },
    "failures": [],
    "passed": true
  },
  "summary": "3/3 labels; 10001 scores",
  "passed": true,
  "verdict": "MET"
}
```

### Criterion 4

Produced by `run_eval.py::trial_result` (appeals).

```json
{
  "trial": 1,
  "criterion": 4,
  "kind": "appeals",
  "cases": [
    {
      "content_id": "57f55524-8978-43d5-bc0b-e1396115c1d2",
      "original": {
        "combined_score": 0.6593,
        "confidence": 0.6593,
        "content_id": "57f55524-8978-43d5-bc0b-e1396115c1d2",
        "creator_id": "eval-after-c4-t1-human-01",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.6922,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.5,
          "punctuation_density": 0.016286644951140065,
          "punctuation_simplicity": 0.8642779587404994,
          "repetition": 0.34976525821596255,
          "sentence_count": 2,
          "sentence_length_spread": 0.352112676056338,
          "style_score": 0.5278,
          "type_token_ratio": 0.6901408450704225,
          "word_count": 71
        },
        "style_score": 0.5278,
        "text_length": 377,
        "timestamp": "2026-11-08T21:53:17+00:00"
      },
      "appeal": {
        "method": "POST",
        "url": "http://127.0.0.1:5054/appeal",
        "request_json": {
          "content_id": "57f55524-8978-43d5-bc0b-e1396115c1d2",
          "reasoning": "Part 2 criterion review after, trial 1: please inspect this estimate."
        },
        "status_code": 200,
        "content_type": "application/json",
        "response_json": {
          "content_id": "57f55524-8978-43d5-bc0b-e1396115c1d2",
          "creator_id": "eval-after-c4-t1-human-01",
          "event": "appeal",
          "message": "Your appeal has been recorded. This writing is now under review.",
          "reasoning": "Part 2 criterion review after, trial 1: please inspect this estimate.",
          "status": "under_review",
          "timestamp": "2026-11-08T21:53:17+00:00"
        },
        "elapsed_ms": 3.96
      },
      "current": {
        "method": "GET",
        "url": "http://127.0.0.1:5054/content/57f55524-8978-43d5-bc0b-e1396115c1d2",
        "status_code": 200,
        "content_type": "application/json",
        "response_json": {
          "appeals": [
            {
              "content_id": "57f55524-8978-43d5-bc0b-e1396115c1d2",
              "creator_id": "eval-after-c4-t1-human-01",
              "event": "appeal",
              "reasoning": "Part 2 criterion review after, trial 1: please inspect this estimate.",
              "status": "under_review",
              "timestamp": "2026-11-08T21:53:17+00:00"
            }
          ],
          "combined_score": 0.6593,
          "confidence": 0.6593,
          "content_id": "57f55524-8978-43d5-bc0b-e1396115c1d2",
          "creator_id": "eval-after-c4-t1-human-01",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.6922,
          "status": "under_review",
          "style_metrics": {
            "evenness": 0.5,
            "punctuation_density": 0.016286644951140065,
            "punctuation_simplicity": 0.8642779587404994,
            "repetition": 0.34976525821596255,
            "sentence_count": 2,
            "sentence_length_spread": 0.352112676056338,
            "style_score": 0.5278,
            "type_token_ratio": 0.6901408450704225,
            "word_count": 71
          },
          "style_score": 0.5278,
          "text_length": 377,
          "timestamp": "2026-11-08T21:53:17+00:00"
        },
        "elapsed_ms": 3.15
      },
      "passed": true,
      "history": [
        {
          "combined_score": 0.6593,
          "confidence": 0.6593,
          "content_id": "57f55524-8978-43d5-bc0b-e1396115c1d2",
          "creator_id": "eval-after-c4-t1-human-01",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.6922,
          "status": "decided",
          "style_metrics": {
            "evenness": 0.5,
            "punctuation_density": 0.016286644951140065,
            "punctuation_simplicity": 0.8642779587404994,
            "repetition": 0.34976525821596255,
            "sentence_count": 2,
            "sentence_length_spread": 0.352112676056338,
            "style_score": 0.5278,
            "type_token_ratio": 0.6901408450704225,
            "word_count": 71
          },
          "style_score": 0.5278,
          "text_length": 377,
          "timestamp": "2026-11-08T21:53:17+00:00"
        },
        {
          "content_id": "57f55524-8978-43d5-bc0b-e1396115c1d2",
          "creator_id": "eval-after-c4-t1-human-01",
          "event": "appeal",
          "reasoning": "Part 2 criterion review after, trial 1: please inspect this estimate.",
          "status": "under_review",
          "timestamp": "2026-11-08T21:53:17+00:00"
        }
      ]
    },
    {
      "content_id": "b7e898ca-5f47-4dd8-8892-45b55232cc1b",
      "original": {
        "combined_score": 0.4608,
        "confidence": 0.4608,
        "content_id": "b7e898ca-5f47-4dd8-8892-45b55232cc1b",
        "creator_id": "eval-after-c4-t1-human-02",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.4863,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.2554540936099331,
          "punctuation_density": 0.04021937842778794,
          "punctuation_simplicity": 0.6648385131017671,
          "repetition": 0.3276836158192091,
          "sentence_count": 4,
          "sentence_length_spread": 0.5956367251120536,
          "style_score": 0.359,
          "type_token_ratio": 0.7033898305084746,
          "word_count": 118
        },
        "style_score": 0.359,
        "text_length": 664,
        "timestamp": "2026-11-08T21:53:17+00:00"
      },
      "appeal": {
        "method": "POST",
        "url": "http://127.0.0.1:5054/appeal",
        "request_json": {
          "content_id": "b7e898ca-5f47-4dd8-8892-45b55232cc1b",
          "reasoning": "Part 2 criterion review after, trial 1: please inspect this estimate."
        },
        "status_code": 200,
        "content_type": "application/json",
        "response_json": {
          "content_id": "b7e898ca-5f47-4dd8-8892-45b55232cc1b",
          "creator_id": "eval-after-c4-t1-human-02",
          "event": "appeal",
          "message": "Your appeal has been recorded. This writing is now under review.",
          "reasoning": "Part 2 criterion review after, trial 1: please inspect this estimate.",
          "status": "under_review",
          "timestamp": "2026-11-08T21:53:17+00:00"
        },
        "elapsed_ms": 3.02
      },
      "current": {
        "method": "GET",
        "url": "http://127.0.0.1:5054/content/b7e898ca-5f47-4dd8-8892-45b55232cc1b",
        "status_code": 200,
        "content_type": "application/json",
        "response_json": {
          "appeals": [
            {
              "content_id": "b7e898ca-5f47-4dd8-8892-45b55232cc1b",
              "creator_id": "eval-after-c4-t1-human-02",
              "event": "appeal",
              "reasoning": "Part 2 criterion review after, trial 1: please inspect this estimate.",
              "status": "under_review",
              "timestamp": "2026-11-08T21:53:17+00:00"
            }
          ],
          "combined_score": 0.4608,
          "confidence": 0.4608,
          "content_id": "b7e898ca-5f47-4dd8-8892-45b55232cc1b",
          "creator_id": "eval-after-c4-t1-human-02",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.4863,
          "status": "under_review",
          "style_metrics": {
            "evenness": 0.2554540936099331,
            "punctuation_density": 0.04021937842778794,
            "punctuation_simplicity": 0.6648385131017671,
            "repetition": 0.3276836158192091,
            "sentence_count": 4,
            "sentence_length_spread": 0.5956367251120536,
            "style_score": 0.359,
            "type_token_ratio": 0.7033898305084746,
            "word_count": 118
          },
          "style_score": 0.359,
          "text_length": 664,
          "timestamp": "2026-11-08T21:53:17+00:00"
        },
        "elapsed_ms": 2.88
      },
      "passed": true,
      "history": [
        {
          "combined_score": 0.4608,
          "confidence": 0.4608,
          "content_id": "b7e898ca-5f47-4dd8-8892-45b55232cc1b",
          "creator_id": "eval-after-c4-t1-human-02",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.4863,
          "status": "decided",
          "style_metrics": {
            "evenness": 0.2554540936099331,
            "punctuation_density": 0.04021937842778794,
            "punctuation_simplicity": 0.6648385131017671,
            "repetition": 0.3276836158192091,
            "sentence_count": 4,
            "sentence_length_spread": 0.5956367251120536,
            "style_score": 0.359,
            "type_token_ratio": 0.7033898305084746,
            "word_count": 118
          },
          "style_score": 0.359,
          "text_length": 664,
          "timestamp": "2026-11-08T21:53:17+00:00"
        },
        {
          "content_id": "b7e898ca-5f47-4dd8-8892-45b55232cc1b",
          "creator_id": "eval-after-c4-t1-human-02",
          "event": "appeal",
          "reasoning": "Part 2 criterion review after, trial 1: please inspect this estimate.",
          "status": "under_review",
          "timestamp": "2026-11-08T21:53:17+00:00"
        }
      ]
    },
    {
      "content_id": "f6b5b60c-af1a-48a6-87c2-ee3a86448830",
      "original": {
        "combined_score": 0.3358,
        "confidence": 0.3358,
        "content_id": "f6b5b60c-af1a-48a6-87c2-ee3a86448830",
        "creator_id": "eval-after-c4-t1-human-03",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.3532,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.0,
          "punctuation_density": 0.027522935779816515,
          "punctuation_simplicity": 0.7706422018348624,
          "repetition": 0.37356321839080464,
          "sentence_count": 4,
          "sentence_length_spread": 0.8882105351861661,
          "style_score": 0.2662,
          "type_token_ratio": 0.6758620689655173,
          "word_count": 145
        },
        "style_score": 0.2662,
        "text_length": 795,
        "timestamp": "2026-11-08T21:53:17+00:00"
      },
      "appeal": {
        "method": "POST",
        "url": "http://127.0.0.1:5054/appeal",
        "request_json": {
          "content_id": "f6b5b60c-af1a-48a6-87c2-ee3a86448830",
          "reasoning": "Part 2 criterion review after, trial 1: please inspect this estimate."
        },
        "status_code": 200,
        "content_type": "application/json",
        "response_json": {
          "content_id": "f6b5b60c-af1a-48a6-87c2-ee3a86448830",
          "creator_id": "eval-after-c4-t1-human-03",
          "event": "appeal",
          "message": "Your appeal has been recorded. This writing is now under review.",
          "reasoning": "Part 2 criterion review after, trial 1: please inspect this estimate.",
          "status": "under_review",
          "timestamp": "2026-11-08T21:53:17+00:00"
        },
        "elapsed_ms": 2.98
      },
      "current": {
        "method": "GET",
        "url": "http://127.0.0.1:5054/content/f6b5b60c-af1a-48a6-87c2-ee3a86448830",
        "status_code": 200,
        "content_type": "application/json",
        "response_json": {
          "appeals": [
            {
              "content_id": "f6b5b60c-af1a-48a6-87c2-ee3a86448830",
              "creator_id": "eval-after-c4-t1-human-03",
              "event": "appeal",
              "reasoning": "Part 2 criterion review after, trial 1: please inspect this estimate.",
              "status": "under_review",
              "timestamp": "2026-11-08T21:53:17+00:00"
            }
          ],
          "combined_score": 0.3358,
          "confidence": 0.3358,
          "content_id": "f6b5b60c-af1a-48a6-87c2-ee3a86448830",
          "creator_id": "eval-after-c4-t1-human-03",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.3532,
          "status": "under_review",
          "style_metrics": {
            "evenness": 0.0,
            "punctuation_density": 0.027522935779816515,
            "punctuation_simplicity": 0.7706422018348624,
            "repetition": 0.37356321839080464,
            "sentence_count": 4,
            "sentence_length_spread": 0.8882105351861661,
            "style_score": 0.2662,
            "type_token_ratio": 0.6758620689655173,
            "word_count": 145
          },
          "style_score": 0.2662,
          "text_length": 795,
          "timestamp": "2026-11-08T21:53:17+00:00"
        },
        "elapsed_ms": 2.86
      },
      "passed": true,
      "history": [
        {
          "combined_score": 0.3358,
          "confidence": 0.3358,
          "content_id": "f6b5b60c-af1a-48a6-87c2-ee3a86448830",
          "creator_id": "eval-after-c4-t1-human-03",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.3532,
          "status": "decided",
          "style_metrics": {
            "evenness": 0.0,
            "punctuation_density": 0.027522935779816515,
            "punctuation_simplicity": 0.7706422018348624,
            "repetition": 0.37356321839080464,
            "sentence_count": 4,
            "sentence_length_spread": 0.8882105351861661,
            "style_score": 0.2662,
            "type_token_ratio": 0.6758620689655173,
            "word_count": 145
          },
          "style_score": 0.2662,
          "text_length": 795,
          "timestamp": "2026-11-08T21:53:17+00:00"
        },
        {
          "content_id": "f6b5b60c-af1a-48a6-87c2-ee3a86448830",
          "creator_id": "eval-after-c4-t1-human-03",
          "event": "appeal",
          "reasoning": "Part 2 criterion review after, trial 1: please inspect this estimate.",
          "status": "under_review",
          "timestamp": "2026-11-08T21:53:17+00:00"
        }
      ]
    },
    {
      "content_id": "c6bb7613-5d3b-4627-847d-6f05a08f9b72",
      "original": {
        "combined_score": 0.3954,
        "confidence": 0.3954,
        "content_id": "c6bb7613-5d3b-4627-847d-6f05a08f9b72",
        "creator_id": "eval-after-c4-t1-human-04",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.4097,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.16602391043278608,
          "punctuation_density": 0.053691275167785234,
          "punctuation_simplicity": 0.5525727069351231,
          "repetition": 0.48148148148148145,
          "sentence_count": 7,
          "sentence_length_spread": 0.6671808716537712,
          "style_score": 0.338,
          "type_token_ratio": 0.6111111111111112,
          "word_count": 108
        },
        "style_score": 0.338,
        "text_length": 552,
        "timestamp": "2026-11-08T21:53:17+00:00"
      },
      "appeal": {
        "method": "POST",
        "url": "http://127.0.0.1:5054/appeal",
        "request_json": {
          "content_id": "c6bb7613-5d3b-4627-847d-6f05a08f9b72",
          "reasoning": "Part 2 criterion review after, trial 1: please inspect this estimate."
        },
        "status_code": 200,
        "content_type": "application/json",
        "response_json": {
          "content_id": "c6bb7613-5d3b-4627-847d-6f05a08f9b72",
          "creator_id": "eval-after-c4-t1-human-04",
          "event": "appeal",
          "message": "Your appeal has been recorded. This writing is now under review.",
          "reasoning": "Part 2 criterion review after, trial 1: please inspect this estimate.",
          "status": "under_review",
          "timestamp": "2026-11-08T21:53:17+00:00"
        },
        "elapsed_ms": 2.98
      },
      "current": {
        "method": "GET",
        "url": "http://127.0.0.1:5054/content/c6bb7613-5d3b-4627-847d-6f05a08f9b72",
        "status_code": 200,
        "content_type": "application/json",
        "response_json": {
          "appeals": [
            {
              "content_id": "c6bb7613-5d3b-4627-847d-6f05a08f9b72",
              "creator_id": "eval-after-c4-t1-human-04",
              "event": "appeal",
              "reasoning": "Part 2 criterion review after, trial 1: please inspect this estimate.",
              "status": "under_review",
              "timestamp": "2026-11-08T21:53:17+00:00"
            }
          ],
          "combined_score": 0.3954,
          "confidence": 0.3954,
          "content_id": "c6bb7613-5d3b-4627-847d-6f05a08f9b72",
          "creator_id": "eval-after-c4-t1-human-04",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.4097,
          "status": "under_review",
          "style_metrics": {
            "evenness": 0.16602391043278608,
            "punctuation_density": 0.053691275167785234,
            "punctuation_simplicity": 0.5525727069351231,
            "repetition": 0.48148148148148145,
            "sentence_count": 7,
            "sentence_length_spread": 0.6671808716537712,
            "style_score": 0.338,
            "type_token_ratio": 0.6111111111111112,
            "word_count": 108
          },
          "style_score": 0.338,
          "text_length": 552,
          "timestamp": "2026-11-08T21:53:17+00:00"
        },
        "elapsed_ms": 2.8
      },
      "passed": true,
      "history": [
        {
          "combined_score": 0.3954,
          "confidence": 0.3954,
          "content_id": "c6bb7613-5d3b-4627-847d-6f05a08f9b72",
          "creator_id": "eval-after-c4-t1-human-04",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.4097,
          "status": "decided",
          "style_metrics": {
            "evenness": 0.16602391043278608,
            "punctuation_density": 0.053691275167785234,
            "punctuation_simplicity": 0.5525727069351231,
            "repetition": 0.48148148148148145,
            "sentence_count": 7,
            "sentence_length_spread": 0.6671808716537712,
            "style_score": 0.338,
            "type_token_ratio": 0.6111111111111112,
            "word_count": 108
          },
          "style_score": 0.338,
          "text_length": 552,
          "timestamp": "2026-11-08T21:53:17+00:00"
        },
        {
          "content_id": "c6bb7613-5d3b-4627-847d-6f05a08f9b72",
          "creator_id": "eval-after-c4-t1-human-04",
          "event": "appeal",
          "reasoning": "Part 2 criterion review after, trial 1: please inspect this estimate.",
          "status": "under_review",
          "timestamp": "2026-11-08T21:53:17+00:00"
        }
      ]
    },
    {
      "content_id": "a6fc5c38-d603-4b8a-ac01-117d39c31d32",
      "original": {
        "combined_score": 0.6497,
        "confidence": 0.6497,
        "content_id": "a6fc5c38-d603-4b8a-ac01-117d39c31d32",
        "creator_id": "eval-after-c4-t1-human-05",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.7577,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.0,
          "punctuation_density": 0.04195804195804196,
          "punctuation_simplicity": 0.6503496503496503,
          "repetition": 0.29227053140096626,
          "sentence_count": 3,
          "sentence_length_spread": 0.8615573303015565,
          "style_score": 0.2178,
          "type_token_ratio": 0.7246376811594203,
          "word_count": 69
        },
        "style_score": 0.2178,
        "text_length": 354,
        "timestamp": "2026-11-08T21:53:17+00:00"
      },
      "appeal": {
        "method": "POST",
        "url": "http://127.0.0.1:5054/appeal",
        "request_json": {
          "content_id": "a6fc5c38-d603-4b8a-ac01-117d39c31d32",
          "reasoning": "Part 2 criterion review after, trial 1: please inspect this estimate."
        },
        "status_code": 200,
        "content_type": "application/json",
        "response_json": {
          "content_id": "a6fc5c38-d603-4b8a-ac01-117d39c31d32",
          "creator_id": "eval-after-c4-t1-human-05",
          "event": "appeal",
          "message": "Your appeal has been recorded. This writing is now under review.",
          "reasoning": "Part 2 criterion review after, trial 1: please inspect this estimate.",
          "status": "under_review",
          "timestamp": "2026-11-08T21:53:17+00:00"
        },
        "elapsed_ms": 2.95
      },
      "current": {
        "method": "GET",
        "url": "http://127.0.0.1:5054/content/a6fc5c38-d603-4b8a-ac01-117d39c31d32",
        "status_code": 200,
        "content_type": "application/json",
        "response_json": {
          "appeals": [
            {
              "content_id": "a6fc5c38-d603-4b8a-ac01-117d39c31d32",
              "creator_id": "eval-after-c4-t1-human-05",
              "event": "appeal",
              "reasoning": "Part 2 criterion review after, trial 1: please inspect this estimate.",
              "status": "under_review",
              "timestamp": "2026-11-08T21:53:17+00:00"
            }
          ],
          "combined_score": 0.6497,
          "confidence": 0.6497,
          "content_id": "a6fc5c38-d603-4b8a-ac01-117d39c31d32",
          "creator_id": "eval-after-c4-t1-human-05",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.7577,
          "status": "under_review",
          "style_metrics": {
            "evenness": 0.0,
            "punctuation_density": 0.04195804195804196,
            "punctuation_simplicity": 0.6503496503496503,
            "repetition": 0.29227053140096626,
            "sentence_count": 3,
            "sentence_length_spread": 0.8615573303015565,
            "style_score": 0.2178,
            "type_token_ratio": 0.7246376811594203,
            "word_count": 69
          },
          "style_score": 0.2178,
          "text_length": 354,
          "timestamp": "2026-11-08T21:53:17+00:00"
        },
        "elapsed_ms": 2.82
      },
      "passed": true,
      "history": [
        {
          "combined_score": 0.6497,
          "confidence": 0.6497,
          "content_id": "a6fc5c38-d603-4b8a-ac01-117d39c31d32",
          "creator_id": "eval-after-c4-t1-human-05",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.7577,
          "status": "decided",
          "style_metrics": {
            "evenness": 0.0,
            "punctuation_density": 0.04195804195804196,
            "punctuation_simplicity": 0.6503496503496503,
            "repetition": 0.29227053140096626,
            "sentence_count": 3,
            "sentence_length_spread": 0.8615573303015565,
            "style_score": 0.2178,
            "type_token_ratio": 0.7246376811594203,
            "word_count": 69
          },
          "style_score": 0.2178,
          "text_length": 354,
          "timestamp": "2026-11-08T21:53:17+00:00"
        },
        {
          "content_id": "a6fc5c38-d603-4b8a-ac01-117d39c31d32",
          "creator_id": "eval-after-c4-t1-human-05",
          "event": "appeal",
          "reasoning": "Part 2 criterion review after, trial 1: please inspect this estimate.",
          "status": "under_review",
          "timestamp": "2026-11-08T21:53:17+00:00"
        }
      ]
    },
    {
      "content_id": "0b8faa49-4a87-4a5a-a07f-576e2ca772f3",
      "original": {
        "combined_score": 0.5545,
        "confidence": 0.5545,
        "content_id": "0b8faa49-4a87-4a5a-a07f-576e2ca772f3",
        "creator_id": "eval-after-c4-t1-human-06",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.5829,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.38795621995783924,
          "punctuation_density": 0.01937046004842615,
          "punctuation_simplicity": 0.8385794995964487,
          "repetition": 0.2640449438202247,
          "sentence_count": 4,
          "sentence_length_spread": 0.48963502403372866,
          "style_score": 0.4409,
          "type_token_ratio": 0.7415730337078652,
          "word_count": 89
        },
        "style_score": 0.4409,
        "text_length": 501,
        "timestamp": "2026-11-08T21:53:17+00:00"
      },
      "appeal": {
        "method": "POST",
        "url": "http://127.0.0.1:5054/appeal",
        "request_json": {
          "content_id": "0b8faa49-4a87-4a5a-a07f-576e2ca772f3",
          "reasoning": "Part 2 criterion review after, trial 1: please inspect this estimate."
        },
        "status_code": 200,
        "content_type": "application/json",
        "response_json": {
          "content_id": "0b8faa49-4a87-4a5a-a07f-576e2ca772f3",
          "creator_id": "eval-after-c4-t1-human-06",
          "event": "appeal",
          "message": "Your appeal has been recorded. This writing is now under review.",
          "reasoning": "Part 2 criterion review after, trial 1: please inspect this estimate.",
          "status": "under_review",
          "timestamp": "2026-11-08T21:53:18+00:00"
        },
        "elapsed_ms": 2.92
      },
      "current": {
        "method": "GET",
        "url": "http://127.0.0.1:5054/content/0b8faa49-4a87-4a5a-a07f-576e2ca772f3",
        "status_code": 200,
        "content_type": "application/json",
        "response_json": {
          "appeals": [
            {
              "content_id": "0b8faa49-4a87-4a5a-a07f-576e2ca772f3",
              "creator_id": "eval-after-c4-t1-human-06",
              "event": "appeal",
              "reasoning": "Part 2 criterion review after, trial 1: please inspect this estimate.",
              "status": "under_review",
              "timestamp": "2026-11-08T21:53:18+00:00"
            }
          ],
          "combined_score": 0.5545,
          "confidence": 0.5545,
          "content_id": "0b8faa49-4a87-4a5a-a07f-576e2ca772f3",
          "creator_id": "eval-after-c4-t1-human-06",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.5829,
          "status": "under_review",
          "style_metrics": {
            "evenness": 0.38795621995783924,
            "punctuation_density": 0.01937046004842615,
            "punctuation_simplicity": 0.8385794995964487,
            "repetition": 0.2640449438202247,
            "sentence_count": 4,
            "sentence_length_spread": 0.48963502403372866,
            "style_score": 0.4409,
            "type_token_ratio": 0.7415730337078652,
            "word_count": 89
          },
          "style_score": 0.4409,
          "text_length": 501,
          "timestamp": "2026-11-08T21:53:17+00:00"
        },
        "elapsed_ms": 2.81
      },
      "passed": true,
      "history": [
        {
          "combined_score": 0.5545,
          "confidence": 0.5545,
          "content_id": "0b8faa49-4a87-4a5a-a07f-576e2ca772f3",
          "creator_id": "eval-after-c4-t1-human-06",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.5829,
          "status": "decided",
          "style_metrics": {
            "evenness": 0.38795621995783924,
            "punctuation_density": 0.01937046004842615,
            "punctuation_simplicity": 0.8385794995964487,
            "repetition": 0.2640449438202247,
            "sentence_count": 4,
            "sentence_length_spread": 0.48963502403372866,
            "style_score": 0.4409,
            "type_token_ratio": 0.7415730337078652,
            "word_count": 89
          },
          "style_score": 0.4409,
          "text_length": 501,
          "timestamp": "2026-11-08T21:53:17+00:00"
        },
        {
          "content_id": "0b8faa49-4a87-4a5a-a07f-576e2ca772f3",
          "creator_id": "eval-after-c4-t1-human-06",
          "event": "appeal",
          "reasoning": "Part 2 criterion review after, trial 1: please inspect this estimate.",
          "status": "under_review",
          "timestamp": "2026-11-08T21:53:18+00:00"
        }
      ]
    },
    {
      "content_id": "b5dea10f-94b1-4898-b93d-776f9ae8edc5",
      "original": {
        "combined_score": 0.5606,
        "confidence": 0.5606,
        "content_id": "b5dea10f-94b1-4898-b93d-776f9ae8edc5",
        "creator_id": "eval-after-c4-t1-human-07",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.5745,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.5,
          "punctuation_density": 0.035343035343035345,
          "punctuation_simplicity": 0.7054747054747055,
          "repetition": 0.3790560471976401,
          "sentence_count": 2,
          "sentence_length_spread": 0.008849557522123894,
          "style_score": 0.5048,
          "type_token_ratio": 0.672566371681416,
          "word_count": 113
        },
        "style_score": 0.5048,
        "text_length": 592,
        "timestamp": "2026-11-08T21:53:17+00:00"
      },
      "appeal": {
        "method": "POST",
        "url": "http://127.0.0.1:5054/appeal",
        "request_json": {
          "content_id": "b5dea10f-94b1-4898-b93d-776f9ae8edc5",
          "reasoning": "Part 2 criterion review after, trial 1: please inspect this estimate."
        },
        "status_code": 200,
        "content_type": "application/json",
        "response_json": {
          "content_id": "b5dea10f-94b1-4898-b93d-776f9ae8edc5",
          "creator_id": "eval-after-c4-t1-human-07",
          "event": "appeal",
          "message": "Your appeal has been recorded. This writing is now under review.",
          "reasoning": "Part 2 criterion review after, trial 1: please inspect this estimate.",
          "status": "under_review",
          "timestamp": "2026-11-08T21:53:18+00:00"
        },
        "elapsed_ms": 2.92
      },
      "current": {
        "method": "GET",
        "url": "http://127.0.0.1:5054/content/b5dea10f-94b1-4898-b93d-776f9ae8edc5",
        "status_code": 200,
        "content_type": "application/json",
        "response_json": {
          "appeals": [
            {
              "content_id": "b5dea10f-94b1-4898-b93d-776f9ae8edc5",
              "creator_id": "eval-after-c4-t1-human-07",
              "event": "appeal",
              "reasoning": "Part 2 criterion review after, trial 1: please inspect this estimate.",
              "status": "under_review",
              "timestamp": "2026-11-08T21:53:18+00:00"
            }
          ],
          "combined_score": 0.5606,
          "confidence": 0.5606,
          "content_id": "b5dea10f-94b1-4898-b93d-776f9ae8edc5",
          "creator_id": "eval-after-c4-t1-human-07",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.5745,
          "status": "under_review",
          "style_metrics": {
            "evenness": 0.5,
            "punctuation_density": 0.035343035343035345,
            "punctuation_simplicity": 0.7054747054747055,
            "repetition": 0.3790560471976401,
            "sentence_count": 2,
            "sentence_length_spread": 0.008849557522123894,
            "style_score": 0.5048,
            "type_token_ratio": 0.672566371681416,
            "word_count": 113
          },
          "style_score": 0.5048,
          "text_length": 592,
          "timestamp": "2026-11-08T21:53:17+00:00"
        },
        "elapsed_ms": 2.77
      },
      "passed": true,
      "history": [
        {
          "combined_score": 0.5606,
          "confidence": 0.5606,
          "content_id": "b5dea10f-94b1-4898-b93d-776f9ae8edc5",
          "creator_id": "eval-after-c4-t1-human-07",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.5745,
          "status": "decided",
          "style_metrics": {
            "evenness": 0.5,
            "punctuation_density": 0.035343035343035345,
            "punctuation_simplicity": 0.7054747054747055,
            "repetition": 0.3790560471976401,
            "sentence_count": 2,
            "sentence_length_spread": 0.008849557522123894,
            "style_score": 0.5048,
            "type_token_ratio": 0.672566371681416,
            "word_count": 113
          },
          "style_score": 0.5048,
          "text_length": 592,
          "timestamp": "2026-11-08T21:53:17+00:00"
        },
        {
          "content_id": "b5dea10f-94b1-4898-b93d-776f9ae8edc5",
          "creator_id": "eval-after-c4-t1-human-07",
          "event": "appeal",
          "reasoning": "Part 2 criterion review after, trial 1: please inspect this estimate.",
          "status": "under_review",
          "timestamp": "2026-11-08T21:53:18+00:00"
        }
      ]
    },
    {
      "content_id": "b4b9c1cb-83bc-483c-8c1d-5aa1fd642974",
      "original": {
        "combined_score": 0.5581,
        "confidence": 0.5581,
        "content_id": "b4b9c1cb-83bc-483c-8c1d-5aa1fd642974",
        "creator_id": "eval-after-c4-t1-human-08",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.5825,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.420697370644045,
          "punctuation_density": 0.03232323232323232,
          "punctuation_simplicity": 0.7306397306397306,
          "repetition": 0.3473520249221185,
          "sentence_count": 4,
          "sentence_length_spread": 0.46344210348476406,
          "style_score": 0.4607,
          "type_token_ratio": 0.6915887850467289,
          "word_count": 107
        },
        "style_score": 0.4607,
        "text_length": 598,
        "timestamp": "2026-11-08T21:53:17+00:00"
      },
      "appeal": {
        "method": "POST",
        "url": "http://127.0.0.1:5054/appeal",
        "request_json": {
          "content_id": "b4b9c1cb-83bc-483c-8c1d-5aa1fd642974",
          "reasoning": "Part 2 criterion review after, trial 1: please inspect this estimate."
        },
        "status_code": 200,
        "content_type": "application/json",
        "response_json": {
          "content_id": "b4b9c1cb-83bc-483c-8c1d-5aa1fd642974",
          "creator_id": "eval-after-c4-t1-human-08",
          "event": "appeal",
          "message": "Your appeal has been recorded. This writing is now under review.",
          "reasoning": "Part 2 criterion review after, trial 1: please inspect this estimate.",
          "status": "under_review",
          "timestamp": "2026-11-08T21:53:18+00:00"
        },
        "elapsed_ms": 2.87
      },
      "current": {
        "method": "GET",
        "url": "http://127.0.0.1:5054/content/b4b9c1cb-83bc-483c-8c1d-5aa1fd642974",
        "status_code": 200,
        "content_type": "application/json",
        "response_json": {
          "appeals": [
            {
              "content_id": "b4b9c1cb-83bc-483c-8c1d-5aa1fd642974",
              "creator_id": "eval-after-c4-t1-human-08",
              "event": "appeal",
              "reasoning": "Part 2 criterion review after, trial 1: please inspect this estimate.",
              "status": "under_review",
              "timestamp": "2026-11-08T21:53:18+00:00"
            }
          ],
          "combined_score": 0.5581,
          "confidence": 0.5581,
          "content_id": "b4b9c1cb-83bc-483c-8c1d-5aa1fd642974",
          "creator_id": "eval-after-c4-t1-human-08",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.5825,
          "status": "under_review",
          "style_metrics": {
            "evenness": 0.420697370644045,
            "punctuation_density": 0.03232323232323232,
            "punctuation_simplicity": 0.7306397306397306,
            "repetition": 0.3473520249221185,
            "sentence_count": 4,
            "sentence_length_spread": 0.46344210348476406,
            "style_score": 0.4607,
            "type_token_ratio": 0.6915887850467289,
            "word_count": 107
          },
          "style_score": 0.4607,
          "text_length": 598,
          "timestamp": "2026-11-08T21:53:17+00:00"
        },
        "elapsed_ms": 2.83
      },
      "passed": true,
      "history": [
        {
          "combined_score": 0.5581,
          "confidence": 0.5581,
          "content_id": "b4b9c1cb-83bc-483c-8c1d-5aa1fd642974",
          "creator_id": "eval-after-c4-t1-human-08",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.5825,
          "status": "decided",
          "style_metrics": {
            "evenness": 0.420697370644045,
            "punctuation_density": 0.03232323232323232,
            "punctuation_simplicity": 0.7306397306397306,
            "repetition": 0.3473520249221185,
            "sentence_count": 4,
            "sentence_length_spread": 0.46344210348476406,
            "style_score": 0.4607,
            "type_token_ratio": 0.6915887850467289,
            "word_count": 107
          },
          "style_score": 0.4607,
          "text_length": 598,
          "timestamp": "2026-11-08T21:53:17+00:00"
        },
        {
          "content_id": "b4b9c1cb-83bc-483c-8c1d-5aa1fd642974",
          "creator_id": "eval-after-c4-t1-human-08",
          "event": "appeal",
          "reasoning": "Part 2 criterion review after, trial 1: please inspect this estimate.",
          "status": "under_review",
          "timestamp": "2026-11-08T21:53:18+00:00"
        }
      ]
    },
    {
      "content_id": "08af0d7c-15c4-49e7-85a3-d110edb24398",
      "original": {
        "combined_score": 0.7081,
        "confidence": 0.7081,
        "content_id": "08af0d7c-15c4-49e7-85a3-d110edb24398",
        "creator_id": "eval-after-c4-t1-human-09",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.7648,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.26494047860054226,
          "punctuation_density": 0.018823529411764704,
          "punctuation_simplicity": 0.8431372549019608,
          "repetition": 0.6,
          "sentence_count": 3,
          "sentence_length_spread": 0.5880476171195662,
          "style_score": 0.4811,
          "type_token_ratio": 0.54,
          "word_count": 100
        },
        "style_score": 0.4811,
        "text_length": 524,
        "timestamp": "2026-11-08T21:53:17+00:00"
      },
      "appeal": {
        "method": "POST",
        "url": "http://127.0.0.1:5054/appeal",
        "request_json": {
          "content_id": "08af0d7c-15c4-49e7-85a3-d110edb24398",
          "reasoning": "Part 2 criterion review after, trial 1: please inspect this estimate."
        },
        "status_code": 200,
        "content_type": "application/json",
        "response_json": {
          "content_id": "08af0d7c-15c4-49e7-85a3-d110edb24398",
          "creator_id": "eval-after-c4-t1-human-09",
          "event": "appeal",
          "message": "Your appeal has been recorded. This writing is now under review.",
          "reasoning": "Part 2 criterion review after, trial 1: please inspect this estimate.",
          "status": "under_review",
          "timestamp": "2026-11-08T21:53:18+00:00"
        },
        "elapsed_ms": 2.91
      },
      "current": {
        "method": "GET",
        "url": "http://127.0.0.1:5054/content/08af0d7c-15c4-49e7-85a3-d110edb24398",
        "status_code": 200,
        "content_type": "application/json",
        "response_json": {
          "appeals": [
            {
              "content_id": "08af0d7c-15c4-49e7-85a3-d110edb24398",
              "creator_id": "eval-after-c4-t1-human-09",
              "event": "appeal",
              "reasoning": "Part 2 criterion review after, trial 1: please inspect this estimate.",
              "status": "under_review",
              "timestamp": "2026-11-08T21:53:18+00:00"
            }
          ],
          "combined_score": 0.7081,
          "confidence": 0.7081,
          "content_id": "08af0d7c-15c4-49e7-85a3-d110edb24398",
          "creator_id": "eval-after-c4-t1-human-09",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.7648,
          "status": "under_review",
          "style_metrics": {
            "evenness": 0.26494047860054226,
            "punctuation_density": 0.018823529411764704,
            "punctuation_simplicity": 0.8431372549019608,
            "repetition": 0.6,
            "sentence_count": 3,
            "sentence_length_spread": 0.5880476171195662,
            "style_score": 0.4811,
            "type_token_ratio": 0.54,
            "word_count": 100
          },
          "style_score": 0.4811,
          "text_length": 524,
          "timestamp": "2026-11-08T21:53:17+00:00"
        },
        "elapsed_ms": 2.86
      },
      "passed": true,
      "history": [
        {
          "combined_score": 0.7081,
          "confidence": 0.7081,
          "content_id": "08af0d7c-15c4-49e7-85a3-d110edb24398",
          "creator_id": "eval-after-c4-t1-human-09",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.7648,
          "status": "decided",
          "style_metrics": {
            "evenness": 0.26494047860054226,
            "punctuation_density": 0.018823529411764704,
            "punctuation_simplicity": 0.8431372549019608,
            "repetition": 0.6,
            "sentence_count": 3,
            "sentence_length_spread": 0.5880476171195662,
            "style_score": 0.4811,
            "type_token_ratio": 0.54,
            "word_count": 100
          },
          "style_score": 0.4811,
          "text_length": 524,
          "timestamp": "2026-11-08T21:53:17+00:00"
        },
        {
          "content_id": "08af0d7c-15c4-49e7-85a3-d110edb24398",
          "creator_id": "eval-after-c4-t1-human-09",
          "event": "appeal",
          "reasoning": "Part 2 criterion review after, trial 1: please inspect this estimate.",
          "status": "under_review",
          "timestamp": "2026-11-08T21:53:18+00:00"
        }
      ]
    },
    {
      "content_id": "254db630-161f-444d-9188-e55bdf4c88b0",
      "original": {
        "combined_score": 0.5475,
        "confidence": 0.5475,
        "content_id": "254db630-161f-444d-9188-e55bdf4c88b0",
        "creator_id": "eval-after-c4-t1-human-10",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.566,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.4729379744287563,
          "punctuation_density": 0.047058823529411764,
          "punctuation_simplicity": 0.607843137254902,
          "repetition": 0.3842975206611571,
          "sentence_count": 4,
          "sentence_length_spread": 0.421649620456995,
          "style_score": 0.4733,
          "type_token_ratio": 0.6694214876033058,
          "word_count": 121
        },
        "style_score": 0.4733,
        "text_length": 626,
        "timestamp": "2026-11-08T21:53:17+00:00"
      },
      "appeal": {
        "method": "POST",
        "url": "http://127.0.0.1:5054/appeal",
        "request_json": {
          "content_id": "254db630-161f-444d-9188-e55bdf4c88b0",
          "reasoning": "Part 2 criterion review after, trial 1: please inspect this estimate."
        },
        "status_code": 200,
        "content_type": "application/json",
        "response_json": {
          "content_id": "254db630-161f-444d-9188-e55bdf4c88b0",
          "creator_id": "eval-after-c4-t1-human-10",
          "event": "appeal",
          "message": "Your appeal has been recorded. This writing is now under review.",
          "reasoning": "Part 2 criterion review after, trial 1: please inspect this estimate.",
          "status": "under_review",
          "timestamp": "2026-11-08T21:53:18+00:00"
        },
        "elapsed_ms": 2.95
      },
      "current": {
        "method": "GET",
        "url": "http://127.0.0.1:5054/content/254db630-161f-444d-9188-e55bdf4c88b0",
        "status_code": 200,
        "content_type": "application/json",
        "response_json": {
          "appeals": [
            {
              "content_id": "254db630-161f-444d-9188-e55bdf4c88b0",
              "creator_id": "eval-after-c4-t1-human-10",
              "event": "appeal",
              "reasoning": "Part 2 criterion review after, trial 1: please inspect this estimate.",
              "status": "under_review",
              "timestamp": "2026-11-08T21:53:18+00:00"
            }
          ],
          "combined_score": 0.5475,
          "confidence": 0.5475,
          "content_id": "254db630-161f-444d-9188-e55bdf4c88b0",
          "creator_id": "eval-after-c4-t1-human-10",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.566,
          "status": "under_review",
          "style_metrics": {
            "evenness": 0.4729379744287563,
            "punctuation_density": 0.047058823529411764,
            "punctuation_simplicity": 0.607843137254902,
            "repetition": 0.3842975206611571,
            "sentence_count": 4,
            "sentence_length_spread": 0.421649620456995,
            "style_score": 0.4733,
            "type_token_ratio": 0.6694214876033058,
            "word_count": 121
          },
          "style_score": 0.4733,
          "text_length": 626,
          "timestamp": "2026-11-08T21:53:17+00:00"
        },
        "elapsed_ms": 2.84
      },
      "passed": true,
      "history": [
        {
          "combined_score": 0.5475,
          "confidence": 0.5475,
          "content_id": "254db630-161f-444d-9188-e55bdf4c88b0",
          "creator_id": "eval-after-c4-t1-human-10",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.566,
          "status": "decided",
          "style_metrics": {
            "evenness": 0.4729379744287563,
            "punctuation_density": 0.047058823529411764,
            "punctuation_simplicity": 0.607843137254902,
            "repetition": 0.3842975206611571,
            "sentence_count": 4,
            "sentence_length_spread": 0.421649620456995,
            "style_score": 0.4733,
            "type_token_ratio": 0.6694214876033058,
            "word_count": 121
          },
          "style_score": 0.4733,
          "text_length": 626,
          "timestamp": "2026-11-08T21:53:17+00:00"
        },
        {
          "content_id": "254db630-161f-444d-9188-e55bdf4c88b0",
          "creator_id": "eval-after-c4-t1-human-10",
          "event": "appeal",
          "reasoning": "Part 2 criterion review after, trial 1: please inspect this estimate.",
          "status": "under_review",
          "timestamp": "2026-11-08T21:53:18+00:00"
        }
      ]
    }
  ],
  "submissions": [
    {
      "method": "POST",
      "url": "http://127.0.0.1:5054/submit",
      "request_json": {
        "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
        "creator_id": "eval-after-c4-t1-human-01"
      },
      "status_code": 200,
      "content_type": "application/json",
      "response_json": {
        "combined_score": 0.6593,
        "confidence": 0.6593,
        "content_id": "57f55524-8978-43d5-bc0b-e1396115c1d2",
        "creator_id": "eval-after-c4-t1-human-01",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.6922,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.5,
          "punctuation_density": 0.016286644951140065,
          "punctuation_simplicity": 0.8642779587404994,
          "repetition": 0.34976525821596255,
          "sentence_count": 2,
          "sentence_length_spread": 0.352112676056338,
          "style_score": 0.5278,
          "type_token_ratio": 0.6901408450704225,
          "word_count": 71
        },
        "style_score": 0.5278,
        "text_length": 377,
        "timestamp": "2026-11-08T21:53:17+00:00"
      },
      "elapsed_ms": 40.99,
      "input_id": "human-01",
      "input_provenance": {
        "id": "human-01",
        "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
        "source_url": "https://www.gutenberg.org/cache/epub/1342/pg1342.txt",
        "author": "Jane Austen",
        "title": "Pride and Prejudice",
        "publication_year": 1813,
        "location": "Chapter I, first two paragraphs",
        "genre": "literary fiction",
        "provenance": "Exact public-domain excerpt from the Project Gutenberg edition of Austen's published novel, verified against the linked primary text on 2026-10-30. Whitespace normalized."
      }
    },
    {
      "method": "POST",
      "url": "http://127.0.0.1:5054/submit",
      "request_json": {
        "text": "There was no possibility of taking a walk that day. We had been wandering, indeed, in the leafless shrubbery an hour in the morning; but since dinner (Mrs. Reed, when there was no company, dined early) the cold winter wind had brought with it clouds so sombre, and a rain so penetrating, that further outdoor exercise was now out of the question. I was glad of it: I never liked long walks, especially on chilly afternoons: dreadful to me was the coming home in the raw twilight, with nipped fingers and toes, and a heart saddened by the chidings of Bessie, the nurse, and humbled by the consciousness of my physical inferiority to Eliza, John, and Georgiana Reed.",
        "creator_id": "eval-after-c4-t1-human-02"
      },
      "status_code": 200,
      "content_type": "application/json",
      "response_json": {
        "combined_score": 0.4608,
        "confidence": 0.4608,
        "content_id": "b7e898ca-5f47-4dd8-8892-45b55232cc1b",
        "creator_id": "eval-after-c4-t1-human-02",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.4863,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.2554540936099331,
          "punctuation_density": 0.04021937842778794,
          "punctuation_simplicity": 0.6648385131017671,
          "repetition": 0.3276836158192091,
          "sentence_count": 4,
          "sentence_length_spread": 0.5956367251120536,
          "style_score": 0.359,
          "type_token_ratio": 0.7033898305084746,
          "word_count": 118
        },
        "style_score": 0.359,
        "text_length": 664,
        "timestamp": "2026-11-08T21:53:17+00:00"
      },
      "elapsed_ms": 63.51,
      "input_id": "human-02",
      "input_provenance": {
        "id": "human-02",
        "text": "There was no possibility of taking a walk that day. We had been wandering, indeed, in the leafless shrubbery an hour in the morning; but since dinner (Mrs. Reed, when there was no company, dined early) the cold winter wind had brought with it clouds so sombre, and a rain so penetrating, that further outdoor exercise was now out of the question. I was glad of it: I never liked long walks, especially on chilly afternoons: dreadful to me was the coming home in the raw twilight, with nipped fingers and toes, and a heart saddened by the chidings of Bessie, the nurse, and humbled by the consciousness of my physical inferiority to Eliza, John, and Georgiana Reed.",
        "source_url": "https://www.gutenberg.org/cache/epub/1260/pg1260.txt",
        "author": "Charlotte Bront\u00eb",
        "title": "Jane Eyre: An Autobiography",
        "publication_year": 1847,
        "location": "Chapter I, first two paragraphs",
        "genre": "first-person literary fiction",
        "provenance": "Exact public-domain excerpt from the Project Gutenberg edition of Bront\u00eb's published novel, verified against the linked primary text on 2026-10-30. Whitespace normalized."
      }
    },
    {
      "method": "POST",
      "url": "http://127.0.0.1:5054/submit",
      "request_json": {
        "text": "Call me Ishmael. Some years ago\u2014never mind how long precisely\u2014having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world. It is a way I have of driving off the spleen and regulating the circulation. Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral I meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people\u2019s hats off\u2014then, I account it high time to get to sea as soon as I can.",
        "creator_id": "eval-after-c4-t1-human-03"
      },
      "status_code": 200,
      "content_type": "application/json",
      "response_json": {
        "combined_score": 0.3358,
        "confidence": 0.3358,
        "content_id": "f6b5b60c-af1a-48a6-87c2-ee3a86448830",
        "creator_id": "eval-after-c4-t1-human-03",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.3532,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.0,
          "punctuation_density": 0.027522935779816515,
          "punctuation_simplicity": 0.7706422018348624,
          "repetition": 0.37356321839080464,
          "sentence_count": 4,
          "sentence_length_spread": 0.8882105351861661,
          "style_score": 0.2662,
          "type_token_ratio": 0.6758620689655173,
          "word_count": 145
        },
        "style_score": 0.2662,
        "text_length": 795,
        "timestamp": "2026-11-08T21:53:17+00:00"
      },
      "elapsed_ms": 69.5,
      "input_id": "human-03",
      "input_provenance": {
        "id": "human-03",
        "text": "Call me Ishmael. Some years ago\u2014never mind how long precisely\u2014having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world. It is a way I have of driving off the spleen and regulating the circulation. Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral I meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people\u2019s hats off\u2014then, I account it high time to get to sea as soon as I can.",
        "source_url": "https://www.gutenberg.org/cache/epub/2701/pg2701.txt",
        "author": "Herman Melville",
        "title": "Moby Dick; Or, The Whale",
        "publication_year": 1851,
        "location": "Chapter 1, Loomings, opening through 'as soon as I can.'",
        "genre": "first-person literary fiction",
        "provenance": "Exact public-domain excerpt from the Project Gutenberg edition of Melville's published novel, verified against the linked primary text on 2026-10-30. Whitespace normalized."
      }
    },
    {
      "method": "POST",
      "url": "http://127.0.0.1:5054/submit",
      "request_json": {
        "text": "You don\u2019t know about me without you have read a book by the name of The Adventures of Tom Sawyer; but that ain\u2019t no matter. That book was made by Mr. Mark Twain, and he told the truth, mainly. There was things which he stretched, but mainly he told the truth. That is nothing. I never seen anybody but lied one time or another, without it was Aunt Polly, or the widow, or maybe Mary. Aunt Polly\u2014Tom\u2019s Aunt Polly, she is\u2014and Mary, and the Widow Douglas is all told about in that book, which is mostly a true book, with some stretchers, as I said before.",
        "creator_id": "eval-after-c4-t1-human-04"
      },
      "status_code": 200,
      "content_type": "application/json",
      "response_json": {
        "combined_score": 0.3954,
        "confidence": 0.3954,
        "content_id": "c6bb7613-5d3b-4627-847d-6f05a08f9b72",
        "creator_id": "eval-after-c4-t1-human-04",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.4097,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.16602391043278608,
          "punctuation_density": 0.053691275167785234,
          "punctuation_simplicity": 0.5525727069351231,
          "repetition": 0.48148148148148145,
          "sentence_count": 7,
          "sentence_length_spread": 0.6671808716537712,
          "style_score": 0.338,
          "type_token_ratio": 0.6111111111111112,
          "word_count": 108
        },
        "style_score": 0.338,
        "text_length": 552,
        "timestamp": "2026-11-08T21:53:17+00:00"
      },
      "elapsed_ms": 59.05,
      "input_id": "human-04",
      "input_provenance": {
        "id": "human-04",
        "text": "You don\u2019t know about me without you have read a book by the name of The Adventures of Tom Sawyer; but that ain\u2019t no matter. That book was made by Mr. Mark Twain, and he told the truth, mainly. There was things which he stretched, but mainly he told the truth. That is nothing. I never seen anybody but lied one time or another, without it was Aunt Polly, or the widow, or maybe Mary. Aunt Polly\u2014Tom\u2019s Aunt Polly, she is\u2014and Mary, and the Widow Douglas is all told about in that book, which is mostly a true book, with some stretchers, as I said before.",
        "source_url": "https://www.gutenberg.org/cache/epub/76/pg76.txt",
        "author": "Mark Twain",
        "title": "Adventures of Huckleberry Finn",
        "publication_year": 1884,
        "location": "Chapter I, first paragraph",
        "genre": "first-person dialect fiction",
        "provenance": "Exact public-domain excerpt from the Project Gutenberg edition of Twain's published novel, verified against the linked primary text on 2026-10-30. Whitespace normalized. First UK publication was 1884; US publication followed in 1885."
      }
    },
    {
      "method": "POST",
      "url": "http://127.0.0.1:5054/submit",
      "request_json": {
        "text": "When I wrote the following pages, or rather the bulk of them, I lived alone, in the woods, a mile from any neighbor, in a house which I had built myself, on the shore of Walden Pond, in Concord, Massachusetts, and earned my living by the labor of my hands only. I lived there two years and two months. At present I am a sojourner in civilized life again.",
        "creator_id": "eval-after-c4-t1-human-05"
      },
      "status_code": 200,
      "content_type": "application/json",
      "response_json": {
        "combined_score": 0.6497,
        "confidence": 0.6497,
        "content_id": "a6fc5c38-d603-4b8a-ac01-117d39c31d32",
        "creator_id": "eval-after-c4-t1-human-05",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.7577,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.0,
          "punctuation_density": 0.04195804195804196,
          "punctuation_simplicity": 0.6503496503496503,
          "repetition": 0.29227053140096626,
          "sentence_count": 3,
          "sentence_length_spread": 0.8615573303015565,
          "style_score": 0.2178,
          "type_token_ratio": 0.7246376811594203,
          "word_count": 69
        },
        "style_score": 0.2178,
        "text_length": 354,
        "timestamp": "2026-11-08T21:53:17+00:00"
      },
      "elapsed_ms": 43.11,
      "input_id": "human-05",
      "input_provenance": {
        "id": "human-05",
        "text": "When I wrote the following pages, or rather the bulk of them, I lived alone, in the woods, a mile from any neighbor, in a house which I had built myself, on the shore of Walden Pond, in Concord, Massachusetts, and earned my living by the labor of my hands only. I lived there two years and two months. At present I am a sojourner in civilized life again.",
        "source_url": "https://www.gutenberg.org/cache/epub/205/pg205.txt",
        "author": "Henry David Thoreau",
        "title": "Walden",
        "publication_year": 1854,
        "location": "Economy, first paragraph",
        "genre": "first-person nonfiction",
        "provenance": "Exact public-domain excerpt from Walden in the Project Gutenberg volume Walden, and On The Duty Of Civil Disobedience, verified against the linked primary text on 2026-10-30. Whitespace normalized."
      }
    },
    {
      "method": "POST",
      "url": "http://127.0.0.1:5054/submit",
      "request_json": {
        "text": "You will rejoice to hear that no disaster has accompanied the commencement of an enterprise which you have regarded with such evil forebodings. I arrived here yesterday, and my first task is to assure my dear sister of my welfare and increasing confidence in the success of my undertaking. I am already far north of London, and as I walk in the streets of Petersburgh, I feel a cold northern breeze play upon my cheeks, which braces my nerves and fills me with delight. Do you understand this feeling?",
        "creator_id": "eval-after-c4-t1-human-06"
      },
      "status_code": 200,
      "content_type": "application/json",
      "response_json": {
        "combined_score": 0.5545,
        "confidence": 0.5545,
        "content_id": "0b8faa49-4a87-4a5a-a07f-576e2ca772f3",
        "creator_id": "eval-after-c4-t1-human-06",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.5829,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.38795621995783924,
          "punctuation_density": 0.01937046004842615,
          "punctuation_simplicity": 0.8385794995964487,
          "repetition": 0.2640449438202247,
          "sentence_count": 4,
          "sentence_length_spread": 0.48963502403372866,
          "style_score": 0.4409,
          "type_token_ratio": 0.7415730337078652,
          "word_count": 89
        },
        "style_score": 0.4409,
        "text_length": 501,
        "timestamp": "2026-11-08T21:53:17+00:00"
      },
      "elapsed_ms": 48.48,
      "input_id": "human-06",
      "input_provenance": {
        "id": "human-06",
        "text": "You will rejoice to hear that no disaster has accompanied the commencement of an enterprise which you have regarded with such evil forebodings. I arrived here yesterday, and my first task is to assure my dear sister of my welfare and increasing confidence in the success of my undertaking. I am already far north of London, and as I walk in the streets of Petersburgh, I feel a cold northern breeze play upon my cheeks, which braces my nerves and fills me with delight. Do you understand this feeling?",
        "source_url": "https://www.gutenberg.org/cache/epub/84/pg84.txt",
        "author": "Mary Wollstonecraft Shelley",
        "title": "Frankenstein; or, The Modern Prometheus",
        "publication_year": 1818,
        "location": "Letter 1, opening through 'Do you understand this feeling?'",
        "genre": "epistolary literary fiction",
        "provenance": "Exact public-domain excerpt from the Project Gutenberg text of Shelley's novel, verified against the linked primary text on 2026-10-30. The work first appeared in 1818 and was revised in 1831; this is a transcription from the linked edition, not a claim that it is the 1818 wording. Whitespace normalized."
      }
    },
    {
      "method": "POST",
      "url": "http://127.0.0.1:5054/submit",
      "request_json": {
        "text": "Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, \u201cand what is the use of a book,\u201d thought Alice \u201cwithout pictures or conversations?\u201d So she was considering in her own mind (as well as she could, for the hot day made her feel very sleepy and stupid), whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her.",
        "creator_id": "eval-after-c4-t1-human-07"
      },
      "status_code": 200,
      "content_type": "application/json",
      "response_json": {
        "combined_score": 0.5606,
        "confidence": 0.5606,
        "content_id": "b5dea10f-94b1-4898-b93d-776f9ae8edc5",
        "creator_id": "eval-after-c4-t1-human-07",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.5745,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.5,
          "punctuation_density": 0.035343035343035345,
          "punctuation_simplicity": 0.7054747054747055,
          "repetition": 0.3790560471976401,
          "sentence_count": 2,
          "sentence_length_spread": 0.008849557522123894,
          "style_score": 0.5048,
          "type_token_ratio": 0.672566371681416,
          "word_count": 113
        },
        "style_score": 0.5048,
        "text_length": 592,
        "timestamp": "2026-11-08T21:53:17+00:00"
      },
      "elapsed_ms": 57.98,
      "input_id": "human-07",
      "input_provenance": {
        "id": "human-07",
        "text": "Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, \u201cand what is the use of a book,\u201d thought Alice \u201cwithout pictures or conversations?\u201d So she was considering in her own mind (as well as she could, for the hot day made her feel very sleepy and stupid), whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her.",
        "source_url": "https://www.gutenberg.org/cache/epub/11/pg11.txt",
        "author": "Lewis Carroll",
        "title": "Alice's Adventures in Wonderland",
        "publication_year": 1865,
        "location": "Chapter I, Down the Rabbit-Hole, first two paragraphs",
        "genre": "literary fiction",
        "provenance": "Exact public-domain excerpt from the Project Gutenberg edition of Carroll's published novel, verified against the linked primary text on 2026-10-30. Whitespace normalized."
      }
    },
    {
      "method": "POST",
      "url": "http://127.0.0.1:5054/submit",
      "request_json": {
        "text": "When on board H.M.S. \u2018Beagle,\u2019 as naturalist, I was much struck with certain facts in the distribution of the inhabitants of South America, and in the geological relations of the present to the past inhabitants of that continent. These facts seemed to me to throw some light on the origin of species\u2014that mystery of mysteries, as it has been called by one of our greatest philosophers. On my return home, it occurred to me, in 1837, that something might perhaps be made out on this question by patiently accumulating and reflecting on all sorts of facts which could possibly have any bearing on it.",
        "creator_id": "eval-after-c4-t1-human-08"
      },
      "status_code": 200,
      "content_type": "application/json",
      "response_json": {
        "combined_score": 0.5581,
        "confidence": 0.5581,
        "content_id": "b4b9c1cb-83bc-483c-8c1d-5aa1fd642974",
        "creator_id": "eval-after-c4-t1-human-08",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.5825,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.420697370644045,
          "punctuation_density": 0.03232323232323232,
          "punctuation_simplicity": 0.7306397306397306,
          "repetition": 0.3473520249221185,
          "sentence_count": 4,
          "sentence_length_spread": 0.46344210348476406,
          "style_score": 0.4607,
          "type_token_ratio": 0.6915887850467289,
          "word_count": 107
        },
        "style_score": 0.4607,
        "text_length": 598,
        "timestamp": "2026-11-08T21:53:17+00:00"
      },
      "elapsed_ms": 52.57,
      "input_id": "human-08",
      "input_provenance": {
        "id": "human-08",
        "text": "When on board H.M.S. \u2018Beagle,\u2019 as naturalist, I was much struck with certain facts in the distribution of the inhabitants of South America, and in the geological relations of the present to the past inhabitants of that continent. These facts seemed to me to throw some light on the origin of species\u2014that mystery of mysteries, as it has been called by one of our greatest philosophers. On my return home, it occurred to me, in 1837, that something might perhaps be made out on this question by patiently accumulating and reflecting on all sorts of facts which could possibly have any bearing on it.",
        "source_url": "https://www.gutenberg.org/cache/epub/1228/pg1228.txt",
        "author": "Charles Darwin",
        "title": "On the Origin of Species By Means of Natural Selection",
        "publication_year": 1859,
        "location": "Introduction, first three sentences",
        "genre": "formal scientific nonfiction",
        "provenance": "Exact public-domain excerpt from the Project Gutenberg edition of Darwin's published work, verified against the linked primary text on 2026-10-30. Whitespace normalized."
      }
    },
    {
      "method": "POST",
      "url": "http://127.0.0.1:5054/submit",
      "request_json": {
        "text": "The produce of industry is what it adds to the subject or materials upon which it is employed. In proportion as the value of this produce is great or small, so will likewise be the profits of the employer. But it is only for the sake of profit that any man employs a capital in the support of industry; and he will always, therefore, endeavour to employ it in the support of that industry of which the produce is likely to be of the greatest value, or to exchange for the greatest quantity either of money or of other goods.",
        "creator_id": "eval-after-c4-t1-human-09"
      },
      "status_code": 200,
      "content_type": "application/json",
      "response_json": {
        "combined_score": 0.7081,
        "confidence": 0.7081,
        "content_id": "08af0d7c-15c4-49e7-85a3-d110edb24398",
        "creator_id": "eval-after-c4-t1-human-09",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.7648,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.26494047860054226,
          "punctuation_density": 0.018823529411764704,
          "punctuation_simplicity": 0.8431372549019608,
          "repetition": 0.6,
          "sentence_count": 3,
          "sentence_length_spread": 0.5880476171195662,
          "style_score": 0.4811,
          "type_token_ratio": 0.54,
          "word_count": 100
        },
        "style_score": 0.4811,
        "text_length": 524,
        "timestamp": "2026-11-08T21:53:17+00:00"
      },
      "elapsed_ms": 49.35,
      "input_id": "human-09",
      "input_provenance": {
        "id": "human-09",
        "text": "The produce of industry is what it adds to the subject or materials upon which it is employed. In proportion as the value of this produce is great or small, so will likewise be the profits of the employer. But it is only for the sake of profit that any man employs a capital in the support of industry; and he will always, therefore, endeavour to employ it in the support of that industry of which the produce is likely to be of the greatest value, or to exchange for the greatest quantity either of money or of other goods.",
        "source_url": "https://www.gutenberg.org/cache/epub/3300/pg3300.txt",
        "author": "Adam Smith",
        "title": "An Inquiry into the Nature and Causes of the Wealth of Nations",
        "publication_year": 1776,
        "location": "Book IV, Chapter II, paragraph beginning 'The produce of industry'",
        "genre": "formal economic nonfiction",
        "provenance": "Exact public-domain excerpt from the Project Gutenberg edition of Smith's published work, verified against the linked primary text on 2026-10-30. Whitespace normalized."
      }
    },
    {
      "method": "POST",
      "url": "http://127.0.0.1:5054/submit",
      "request_json": {
        "text": "My elder brothers were all put apprentices to different trades. I was put to the grammar-school at eight years of age, my father intending to devote me, as the tithe[13] of his sons, to the service of the Church. My early readiness in learning to read (which must have been very early, as I do not remember when I could not read), and the opinion of all his friends, that I should certainly make a good scholar, encouraged him in this purpose of his. My uncle Benjamin, too, approved of it, and proposed to give me all his short-hand volumes of sermons, I suppose as a stock to set up with, if I would learn his character.[14]",
        "creator_id": "eval-after-c4-t1-human-10"
      },
      "status_code": 200,
      "content_type": "application/json",
      "response_json": {
        "combined_score": 0.5475,
        "confidence": 0.5475,
        "content_id": "254db630-161f-444d-9188-e55bdf4c88b0",
        "creator_id": "eval-after-c4-t1-human-10",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.566,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.4729379744287563,
          "punctuation_density": 0.047058823529411764,
          "punctuation_simplicity": 0.607843137254902,
          "repetition": 0.3842975206611571,
          "sentence_count": 4,
          "sentence_length_spread": 0.421649620456995,
          "style_score": 0.4733,
          "type_token_ratio": 0.6694214876033058,
          "word_count": 121
        },
        "style_score": 0.4733,
        "text_length": 626,
        "timestamp": "2026-11-08T21:53:17+00:00"
      },
      "elapsed_ms": 61.06,
      "input_id": "human-10",
      "input_provenance": {
        "id": "human-10",
        "text": "My elder brothers were all put apprentices to different trades. I was put to the grammar-school at eight years of age, my father intending to devote me, as the tithe[13] of his sons, to the service of the Church. My early readiness in learning to read (which must have been very early, as I do not remember when I could not read), and the opinion of all his friends, that I should certainly make a good scholar, encouraged him in this purpose of his. My uncle Benjamin, too, approved of it, and proposed to give me all his short-hand volumes of sermons, I suppose as a stock to set up with, if I would learn his character.[14]",
        "source_url": "https://www.gutenberg.org/cache/epub/20203/pg20203.txt",
        "author": "Benjamin Franklin",
        "title": "Autobiography of Benjamin Franklin",
        "publication_year": 1791,
        "location": "Passage beginning 'My elder brothers were all put apprentices', first four sentences",
        "genre": "first-person autobiographical nonfiction",
        "provenance": "Exact public-domain excerpt from the Project Gutenberg transcription of the 1916 English edition (1922 printing), verified against the linked primary text on 2026-10-30. The memoir was composed in 1771\u20131790 and initially published in French in 1791. The linked edition states that its text follows Bigelow's nineteenth-century editions. Edition footnote markers retained; whitespace normalized."
      }
    }
  ],
  "unknown_id": {
    "method": "POST",
    "url": "http://127.0.0.1:5054/appeal",
    "request_json": {
      "content_id": "510b0553-acad-4561-ac88-0527a3e9aa9f",
      "reasoning": "Unknown-ID development check."
    },
    "status_code": 404,
    "content_type": "application/json",
    "response_json": {
      "error": "content_not_found",
      "message": "No submission exists with this content_id."
    },
    "elapsed_ms": 3.04
  },
  "fresh_instance": {
    "detector_loaded": false,
    "items": [
      {
        "content_id": "57f55524-8978-43d5-bc0b-e1396115c1d2",
        "status_code": 200,
        "response": {
          "appeals": [
            {
              "content_id": "57f55524-8978-43d5-bc0b-e1396115c1d2",
              "creator_id": "eval-after-c4-t1-human-01",
              "event": "appeal",
              "reasoning": "Part 2 criterion review after, trial 1: please inspect this estimate.",
              "status": "under_review",
              "timestamp": "2026-11-08T21:53:17+00:00"
            }
          ],
          "combined_score": 0.6593,
          "confidence": 0.6593,
          "content_id": "57f55524-8978-43d5-bc0b-e1396115c1d2",
          "creator_id": "eval-after-c4-t1-human-01",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.6922,
          "status": "under_review",
          "style_metrics": {
            "evenness": 0.5,
            "punctuation_density": 0.016286644951140065,
            "punctuation_simplicity": 0.8642779587404994,
            "repetition": 0.34976525821596255,
            "sentence_count": 2,
            "sentence_length_spread": 0.352112676056338,
            "style_score": 0.5278,
            "type_token_ratio": 0.6901408450704225,
            "word_count": 71
          },
          "style_score": 0.5278,
          "text_length": 377,
          "timestamp": "2026-11-08T21:53:17+00:00"
        }
      },
      {
        "content_id": "b7e898ca-5f47-4dd8-8892-45b55232cc1b",
        "status_code": 200,
        "response": {
          "appeals": [
            {
              "content_id": "b7e898ca-5f47-4dd8-8892-45b55232cc1b",
              "creator_id": "eval-after-c4-t1-human-02",
              "event": "appeal",
              "reasoning": "Part 2 criterion review after, trial 1: please inspect this estimate.",
              "status": "under_review",
              "timestamp": "2026-11-08T21:53:17+00:00"
            }
          ],
          "combined_score": 0.4608,
          "confidence": 0.4608,
          "content_id": "b7e898ca-5f47-4dd8-8892-45b55232cc1b",
          "creator_id": "eval-after-c4-t1-human-02",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.4863,
          "status": "under_review",
          "style_metrics": {
            "evenness": 0.2554540936099331,
            "punctuation_density": 0.04021937842778794,
            "punctuation_simplicity": 0.6648385131017671,
            "repetition": 0.3276836158192091,
            "sentence_count": 4,
            "sentence_length_spread": 0.5956367251120536,
            "style_score": 0.359,
            "type_token_ratio": 0.7033898305084746,
            "word_count": 118
          },
          "style_score": 0.359,
          "text_length": 664,
          "timestamp": "2026-11-08T21:53:17+00:00"
        }
      },
      {
        "content_id": "f6b5b60c-af1a-48a6-87c2-ee3a86448830",
        "status_code": 200,
        "response": {
          "appeals": [
            {
              "content_id": "f6b5b60c-af1a-48a6-87c2-ee3a86448830",
              "creator_id": "eval-after-c4-t1-human-03",
              "event": "appeal",
              "reasoning": "Part 2 criterion review after, trial 1: please inspect this estimate.",
              "status": "under_review",
              "timestamp": "2026-11-08T21:53:17+00:00"
            }
          ],
          "combined_score": 0.3358,
          "confidence": 0.3358,
          "content_id": "f6b5b60c-af1a-48a6-87c2-ee3a86448830",
          "creator_id": "eval-after-c4-t1-human-03",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.3532,
          "status": "under_review",
          "style_metrics": {
            "evenness": 0.0,
            "punctuation_density": 0.027522935779816515,
            "punctuation_simplicity": 0.7706422018348624,
            "repetition": 0.37356321839080464,
            "sentence_count": 4,
            "sentence_length_spread": 0.8882105351861661,
            "style_score": 0.2662,
            "type_token_ratio": 0.6758620689655173,
            "word_count": 145
          },
          "style_score": 0.2662,
          "text_length": 795,
          "timestamp": "2026-11-08T21:53:17+00:00"
        }
      },
      {
        "content_id": "c6bb7613-5d3b-4627-847d-6f05a08f9b72",
        "status_code": 200,
        "response": {
          "appeals": [
            {
              "content_id": "c6bb7613-5d3b-4627-847d-6f05a08f9b72",
              "creator_id": "eval-after-c4-t1-human-04",
              "event": "appeal",
              "reasoning": "Part 2 criterion review after, trial 1: please inspect this estimate.",
              "status": "under_review",
              "timestamp": "2026-11-08T21:53:17+00:00"
            }
          ],
          "combined_score": 0.3954,
          "confidence": 0.3954,
          "content_id": "c6bb7613-5d3b-4627-847d-6f05a08f9b72",
          "creator_id": "eval-after-c4-t1-human-04",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.4097,
          "status": "under_review",
          "style_metrics": {
            "evenness": 0.16602391043278608,
            "punctuation_density": 0.053691275167785234,
            "punctuation_simplicity": 0.5525727069351231,
            "repetition": 0.48148148148148145,
            "sentence_count": 7,
            "sentence_length_spread": 0.6671808716537712,
            "style_score": 0.338,
            "type_token_ratio": 0.6111111111111112,
            "word_count": 108
          },
          "style_score": 0.338,
          "text_length": 552,
          "timestamp": "2026-11-08T21:53:17+00:00"
        }
      },
      {
        "content_id": "a6fc5c38-d603-4b8a-ac01-117d39c31d32",
        "status_code": 200,
        "response": {
          "appeals": [
            {
              "content_id": "a6fc5c38-d603-4b8a-ac01-117d39c31d32",
              "creator_id": "eval-after-c4-t1-human-05",
              "event": "appeal",
              "reasoning": "Part 2 criterion review after, trial 1: please inspect this estimate.",
              "status": "under_review",
              "timestamp": "2026-11-08T21:53:17+00:00"
            }
          ],
          "combined_score": 0.6497,
          "confidence": 0.6497,
          "content_id": "a6fc5c38-d603-4b8a-ac01-117d39c31d32",
          "creator_id": "eval-after-c4-t1-human-05",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.7577,
          "status": "under_review",
          "style_metrics": {
            "evenness": 0.0,
            "punctuation_density": 0.04195804195804196,
            "punctuation_simplicity": 0.6503496503496503,
            "repetition": 0.29227053140096626,
            "sentence_count": 3,
            "sentence_length_spread": 0.8615573303015565,
            "style_score": 0.2178,
            "type_token_ratio": 0.7246376811594203,
            "word_count": 69
          },
          "style_score": 0.2178,
          "text_length": 354,
          "timestamp": "2026-11-08T21:53:17+00:00"
        }
      },
      {
        "content_id": "0b8faa49-4a87-4a5a-a07f-576e2ca772f3",
        "status_code": 200,
        "response": {
          "appeals": [
            {
              "content_id": "0b8faa49-4a87-4a5a-a07f-576e2ca772f3",
              "creator_id": "eval-after-c4-t1-human-06",
              "event": "appeal",
              "reasoning": "Part 2 criterion review after, trial 1: please inspect this estimate.",
              "status": "under_review",
              "timestamp": "2026-11-08T21:53:18+00:00"
            }
          ],
          "combined_score": 0.5545,
          "confidence": 0.5545,
          "content_id": "0b8faa49-4a87-4a5a-a07f-576e2ca772f3",
          "creator_id": "eval-after-c4-t1-human-06",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.5829,
          "status": "under_review",
          "style_metrics": {
            "evenness": 0.38795621995783924,
            "punctuation_density": 0.01937046004842615,
            "punctuation_simplicity": 0.8385794995964487,
            "repetition": 0.2640449438202247,
            "sentence_count": 4,
            "sentence_length_spread": 0.48963502403372866,
            "style_score": 0.4409,
            "type_token_ratio": 0.7415730337078652,
            "word_count": 89
          },
          "style_score": 0.4409,
          "text_length": 501,
          "timestamp": "2026-11-08T21:53:17+00:00"
        }
      },
      {
        "content_id": "b5dea10f-94b1-4898-b93d-776f9ae8edc5",
        "status_code": 200,
        "response": {
          "appeals": [
            {
              "content_id": "b5dea10f-94b1-4898-b93d-776f9ae8edc5",
              "creator_id": "eval-after-c4-t1-human-07",
              "event": "appeal",
              "reasoning": "Part 2 criterion review after, trial 1: please inspect this estimate.",
              "status": "under_review",
              "timestamp": "2026-11-08T21:53:18+00:00"
            }
          ],
          "combined_score": 0.5606,
          "confidence": 0.5606,
          "content_id": "b5dea10f-94b1-4898-b93d-776f9ae8edc5",
          "creator_id": "eval-after-c4-t1-human-07",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.5745,
          "status": "under_review",
          "style_metrics": {
            "evenness": 0.5,
            "punctuation_density": 0.035343035343035345,
            "punctuation_simplicity": 0.7054747054747055,
            "repetition": 0.3790560471976401,
            "sentence_count": 2,
            "sentence_length_spread": 0.008849557522123894,
            "style_score": 0.5048,
            "type_token_ratio": 0.672566371681416,
            "word_count": 113
          },
          "style_score": 0.5048,
          "text_length": 592,
          "timestamp": "2026-11-08T21:53:17+00:00"
        }
      },
      {
        "content_id": "b4b9c1cb-83bc-483c-8c1d-5aa1fd642974",
        "status_code": 200,
        "response": {
          "appeals": [
            {
              "content_id": "b4b9c1cb-83bc-483c-8c1d-5aa1fd642974",
              "creator_id": "eval-after-c4-t1-human-08",
              "event": "appeal",
              "reasoning": "Part 2 criterion review after, trial 1: please inspect this estimate.",
              "status": "under_review",
              "timestamp": "2026-11-08T21:53:18+00:00"
            }
          ],
          "combined_score": 0.5581,
          "confidence": 0.5581,
          "content_id": "b4b9c1cb-83bc-483c-8c1d-5aa1fd642974",
          "creator_id": "eval-after-c4-t1-human-08",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.5825,
          "status": "under_review",
          "style_metrics": {
            "evenness": 0.420697370644045,
            "punctuation_density": 0.03232323232323232,
            "punctuation_simplicity": 0.7306397306397306,
            "repetition": 0.3473520249221185,
            "sentence_count": 4,
            "sentence_length_spread": 0.46344210348476406,
            "style_score": 0.4607,
            "type_token_ratio": 0.6915887850467289,
            "word_count": 107
          },
          "style_score": 0.4607,
          "text_length": 598,
          "timestamp": "2026-11-08T21:53:17+00:00"
        }
      },
      {
        "content_id": "08af0d7c-15c4-49e7-85a3-d110edb24398",
        "status_code": 200,
        "response": {
          "appeals": [
            {
              "content_id": "08af0d7c-15c4-49e7-85a3-d110edb24398",
              "creator_id": "eval-after-c4-t1-human-09",
              "event": "appeal",
              "reasoning": "Part 2 criterion review after, trial 1: please inspect this estimate.",
              "status": "under_review",
              "timestamp": "2026-11-08T21:53:18+00:00"
            }
          ],
          "combined_score": 0.7081,
          "confidence": 0.7081,
          "content_id": "08af0d7c-15c4-49e7-85a3-d110edb24398",
          "creator_id": "eval-after-c4-t1-human-09",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.7648,
          "status": "under_review",
          "style_metrics": {
            "evenness": 0.26494047860054226,
            "punctuation_density": 0.018823529411764704,
            "punctuation_simplicity": 0.8431372549019608,
            "repetition": 0.6,
            "sentence_count": 3,
            "sentence_length_spread": 0.5880476171195662,
            "style_score": 0.4811,
            "type_token_ratio": 0.54,
            "word_count": 100
          },
          "style_score": 0.4811,
          "text_length": 524,
          "timestamp": "2026-11-08T21:53:17+00:00"
        }
      },
      {
        "content_id": "254db630-161f-444d-9188-e55bdf4c88b0",
        "status_code": 200,
        "response": {
          "appeals": [
            {
              "content_id": "254db630-161f-444d-9188-e55bdf4c88b0",
              "creator_id": "eval-after-c4-t1-human-10",
              "event": "appeal",
              "reasoning": "Part 2 criterion review after, trial 1: please inspect this estimate.",
              "status": "under_review",
              "timestamp": "2026-11-08T21:53:18+00:00"
            }
          ],
          "combined_score": 0.5475,
          "confidence": 0.5475,
          "content_id": "254db630-161f-444d-9188-e55bdf4c88b0",
          "creator_id": "eval-after-c4-t1-human-10",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.566,
          "status": "under_review",
          "style_metrics": {
            "evenness": 0.4729379744287563,
            "punctuation_density": 0.047058823529411764,
            "punctuation_simplicity": 0.607843137254902,
            "repetition": 0.3842975206611571,
            "sentence_count": 4,
            "sentence_length_spread": 0.421649620456995,
            "style_score": 0.4733,
            "type_token_ratio": 0.6694214876033058,
            "word_count": 121
          },
          "style_score": 0.4733,
          "text_length": 626,
          "timestamp": "2026-11-08T21:53:17+00:00"
        }
      }
    ],
    "passed": true
  },
  "summary": "10/10 appeals; persistence True",
  "passed": true,
  "no_rescoring_evidence": "Fresh instance remains detector_loaded=false; isolated service tests separately patch the detector and assert zero appeal calls.",
  "verdict": "MET"
}
```

### Criterion 5

Produced by `run_eval.py::trial_result` (bad_input).

```json
{
  "trial": 1,
  "criterion": 5,
  "kind": "bad_input",
  "cases": [
    {
      "matrix_group": 1,
      "name": "missing text",
      "expected_status": 400,
      "http": {
        "method": "POST",
        "url": "http://127.0.0.1:5054/submit",
        "request_json": {
          "creator_id": "eval-after-c5-t1-case0"
        },
        "status_code": 400,
        "content_type": "application/json",
        "response_json": {
          "error": "invalid_text",
          "message": "text must be a nonempty string."
        },
        "elapsed_ms": 1.33
      },
      "passed": true
    },
    {
      "matrix_group": 2,
      "name": "empty text",
      "expected_status": 400,
      "http": {
        "method": "POST",
        "url": "http://127.0.0.1:5054/submit",
        "request_json": {
          "text": "",
          "creator_id": "eval-after-c5-t1-case1"
        },
        "status_code": 400,
        "content_type": "application/json",
        "response_json": {
          "error": "invalid_text",
          "message": "text must be a nonempty string."
        },
        "elapsed_ms": 0.92
      },
      "passed": true
    },
    {
      "matrix_group": 3,
      "name": "whitespace text",
      "expected_status": 400,
      "http": {
        "method": "POST",
        "url": "http://127.0.0.1:5054/submit",
        "request_json": {
          "text": "                              ",
          "creator_id": "eval-after-c5-t1-case2"
        },
        "status_code": 400,
        "content_type": "application/json",
        "response_json": {
          "error": "invalid_text",
          "message": "text must be a nonempty string."
        },
        "elapsed_ms": 0.87
      },
      "passed": true
    },
    {
      "matrix_group": 4,
      "name": "non-string text NoneType",
      "expected_status": 400,
      "http": {
        "method": "POST",
        "url": "http://127.0.0.1:5054/submit",
        "request_json": {
          "text": null,
          "creator_id": "eval-after-c5-t1-case3"
        },
        "status_code": 400,
        "content_type": "application/json",
        "response_json": {
          "error": "invalid_text",
          "message": "text must be a nonempty string."
        },
        "elapsed_ms": 0.96
      },
      "passed": true
    },
    {
      "matrix_group": 4,
      "name": "non-string text int",
      "expected_status": 400,
      "http": {
        "method": "POST",
        "url": "http://127.0.0.1:5054/submit",
        "request_json": {
          "text": 9,
          "creator_id": "eval-after-c5-t1-case4"
        },
        "status_code": 400,
        "content_type": "application/json",
        "response_json": {
          "error": "invalid_text",
          "message": "text must be a nonempty string."
        },
        "elapsed_ms": 0.88
      },
      "passed": true
    },
    {
      "matrix_group": 4,
      "name": "non-string text list",
      "expected_status": 400,
      "http": {
        "method": "POST",
        "url": "http://127.0.0.1:5054/submit",
        "request_json": {
          "text": [
            "word",
            "word",
            "word",
            "word",
            "word"
          ],
          "creator_id": "eval-after-c5-t1-case5"
        },
        "status_code": 400,
        "content_type": "application/json",
        "response_json": {
          "error": "invalid_text",
          "message": "text must be a nonempty string."
        },
        "elapsed_ms": 0.79
      },
      "passed": true
    },
    {
      "matrix_group": 5,
      "name": "too few characters",
      "expected_status": 400,
      "http": {
        "method": "POST",
        "url": "http://127.0.0.1:5054/submit",
        "request_json": {
          "text": "one two three four",
          "creator_id": "eval-after-c5-t1-case6"
        },
        "status_code": 400,
        "content_type": "application/json",
        "response_json": {
          "error": "text_too_short",
          "message": "text needs at least 20 characters and 5 word tokens."
        },
        "elapsed_ms": 0.74
      },
      "passed": true
    },
    {
      "matrix_group": 5,
      "name": "too few words",
      "expected_status": 400,
      "http": {
        "method": "POST",
        "url": "http://127.0.0.1:5054/submit",
        "request_json": {
          "text": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
          "creator_id": "eval-after-c5-t1-case7"
        },
        "status_code": 400,
        "content_type": "application/json",
        "response_json": {
          "error": "text_too_short",
          "message": "text needs at least 20 characters and 5 word tokens."
        },
        "elapsed_ms": 0.73
      },
      "passed": true
    },
    {
      "matrix_group": 6,
      "name": "oversized text",
      "expected_status": 413,
      "http": {
        "method": "POST",
        "url": "http://127.0.0.1:5054/submit",
        "request_json": {
          "text": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
          "creator_id": "eval-after-c5-t1-case8"
        },
        "status_code": 413,
        "content_type": "application/json",
        "response_json": {
          "error": "text_too_large",
          "message": "text must not exceed 10,000 characters."
        },
        "elapsed_ms": 0.83
      },
      "passed": true
    },
    {
      "matrix_group": 7,
      "name": "missing creator",
      "expected_status": 400,
      "http": {
        "method": "POST",
        "url": "http://127.0.0.1:5054/submit",
        "request_json": {
          "text": "This development paragraph contains enough ordinary words to validate."
        },
        "status_code": 400,
        "content_type": "application/json",
        "response_json": {
          "error": "invalid_creator_id",
          "message": "creator_id must be a nonempty string of at most 128 characters."
        },
        "elapsed_ms": 0.84
      },
      "passed": true
    },
    {
      "matrix_group": 8,
      "name": "blank creator",
      "expected_status": 400,
      "http": {
        "method": "POST",
        "url": "http://127.0.0.1:5054/submit",
        "request_json": {
          "text": "This development paragraph contains enough ordinary words to validate.",
          "creator_id": ""
        },
        "status_code": 400,
        "content_type": "application/json",
        "response_json": {
          "error": "invalid_creator_id",
          "message": "creator_id must be a nonempty string of at most 128 characters."
        },
        "elapsed_ms": 0.78
      },
      "passed": true
    },
    {
      "matrix_group": 8,
      "name": "blank creator",
      "expected_status": 400,
      "http": {
        "method": "POST",
        "url": "http://127.0.0.1:5054/submit",
        "request_json": {
          "text": "This development paragraph contains enough ordinary words to validate.",
          "creator_id": "  "
        },
        "status_code": 400,
        "content_type": "application/json",
        "response_json": {
          "error": "invalid_creator_id",
          "message": "creator_id must be a nonempty string of at most 128 characters."
        },
        "elapsed_ms": 0.72
      },
      "passed": true
    },
    {
      "matrix_group": 9,
      "name": "non-string creator",
      "expected_status": 400,
      "http": {
        "method": "POST",
        "url": "http://127.0.0.1:5054/submit",
        "request_json": {
          "text": "This development paragraph contains enough ordinary words to validate.",
          "creator_id": 42
        },
        "status_code": 400,
        "content_type": "application/json",
        "response_json": {
          "error": "invalid_creator_id",
          "message": "creator_id must be a nonempty string of at most 128 characters."
        },
        "elapsed_ms": 0.75
      },
      "passed": true
    },
    {
      "matrix_group": 10,
      "name": "oversized creator",
      "expected_status": 400,
      "http": {
        "method": "POST",
        "url": "http://127.0.0.1:5054/submit",
        "request_json": {
          "text": "This development paragraph contains enough ordinary words to validate.",
          "creator_id": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        },
        "status_code": 400,
        "content_type": "application/json",
        "response_json": {
          "error": "invalid_creator_id",
          "message": "creator_id must be a nonempty string of at most 128 characters."
        },
        "elapsed_ms": 0.74
      },
      "passed": true
    },
    {
      "matrix_group": 11,
      "name": "malformed JSON",
      "expected_status": 400,
      "http": {
        "method": "POST",
        "url": "http://127.0.0.1:5054/submit",
        "request_body": "{",
        "request_headers": {
          "Content-Type": "application/json"
        },
        "status_code": 400,
        "content_type": "application/json",
        "response_json": {
          "error": "invalid_json",
          "message": "Send a valid JSON object."
        },
        "elapsed_ms": 0.88
      },
      "passed": true
    },
    {
      "matrix_group": 12,
      "name": "non-object JSON []",
      "expected_status": 400,
      "http": {
        "method": "POST",
        "url": "http://127.0.0.1:5054/submit",
        "request_body": "[]",
        "request_headers": {
          "Content-Type": "application/json"
        },
        "status_code": 400,
        "content_type": "application/json",
        "response_json": {
          "error": "invalid_json",
          "message": "Send a valid JSON object."
        },
        "elapsed_ms": 0.74
      },
      "passed": true
    },
    {
      "matrix_group": 12,
      "name": "non-object JSON null",
      "expected_status": 400,
      "http": {
        "method": "POST",
        "url": "http://127.0.0.1:5054/submit",
        "request_body": "null",
        "request_headers": {
          "Content-Type": "application/json"
        },
        "status_code": 400,
        "content_type": "application/json",
        "response_json": {
          "error": "invalid_json",
          "message": "Send a valid JSON object."
        },
        "elapsed_ms": 0.77
      },
      "passed": true
    },
    {
      "matrix_group": 12,
      "name": "non-object JSON \"text\"",
      "expected_status": 400,
      "http": {
        "method": "POST",
        "url": "http://127.0.0.1:5054/submit",
        "request_body": "\"text\"",
        "request_headers": {
          "Content-Type": "application/json"
        },
        "status_code": 400,
        "content_type": "application/json",
        "response_json": {
          "error": "invalid_json",
          "message": "Send a valid JSON object."
        },
        "elapsed_ms": 0.73
      },
      "passed": true
    },
    {
      "matrix_group": 12,
      "name": "non-object JSON 7",
      "expected_status": 400,
      "http": {
        "method": "POST",
        "url": "http://127.0.0.1:5054/submit",
        "request_body": "7",
        "request_headers": {
          "Content-Type": "application/json"
        },
        "status_code": 400,
        "content_type": "application/json",
        "response_json": {
          "error": "invalid_json",
          "message": "Send a valid JSON object."
        },
        "elapsed_ms": 0.73
      },
      "passed": true
    },
    {
      "matrix_group": 13,
      "name": "non-JSON content type",
      "expected_status": 415,
      "http": {
        "method": "POST",
        "url": "http://127.0.0.1:5054/submit",
        "request_body": "hello",
        "request_headers": {
          "Content-Type": "text/plain"
        },
        "status_code": 429,
        "content_type": "application/json",
        "response_json": {
          "error": "rate_limited",
          "message": "Too many submissions. Try again shortly."
        },
        "elapsed_ms": 0.72
      },
      "passed": false
    },
    {
      "matrix_group": 18,
      "name": "oversized body",
      "expected_status": 413,
      "http": {
        "method": "POST",
        "url": "http://127.0.0.1:5054/submit",
        "request_body": "{\"padding\":\"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\"}",
        "request_headers": {
          "Content-Type": "application/json"
        },
        "status_code": 413,
        "content_type": "application/json",
        "response_json": {
          "error": "request_too_large",
          "message": "Request body must not exceed 65,536 bytes."
        },
        "elapsed_ms": 0.68
      },
      "passed": true
    },
    {
      "matrix_group": 11,
      "name": "malformed JSON",
      "expected_status": 400,
      "http": {
        "method": "POST",
        "url": "http://127.0.0.1:5054/appeal",
        "request_body": "{",
        "request_headers": {
          "Content-Type": "application/json"
        },
        "status_code": 400,
        "content_type": "application/json",
        "response_json": {
          "error": "invalid_json",
          "message": "Send a valid JSON object."
        },
        "elapsed_ms": 0.69
      },
      "passed": true
    },
    {
      "matrix_group": 12,
      "name": "non-object JSON []",
      "expected_status": 400,
      "http": {
        "method": "POST",
        "url": "http://127.0.0.1:5054/appeal",
        "request_body": "[]",
        "request_headers": {
          "Content-Type": "application/json"
        },
        "status_code": 400,
        "content_type": "application/json",
        "response_json": {
          "error": "invalid_json",
          "message": "Send a valid JSON object."
        },
        "elapsed_ms": 0.65
      },
      "passed": true
    },
    {
      "matrix_group": 12,
      "name": "non-object JSON null",
      "expected_status": 400,
      "http": {
        "method": "POST",
        "url": "http://127.0.0.1:5054/appeal",
        "request_body": "null",
        "request_headers": {
          "Content-Type": "application/json"
        },
        "status_code": 400,
        "content_type": "application/json",
        "response_json": {
          "error": "invalid_json",
          "message": "Send a valid JSON object."
        },
        "elapsed_ms": 0.68
      },
      "passed": true
    },
    {
      "matrix_group": 12,
      "name": "non-object JSON \"text\"",
      "expected_status": 400,
      "http": {
        "method": "POST",
        "url": "http://127.0.0.1:5054/appeal",
        "request_body": "\"text\"",
        "request_headers": {
          "Content-Type": "application/json"
        },
        "status_code": 400,
        "content_type": "application/json",
        "response_json": {
          "error": "invalid_json",
          "message": "Send a valid JSON object."
        },
        "elapsed_ms": 0.7
      },
      "passed": true
    },
    {
      "matrix_group": 12,
      "name": "non-object JSON 7",
      "expected_status": 400,
      "http": {
        "method": "POST",
        "url": "http://127.0.0.1:5054/appeal",
        "request_body": "7",
        "request_headers": {
          "Content-Type": "application/json"
        },
        "status_code": 400,
        "content_type": "application/json",
        "response_json": {
          "error": "invalid_json",
          "message": "Send a valid JSON object."
        },
        "elapsed_ms": 0.76
      },
      "passed": true
    },
    {
      "matrix_group": 13,
      "name": "non-JSON content type",
      "expected_status": 415,
      "http": {
        "method": "POST",
        "url": "http://127.0.0.1:5054/appeal",
        "request_body": "hello",
        "request_headers": {
          "Content-Type": "text/plain"
        },
        "status_code": 415,
        "content_type": "application/json",
        "response_json": {
          "error": "json_required",
          "message": "Send an application/json request body."
        },
        "elapsed_ms": 0.71
      },
      "passed": true
    },
    {
      "matrix_group": 18,
      "name": "oversized body",
      "expected_status": 413,
      "http": {
        "method": "POST",
        "url": "http://127.0.0.1:5054/appeal",
        "request_body": "{\"padding\":\"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\"}",
        "request_headers": {
          "Content-Type": "application/json"
        },
        "status_code": 413,
        "content_type": "application/json",
        "response_json": {
          "error": "request_too_large",
          "message": "Request body must not exceed 65,536 bytes."
        },
        "elapsed_ms": 0.64
      },
      "passed": true
    },
    {
      "matrix_group": 14,
      "name": "missing content id",
      "expected_status": 400,
      "http": {
        "method": "POST",
        "url": "http://127.0.0.1:5054/appeal",
        "request_json": {
          "reasoning": "Review this."
        },
        "status_code": 400,
        "content_type": "application/json",
        "response_json": {
          "error": "invalid_content_id",
          "message": "content_id must be a nonempty UUID string."
        },
        "elapsed_ms": 0.66
      },
      "passed": true
    },
    {
      "matrix_group": 14,
      "name": "non-string content id",
      "expected_status": 400,
      "http": {
        "method": "POST",
        "url": "http://127.0.0.1:5054/appeal",
        "request_json": {
          "content_id": 42,
          "reasoning": "Development review request."
        },
        "status_code": 400,
        "content_type": "application/json",
        "response_json": {
          "error": "invalid_content_id",
          "message": "content_id must be a nonempty UUID string."
        },
        "elapsed_ms": 0.67
      },
      "passed": true
    },
    {
      "matrix_group": 14,
      "name": "malformed content id",
      "expected_status": 404,
      "http": {
        "method": "POST",
        "url": "http://127.0.0.1:5054/appeal",
        "request_json": {
          "content_id": "typo",
          "reasoning": "Development review request."
        },
        "status_code": 404,
        "content_type": "application/json",
        "response_json": {
          "error": "content_not_found",
          "message": "No submission exists with this content_id."
        },
        "elapsed_ms": 0.75
      },
      "passed": true
    },
    {
      "matrix_group": 14,
      "name": "unknown content id",
      "expected_status": 404,
      "http": {
        "method": "POST",
        "url": "http://127.0.0.1:5054/appeal",
        "request_json": {
          "content_id": "0e20467a-5cb8-4fd1-8ffc-9ff17db2a67f",
          "reasoning": "Development review request."
        },
        "status_code": 404,
        "content_type": "application/json",
        "response_json": {
          "error": "content_not_found",
          "message": "No submission exists with this content_id."
        },
        "elapsed_ms": 2.98
      },
      "passed": true
    },
    {
      "matrix_group": 15,
      "name": "missing reasoning",
      "expected_status": 400,
      "http": {
        "method": "POST",
        "url": "http://127.0.0.1:5054/appeal",
        "request_json": {
          "content_id": "254db630-161f-444d-9188-e55bdf4c88b0"
        },
        "status_code": 400,
        "content_type": "application/json",
        "response_json": {
          "error": "invalid_reasoning",
          "message": "reasoning must be a nonempty string."
        },
        "elapsed_ms": 0.74
      },
      "passed": true
    },
    {
      "matrix_group": 15,
      "name": "blank reasoning",
      "expected_status": 400,
      "http": {
        "method": "POST",
        "url": "http://127.0.0.1:5054/appeal",
        "request_json": {
          "content_id": "254db630-161f-444d-9188-e55bdf4c88b0",
          "reasoning": ""
        },
        "status_code": 400,
        "content_type": "application/json",
        "response_json": {
          "error": "invalid_reasoning",
          "message": "reasoning must be a nonempty string."
        },
        "elapsed_ms": 0.69
      },
      "passed": true
    },
    {
      "matrix_group": 15,
      "name": "blank reasoning",
      "expected_status": 400,
      "http": {
        "method": "POST",
        "url": "http://127.0.0.1:5054/appeal",
        "request_json": {
          "content_id": "254db630-161f-444d-9188-e55bdf4c88b0",
          "reasoning": "  "
        },
        "status_code": 400,
        "content_type": "application/json",
        "response_json": {
          "error": "invalid_reasoning",
          "message": "reasoning must be a nonempty string."
        },
        "elapsed_ms": 0.67
      },
      "passed": true
    },
    {
      "matrix_group": 16,
      "name": "non-string reasoning",
      "expected_status": 400,
      "http": {
        "method": "POST",
        "url": "http://127.0.0.1:5054/appeal",
        "request_json": {
          "content_id": "254db630-161f-444d-9188-e55bdf4c88b0",
          "reasoning": [
            "review"
          ]
        },
        "status_code": 400,
        "content_type": "application/json",
        "response_json": {
          "error": "invalid_reasoning",
          "message": "reasoning must be a nonempty string."
        },
        "elapsed_ms": 0.64
      },
      "passed": true
    },
    {
      "matrix_group": 17,
      "name": "oversized reasoning",
      "expected_status": 413,
      "http": {
        "method": "POST",
        "url": "http://127.0.0.1:5054/appeal",
        "request_json": {
          "content_id": "254db630-161f-444d-9188-e55bdf4c88b0",
          "reasoning": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        },
        "status_code": 413,
        "content_type": "application/json",
        "response_json": {
          "error": "reasoning_too_large",
          "message": "reasoning must not exceed 2,000 characters."
        },
        "elapsed_ms": 0.69
      },
      "passed": true
    }
  ],
  "groups": [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18
  ],
  "successful_events_unchanged": true,
  "summary": "36/37 exact responses; 18/18 groups",
  "passed": false,
  "no_scoring_evidence": "Isolated validation tests assert zero detector calls; the live log contains no added successful events.",
  "verdict": "MISSED"
}
```
