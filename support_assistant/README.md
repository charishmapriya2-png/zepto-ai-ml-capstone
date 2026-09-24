# Module 3: FastAPI & LangGraph Support Assistant

## Pipeline Architecture
The support assistant uses a stateful graph workflow (`LangGraph`) integrated with a REST API (`FastAPI`):
1. **Classifier Node**: Evaluates user query text using keyword matching to categorize inquiries into *Delivery Issue*, *Refund / Payment*, or *General Inquiry*.
2. **Responder Node**: Generates tailored, context-aware responses based on the classified category.
3. **API Endpoint**: Exposes a `/chat` POST endpoint that processes inputs through the state machine and returns structured JSON output.

## Example Call Transcripts (MOCK_LLM Default)

- **Request**: `POST /chat?query=Where is my delivery?`
  - **Response**:
    ```json
    {
      "user_query": "Where is my delivery?",
      "detected_category": "Delivery Issue",
      "support_response": "We are sorry for the delay regarding your query: 'Where is my delivery?'. Our delivery partner has been notified and will reach out shortly."
    }
    ```

- **Request**: `POST /chat?query=I want a refund for my order`
  - **Response**:
    ```json
    {
      "user_query": "I want a refund for my order",
      "detected_category": "Refund / Payment",
      "support_response": "Regarding your payment query ('I want a refund for my order'), refunds typically process within 3-5 business days to your original payment method."
    }
    ```
