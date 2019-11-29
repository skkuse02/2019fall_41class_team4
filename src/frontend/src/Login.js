import React from 'react';
import './Form.css';

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
          <button class="login-btn">create</button>
          <HelpMessage msg="Already registered? " detail="Sign In" />
        </form>
        <form class="login-form">
          <h2>LOGIN</h2>
          <input type="text" placeholder="username" />
          <input type="password" placeholder="password" />
          <button class="login-btn" onClick={props.onlogin} type="button">login</button>
          <HelpMessage msg="Not registered? " detail="Create an account" />
        </form>
      </div>
    </div>
  );
}

export default Login;
