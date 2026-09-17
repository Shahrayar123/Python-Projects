# WhatsApp Chats Sentiment Analysis

## Overview
This project performs sentiment analysis on WhatsApp chat data using Natural Language Processing (NLP) techniques. The implementation extracts chat messages from a WhatsApp export file, processes the text data, and analyzes sentiment patterns using VADER (Valence Aware Dictionary and sentiment Reasoner).

## Features
- WhatsApp chat file parsing and message extraction
- Multiline message handling
- Sentiment analysis using NLTK's VADER
- Visualization of sentiment distribution (Positive, Negative, Neutral)


## Technologies Used
- Python 3
- Pandas & NumPy for data manipulation
- NLTK for sentiment analysis
- Matplotlib & Seaborn for visualization
- Emoji library for special character handling
- Regular expressions for text parsing

## Installation
1. Clone this repository
2. Install required packages:


## Usage
1. Export your WhatsApp chat as a .txt file (without media)
2. Place the file in the project directory
3. Update the file path in the notebook:
```python
conversation = r"your_whatsapp_chat.txt"
```
4. Run the Jupyter notebook cells sequentially

## Code Structure
1. **Data Extraction**: Parses WhatsApp chat format and extracts messages with metadata
2. **Data Cleaning**: Handles multiline messages and missing values
3. **Sentiment Analysis**: Uses VADER to compute positive, negative, and neutral scores
4. **Visualization**: Generates bar charts showing sentiment distribution

## Results
The analysis provides:
- Average sentiment scores for the conversation
- Visual representation of sentiment distribution
- Message-level sentiment scoring

## Note
- The implementation handles WhatsApp's specific date-time format and message structure
- Supports both 12-hour time formats
- Properly processes messages with emojis and special characters
- Maintains message context across line breaks

## Privacy
This tool processes chat data locally. No data is sent to external servers, ensuring your conversations remain private.

