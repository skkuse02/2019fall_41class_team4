import React from 'react';
import './Review.css';

function Review() {
  return (
    <div class="container">
      <img class="review-img" src="img/review.png" />
      <ul class="ks-cboxtags">
        <li><input type="checkbox" id="checkboxAll" value="All" /><label for="checkboxAll">All Reviews</label></li>
        <li><input type="checkbox" id="checkboxDelivery" value="Delivery" /><label for="checkboxDelivery">Delivery</label></li>
        <li><input type="checkbox" id="checkboxQuality" value="Quality" /><label for="checkboxQuality">Quality</label></li>
        <li><input type="checkbox" id="checkboxSize" value="Size" /><label for="checkboxSize">Size</label></li>
        <li><input type="checkbox" id="checkboxAS" value="AS" /><label for="checkboxAS">Afeter Service</label></li>
      </ul>
    </div>
  );
}

export default Review;