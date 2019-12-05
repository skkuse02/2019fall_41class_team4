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

function Notification(type,message) {
  if(type === 'login-fail'){
    NotificationManager.error(message, 'Login Faild', 2700, () => {});
  }
  if(type==='register-fail'){
    NotificationManager.error(message, 'Register Faild', 2700, () => {});
  }
  if(type==='register-success'){
    NotificationManager.success(message, 'Success Create Account', 2000);
  }
}

function Login(props) {

  const [id, setID] = useState('');
  const [password, setPassword] = useState('');
  const [email, setEmail] = useState('');

  const server = "http://ec2-13-125-249-233.ap-northeast-2.compute.amazonaws.com:8080";

  function loginHandler() {
    axios.post(server +"/login", {
      user_id: id,
      user_pw: password
    })
      .then(function (response) {
        console.log(response.data);
        if(response.data.status ==='fail') Notification('login-fail',response.data.message);
      })
      .catch(function (error) {
        console.log('err', error);
      });
  }

  function registerHandler() {
    axios.post(server + "/register", {
      user_id: id,
      user_pw: password,
      user_email :email
    })
      .then(function (response) {
        if(response.data.status === 'fail') Notification('register-fail',response.data.message);
        else Notification('register-success',response.data.message)
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
          <input type="text" placeholder="name" value={id} onChange={(e) => setID(e.target.value)} />
          <input type="password" placeholder="password" value={password} onChange={(e) => setPassword(e.target.value)} />
          <input type="text" placeholder="email address" value={email} onChange={(e) => setEmail(e.target.value)}/>
          <button class="create-btn" type="reset" onClick={registerHandler}>create</button>
          <HelpMessage msg="Already registered? " detail="Sign In" />
        </form>

        <form class="login-form">
          <h2>LOGIN</h2>
          <input type="text" placeholder="username" value={id} onChange={(e) => setID(e.target.value)} />
          <input type="password" placeholder="password"  value={password} onChange={(e) => setPassword(e.target.value)}/>
          <button class="login-btn" type="reset" onClick={loginHandler} type="button">login</button>
          <HelpMessage msg="Not registered? " detail="Create an account" />
        </form>

        <NotificationContainer />
      </div>
    </div>
  );
}

export default Login;
