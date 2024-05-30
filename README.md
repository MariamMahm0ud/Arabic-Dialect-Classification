# Arabic Dialect Classification

Welcome to the **Arabic Dialect Classification** project! 🌟

This project aims to predict the dialect of Arabic text, encompassing dialects from various Arabic-speaking countries. Leveraging natural language processing (NLP) techniques and machine learning models, the system accurately identifies the dialect of input text.

## Overview

Arabic, a language with diverse dialects across different regions, presents a unique challenge for language processing tasks. This project addresses this challenge by implementing a robust classification system capable of distinguishing between various Arabic dialects.

## Features

- **Multiclass Classification**: The system classifies Arabic text into one of five dialects: Egyptian, Lebanese, Sudanese, Moroccan, and Libyan.
- **Machine Learning and Deep Learning Models**: Two models are trained and compared: logistic regression and multinomial naive Bayes for machine learning, and a deep learning model with LSTM architecture.
- **Web Application**: Utilizing Flask for creating a web-based interface and RESTful API, users can input Arabic text and receive real-time predictions for the dialect.
- **Text Preprocessing**: TF-IDF and CountVectorizer techniques are employed for text preprocessing and feature extraction, enhancing NLP accuracy.


## Data

The dataset used for this project was provided by the Qatar Computing Research Institute. For more insights, refer to their paper: [Dialect Identification in the Arab World](https://arxiv.org/pdf/2005.06557.pdf).

## Future Enhancements

- **Fine-tuning Models**: Further fine-tuning of machine learning and deep learning models to improve classification accuracy.
- **Expansion of Dialects**: Extending the system to classify additional Arabic dialects, facilitating broader linguistic analysis.
- **User Feedback Integration**: Incorporating user feedback to continuously enhance the system's performance and usability.

## Results

The project achieves impressive accuracy in dialect classification, providing valuable insights into the linguistic diversity of the Arabic language. Through comprehensive evaluation and comparison of different models.
In the deployment phase, the Multinomial Naive Bayes model trained with CountVectorizer achieved an impressive accuracy of 82%. This model efficiently predicted the Arabic dialect given the input text, showcasing its effectiveness in real-world scenarios.

![Alt text](https://github.com/MariamMahm0ud/MariamMahm0ud-Arabic-Dialect-Classification/blob/master/Screenshot%202024-05-30%20192533.png)



