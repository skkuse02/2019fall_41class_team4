import React, { useState } from 'react';
import './Modal.css';
import ReactTransitionGroup from 'react-addons-css-transition-group';

const Modal = (props) => {

  const modify_item_info = {
    item_name: '',
    domain_name: '',
    item_price: ''
  }

  return (
    <React.Fragment>
      {
        props.isOpen ?
          <ReactTransitionGroup
            transitionName={'Modal-anim'}
            transitionEnterTimeout={200}
            transitionLeaveTimeout={200}
          >
            <div className="Modal-overlay" onClick={() => props.close()} />
            <div className="Modal">
              <p className="title">Modify Item Information</p>
              <div className="content">
                <label for="inp" class="inp">
                  <input type="text" id="inp" placeholder="&nbsp;" onChange={(e) => modify_item_info.item_name = e.target.value} />
                  <span class="label">Product Name</span>
                  <span class="border"></span>
                </label>
                <label for="inp" class="inp">
                  <input type="text" id="inp" placeholder="&nbsp;" onChange={(e) => modify_item_info.domain_name = e.target.value} />
                  <span class="label">Domain Name</span>
                  <span class="border"></span>
                </label>
                <label for="inp" class="inp">
                  <input type="text" id="inp" placeholder="&nbsp;" onChange={(e) => modify_item_info.item_price = e.target.value} />
                  <span class="label">Price</span>
                  <span class="border"></span>
                </label>
              </div>
              <div className="button-wrap">
                <button onClick={() => props.close(modify_item_info)}>Confirm</button>
              </div>
            </div>
          </ReactTransitionGroup>
          :
          <ReactTransitionGroup transitionName={'Modal-anim'} transitionEnterTimeout={200} transitionLeaveTimeout={200} />
      }
    </React.Fragment>
  )
}
export default Modal;