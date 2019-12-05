import React, { useState } from 'react';
import './Form.css';
import { NotificationContainer, NotificationManager } from 'react-notifications';
import 'react-notifications/lib/notifications.css';
import axios from "axios";

function HelpMessage(props) {
  function onScroller() {
    window.$('form').animate({ height: "toggle", opacity: "toggle" }, "slow");
  }

  return (
    <p class="message">
      {props.msg}
      <a href="#" onClick={onScroller}>
        {props.detail}
      </a>
    </p>
  );
}
function failNotification() {
  NotificationManager.error('Please Check Your ID or Password', 'Login Faild', 2500, () => {
  });
}

function createNotification() {
  NotificationManager.success('Sign in and Enjoy PICKET', 'Success Create Account', 2000);
}

function Login(props) {

  const [state, setState] = useState({
    name: "",
    password: "",
    email: ""
  });

  const LoginServer = "http://ec2-13-125-249-233.ap-northeast-2.compute.amazonaws.com:8080/login";

  function handleNameChange(e) {
    setState({ fields: { name: e.target.value } });
  }
  function handlePasswordChange(e) {
    setState({ password: e.target.value });
  }
  function loginHandler() {
    console.log(state.name);
    axios.post(LoginServer, {
      user_id: state.name,
      user_pw: state.password
    })
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log('err', error);
      });
  }
  return (
    <div class="login-page">
      <img class="logo-img" src="img/logo.png" />
      <div class="form">
        <form class="register-form">
          <h2>REGISTER</h2>
          <input type="text" placeholder="name" />
          <input type="password" placeholder="password" />
          <input type="text" placeholder="email address" />
          <button class="create-btn" type="reset" onClick={createNotification}>create</button>
          <HelpMessage msg="Already registered? " detail="Sign In" />
        </form>
        <form class="login-form">
          <h2>LOGIN</h2>
          <input
            type="text"
            placeholder="username"
            value={state.name}
            onChange={handleNameChange} />
          <input
            type="password"
            placeholder="password"
            value={state.password}
            onChange={handlePasswordChange} />
          <button class="login-btn" type="reset" onClick={loginHandler} type="button">login</button>
          <HelpMessage msg="Not registered? " detail="Create an account" />
        </form>
        <NotificationContainer />
      </div>
    </div>
  );
}

export default Login;
