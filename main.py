"""
main.py
Aplicación de escritorio con interfaz gráfica para cifrado y descifrado de datos.
Asignatura  : Aplicaciones I
Programa    : Maestría en Inteligencia Artificial
Universidad : Universidad de La Salle
Autora      : Carolina Rodríguez Chacón
Fecha       : Mayo 2026
"""

import tkinter as tk
from ventana_cifrado import abrir_ventana_cifrado
from ventana_descifrado import abrir_ventana_descifrado


def centrar_ventana(ventana: tk.Tk, ancho: int, alto: int) -> None:
    """Centra la ventana en la pantalla del usuario."""
    x = (ventana.winfo_screenwidth() - ancho) // 2
    y = (ventana.winfo_screenheight() - alto) // 2
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")


def crear_ventana_principal() -> None:
    """Construye y ejecuta la ventana principal de la aplicación."""

    # ── Raíz ─────────────────────────────────────────────────────────────────
    root = tk.Tk()
    root.title("Aplicación de Cifrado y Descifrado")
    root.resizable(False, False)
    root.configure(bg="#0D1B2A")
    centrar_ventana(root, 540, 500)

    # ── Encabezado azul oscuro ────────────────────────────────────────────────
    marco_header = tk.Frame(root, bg="#1565C0", pady=18)
    marco_header.pack(fill=tk.X)

    tk.Label(
        marco_header,
        text="🔐  SISTEMA DE CIFRADO",
        font=("Arial", 20, "bold"),
        bg="#1565C0",
        fg="white",
    ).pack()

    tk.Label(
        marco_header,
        text="Transmisión Segura de Datos",
        font=("Arial", 11, "italic"),
        bg="#1565C0",
        fg="#90CAF9",
    ).pack()

    # ── Sección de la autora ─────────────────────────────────────────────────────
    marco_autora = tk.Frame(root, bg="#0D2137", bd=0, pady=16, padx=24)
    marco_autora.pack(fill=tk.X, padx=24, pady=(18, 0))

    tk.Label(
        marco_autora,
        text="👤  Información de la Autora",
        font=("Arial", 12, "bold"),
        bg="#0D2137",
        fg="#F5A623",
    ).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 8))

    # Datos de la autora 
    datos_autora = [
        ("Estudiante:", "Carolina Rodríguez Chacón"),
        ("Programa:", "Maestría en Inteligencia Artificial"),
        ("Asignatura:", "Aplicaciones I"),
        ("Universidad:", "Universidad de La Salle"),
        ("Fecha:", "Mayo 2026"),
    ]

    for fila, (etiqueta, valor) in enumerate(datos_autora, start=1):
        tk.Label(
            marco_autora,
            text=etiqueta,
            font=("Arial", 10, "bold"),
            bg="#0D2137",
            fg="#90CAF9",
            anchor="w",
        ).grid(row=fila, column=0, sticky="w", padx=(0, 10), pady=2)

        tk.Label(
            marco_autora,
            text=valor,
            font=("Arial", 10),
            bg="#0D2137",
            fg="white",
            anchor="w",
        ).grid(row=fila, column=1, sticky="w", pady=2)

    # ── Descripción ───────────────────────────────────────────────────────────
    marco_desc = tk.Frame(root, bg="#0D1B2A")
    marco_desc.pack(pady=(18, 4))

    tk.Label(
        marco_desc,
        text="Seleccione una operación para continuar:",
        font=("Arial", 12),
        bg="#0D1B2A",
        fg="white",
    ).pack()

    # ── Botones de navegación ─────────────────────────────────────────────────
    marco_botones = tk.Frame(root, bg="#0D1B2A")
    marco_botones.pack(pady=20)

    btn_cifrar = tk.Button(
        marco_botones,
        text="🔒  Ir a Cifrado",
        command=lambda: abrir_ventana_cifrado(root),
        font=("Arial", 13, "bold"),
        bg="#F5A623",
        fg="#0D1B2A",
        relief="flat",
        cursor="hand2",
        padx=20,
        pady=12,
        width=16,
    )
    btn_cifrar.grid(row=0, column=0, padx=14)

    btn_descifrar = tk.Button(
        marco_botones,
        text="🔓  Ir a Descifrado",
        command=lambda: abrir_ventana_descifrado(root),
        font=("Arial", 13, "bold"),
        bg="#00C853",
        fg="#0D1B2A",
        relief="flat",
        cursor="hand2",
        padx=20,
        pady=12,
        width=16,
    )
    btn_descifrar.grid(row=0, column=1, padx=14)

    # ── Pie ───────────────────────────────────────────────────────────────────
    tk.Label(
        root,
        text="Universidad de La Salle  •  2026",
        font=("Arial", 9),
        bg="#0D1B2A",
        fg="#546E7A",
    ).pack(side=tk.BOTTOM, pady=10)

    root.mainloop()


if __name__ == "__main__":
    crear_ventana_principal()
