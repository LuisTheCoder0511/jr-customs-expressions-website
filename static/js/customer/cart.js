document.getElementById("checkout_button").addEventListener("mousedown", e => {
            if (e.button !== 0) return
    window.location.href = "/customer_page/order_checkout"
})