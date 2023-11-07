import { userToken } from './firebase.js';

URL = "http://127.0.0.1:8000";

async function authenticatedFetch(url, token, options = {}) {
    options.headers = {
      ...options.headers,
      Authorization: token,
    };
    return fetch(url, options).then((response) => response.json());
}

export async function createAccount(firebaseUid, displayName) {
  return fetch(`${URL}/signup`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ firebase_uid: firebaseUid, display_name: displayName }),
  });
}

export async function getFriendCount(token) {
  return await authenticatedFetch(`${URL}/friend_count`, token, {
    method: "GET",
  });
}

export async function getUserData() {
  return authenticatedFetch(`${URL}/get_data`, userToken)
}
