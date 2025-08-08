import axios from 'axios';

const base_url = 'http://127.0.0.1:5000';

const batches_url = `${base_url}/batches`;
const getBatchData = async () => {
  try {
    const response = await axios.get(batches_url);
    return response.data;
  } catch (error) {
    console.error('Error fetching batch data:', error.message);
    return [];
  }
}

const calendardata_url = `${base_url}/calendar-batches`;
export const getCalendarData = async () => {
  try {
    const response = await axios.get(calendardata_url);
    return response.data;
  } catch (error) {
    console.error('Error fetching calendar data:', error.message);
    return [];
  }
}

const qe_url = `${base_url}/qe-batches`;
export const getQeData = async () => {
  try {
    const response = await axios.get(qe_url);
    return response.data;
  } catch (error) {
    console.error('Error fetching QE data:', error.message);
    return [];
  }
}

const qc_url = `${base_url}/qc-batches`;
export const getQcData = async () => {
  try {
    const response = await axios.get(qc_url);
    return response.data;
  } catch (error) {
    console.error('Error fetching QC data:', error.message);
    return [];
  }
}

export default getBatchData;
