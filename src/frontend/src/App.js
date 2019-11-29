/*global chrome*/
import React, { useState } from 'react';
import Login from './Login';
import Request from './Request';
import Cart from './Cart';
import { REFUSED } from 'dns';

function App() {
  // chrome.tabs.getSelected(null, function (tab) {
  //   document.getElementById("url-input").value = tab.url;
  // });

  const [page, setPage] = useState('login');

  function openRequest() {
    setPage('request');
  }
  if(page==='login'){
    return (
      <div className="App">
        <Login></Login>
      </div>
    )
  }
  if (page === 'cart') {
    return (
      <div className="App">
        <Cart openRequest={openRequest}></Cart>
      </div>
    )
  } else if (page === 'request') {
    return (
      <div className="App">
        <Request></Request>
      </div>
    )
  }
}

export default App;