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
    <h3>Agregar nuevo cliente:</h3>
    <form>
        <table style="*">
        <tr>
            <td>Nombre:</td>
            <td><input type="text" name="nombre"></td>
        </tr>
        <tr>
            <td>Direccion:</td>
            <td><input type="text" name="direccion"></td>
        </tr>
        <tr>
            <td>Tienda: (Pony o Impor) </td>
            <td><input type="text" name="tienda"></td>
        </tr>        
        <tr>
            <td>Credito inicial:</td>
            <td><input type="number" name="credito"></td>
        </tr>

        <tr><td><input type="submit" name="add" value="Agregar"></td></tr>
        </table>
    </form>

    <h3>Lista de clientes:</h3>
     <table style="*">
      <tr>
        <td><b>ID</b></td>
        <td><b>Nombre</b></td>
		<td><b>Dirección</b></td>
		<td><b>Tienda</b></td>
		<td><b>Crédito</b></td>
      </tr>
      %for row in rows:
      <tr>
        %for col in row:
        <td>{{col}}</td>
        %end
      </tr>
      %end
    </table>

    <h3>Borrar cliente:</h3>
    <form>
        <table style="*">
        <tr>
            <td>ID:</td>
            <td><input type="text" name="ID"></td>
        </tr>
        <tr><td><input type="submit" name="del" value="Borrar"></td></tr>
        </table>
    </form>


</body>
</html>

