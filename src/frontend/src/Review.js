import React, { useState, useEffect } from 'react';
import './Review.css';
import { NotificationContainer, NotificationManager } from 'react-notifications';
import 'react-notifications/lib/notifications.css';
import axios from "axios";
import { Badge } from 'styled-badge-component';

function ReviewContent(props) {
  return (
    <div class="review">
      <p class="review-txt">{props.reviews}</p>
    </div>
  )
}
function Review(props) {

  const [positiveReview, setPositiveReview] = useState([]);
  const [negativeReview, setNegativeReview] = useState([]);
  const [review, setReview] = useState([]);
  const server = "http://ec2-54-180-89-72.ap-northeast-2.compute.amazonaws.com:8080";

  function Notification(type, message) {
    if (type === 'fail') NotificationManager.error(message, 'Failed to laod Review', 2700, () => { });
    if (type === 'none') NotificationManager.info('', message, 2000);
  }

  useEffect(() => {
    axios.post(server + "/review", {
      item_url: props.itemUrl
    })
      .then(function (response) {
        console.log(response);
        if (response.data.status === 'fail') Notification("fail", response.data.message);
        else if (response.data.status === 'none') Notification("none", response.data.message)
        else {
          setPositiveReview(response.data.positive_review);
          setNegativeReview(response.data.negative_review);
        }
      })
      .catch(function (error) {
        console.log('err', error);
      });
  }, [])

  function checkPositive(event) {
    const positiveChecked = event.target.checked;
    if (positiveChecked) setReview(positiveReview);
    else {
      setReview([]);
    }
  }

  function checkNegative(event) {
    const negativeChecked = event.target.checked;
    if (negativeChecked) setReview(negativeReview);
    else {
      setReview([]);
    }
  }


  const addReviews = review.map(
    (review) => <ReviewContent reviews={review}></ReviewContent>
  );

  return (
    <div class="container">
      <div class="wrap">
        <a href="#" class="back-btn" onClick={props.openCart}>Back to Cart</a>
      </div>
      <img class="review-img" src="img/review.png" />
      <ul class="ks-cboxtags">
        <li><input type="checkbox" id="checkboxPositive" name="category" onChange={checkPositive} />
          <label for="checkboxPositive">
            Positive <Badge primary pill>{positiveReview.length}</Badge>
          </label></li>
        <li><input type="checkbox" id="checkboxNegative" name="category" onChange={checkNegative} />
          <label for="checkboxNegative">
            Negative <Badge primary pill>{negativeReview.length}</Badge>
          </label></li>
      </ul>
      {addReviews}
      <NotificationContainer />
    </div>
  );
}

export default Review;