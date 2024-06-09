<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="icon" type="image/x-icon" href="img/iconesp32IA.ico">
  <link rel="stylesheet" href="css/styleSignIn.css">
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <title>Data Logs</title>
</head>
<body>
  <header>
    <img src="img/LogoSecurity.png" width="100px" alt="pic1" style="float: right;">
    <img src="img/iconesp32IA.png" width="100px" alt="pic2" style="float: left;">
    <h1 class="titulo">Data log</h1>
    <h2>Welcome! :D</h2>
  </header>
  <main>
    <table border="1" class="tabla"><!-- Class table-->
      <thead>
        <tr>
          <th>Id</th>
          <th>Time</th>
          <th>IP Source</th>
          <th>IP Destine</th>
          <th>Protocol</th>
          <th>Size of Packet</th>
          <th>Info</th>
        </tr>
      </thead>
      <tbody>
        <?php
          // Conectandonos a la basesuki de datukis
          $servername = "localhost";
          $username = "root";
          $password = "root";
          $dbname = "ids";
          $db = new mysqli($servername, $username, $password, $dbname); // Aqui se hace la conexión

          // Verificando la conexión
          if ($db->connect_error) { // Para depurar y cachar el errorsito
              die("Connection failed: " . $db->connect_error);
          }

          // Check database
          $query = "SELECT * FROM traffic";
          $result = $db->query($query);

          // Verifica el resultado
          if ($result) {
            // Data loop
            while ($row = $result->fetch_assoc()) {
              echo "<tr>";
              echo "<td>" . htmlspecialchars($row["id"]) . "</td>"; // Para evitar ataques XSS
              echo "<td>" . htmlspecialchars($row["time"]) . "</td>";
              echo "<td>" . htmlspecialchars($row["ipsrc"]) . "</td>";
              echo "<td>" . htmlspecialchars($row["ipdst"]) . "</td>";
              echo "<td>" . htmlspecialchars($row["protocol"]) . "</td>";
              echo "<td>" . htmlspecialchars($row["packlen"]) . "</td>";
              echo "<td>" . htmlspecialchars($row["info"]) . "</td>";
              echo "</tr>";
          }
          } else {
            echo "Error in query: " . $db->error;
          }
          // Cerrando la conexion a la base para liberar recursos :)
          $db->close();

        ?>
      </tbody>
    </table>
    <canvas id="myChart" width="400" height="200"></canvas>
    <div class="form_container">
        <a href="index.php"  class="form_submit" onclick="session_destroy();">Sign out</a>
    </div>
    <br>
    <br>    
  </main>
  <br>
  <br>
  <script src="graficas.js"></script>
</body>
</html>
