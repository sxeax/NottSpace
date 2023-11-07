import { initializeApp } from "https://www.gstatic.com/firebasejs/10.5.2/firebase-app.js";
import {
  getAuth,
  signInWithEmailAndPassword,
  createUserWithEmailAndPassword,
  onAuthStateChanged,
  signOut,
  getIdToken,
} from "https://www.gstatic.com/firebasejs/10.5.2/firebase-auth.js";
import { createAccount, getFriendCount } from "./api.js";

export let userToken = null;

const firebaseConfig = {
  apiKey: "AIzaSyAb2tCj_qrHc9nDDUxeBAI52vWHFtxbrv4",
  authDomain: "nottspace.firebaseapp.com",
  projectId: "nottspace",
  storageBucket: "nottspace.appspot.com",
  messagingSenderId: "978055665610",
  appId: "1:978055665610:web:d6dbe1bedd8c45bb15a133",
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

export function login(event) {
  event.preventDefault();
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;
  const loginStatus = document.getElementById("login-status");

  signInWithEmailAndPassword(auth, email, password)
    .then(function (userCredential) {
      const user = userCredential.user;
      document.location.href =  '/index-logged-in.html';
      loginStatus.textContent = `Logged in as ${user.email}`;
    })
    .catch(function (error) {
      const errorCode = error.code;
      const errorMessage = error.message;
      loginStatus.textContent = `Login error: ${errorCode} - ${errorMessage}`;
    });
}

export function signup(event) {
  event.preventDefault();
  const displayName = document.getElementById("displayName").value;
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;
  const signupStatus = document.getElementById("signup-status");

  createUserWithEmailAndPassword(auth, email, password)
    .then(function (userCredential) {
      const user = userCredential.user;
      createAccount(userCredential.user.uid, displayName).then(() => {
        document.location.href = "/index-logged-in.html";
      });
      signupStatus.textContent = `Sign-up successful for ${user.email}`;
    })
    .catch(function (error) {
      const errorCode = error.code;
      const errorMessage = error.message;
      signupStatus.textContent = `Sign-up error: ${errorCode} - ${errorMessage}`;
    });
}

export function logout() {
  signOut(auth);
}

onAuthStateChanged(auth, async (user) => {
  if (user) {
    user.getIdToken().then(token => userToken = token)
  } else {
    userToken = null;
  }
});
