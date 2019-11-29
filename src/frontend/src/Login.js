import React from 'react';
import './Form.css';
import {NotificationContainer, NotificationManager} from 'react-notifications';
import 'react-notifications/lib/notifications.css';
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
function createNotification() {

  NotificationManager.error('Please Check Your ID or Password', 'Login Faild', 2500, () => {
  });
      // NotificationManager.success('Success Create Account', 'Sign in and Enjoy PICKET');
}
function Login(props) {
  return (
    <div class="login-page">
      <img class="logo-img" src="img/logo.png" />
      <div class="form">
        <form class="register-form">
          <h2>REGISTER</h2>
          <input type="text" placeholder="name" />
          <input type="password" placeholder="password" />
          <input type="text" placeholder="email address" />
          <button class="create-btn" type="button">create</button>
          <HelpMessage msg="Already registered? " detail="Sign In" />
        </form>
        <form class="login-form">
          <h2>LOGIN</h2>
          <input type="text" placeholder="username" />
          <input type="password" placeholder="password" />
          <button class="login-btn" onClick={createNotification} type="button">login</button>
          <HelpMessage msg="Not registered? " detail="Create an account" />
          <NotificationContainer/>
        </form>
      </div>
    </div>
  );
}

export default Login;