# React Flask Proxy Client

This project is a React application that serves as a client-side proxy to interact with a Flask API defined in `DataSentinal.py`. The application allows users to validate client calls and check the health of the API.

## Project Structure

```
react-flask-proxy-client
├── src
│   ├── api
│   │   └── dataSentinelProxy.js
│   ├── App.js
│   ├── index.js
│   └── README.md
├── package.json
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd react-flask-proxy-client
   ```

2. **Install dependencies:**
   Make sure you have Node.js installed. Then run:
   ```
   npm install
   ```

3. **Start the React application:**
   ```
   npm start
   ```

4. **Ensure the Flask API is running:**
   Make sure the Flask API defined in `DataSentinal.py` is running on the specified port (default is 5000).

## Usage

- The application provides a user interface to send requests to the Flask API.
- Use the `/validate` endpoint to validate client calls by providing the necessary data.
- Use the `/health` endpoint to check the health status of the API.

## Example

To validate a client call, the application will send a POST request to the `/validate` endpoint with the required data in the request body. The response will indicate whether the request was successful or if it was blocked due to suspicious activity.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes. 

## License

This project is licensed under the MIT License.