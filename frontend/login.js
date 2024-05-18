
  // Import the functions you need from the SDKs you need
  import { initializeApp } from "firebase/app";
  import { getAuth, signInWithEmailAndPassword } from "firebase/auth";
  // TODO: Add SDKs for Firebase products that you want to use
  // https://firebase.google.com/docs/web/setup#available-libraries

  // Your web app's Firebase configuration
  const firebaseConfig = {
    apiKey: "AIzaSyC4cCWfu8lG8g_tEA-j6RrbsNgPiM-3dNc",
    authDomain: "brainbox-75c7e.firebaseapp.com",
    projectId: "brainbox-75c7e",
    storageBucket: "brainbox-75c7e.appspot.com",
    messagingSenderId: "445624445622",
    appId: "1:445624445622:web:fa2a0502e2957064665417"
  };

  // Initialize Firebase
  const app = initializeApp(firebaseConfig);

  //inputs
  
  

  const submit = document.getElementById('submit');
  submit.addEventListener("click",function(event) {
    event.preventDefault();
    const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;
  const auth = getAuth(app);
signInWithEmailAndPassword(auth, email, password)
  .then((userCredential) => {
    // Signed in 
    const user = userCredential.user;
    window.location.href = "dashboard.html";
    // ...
  })
  .catch((error) => {
    const errorCode = error.code;
    const errorMessage = error.message;
  });
  })