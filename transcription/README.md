# Mock Video Transcription API

This project is a mock API that simulates a video transcription service. It provides an endpoint to submit a video file path and receive a mock transcription response. This API is built with Python and FastAPI and is intended for development and testing purposes.

## Features

-   **Mock Transcription**: Simulates a transcription process without any actual audio or video processing.
-   **Realistic Responses**: Generates realistic transcription data, including text, summary, speakers, and confidence scores.
-   **Easy to Use**: Simple to set up and run locally.
-   **Fast and Efficient**: Built with FastAPI for high performance.

## Getting Started

To get started with this mock API, follow these steps:

### Prerequisites

-   Python 3.7+
-   An API client like [Postman](https://www.postman.com/) or [Insomnia](https://insomnia.rest/)

### Installation

1.  **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/mock-transcription-api.git
    cd mock-transcription-api
    ```

2.  **Create and activate a virtual environment**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies**:

    ```bash
    pip install "fastapi[all]"
    ```

### Running the API

1.  **Start the server**:

    ```bash
    uvicorn main:app --reload
    ```

2.  **Access the API documentation**:

    The API documentation is available at `http://127.0.0.1:8000/docs`.

## API Endpoints

### Transcribe

-   **URL**: `/transcribe`
-   **Method**: `POST`
-   **Description**: Submits a video file path for mock transcription.

#### Request Body

```json
{
  "original_file_path": "/path/to/your/video.mp4",
  "user": "your-username"
}
```

#### Response Body

```json
{
  "document_id": "a8d8b8e8-8d8d-8d8d-8d8d-8d8d8d8d8d8d",
  "transcription_text": "This is a sample transcription.",
  "summary": "This is a sample summary.",
  "transcription_json": {
    "text": "This is a sample transcription."
  },
  "speakers": [
    "speaker1",
    "speaker2"
  ],
  "confidence_score": 0.95,
  "processing_time_ms": 15000,
  "audio_duration_sec": 450
}
```

## Technologies Used

-   [FastAPI](https://fastapi.tiangolo.com/): A modern, fast (high-performance) web framework for building APIs with Python 3.7+.
-   [Pydantic](https://pydantic-docs.helpmanual.io/): Data validation and settings management using Python type annotations.
-   [Uvicorn](https://www.uvicorn.org/): A lightning-fast ASGI server implementation.

