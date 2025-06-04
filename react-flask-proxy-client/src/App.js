import React, { useState } from 'react';
import { validateClientCall, healthCheck } from './api/dataSentinelProxy';

function App() {
    const [clientCall, setClientCall] = useState('');
    const [response, setResponse] = useState(null);
    const [error, setError] = useState(null);

    const handleValidate = async () => {
        setError(null);
        setResponse(null);
        try {
            const result = await validateClientCall(clientCall);
            setResponse(result);
        } catch (err) {
            setError(err.message);
        }
    };

    const handleHealthCheck = async () => {
        setError(null);
        setResponse(null);
        try {
            const result = await healthCheck();
            setResponse(result);
        } catch (err) {
            setError(err.message);
        }
    };

    return (
        <div>
            <h1>Data Sentinel Client</h1>
            <input
                type="text"
                value={clientCall}
                onChange={(e) => setClientCall(e.target.value)}
                placeholder="Enter client call"
            />
            <button onClick={handleValidate}>Validate Client Call</button>
            <button onClick={handleHealthCheck}>Health Check</button>
            {response && <pre>{JSON.stringify(response, null, 2)}</pre>}
            {error && <p style={{ color: 'red' }}>{error}</p>}
        </div>
    );
}

export default App;