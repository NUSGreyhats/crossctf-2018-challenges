<?php

class dbConn {
  private $conn;
  public function __construct() {
    $dbhost = 'localhost';
    $dbuser = 'crossctf';
    $dbpass = '9A&*h^F68l9QgzQyc6C4MajY3SHf332I1ENYcVjb';
    $dbname = 'crossctf';
    $this->conn = new mysqli($dbhost, $dbuser, $dbpass, $dbname) or die("Wrong info given");
    if (mysqli_connect_errno()) {
      exit();
    }
  }

  public function getConn() {
    return $this->conn;
  }


  public function clearResult() {
    while ($this->conn->more_results() && $this->conn->next_result()) {
      $result = $this->conn->use_result();
      if ($result instanceof mysqli_result) {
        $result->free();
      }
    }
  }

  public function checkLogin($username, $password) {
    $username = $this->conn->real_escape_string($username);
    $password = $this->conn->real_escape_string($password);
    $sql = "SELECT * FROM users WHERE username = '$username' AND password = MD5('$password');";
    if ($this->conn->multi_query($sql)) {
      $result = $this->conn->store_result();
      $row = $result->fetch_array();
      $this->conn->close();
      return $row;
    } else {
      $this->conn->close();
      return false;
    }
  }

  public function getProfile($username) {
    $username = $this->conn->real_escape_string($username);
    $sql = "SELECT username, profile from users where username = '$username';";
    if ($this->conn->multi_query($sql)) {
      $result = $this->conn->store_result();
      $row = $result->fetch_array();
      $this->conn->close();
      return $row;
    } else {
      $this->conn->close();
      return false;
    }
  }

  public function updateProfile($username, $profile) {
    $username = $this->conn->real_escape_string($username);
    $profile = $this->conn->real_escape_string($profile);
    $sql = "UPDATE users set profile = '$profile' where username = '$username';";
    if ($this->conn->query($sql)) {
        $this->conn->close();
        return True;
    } else {
        $this->conn->close();
        return False;
    }
  }

  public function createNewUser($username, $password) {
    $username = $this->conn->real_escape_string($username);
    $password = $this->conn->real_escape_string($password);
    $sql = "INSERT INTO users VALUES (null, '$username', MD5('$password'), 'Your New Profile!');";
    if ($this->conn->multi_query($sql)) {
      $id = mysqli_insert_id($this->conn);
      $this->conn->close();
      return $id;
    } else {
      $this->conn->close();
      return false;
    }
  }

  public function doesUsernameExist($username) {
    $username = $this->conn->real_escape_string($username);
    $sql = "SELECT * from users where username = '$username';";
    if ($this->conn->multi_query($sql)) {
      $result = $this->conn->store_result();
      $row = $result->fetch_array();
      $this->conn->close();
      return sizeof($row)>0;
    } else {
      $this->conn->close();
      return false;
    }
  }
}
?>