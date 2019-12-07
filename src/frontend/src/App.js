/*global chrome*/
import React, { useState } from 'react';
import Login from './Login';
import Request from './Request';
import Cart from './Cart';
import Review from './Review';
import { loadLoginInfo, logout } from './authlib';

function App() {
  chrome.tabs.getSelected(null, function (tab) {
    document.getElementById("url-input").value = tab.url;
  });
  window.logout = logout;
  const [page, setPage] = useState('login');

  loadLoginInfo().then(id => {
    if (id && page === 'login') {
      console.log(id);
      setPage('cart');
    }
  })

  function openRequest() {
    setPage('request');
  }
  function openCart() {
    setPage('cart');
  }
  function openReview() {
    setPage('review');
  }
  if (page === 'review') {
    return (
      <div className="App">
        <Review openCart={openCart}></Review>
      </div>
    )
  }
  if (page === 'login') {
    return (
      <div className="App">
        <Login openCart={openCart}></Login>
      </div>
    )
  }
  if (page === 'cart') {
    return (
      <div className="App">
        <Cart openReview={openReview} openRequest={openRequest}></Cart>
      </div>
    )
  } else if (page === 'request') {
    return (
      <div className="App">
        <Request openCart={openCart}></Request>
      </div>
    )
  }
}

export default App;
