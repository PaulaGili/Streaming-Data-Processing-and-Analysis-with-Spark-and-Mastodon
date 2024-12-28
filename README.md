# Streaming Data Processing and Analysis with Spark and Mastodon

## Project Overview
This project focuses on processing and analyzing streaming data using Apache Spark and the Mastodon social media platform. The primary goal is to capture live toots from Mastodon using sockets, process the data with Spark Streaming, and perform various tasks like word frequency counting, trend tracking, and sentiment analysis.

### Key Objectives:
1. **Real-Time Word Counting**: Count the occurrences of words in streaming data from Mastodon with a special focus on words starting with a capital letter.
2. **Trend Analysis**: Track the evolution of word frequencies over time.
3. **Sentiment Analysis**: Perform sentiment analysis (positive, negative, neutral) on Mastodon toots using the TextBlob library.
4. **HDFS Integration**: Store processed data in HDFS for long-term storage and further analysis.

## Project Structure
The project is divided into multiple directories and files. Below is the description of each section:

### 1. **1_intro_spark_streaming**
   - **Description**: This folder contains the basic implementation for Spark Streaming. It includes scripts that focus on the initial tasks like word counting using Spark’s StreamingContext and DStreams.
   - **Files**:
     - `top_words_withinMicroBatch.py`: Template for counting word occurrences in streaming data.
     - `top_words_withGlobalState.py`: Template for maintaining a global word count across multiple micro-batches.

### 2. **mastodon_spark**
   - **Description**: This folder contains scripts that integrate with the Mastodon API to stream live toots. The data is processed using Spark Streaming to extract insights, like frequent words and user activity.
   - **Files**:
     - `socket_Mastodon.py`: Connects to the Mastodon API and streams the toots using sockets.
     - `ejercicio_Socket.py`: Processes the Mastodon toots in Spark Streaming and tracks the most frequent words.
     - `ejercicio_HDFS.py`: Stores processed data in HDFS with the number of toots sent by each user.
     - `mastodon_Socket_autor.py`: Modified version of `socket_Mastodon.py` to stream the author of each toot instead of the toot content.

### 3. **3_sentiment_analysis**
   - **Description**: This folder focuses on performing sentiment analysis on the toots using the TextBlob library. It analyzes the polarity of the toots to classify them as positive, negative, or neutral.
   - **Files**:
     - `polaridad_global.py`: Implements sentiment analysis and tracks the evolution of sentiments (positive, negative, neutral) over time using Spark Streaming.
     - `socket_Mastodon.py`: Modified version for streaming toots to be analyzed for sentiment.

## Prerequisites
Before running the scripts, make sure you have the following installed:

- **Apache Spark** (version 2.4.0 or higher)
- **Python 3** (ensure you have the correct version for compatibility with Spark and the libraries)
- **TextBlob** (for sentiment analysis)
  - Install via pip: `pip install textblob`
- **Mastodon API Access**: You need a Mastodon account and an API token to stream toots. Instructions for setting up the API token can be found in the Mastodon developer documentation.
- **HDFS Setup**: You should have access to an HDFS cluster for storing processed data.

## Setup Instructions
1. **Clone or Download the Project**:
   - Download or clone the project repository to your local machine.

2. **Modify the Python Scripts**:
   - Modify the Python scripts to use your **Mastodon API token** and **assigned port**.
   - Ensure that the ports used for connecting to the Mastodon API (via `netcat` or socket connection) match the ones provided to you.

3. **Start the Mastodon Data Stream**:
   - In one terminal, run the script to stream data from Mastodon:
     ```bash
     python3 socket_Mastodon.py
     ```
   - This script will connect to Mastodon and stream toots over the specified socket.

4. **Run the Spark Streaming Scripts**:
   - In another terminal, run the Spark Streaming scripts to process the data:
     - For word counting in micro-batches:
       ```bash
       python3 top_words_withinMicroBatch.py
       ```
     - For word counting with global state:
       ```bash
       python3 top_words_withGlobalState.py
       ```
     - For sentiment analysis:
       ```bash
       python3 polaridad_global.py
       ```
   - Ensure that the scripts process the data from the Mastodon stream and generate the desired outputs.

5. **Verify the Output**:
   - Check the output in the terminal. You should see live updates of the processed data, such as the most frequent words, user activity, or sentiment analysis results.
   - Capture screenshots of the results as specified in the deliverables section.

## Running the Project

1. **Start Mastodon Socket**:
   - Open a terminal and run:
     ```bash
     python3 socket_Mastodon.py
     ```
2. **Run Spark Streaming Scripts**:
   - Open another terminal and run one of the Spark Streaming scripts, depending on the task you are working on:
     ```bash
     python3 top_words_withinMicroBatch.py  # Word count in micro-batches
     python3 top_words_withGlobalState.py  # Word count with global state
     python3 polaridad_global.py           # Sentiment analysis
     ```
3. **View Results**:
   - Observe the output in the terminal. For example, you should see real-time word frequencies, sentiment classifications, or the user activity data stored in HDFS.

4. **Capturing Results**:
   - After running the scripts, take screenshots of the console outputs and save them in the project directories as specified (e.g., `intro_spark_1.png`, `ejercicio_Socket.png`, etc.).

## Deliverables
- **Modified Python Scripts**: Submit the Python scripts with your changes based on the project requirements.
- **Screenshots**: Capture the output in the terminal and save screenshots as per the provided example.
- **WRITEME.txt**: Provide answers to the theoretical questions outlined in the project, such as explaining DStreams and the origins of data streams.

## License
This project is for educational purposes only and should not be distributed or used for commercial purposes.


