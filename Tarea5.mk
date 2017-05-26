Resultados_hw5.pdf: Radio_ionico.jpg experimentales.jpg histcircuitos.jpg Radio_ion1.jpg hist2.jpg hist1.jpg Resultados_hw5.tex
			pdflatex Resultados_hw5.tex

Radio_ionico.jpg: radios.txt canal_ionico.py
	python plots_canal_ionico.py 

experimentales.jpg: CircuitoRC.txt circuitoRC.py
	python circuitoRC.py

histcircuitos.jpg:CircuitoRC.txt circuitoRC.py
	python circuitoRC.py

Radio_ion1.jpg:radios.txt canal_ionico.py
	python plots_canal_ionico.py

hist1:radios.txt canal_ionico.py
	python plots_canal_ionico.py
	
hist2:radios.txt canal_ionico.py
	python plots_canal_ionico.py

radios.txt: canal_ionico.txt canal_ionico1.txt canal_ionico.c 
	gcc canal_ionico.c 
	./a.out>radios.txt


