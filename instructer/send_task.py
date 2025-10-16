import requests
import json

# The URL where your Flask application is running
# This must match the host and port of your app.py
STUDENT_API_ENDPOINT = "http://127.0.0.1:8080/api-endpoint"

# The secret key that your application expects
# This MUST match the MY_SECRET value in your .env file
STUDENT_SECRET = "your-super-secret-string-from-the-form"


def send_task_request():
    """
    Builds and sends a sample task request to the student's application.
    """
    # This is the JSON "work order" we are sending.
    # You can easily change the 'brief' or other details here for different tests.
    payload = {
  "email": "student@example.com",
  "secret": "Komal@123",
  "task": "captcha-solver-test-01",
  "round": 1,
  "nonce": "abcd-1234-efgh-5678",
  "brief": "Create a captcha solver that handles ?url=https://example.com/sample.png. Default to attached sample.",
  "checks": [
    "Repo has MIT license",
    "README.md is professional",
    "Page displays captcha URL passed at ?url=...",
    "Page displays solved captcha text within 15 seconds"
  ],
  "evaluation_url": "https://example.com/evaluate-captcha",
  "attachments": [
    {
      "name": "sample.png",
      "url": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA..."
    }
  ]
}




    print(f"Sending POST request to: {STUDENT_API_ENDPOINT}")
    print("Payload:")
    print(json.dumps(payload, indent=2))

    try:
        # Make the POST request
        response = requests.post(STUDENT_API_ENDPOINT, json=payload)

        # Check the response from the server
        response.raise_for_status()  # This will raise an error for bad status codes (4xx or 5xx)

        print("\n--- Response from Server ---")
        print(f"Status Code: {response.status_code}")
        print("Response JSON:")
        print(response.json())
        print("--------------------------\n")
        print("Test successful! Your server received the request and responded correctly.")

    except requests.exceptions.RequestException as e:
        print(f"\n--- ERROR ---")
        print(f"Failed to connect to the server: {e}")
        print("Please make sure your Flask app (app.py) is running in another terminal.")
        print("---------------")


if __name__ == "__main__":
    send_task_request()