<!-- ./php/index.php -->
<html>
<head>
    <title>PHP MySQL Docker Test</title>
    <style>
        body { font-family: sans-serif; margin: 20px; }
        .success { color: green; }
        .error { color: red; }
        .info { color: blue; }
    </style>
</head>
<body>
    <h1>PHP MySQL Docker Example</h1>

    <?php
    // Database connection parameters from docker-compose.yml
    $host = 'db'; // This is the service name of the MySQL container
    $port = '3306'; // Default MySQL port
    $db_name = getenv('MYSQL_DATABASE') ?: 'test_db'; // Environment variable from db service
    $user = getenv('MYSQL_USER') ?: 'devuser';         // Environment variable from db service
    $pass = getenv('MYSQL_PASSWORD') ?: 'devpass';     // Environment variable from db service

    echo "<p class='info'>Attempting to connect to MySQL server: Host='{$host}', Database='{$db_name}', User='{$user}'</p>";

    // Check if mysqli extension is loaded
    if (!extension_loaded('mysqli')) {
        echo "<p class='error'>Error: MySQLi extension is not loaded in PHP. Please ensure it is enabled in your PHP configuration.</p>";
        exit;
    }

    // Create connection
    $conn = new mysqli($host, $user, $pass, $db_name, (int)$port);

    // Check connection
    if ($conn->connect_error) {
        echo "<p class='error'>Connection Failed: " . htmlspecialchars($conn->connect_error) . "</p>";
        echo "<p><strong>Common issues:</strong></p>";
        echo "<ul>";
        echo "<li>Is the 'db' service running? Check with <code>docker compose ps</code>.</li>";
        echo "<li>Are the environment variables (MYSQL_DATABASE, MYSQL_USER, MYSQL_PASSWORD) correctly set for the 'db' service in <code>docker-compose.yml</code> and matching here?</li>";
        echo "<li>Is the MySQL server fully initialized? It might take a few moments after starting.</li>";
        echo "</ul>";
    } else {
        echo "<p class='success'>Successfully connected to MySQL database '<strong>" . htmlspecialchars($db_name) . "</strong>'!</p>";

        // Example: Show server version
        $result = $conn->query("SELECT VERSION() as version;");
        if ($result) {
            $row = $result->fetch_assoc();
            echo "<p>MySQL Server Version: <strong>" . htmlspecialchars($row['version']) . "</strong></p>";
            $result->free();
        } else {
            echo "<p class='error'>Failed to execute query 'SELECT VERSION()': " . htmlspecialchars($conn->error) . "</p>";
        }

        // Example: List tables (if any)
        $result = $conn->query("SHOW TABLES;");
        if ($result) {
            if ($result->num_rows > 0) {
                echo "<p>Tables in database '<strong>" . htmlspecialchars($db_name) . "</strong>':</p><ul>";
                while($row = $result->fetch_array(MYSQLI_NUM)) {
                    echo "<li>" . htmlspecialchars($row[0]) . "</li>";
                }
                echo "</ul>";
            } else {
                echo "<p>No tables found in database '<strong>" . htmlspecialchars($db_name) . "</strong>'.</p>";
            }
            $result->free();
        } else {
            echo "<p class='error'>Failed to execute query 'SHOW TABLES;': " . htmlspecialchars($conn->error) . "</p>";
        }
        $conn->close();
    }
    ?>
</body>
</html>
