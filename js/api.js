URL = "http://127.0.0.1:8000";

function authenticatedFetch(url, token, options = {}) {
  options.headers = {
    ...options.headers,
    Authorization: token,
  };

  return fetch(url, options);
}

export function createAccount(firebaseUid) {
  fetch(`${URL}/signup`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ firebase_uid: firebaseUid }),
  });
}
