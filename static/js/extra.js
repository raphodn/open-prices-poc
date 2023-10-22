// https://stackoverflow.com/a/61975440/4293684
function observeElement(element, property, callback, delay = 0) {
    let elementPrototype = Object.getPrototypeOf(element);
    if (elementPrototype.hasOwnProperty(property)) {
        let descriptor = Object.getOwnPropertyDescriptor(elementPrototype, property);
        Object.defineProperty(element, property, {
            get: function() {
                return descriptor.get.apply(this, arguments);
            },
            set: function () {
                let oldValue = this[property];
                descriptor.set.apply(this, arguments);
                let newValue = this[property];
                if (typeof callback == "function") {
                    setTimeout(callback.bind(this, oldValue, newValue), delay);
                }
                return newValue;
            }
        });
    }
}


function getOrCreateLocalStorageItem(itemKey, defaultValue=[]) {
    if (!localStorage.getItem(itemKey)) {
        localStorage.setItem(itemKey, JSON.stringify(defaultValue));
    }
    return localStorage.getItem(itemKey);
}

function clearLocalStorageItem(itemKey, defaultValue=[]) {
    return localStorage.setItem(itemKey, JSON.stringify(defaultValue));
}

function getParsedLocalStorageItem(itemKey) {
    let item = getOrCreateLocalStorageItem(itemKey);
    return JSON.parse(item);
}

function addObjectToLocalStorageItemList(itemKey, obj, avoidDuplicates=true) {
    let itemJSON = getParsedLocalStorageItem(itemKey);
    var existingItem = itemJSON.find(item => JSON.stringify(item) === JSON.stringify(obj));
    if (avoidDuplicates && existingItem) {
        return;
    }
    itemJSON[itemJSON.length] = obj;
    return localStorage.setItem(itemKey, JSON.stringify(itemJSON));
}
