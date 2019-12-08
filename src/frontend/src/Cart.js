/*global chrome*/
import React, { useState, useEffect } from 'react';
import './Cart.css';
import { NotificationContainer, NotificationManager } from 'react-notifications';
import 'react-notifications/lib/notifications.css';
import axios from "axios";
import { loadLoginInfo } from "./authlib";
import Modal from './Modal/Modal';

function openUrl(url) {
    window.open(url);
}


function ItemCard(props) {
    return (
        <div class="el-wrapper">
            <div class="box-up" onClick={() => openUrl(props.itemInfo.item_url)}>
                <img class="img" src={props.itemInfo.item_image} alt="" />
                <div class="img-info">
                    <div class="info-inner">
                        <span class="p-name">{props.itemInfo.item_name}</span>
                        <span class="p-company">{props.itemInfo.item_domain}</span>
                    </div>
                </div>
            </div>
            <div class="box-down-wrapper">
                <div class="box-down">
                    <div class="h-bg">
                    </div>
                    <a class="cart" href="#" onClick={() => props.openReview(props.itemInfo.item_url)}>
                        <span class="add-to-cart">
                            <span class="txt">Review</span>
                        </span>
                    </a>
                </div>
                <div class="box-down">
                    <div class="h-bg">
                    </div>
                    <a class="cart" onClick={() => props.onModify(props.itemInfo)}>
                        <span class="add-to-cart">
                            <span class="txt">Modify</span>
                        </span>
                    </a>
                </div>

                <div class="box-down">
                    <div class="h-bg">
                    </div>

                    <a class="cart" href="#" onClick={() => props.removeItem(props.itemInfo)}>
                        <span class="price">{props.itemInfo.item_price}원</span>
                        <span class="add-to-cart" >
                            <span class="txt">Delete</span>
                        </span>
                    </a>
                </div>
            </div>
        </div>
    );
}

function Cart(props) {
    function Notification(type, message) {
        if (type === 'parsing-fail') NotificationManager.error(message, 'Failed to add cart', 2700, () => { });
        if (type === 'load-fail') NotificationManager.error(message, 'Failed to load cart', 2700, () => { });
        if (type === 'save-fail') NotificationManager.error(message, 'Failed to save cart', 2700, () => { });
        if (type === 'save-success') NotificationManager.info('', 'Save Completed', 1000);
    }

    const server = "http://ec2-54-180-89-72.ap-northeast-2.compute.amazonaws.com:8080";
    const [item_info, setItemInfo] = useState([]);
    const [user_id, setID] = useState('');
    const [url, setUrl] = useState('');
    const [isModalOpen, setModalOpen] = useState(false);
    const [modifyIndex, setModifyIndex] = useState(-1);


    const openModal = () => {
        setModalOpen(true);
    }

    const closeModal = (modify_item_info) => {
        setModalOpen(false);
        if (modify_item_info) {
            item_info[modifyIndex].item_domain = modify_item_info.domain_name;
            item_info[modifyIndex].item_name = modify_item_info.item_name;
            item_info[modifyIndex].item_price = modify_item_info.item_price;
        }
    }

    function onModify(itemInfo) {
        setModalOpen(true);
        setModifyIndex(item_info.indexOf(itemInfo));
    }

    useEffect(() => {
        loadLoginInfo()
            .then((user_id) => {
                setID(user_id)
                return axios.post(server + "/loadcart", {
                    user_id: user_id
                })
            })
            .then(function (response) {
                if (response.data.status === 'fail') Notification('load-fail', response.data.message);
                else {
                    setItemInfo(response.data.user_cart);
                    console.log(response.data.user_cart)
                }
            })
            .catch(function (error) {
                console.log('err', error);
            });
        chrome.tabs.getSelected(null, function (tab) {
            setUrl(tab.url);
        });
    }, [])

    function addItem() {
        axios.post(server + "/item", { item_url: url })
            .then(function (response) {
                if (response.data.status === 'fail') Notification('parsing-fail', response.data.message);
                else {
                    setItemInfo(
                        item_info.concat({
                            item_url: response.data.item_url,
                            item_domain: response.data.domain_name,
                            item_name: response.data.item_name,
                            item_price: response.data.item_price,
                            item_image: response.data.item_image
                        })
                    );
                }
            })
            .catch(function (error) {
                console.log('err', error);
            });
    }

    function removeItem(target) {
        const items = item_info.filter(item_info => item_info !== target);
        setItemInfo(items);
    }

    function saveItem() {
        axios.post(server + "/savecart", {
            user_id: user_id,
            user_cart: item_info
        })
            .then(function (response) {
                console.log(response.data);
                if (response.data.status === 'fail') Notification('save-fail', response.data.message);
                else Notification('save-success', "");
            })
            .catch(function (error) {
                console.log('err', error);
            });
    }

    function getTotalPrice() {
        let total_price = 0;
        for (let i = 0; i < item_info.length; i++) {
            total_price += parseInt(item_info[i].item_price.replace(/,/g, ''));
        }
        return total_price;
    }
    const addCart = item_info.map(
        (item) => (<ItemCard itemInfo={item} openReview={props.openReview} removeItem={removeItem} onModify={onModify}></ItemCard>)
    );

    return (
        <div class="container page-wrapper">
            <div class="menu-bar">
                <img class="menu icon1" src="img/shopping-cart.png" />
                <h2 class="menu picket">PICKET</h2>
                <h2 class="menu price">PRICE : {getTotalPrice()}원</h2>
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
                    <a href="#" class="save-btn" onClick={saveItem} >
                        <h5 class="save-txt">SAVE</h5>
                    </a>
                    <NotificationContainer />
                    <Modal isOpen={isModalOpen} close={closeModal} />
                </div>
            </div>
        </div>
    );
}

export default Cart;
