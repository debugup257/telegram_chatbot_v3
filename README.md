# Telegram Bot For 1st screening HR round ( Technical )
1. The all_names file has to be extracted from 7z before using this. 
2. You will need a telegram account to use the code.
3. you can create a bot on the account and connect the bot into the app.py account. 
4. all db changes can be made in db.py file.

This repository contains a Telegram chatbot created using Python and the Telegram API. The chatbot is designed to provide automated responses based on user input, allowing for interactive and dynamic conversations.

## Installation

To run the chatbot locally, follow these steps:

1. Clone the repository to your local machine using the following command:
2. Navigate to the project directory:
3. Create a virtual environment (optional but recommended) to isolate the project dependencies:
4. Activate the virtual environment:

- On Windows:

  ```
  venv\Scripts\activate.bat
  ```

- On macOS and Linux:

  ```
  source venv/bin/activate
  ```

5. Install the required dependencies:
6. Set up the PostgreSQL database by executing the necessary SQL queries. Make sure you have a running PostgreSQL server and update the connection details in the `config.py` file.
7. Customize the interview questions in the `questions.py` file according to your requirements.
8. Set up a Telegram Bot and obtain the API token. Update the `config.py` file with your bot's API token.
9. Run the chatbot:
## Usage

1. Start a conversation with the chatbot on Telegram by searching for your bot and sending a message.

2. The chatbot will present the preliminary interview questions and expect the candidate's responses.

3. Once the interview is complete, the data will be stored in the PostgreSQL database.

4. Run the `score.py` script to generate the summary report:
5. Check the generated Excel report for candidate details and scores.

## Contributions

Contributions to this project are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. You are free to modify and distribute the code as per the terms of the license.

## Acknowledgments

This project utilizes the following open-source tools and libraries:

- [Python](https://www.python.org/)
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [PostgreSQL](https://www.postgresql.org/)
- [pandas](https://pandas.pydata.org/)
- [openpyxl](https://openpyxl.readthedocs.io/)

A special thanks to the creators and contributors of these amazing projects!








