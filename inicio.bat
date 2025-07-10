@echo off
REM Activar el entorno virtual
call env\Scripts\activate

REM Ejecutar la aplicación de Streamlit
streamlit run app.py

REM Dejar la consola abierta después de ejecutar
pause