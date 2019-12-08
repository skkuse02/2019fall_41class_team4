/*global chrome*/
import React, { useState } from 'react';
import Login from './Login';
import Request from './Request';
import Cart from './Cart';
import Review from './Review';
import { loadLoginInfo, logout } from './authlib';
import { tsPropertySignature } from '@babel/types';

function App() {

  window.logout = logout;
  const [page, setPage] = useState('login');
  const [url, setUrl] = useState('');

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
  function openReview(url) {
    setPage('review');
    setUrl(url);
  }
  if (page === 'review') {
    return (
      <div className="App">
        <Review openCart={openCart} itemUrl={url}></Review>
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
