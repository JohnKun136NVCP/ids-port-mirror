<?php
  // Conectarse a la base de datos
  $db = new mysqli("localhost", "root", "root", "ids");

  // Obtener los datos del formulario
  $username = $_POST["user"];
  $password = $_POST["password"];
  $email = $_POST["email"];
  // Verificar si la dirección de correo electrónico es válida
  if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    echo "La dirección de correo electrónico no es válida.";
    return;
  }
  // Consultar la base de datos para el nombre de usuario, la contraseña y el correo electrónico
  $query = "SELECT * FROM administrator WHERE user='$username' AND pass='$password' AND email='$email'";
  $result = $db->query($query);
  // Si hay un resultado, el inicio de sesión es correcto
  if ($result->num_rows > 0) {
    // Obtener los datos del usuario
    $row = $result->fetch_assoc();

    // Establecer la sesión
    session_start();
    $_SESSION["user"] = $row["user"];

    // Redirigir al usuario a la página de bienvenida
    header("Location: welcome.php");
  } else {
    // El inicio de sesión es incorrecto
    echo " $username $password $email";
    echo "El nombre de usuario o la contraseña son incorrectos.";
  }
?>
