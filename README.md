# Fuzzy String Search [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/MarcSkovMadsen/awesome-streamlit)

[<img src="https://static.vecteezy.com/system/resources/thumbnails/000/623/500/small/5-29.jpg" align="right" height="75" width="100">](https://streamlit.io)

> An advanced application for fuzzy search matching.!


## Description

This is a application that matches incomplete search phrases of popular cartoon series, web series and etc .


Input Field            |  Steps & Mathematical Formulation |
:-------------------------:|:-------------------------: |
![](https://github.com/Sghosh1999/fuzzy_search/blob/3c883d4a077c758536e8b2a76e4cb80e4236c237/images/screen1.PNG)  |  ![](https://github.com/Sghosh1999/fuzzy_search/blob/3c883d4a077c758536e8b2a76e4cb80e4236c237/images/screen2.PNG) |


## Features

- Automatic Search Phrase Matcher.
- Can Handle wrong Spellings.

## Result Dependencies

- The search results are fetching from Google Search API ( rapid API) . So search resposnses may differ in each API call.

## Examples

- The search results are fetching from **Google Search API ( rapid API)** . So **search resposnses may differ** in each API call.

---


### Application Demo

<p align="center">
  <img src="https://github.com/Sghosh1999/AutoGenerateTrackers/blob/78abe5fbcf58ed1054bbfc28e3b3029ba6835384/demos/week_month_demo1.gif" alt="animated" />
</p>

# Steps :heart_eyes:

- Step 1: Generating a Bag Of Words of teh Search results
- Step 2: Calculating Word frequency ofeach words in the Bag Of Words.
- Step 3: Calculating the Stop Index.
- Step 4: Finalizing the results.



<p align="center">
  <img src="https://github.com/Sghosh1999/fuzzy_search/blob/7ab472ecfd877f8a3fb11ebeadd7fa68809bf7e9/images/screen3.PNG" alt="formula" />
</p>

----

## Built With

This section should list any major frameworks that we have used to build the application.

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)

---

<!-- GETTING STARTED -->

## Getting Started :robot:

In this section, A whole installation guide is mentioned. also trouble shooting guide is also given.

## Prerequisites

This is an example of how to list things you need to use the software and how to install them.

- Python ( Version 3.8.5)
- Streamlit (0.82.0)
- Git

## Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Sghosh1999/fuzzy_search.git
   ```
2. Create a Virtual Python environment
   ```python
   > python -m virtualenv myenv
   ```
3. Activate the Virtual environment
   ```python
   > myenv\scripts\activate
   ```
4. Install necessary packages
   ```sh
   python -m pip install -r requirements.txt
   ```
5. Check if these two packages are installed or not:
   ```sh
   python -m streamlit --version
   ```
   If streamlit is not recognized, then run the command

```sh
  python -m pip install streamlit
```

## Running the Application

```python
$python -m streamlit run app.py
```

- For the first time it will ask you for the email. Please provide the email and the application will be open in your browser.

### Built with :heart:
