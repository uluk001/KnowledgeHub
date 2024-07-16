# Information Finder

Information Finder is a web application that retrieves information from Wikipedia and OpenAI based on user input. Users can enter a word, and the application will display information from Wikipedia and the OpenAI API. If there are multiple references in Wikipedia, the user can select the desired option to get more specific information.

## Features

- Retrieve information from Wikipedia
- Retrieve information from OpenAI API
- Handle multiple references from Wikipedia with user selection
- Dynamic information display based on user input

## Prerequisites

- Python 3.7 or higher
- OpenAI API key

## Installation

1. Clone the repository:
    ```bash
    https://github.com/uluk001/KnowledgeHub.git
    cd KnowledgeHub
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. Set up your OpenAI API key:
    Create a `config.py` file inside the `app` directory and add your OpenAI API key:

    ```python
    OPENAI_API_KEY = 'your_openai_api_key'
    OPENAI_MODEL = 'your_openai_api_model'
    ```

## Usage

1. Run the Streamlit application:
    ```bash
    streamlit run app/main.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

3. Enter a word to get information from Wikipedia and OpenAI API.


## Contributing

We welcome contributions to the KnowledgeHub project! If you're interested in helping improve KnowledgeHub, please follow these steps:

1. **Fork the repository**: This creates your own copy of the repository where you can make your changes.
2. **Create a new branch**: Use the command `git checkout -b feature/AmazingFeature` to create a new branch for your feature.
3. **Make your changes**: Implement your new feature or bug fix in this branch.
4. **Commit your changes**: Use the command `git commit -m 'Add some AmazingFeature'` to save your changes with a descriptive commit message.
5. **Push the branch**: Use the command `git push origin feature/AmazingFeature` to upload your changes to your forked repository.
6. **Open a Pull Request**: Go to the GitHub page of your forked repository and click on "New pull request" to submit your changes for review.

## Author & Contact

- **Ismailov** - Initial work - [uluk001](https://github.com/uluk001)

If you have questions, suggestions, or would like to report a bug, feel free to contact me at [ulukmanmuratov@gmail.com](mailto:ulukmanmuratov@gmail.com), via Telegram [@ismailovvv001](https://t.me/ismailovvv001), or connect with me on [LinkedIn](https://www.linkedin.com/in/ismailov-uluk-92784a233/).
