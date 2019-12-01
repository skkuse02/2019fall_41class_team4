import React, { useState } from 'react';
import './Cart.css';
import { NotificationContainer, NotificationManager } from 'react-notifications';
import 'react-notifications/lib/notifications.css';
import { getDiffieHellman } from 'crypto';

function ItemCard(props) {
    return (
        <div class="el-wrapper">
            <div class="box-up">
                <img class="img" src={props.itemInfo.img_src} alt="" />
                <div class="img-info">
                    <div class="info-inner">
                        <span class="p-name">{props.itemInfo.pname}</span>
                        <span class="p-company">{props.itemInfo.pcompany}</span>
                    </div>
                </div>
            </div>
            <div class="box-down-wrapper">
                <div class="box-down">
                    <div class="h-bg">
                    </div>
                    <a class="cart" href="#" onClick={props.openReview}>
                        <span class="add-to-cart">
                            <span class="txt">Review</span>
                        </span>
                    </a>
                </div>
                <div class="box-down">
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

                    <a class="cart" href="#" onClick={() => props.removeItem(props.itemInfo.id)}>
                        <span class="price">{props.itemInfo.price}</span>
                        <span class="add-to-cart" >
                            <span class="txt">Delete</span>
                        </span>
                    </a>
                </div>
            </div>
        </div>
    );
}
var id = 0;
function Cart(props) {
    function saveNotification() {
        NotificationManager.info('', 'Save Completed', 1000);
    } 

    const [item_info, setItemInfo] = useState(
        [{
            id: 0,
            img_src: 'http://code.slicecrowd.com/labs/4/images/t-shirt.png',
            pname: "I feel like Pablo",
            pcompany: "Yeezy",
            price: "$100"
        }]
    );

    function addItem() {
        setItemInfo(
            item_info.concat({
                id: ++id,
                img_src: 'http://code.slicecrowd.com/labs/4/images/t-shirt.png',
                pname: "I feel like Pablo",
                pcompany: "Yeezy",
                price: "$120"
            })
        );
    }

    function removeItem(id) {
        const items = item_info.filter(item_info => item_info.id !== id);
        setItemInfo(items);
    }

    const addCart = item_info.map(
        (item) => (<ItemCard itemInfo={item} openReview={props.openReview} removeItem={removeItem}></ItemCard>)
    );

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
                    <div class="blank-wrapper" onClick={addItem}>
                        <h1>Add to Cart</h1>
                    </div>
                    {addCart}
                    <a href="#" class="save-btn" onClick={saveNotification}>
                        <h5 class="save-txt">SAVE</h5>
                    </a>
                    <NotificationContainer />
                </div>
            </div>
        </div>
    );
}

export default Cart;
