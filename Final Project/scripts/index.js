let bagItems;
onLoad()

function onLoad() {
    let bagItemsStr = localStorage.getItem('bagItems')
    bagItems = bagItemsStr ? JSON.parse(bagItemsStr) : []
    displayItemOnHomePage()
    displayBagIcon()
}

function addToBag(itemId) {
    bagItems.push(itemId);
    localStorage.setItem('bagItems', JSON.stringify(bagItems))
    displayBagIcon()
}

function displayBagIcon() {
    let bagItemsCountElement = document.querySelector('.bag-items-count')
    if (bagItems.length > 0) {
        bagItemsCountElement.style.visibility = 'visible'
        bagItemsCountElement.innerText = bagItems.length
    } else {
        bagItemsCountElement.style.visibility = 'hidden'
    }
}
function displayItemOnHomePage() {
    // Select the element with class "items-container"
    let itemsContainerElement = document.querySelector('.items-container');
    if (!itemsContainerElement) {
        return
    }
    // Initialize an empty string to hold the inner HTML
    let innerHTML = '';

    // Loop through each item and build the HTML
    items.forEach(item => {
        innerHTML += `
        <div class="item-container">
            <img class="item-image" src="${item.image}" alt="image">
            <div class="rating">
               ${item.rating.stars}⭐ | ${item.rating.count}
            </div>
            <div class="company-name">${item.company}</div>
            <div class="item-name">${item.item_name}</div>
            <div class="price">
                <span class="current-price">₹${item.current_price}</span>
                <span class="original-price">₹${item.original_price}</span>
                <span class="discount">(${item.discount_percentage}% Off)</span>
            </div>
            <button class="btn-add-bag" onclick="addToBag(${item.id})">Add to Bag</button>
        </div>
    `;
    });

    // Inject the generated HTML into the container
    itemsContainerElement.innerHTML = innerHTML;

}

