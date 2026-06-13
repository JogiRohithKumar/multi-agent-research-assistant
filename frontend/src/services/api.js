import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export async function runResearch(query) {
  const response = await axios.post(
    `${API_URL}/research`,
    {
      query
    }
  );

  return response.data;
}

export async function getStream() {
  const response = await axios.get(
    `${API_URL}/stream`
  );

  return response.data;
}