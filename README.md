# 🔐 Aplicación de Cifrado y Descifrado de Datos

Aplicación de escritorio con interfaz gráfica desarrollada en **Python + Tkinter** para cifrar y descifrar números enteros de 6 dígitos.

Desarrollada como parte de la **Actividad 3 – Unidad 2** de la asignatura **Aplicaciones I**, Maestría en Inteligencia Artificial – Universidad de La Salle.

---

## 📋 Descripción

Una organización necesita transmitir datos a través de dispositivos móviles de forma segura. Esta aplicación implementa un algoritmo de cifrado por **sustitución y transposición** de dígitos antes de la transmisión.

### Algoritmo de cifrado

**Fase 1 – Sustitución:** a cada dígito `d` se aplica:
```
d' = (d + 7) mod 10
```

**Fase 2 – Transposición:** se intercambian las posiciones:
- Posición 1 ↔ Posición 3
- Posición 2 ↔ Posición 4
- Posición 5 ↔ Posición 6

### Casos de prueba verificados

| Entrada | Cifrado | Descifrado |
|---------|---------|------------|
| 123456  | 018932  | 123456 ✓  |
| 791658  | 834652  | 791658 ✓  |

---

## 🗂️ Estructura del proyecto

```
cifrado_app/
│
├── main.py                 # Ventana principal (punto de entrada)
├── logica.py               # Lógica de cifrado y descifrado
├── ventana_cifrado.py      # Ventana de cifrado
└── ventana_descifrado.py   # Ventana de descifrado
```

---

## ⚙️ Requisitos

- Python **3.8** o superior
- Tkinter (incluido por defecto con Python — no requiere instalación adicional)

Para verificar que Python está instalado:
```bash
python --version
```

Para verificar que Tkinter está disponible:
```bash
python -m tkinter
```
> Si se abre una pequeña ventana de prueba, Tkinter está correctamente instalado.

---

## 🚀 Instalación y ejecución

**1. Clonar el repositorio:**
```bash
git clone https://github.com/[tu-usuario]/[nombre-del-repo].git
cd [nombre-del-repo]
```

**2. Ejecutar la aplicación:**
```bash
python main.py
```

> No se requiere instalar dependencias adicionales. La aplicación usa únicamente la biblioteca estándar de Python.

---

## 🖥️ Uso de la aplicación

La aplicación cuenta con **tres ventanas**:

### Ventana principal
- Muestra la información del autor.
- Contiene dos botones: **Ir a Cifrado** e **Ir a Descifrado**.

### Ventana de cifrado
1. Ingresa un número entero de **exactamente 6 dígitos**.
2. Presiona el botón **Cifrar** (o tecla `Enter`).
3. La aplicación muestra el número cifrado resultante.

### Ventana de descifrado
1. Ingresa el número cifrado de **6 dígitos**.
2. Presiona el botón **Descifrar** (o tecla `Enter`).
3. La aplicación recupera y muestra el número original.

---

## 📁 Descripción de módulos

| Archivo | Responsabilidad |
|---|---|
| `main.py` | Inicializa la ventana principal y el bucle de eventos (`mainloop`). |
| `logica.py` | Contiene las funciones `cifrar_numero()`, `descifrar_numero()` y `validar_entrada()`. |
| `ventana_cifrado.py` | Construye y gestiona la ventana modal de cifrado. |
| `ventana_descifrado.py` | Construye y gestiona la ventana modal de descifrado. |

---

## 📚 Referencias

- Python Software Foundation. (2024). *tkinter — Python interface to Tcl/Tk*. https://docs.python.org/3/library/tkinter.html
- Python Software Foundation. (2020). *PEP 8 – Style guide for Python code*. https://peps.python.org/pep-0008/
- Bermudez Quintero, C. D. (2025). *Unidad 2: Aplicaciones web analíticas con Python y Dash*. Universidad de La Salle.

---

## 👤 Autor

**[Tu nombre completo]**  
Maestría en Inteligencia Artificial  
Universidad de La Salle – Bogotá, Colombia  
Mayo 2026
