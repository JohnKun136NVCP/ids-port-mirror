<!DOCTYPE html>
<html lang="en-US">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="icon" type="image/x-icon" href="img/iconesp32IA.ico">
	<title>IDS LOGGIN</title>
    <link rel="stylesheet" href="css/styles.css">
	
</head>
<body>
	<div class="img_circular">
		<img src="img/IA1.jpeg" alt="imagen1" >
	</div>
	<div>
        <form class="form" action="login.php" method="post">
        <h2 class="form_title">Login</h2>
        <div class="form_container">
            <div class="form_group">
                <input type="text" name="user" id="user" class="form_input" placeholder=" " required>
                <label for="user" class="form_label">User</label>
                <span class="form_line"></span>
            </div>
            <div class="form_group">
                <input type="password" name="password" id="password" class="form_input" placeholder=" " required>
                <label for="password" class="form_label">Password</label>
                <span class="form_line"></span>
            </div>
            <div class="form_group">
                <input type="email" name="email" id="email" class="form_input" placeholder=" " required>
                <label for="email" class="form_label">Email</label>
                <span class="form_line"></span>
            </div>
            <input type="submit" class="form_submit" value="Login">
        </div>
    </form>
	</div>
</body>
</html>