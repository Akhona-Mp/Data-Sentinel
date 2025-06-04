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

3. **Run the application:**
   ```
   npm start
   ```
   This will start the React application in development mode. Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

## Usage

### API Calls

The application uses the following API calls:

- **Validate Client Call**
  - Endpoint: `/validate`
  - Method: `POST`
  - Description: Sends a request to validate a client call. Requires an Authorization header with a Firebase token.

- **Health Check**
  - Endpoint: `/health`
  - Method: `GET`
  - Description: Checks the health status of the Flask API.

### Example

To validate a client call, you can use the `validateClientCall` function from the `dataSentinelProxy.js` file. Ensure you pass the necessary data and authorization token.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes. 

## License

This project is licensed under the MIT License.