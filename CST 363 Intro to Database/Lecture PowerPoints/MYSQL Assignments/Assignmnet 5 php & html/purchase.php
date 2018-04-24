<?php 
// retrieve user data   
$item_id= $_POST["id"];
$quantity = $_POST["quantity"];
$order_name = $_POST["name"];
$discount_code=$_POST["code"];
        
$host = "localhost";
$user = "root";
$password = "Scorpio182";
$database = "A5";
$port = 3306;
// create connection
$conn = new mysqli($host, $user, $password, $database, $port);
if ($conn->connect_errno) {
    exit ("Failed to connect: (" . $conn->connect_errno . ") " . $conn->connect_error );
}
// check that item_id entered by user is valid 
$sql = "select name, price from items where id = ?";
$stmt = $conn->prepare($sql);
$stmt->bind_param("i", $item_id);
$stmt->execute();
$stmt->store_result();
if ($stmt->num_rows <= 0) {
    exit ("Error.  Item id entered is not valid." . $conn->connect_errno . ":" . $conn->connect_error);
}
// retrieve item_name and price 
$stmt->bind_result($item_name, $price);
$stmt->fetch();
// calculate total purchase 
if($discount_code=="SAVE10"){
	$discount=10;
	$total = ( $quantity * $price)-(($quantity * $price)*0.1);
}elseif ($discount_code==""){
	$discount=0;
	$total = $quantity * $price;
}else{
	if(($quantity * $price)>25.00){
		$discount=5;
		$total = ( $quantity * $price)-(($quantity * $price)*0.05);
	}else{
		$discount=0;
		$total = $quantity * $price;
	}
}
 
// store order 
$sqli = "insert into orders values( null, ?, ?, ?, ?,?)";
$stmti = $conn->prepare($sqli);
$stmti->bind_param("siidi", $order_name, $item_id,  $quantity, $total,$discount);
if (!$stmti->execute()) {
    exit ("Error.  Unable to place order." . $conn->error);
}
// commit transaction and close connection
$conn->commit();
$conn->close();
?>
 
<!DOCTYPE html>
<html>
<head>
<style>
table {
    border-collapse: collapse;
    width: 100%;
}
 
td, th {
    border: 1px solid #dddddd;
    text-align: left;
    padding: 8px;
}
 
</style>
</head>
<body>
<h1>Thank you for shopping!</h1>
<p>Your order</p>
 
<?php 
echo date("l jS \of F Y h:i:s A"); 
?>
 
<br>
<p>Name = <?= $order_name;?> </p>
<br>
<table>
<tr><th>Item Id</th><th>Item Name</th><th>Quantity</th><th>Price</th></tr>
<tr><td><?= $item_id;?></td> <td> <?= $item_name; ?> </td> <td> <?= $quantity; ?> </td> <td> <?= $price; ?> </td></tr>
</table>
<p>Total = $<?= $total;?></p>
 
</body>
</html>
