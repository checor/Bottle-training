
%#Muestra los productos en la db
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<style type="text/css">
table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
}
</style>
  <meta http-equiv="content-type"
 content="text/html; charset=ISO-8859-1">
  <title>Cotizador</title>
</head>
<body>
	<h1><img src="https://cock.li/cock.png" alt="cock" />Cocktizador</h2>
	<p>Minimalista because fuck you</p>
	<a href="/">home</a> |
	<a href="./productos">Productos</a> |
	<a href="./clientes">Clientes</a> |
	<a href="#">Ventas</a> | 
	<a href="#">Compras</a> |
	<a href="#">Backorder</a> |
	<a href="#">Cuentas</a> | 
	<a href="https://twitter.com/checor">twitter</a>
	<hr>
	<h3>Agregar nuevo produto:</h3>
	<form>
		<table style="*">
		<tr>
			<td>SKU:</td>
			<td><input type="text" name="SKU"></td>
		</tr>
		<tr>
			<td>Nombre:</td>
			<td><input type="text" name="nombre"></td>
		</tr>
		<tr>
			<td>Link:</td>
			<td><input type="text" name="link"></td>
		</tr>
		
		<tr><td><input type="submit" name="add" value="Agregar"></td></tr>
		</table>
	</form>

	<h3>Agregar nuevo link a producto existente:</h3>
	<form>
		<table style="*">
		<tr>
			<td>SKU:</td>
			<td><input type="text" name="SKU"></td>
		</tr>
		<tr>
			<td>Link:</td>
			<td><input type="text" name="link"></td>
		</tr>
		
		<tr><td><input type="submit" name="add_link" value="Agregar"></td></tr>
		</table>
	</form>

	<h3>Lista de productos:</h3>
	 <table style="*">
	  <tr>
	    <td><b>ID</b></td>
	    <td><b>Nombre</b></td>
	  </tr>
	  %for row in rows:
	  <tr>
	  	%for col in row:
	    <td>{{col}}</td>
	    %end
	  </tr>
	  %end
	</table>

    <h3>Borrar producto:</h3>
    <form>
        <table style="*">
        <tr>
            <td>SKU:</td>
            <td><input type="text" name="SKU"></td>
        </tr>
        <tr><td><input type="submit" name="del" value="Borrar"></td></tr>
        </table>
    </form>


</body>
</html>
