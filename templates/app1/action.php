<?php
$conn = new PDO('mysql:host=localhost;dbname:infoxfinsystem','root','');

foreach($_POST['productname'] as $key => $value ){
    $sql =  'INSERT INTO  items(productname,sku,quantity,price,amount) VALUES (:productname, :sku, :quantity, :price, :amount)';
    $stmt = $conn->prepare($sql);
    $stmt->execute([
        'productname' => $value,
        'sku' => $_POST['sku'][$key],
        'quantity' => $_POST['quantity'][$key],
        'price' => $_POST['price'][$key],
        'amount' => $_POST['amount'][$key]
    ]);
}
echo 'Items inserted successfully!';