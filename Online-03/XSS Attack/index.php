<!DOCTYPE html>
<html>
<title> XSS Tutorial (Reflected) </title>
<body>
<h1 align="center"> Try  New Search Feature! </h1>
<table align="center">
<tr><td>
<form action="index.php" method="get">
	<input type="text" name="search" placeholder="search" />
	<input type="submit" value="Search" />
</form>
</td></tr>
</table>
<br />
<br />
<p align="center">
<?php
if(isset($_GET["search"]))
{
	echo "The results of your search for: ".$_GET["search"];
	echo "<br /><br /> <i>Sorry No Results Found! </i>";
}
?>
</p>
<h3 align="center"> Beautiful Search website </h3>
</body>
</html> 