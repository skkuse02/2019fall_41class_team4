import React from 'react';
import './Review.css';
import { tsPropertySignature } from '@babel/types';

function checkAllCheckbox(event){
  const allCheckboxChecked = event.target.checked;
  var categories = document.getElementsByName("category");
  if(allCheckboxChecked){
    for(var i in categories){
      if(categories[i].checked == false) categories[i].checked =true;
    }
  } else{
    for(var i in categories){
      if(categories[i].checked == true) categories[i].checked =false;
    }
  }
}

function Review(props) {
  return (
    <div class="container">
      <div class="wrap">
  		  <a href="#" class="back-btn" onClick={props.openCart}>Back to Cart</a>
	    </div>
      <img class="review-img" src="img/review.png" />
      <ul class="ks-cboxtags">
        <li><input type="checkbox" id="checkboxAll" value="All" onChange={checkAllCheckbox}/><label for="checkboxAll">Select All</label></li>
        <li><input type="checkbox" id="checkboxDelivery" name="category" /><label for="checkboxDelivery">Delivery</label></li>
        <li><input type="checkbox" id="checkboxQuality" name="category" /><label for="checkboxQuality">Quality</label></li>
        <li><input type="checkbox" id="checkboxSize" name="category" /><label for="checkboxSize">Size</label></li>
        <li><input type="checkbox" id="checkboxAS" name="category" /><label for="checkboxAS">Afeter Service</label></li>
      </ul>
      <div class="review">
        <p class="review-txt">This is Review</p>
      </div>
      <div class="review">
        <p class="review-txt">This is review</p>
      </div>
      
    </div>
  );
}

export default Review;