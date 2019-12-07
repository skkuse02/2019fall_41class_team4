/*global chrome*/
export function saveLoginInfo(id, pw) {
  chrome.storage.local.set({ id, pw }, function () {
    chrome.extension.getBackgroundPage().console.log('Value stored : ', id, pw);
  });
}

export function loadLoginInfo() {
  return new Promise((resolve, reject) => {
    chrome.storage.local.get(['id'], function (result) {
      console.log('Current Login INfo :  ' + result.id);
      resolve(result.id);
    });
  });
}

export function logout() {
  chrome.storage.local.clear(function () {
    var error = chrome.runtime.lastError;
    if (error) {
      console.error(error);
    }
  });
}