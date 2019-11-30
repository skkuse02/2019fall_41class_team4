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

function submitNotification() {
    NotificationManager.info('Request Submit Completed','Thank You for Request', 1000);
}

function Request() {

    return (
        <div class="request-page">
            <img class="logo-img-in-request" src="img/logo.png" />
            <div class="form">
                <h2>Contact Us</h2>

                <form class="url-request-from">
                    <input type="text" placeholder="username" />
                    <input id="url-input" class="url-input" type="url" placeholder="URL" />
                    <button class="close-btn" type="reset"></button>
                    <button class="submit-btn" onClick={submitNotification}>Submit</button>
                    <HelpMessage msg="More Request? " detail="Click Here!" />
                </form>

                <form class="other-request-form">
                    <input type="text" placeholder="username" />
                    <textarea type="text" placeholder="Message"></textarea>
                    <button class="submit-btn" onClick={submitNotification}>Submit</button>
                    <HelpMessage msg="URL Request? " detail="Click Here!" />
                </form>
                <NotificationContainer/>
            </div>
        </div>
    );
}

export default Request;
