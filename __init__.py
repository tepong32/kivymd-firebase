from pyrebase import pyrebase

config = {

    "apiKey": "AIzaSyCXh16GzLvXTQIpZ6vamKhqJF3QdbQ_Stg",

    "authDomain": "bocaue-app.firebaseapp.com",

    "databaseURL": "YOUR_DATABASE_URL",

    "projectId": "bocaue-app",

    "storageBucket": "bocaue-app.firebasestorage.app",

    "messagingSenderId": "562614047023",

    "appId": "1:562614047023:web:ce11a9057c99d5add1d1da"

    "measurementId": "G-KTY2YY2F8N"

}


firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

db = firebase.database()




'''
// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCXh16GzLvXTQIpZ6vamKhqJF3QdbQ_Stg",
  authDomain: "bocaue-app.firebaseapp.com",
  projectId: "bocaue-app",
  storageBucket: "bocaue-app.firebasestorage.app",
  messagingSenderId: "562614047023",
  appId: "1:562614047023:web:ce11a9057c99d5add1d1da",
  measurementId: "G-KTY2YY2F8N"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
'''