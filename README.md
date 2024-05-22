# Retail Store Chatbot

This project is an end-to-end Large Language Model (LLM) application that facilitates natural language interaction with a retail store's database. Developed using the LangChain framework, Google Gemini API, and Streamlit for the frontend interface, the chatbot enables users to query the database effortlessly and obtain accurate responses.


![image](https://github.com/skateryash/Retail-Store-Chatbot/assets/46641912/d890f083-1eed-4a75-af80-8952f93f5d51)


## Project Description
Retail Store Chatbot is designed to streamline operations for store managers by providing an intuitive interface to interact with the store's data. Users can ask questions in natural language, and the system translates these queries into SQL to fetch data from the MySQL database. The application is particularly useful for managing inventory, sales, and discounts.

### Key Features
- **Natural Language Processing**: Understands user queries and converts them into SQL.
- **Data Management**: Interacts with the MySQL database to fetch real-time data.
- **User Interface**: Built with Streamlit to provide a user-friendly interaction platform.

## Technologies Used
- **LangChain Framework**
- **Google Gemini API**
- **Streamlit for UI**
- **Hugging Face Embeddings**
- **FAISS for Vector Storage**

## Installation

### Prerequisites
- Python 3.9+
- MySQL Database

### Steps to Setup
1. **Clone the Repository**
   ```bash
   git clone https://github.com/skateryash/Retail-Store-Chatbot.git
   cd Retail-Store-Chatbot
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Key**
   - Acquire an API key from [Google MakerSuite](https://makersuite.google.com) and add it to a `.env` file in the project root:
     ```bash
     GOOGLE_API_KEY="your_api_key_here"
     ```

4. **Setup Database**
   - Run the `database/db_creation_atliq_t_shirts.sql` script in your MySQL workbench to set up the required tables and data.

## Usage

### Running the Application
Start the Streamlit app by executing:
```bash
streamlit run main.py
```
This will open the web application in your default browser where you can start asking questions.

### Sample Questions
- "How many Adidas t-shirts are left in stock?"
- "What are the total sales for Nike in size XS?"
- "How much is the total inventory value for all S-size t-shirts?"
- "What will be the sales amount if we sell all small size Adidas shirts today after discounts?"


## Project Highlights
- **Inventory Management**: Tracks inventory for brands like Adidas, Nike, Van Heusen, and Levi's.
- **Sales Analysis**: Provides insights on sales performance.
- **Discounts Management**: Helps in managing and querying discount data.

## Acknowledgements
- Guided by: Dhaval Patel
- Special thanks to the open-source community and developers of LangChain, Google Gemini API, and Streamlit.

## Contact
For questions, issues, or contributions, please reach out via [LinkedIn](https://www.linkedin.com/in/yashgchaudhary).
