import axios from 'axios';

const API_URL = 'https://jsonplaceholder.typicode.com/users1';

const getBatchData = async () => {
  try {
    const response = await axios.get(API_URL);
    return response.data;
  } catch (error) {
    console.error('Error fetching batch data:', error.message);
    return [];
  }
}

export default getBatchData;
