import React from 'react';
import './Modal.css';
import ReactTransitionGroup from 'react-addons-css-transition-group';

const Modal = ({ isOpen, close }) => {
  return (
    <React.Fragment>
      {
        isOpen ?
          <ReactTransitionGroup
            transitionName={'Modal-anim'}
            transitionEnterTimeout={200}
            transitionLeaveTimeout={200}
          >
            <div className="Modal-overlay" onClick={close} />
            <div className="Modal">
              <p className="title">Modify Item Information</p>
              <div className="content">
                <label for="inp" class="inp">
                  <input type="text" id="inp" placeholder="&nbsp;" />
                  <span class="label">Product Name</span>
                  <span class="border"></span>
                </label>
                <label for="inp" class="inp">
                  <input type="text" id="inp" placeholder="&nbsp;" />
                  <span class="label">Domain Name</span>
                  <span class="border"></span>
                </label>
                <label for="inp" class="inp">
                  <input type="text" id="inp" placeholder="&nbsp;" />
                  <span class="label">Price</span>
                  <span class="border"></span>
                </label>
              </div>
              <div className="button-wrap">
                <button onClick={close}>Confirm</button>
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