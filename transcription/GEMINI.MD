Of course. Here are the step-by-step instructions to build the mock API in Python.

### **Instructions to Build a Mock Video Transcription API in Python**

This guide will walk you through setting up a project, defining the API structure, implementing the mock logic, and testing the final result.

---

#### **Step 1: Set Up Your Project Environment**

1.  **Create a Project Directory:** Make a new folder for your project (e.g., `mock_transcription_api`).
2.  **Navigate into the Directory:** Open your terminal or command prompt and go into the newly created folder.
3.  **Create a Virtual Environment:** Create a self-contained Python environment to manage dependencies. This is a best practice.
    *   Run: `python -m venv venv`
4.  **Activate the Virtual Environment:**
    *   **On macOS/Linux:** `source venv/bin/activate`
    *   **On Windows:** `venv\Scripts\activate`
    *   Your terminal prompt should now show `(venv)`.

---

#### **Step 2: Install Necessary Libraries**

You will need a web framework to build the API and a server to run it. We will use FastAPI and Uvicorn, which are modern and efficient choices.

1.  **Install FastAPI and Uvicorn:** With your virtual environment active, run the following command:
    *   `pip install "fastapi[all]"`

    *(This installs FastAPI, Uvicorn for the server, and Pydantic for data validation, which is exactly what we need for this task).*

---

#### **Step 3: Define the Data Structures (Models)**

Before creating the API endpoint, define the structure of the incoming request and the outgoing response using Pydantic models. This ensures your API correctly handles the data.

1.  **Create a Python file:** Inside your project directory, create a new file named `main.py`.
2.  **Define the Request Model:** In `main.py`, create a class that represents the incoming payload. This class will enforce that the request has `original_file_path` and `user` fields, both as strings.
3.  **Define the Response Model:** In the same file, create another class that represents the JSON response your API will send. This class should include all the fields you specified: `document_id`, `transcription_text`, `summary`, `transcription_json`, `speakers`, `confidence_score`, `processing_time_ms`, and `audio_duration_sec`, with their respective data types (e.g., `str`, `dict`, `list`, `float`, `int`).

---

#### **Step 4: Create the API Endpoint**

Now, create the actual API endpoint that will receive the request and return the mock response.

1.  **Instantiate the FastAPI App:** At the top of `main.py`, create an instance of the FastAPI application.
2.  **Define the Endpoint Function:**
    *   Create a new Python function that will handle the logic.
    *   Use a FastAPI "decorator" to link this function to a specific URL path and HTTP method. The appropriate method is **POST**, and you can use a path like `/transcribe`.
    *   Set the function's parameter to be an instance of your **Request Model**. FastAPI will automatically read the incoming JSON, validate it, and convert it into a Python object for you.

---

#### **Step 5: Implement the Mocking Logic**

Inside your endpoint function, you need to generate the fake data for the response. The API should not actually process any files.

1.  **Generate a Unique ID:** Use Python's built-in `uuid` module to generate a unique `document_id` for each request.
2.  **Create Placeholder Content:**
    *   For `transcription_text` and `summary`, create hard-coded strings with some sample text (e.g., "This is a sample transcription." or lorem ipsum).
    *   For `transcription_json` and `speakers`, create simple, hard-coded dictionary and list structures that look realistic.
3.  **Generate Random Numeric Values:**
    *   Use Python's `random` module to generate plausible numbers for `confidence_score` (e.g., a float between 0.90 and 0.99), `processing_time_ms` (e.g., an integer between 5000 and 30000), and `audio_duration_sec`.
4.  **Construct the Response:** Create an instance of your **Response Model** and populate its fields with the mock data you just generated.
5.  **Return the Response:** Return the response model instance from your function. FastAPI will automatically convert it to a JSON response.

---

#### **Step 6: Run the Mock API Server**

With the code complete, you can now run the local server.

1.  **Go to your terminal** (ensure you are in the project directory with the virtual environment active).
2.  **Start the Uvicorn server:** Run the following command:
    *   `uvicorn main:app --reload`
    *   `main` refers to your `main.py` file.
    *   `app` refers to the FastAPI instance you created inside the file.
    *   `--reload` makes the server restart automatically when you save changes to the code.
3.  **Check the Output:** The terminal should indicate that the server is running, typically on `http://127.0.0.1:8000`.

---

#### **Step 7: Test the API Endpoint**

Finally, send a request to your running API to verify that it works as expected.

1.  **Use an API Client:** You can use a tool like **Postman**, **Insomnia**, or a command-line tool like **cURL**.
2.  **Configure the Request:**
    *   **Method:** `POST`
    *   **URL:** `http://127.0.0.1:8000/transcribe` (or whatever path you chose).
    *   **Headers:** Set `Content-Type` to `application/json`.
    *   **Body (Payload):** Provide a JSON object matching your request model's structure. For example:
        ```json
        {
            "original_file_path": "/some/fake/path/video.mp4",
            "user": "test_user"
        }
        ```
3.  **Send the Request:** Execute the request.
4.  **Verify the Response:** You should receive a `200 OK` status code and a JSON body containing the mock data structure you defined, with a unique ID and randomized numbers for each new request.