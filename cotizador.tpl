%# Pagina donde se muestran los resultados cotiazados
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
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
	Precio en USD: {{usd_price}}<br/>
	1 USD = {{usd_mxn}} MXN<br/>
	Precio sin taxas ni ganacias {{usd_mxn * usd_price}}<br/>
	Precio al 30%: {{usd_mxn * usd_price * 1.3}}<br/>
</body>
</html>
