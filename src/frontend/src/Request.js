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
function Request() {

    return (

        <div class="request-page">
            <div class="form">
                <h2>Contact Us</h2>

                <form class="url-request-from">
                    <input type="text" placeholder="username" />
                    <input id="url-input" class="url-input" type="url" placeholder="URL" />
                    <button class="close-btn" type="reset"></button>
                    <button class="submit-btn">Submit</button>
                    <HelpMessage msg="More Request? " detail="Click Here!" />
                </form>

                <form class="other-request-form">
                    <input type="text" placeholder="username" />
                    <textarea type="text" placeholder="Message"></textarea>
                    <button class="submit-btn">Submit</button>
                    <HelpMessage msg="URL Request? " detail="Click Here!" />
                </form>
            </div>
        </div>
    );
}

export default Request;
