<?php
	header("Access-Control-Allow-Origin: *");
	$str = $_POST["ID"];
	try{
		$db = new SQLite3('census.db');
		$stm = $db->prepare("SELECT * FROM people WHERE CountyId = '$str' LIMIT 1");
		$out = [];
  		$res = $stm->execute();
		while ($row = $res->fetchArray(SQLITE3_ASSOC)) {
    			array_push($out, $row);
		}
		$temp = json_encode($out);
		header('Content-Type: application/json');
		echo $temp;
	}
catch(Exception $e){
	echo $e->getmessage();
}
?>