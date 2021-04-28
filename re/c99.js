fetch("/9786685467/4070952349/137.115.166.22").then((response)=>{
    return response.json();
}
).then((data)=>{
    document.querySelector("#jn").value = "JS aan, T aangeroepen";
    let selectedItems = document.getElementsByName("CSRF98434202127048797932");
    selectedItems.forEach(item=>{
        item.setAttribute("name", "CSRF98434" + data.d02e74f10e0327ad868d138f2b4fdd6f0 + "8797932");
        document.querySelector("#jn").value = "JS aan, T aangeroepen, CSRF aangepast";
    }
    );
}
).catch(function(error) {
    document.querySelector("#jn").value = "JS aan, T niet aangeroepen, error: " + error;
    console.log("Something went wrong while fetching token.");
});

