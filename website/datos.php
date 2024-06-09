<?php
$servername = "localhost";
$username = "root";
$password = "root";
$dbname = "ids";

// Crea la conexión a la base de datos
$conn = new mysqli($servername, $username, $password, $dbname);

// Verifica la conexión
if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}

// Realiza la consulta para obtener los datos
$sql = "SELECT time, packlen FROM traffic";
$result = $conn->query($sql);

// Verifica si hay resultados y convierte los resultados a un array asociativo
if ($result->num_rows > 0) {
    $data = array();
    while ($row = $result->fetch_assoc()) {
        $data[] = $row;
    }
    // Convierte el array a formato JSON y lo imprime
    header('Content-Type: application/json');
    echo json_encode($data);
} else {
    echo "0 results";
}

// Cierra la conexión a la base de datos
$conn->close();
?>

