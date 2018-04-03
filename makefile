album.pdf: monas.txt graf.py
	python graf.py

monas.txt: album
	./album > monas.txt

album:
	c++ album.cpp -o album
