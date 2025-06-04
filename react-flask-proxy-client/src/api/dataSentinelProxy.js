import axios from 'axios';

const API_URL = 'http://localhost:5000'; // Adjust the URL if your Flask API is hosted elsewhere

export const validateClientCall = async (token, requestData) => {
    try {
        const response = await axios.post(`${API_URL}/validate`, requestData, {
            headers: {
                Authorization: `Bearer ${token}`,
                'Content-Type': 'application/json'
            }
        });
        return response.data;
    } catch (error) {
        throw error.response ? error.response.data : new Error('Network error');
    }
};

export const healthCheck = async () => {
    try {
        const response = await axios.get(`${API_URL}/health`);
        return response.data;
    } catch (error) {
        throw error.response ? error.response.data : new Error('Network error');
    }
};