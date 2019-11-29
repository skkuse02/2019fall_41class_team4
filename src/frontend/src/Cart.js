import React from 'react';
import './Cart.css';


function Cart(props) {

    return (
        <div class="container page-wrapper">
            <div class="menu-bar">
                <img class="menu icon1" src="img/shopping-cart.png" />
                <h2 class="menu picket">PICKET</h2>
                <h2 class="menu price">PRICE : </h2>
                <div class=" menu contact-box" onClick={props.openRequest}>
                    <img class="menu icon2" src="img/phone.png" />
                    <h2 class="menu contact">Contact Us</h2>
                </div>
            </div>
            <div class="page-inner">
                <div class="row">
                    <div class="blank-wrapper">
                        <h1>Add to Cart</h1>
                    </div>

                    <div class="el-wrapper">
                        <div class="box-up">
                            <img class="img" src="http://code.slicecrowd.com/labs/4/images/t-shirt.png" alt="" />
                            <div class="img-info">
                                <div class="info-inner">
                                    <span class="p-name">I feel like Pablo</span>
                                    <span class="p-company">Yeezy</span>
                                </div>
                            </div>
                        </div>
                        <div class="not-delete-box">
                            <div class="h-bg">
                            </div>
                            <a class="cart" href="#">
                                <span class="add-to-cart">
                                    <span class="txt">Review</span>
                                </span>
                            </a>
                        </div>
                        <div class="not-delete-box">
                            <div class="h-bg">
                            </div>
                            <a class="cart" href="#">
                                <span class="add-to-cart">
                                    <span class="txt">Modify</span>
                                </span>
                            </a>
                        </div>

                        <div class="box-down">
                            <div class="h-bg">
                            </div>

                            <a class="cart" href="#">
                                <span class="price">$120</span>
                                <span class="add-to-cart">
                                    <span class="txt">Delete</span>
                                </span>
                            </a>
                        </div>
                    </div>
                    <a href="#" class="save-btn">
                        <h5 class="save-txt">SAVE</h5>
                    </a>
                </div>
            </div>
        </div>
    );
}

export default Cart;
