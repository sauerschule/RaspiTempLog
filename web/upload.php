<?php
  if ( isset($_FILES["PASSWORD_CHANGE_ME"]) ) {
    $oldName = $_FILES["PASSWORD_CHANGE_ME"]["tmp_name"];
    $newFileName = "wetter.log";
    $newName = "/path/to/webspace/" . $newFileName;
    rename($oldName,$newName);
    chmod($newName, 0644);
  }
?>
