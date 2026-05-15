function swapCurrencies() {

    const from = document.getElementById("from_currency");
    const to = document.getElementById("to_currency");

    const temp = from.value;
    from.value = to.value;
    to.value = temp;

    // déclenche conversion live si tu l'as activée
    if (typeof autoConvert === "function") {
        autoConvert();
    }
}