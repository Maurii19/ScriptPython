#!/usr/bin/env python
# -*- coding: utf-8 -*-
#https://www.python-course.eu/global_vs_local_variables.php

#definimos un array con los tipos de billetes, monedas y centimos
billetes=[500, 200, 100, 50, 20, 10, 5]

monedas = [2, 1]

centimos = [0.5, 0.2, 0.1, 0.05, 0.02, 0.01]

#Definimos la funcion "calcular"
def calcular(euros):
	while len(billetes)>0:
		billete = billetes.pop(0)
		cantidadBilletes = int(euros/billete)
		euros = float(euros) - float(cantidadBilletes)*float(billete)
		calcular(round(euros,2))
		if cantidadBilletes>0:
			print "Billetes de %s: %d " % (billete, cantidadBilletes)
		else:
			continue
			
	while len(monedas)>0:
		moneda = monedas.pop(0)
		cantidadMonedas = int(euros/moneda)
		euros = float(euros) - float(cantidadMonedas)*float(moneda)
		calcular(round(euros,2))
		if cantidadMonedas>0:
			print "Monedas de %s: %d " % (moneda, cantidadMonedas)
		else:
			continue
			
	while len(centimos)>0:
		centimo = centimos.pop(0)
		cantidadCentimos = int(euros/centimo)
		euros = float(euros) - float(cantidadCentimos)*float(centimo)
		calcular(round(euros,2))
		if cantidadCentimos>0:
			print "Centimos de %s: %d " % (centimo, cantidadCentimos)
		else:
			continue

euros=float(input("Introduce la cantidad de euros: "))
calcular(round(euros, 2))
