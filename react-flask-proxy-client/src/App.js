import React, { useState } from 'react';

function App() {
    const [response, setResponse] = useState(null);

    const checkHealth = async () => {
        try {
            const res = await fetch('http://localhost:5000/health');
            const data = await res.json();
            setResponse(data);
        } catch (error) {
            setResponse({ error: error.message });
        }
    };

    return (
        <div style={{ padding: '20px', maxWidth: '800px', margin: '0 auto' }}>
            <h1>Data Sentinel Dashboard</h1>
            <button 
                onClick={checkHealth}
                style={{
                    padding: '10px 20px',
                    fontSize: '16px',
                    cursor: 'pointer',
                    backgroundColor: '#007bff',
                    color: 'white',
                    border: 'none',
                    borderRadius: '4px'
                }}
            >
                Check API Health
            </button>
            {response && (
                <pre style={{ marginTop: '20px', padding: '10px', backgroundColor: '#f5f5f5' }}>
                    {JSON.stringify(response, null, 2)}
                </pre>
            )}
        </div>
    );
}

export default App;