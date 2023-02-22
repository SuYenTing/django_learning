function onsale(){
    var name=document.getElementById('name');
    var price=document.getElementById('price');
    var qty=document.getElementById('qty');
    document.getElementById('demo').innerHTML="<hr>名稱:" + name.value + "<br>" +
                                              "價格:" + price.value + "<br>" +
                                              "數量:" + qty.value + "<br>" +
                                              "<hr>合計: " + (price.value * qty.value) + "<br>";
    
};

document.getElementById('cup').addEventListener('mouseenter', function(){
    setBG(this);
});

document.getElementById('cup').addEventListener('mouseleave', function(){
    clearBG(this);
});