@echo off
call venv\Scripts\activate
python train_model.py
python app.py
