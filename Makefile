run:
	python main.py

conda-install:
	conda env create -f environment.yml
	conda activate text2sql

pip-install:
	pip install -r requirements.txt