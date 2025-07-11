# first flet app
## Entorno virtual
Creamos el entorno virtual, el nombre <i>v_env</i>  esta agregado en gitignore.
```
python3 -m venv v_env
```
Activamos el entorno
```
source v_env/bin/activate
```
Instalamos los requerimientos
```
pip3 install -r requirements.txt
```
## Libreria necesaria para ejecutar
```
sudo apt update
sudo apt install libmpv1
```
libmpv1 permite a otras aplicaciones (como Flet Desktop) mostrar contenido HTML, multimedia o incluso interfaces web dentro de una ventana de escritorio.

En el caso de Flet, se usa indirectamente a través de un componente embebido tipo WebView (navegador embebido) que depende de MPV en Linux.

Lo que permite:
✅ Mostrar interfaces basadas en HTML/CSS/JS en una ventana nativa.
✅ Renderizar páginas como si fuera un mini navegador.
✅ Controlar ese rendering desde tu código Python.
✅ Mostrar contenido multimedia si hace falta.