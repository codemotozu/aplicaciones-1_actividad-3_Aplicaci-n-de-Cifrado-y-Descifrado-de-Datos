"""
ventana_descifrado.py
Ventana de descifrado de la aplicación.
"""
import tkinter as tk
from tkinter import messagebox
from logica import descifrar_numero, validar_entrada


def abrir_ventana_descifrado(ventana_padre: tk.Tk) -> None:
    """Abre la ventana de descifrado como Toplevel sobre la ventana principal."""

    ventana = tk.Toplevel(ventana_padre)
    ventana.title("🔓 Descifrado de Datos")
    ventana.resizable(False, False)

    ancho, alto = 480, 380
    x = (ventana.winfo_screenwidth() - ancho) // 2
    y = (ventana.winfo_screenheight() - alto) // 2
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")
    ventana.configure(bg="#1A3A2F")
    ventana.grab_set()  # Modal

    # ── Título ───────────────────────────────────────────────────────────────
    marco_titulo = tk.Frame(ventana, bg="#00C853", pady=10)
    marco_titulo.pack(fill=tk.X)
    tk.Label(
        marco_titulo,
        text="🔓  DESCIFRADO DE DATOS",
        font=("Arial", 16, "bold"),
        bg="#00C853",
        fg="#1A3A2F",
    ).pack()

    # ── Instrucción ───────────────────────────────────────────────────────────
    tk.Label(
        ventana,
        text="Ingrese el número cifrado de 6 dígitos:",
        font=("Arial", 12),
        bg="#1A3A2F",
        fg="white",
    ).pack(pady=(20, 6))

    # ── Campo de entrada ──────────────────────────────────────────────────────
    var_entrada = tk.StringVar()
    entrada = tk.Entry(
        ventana,
        textvariable=var_entrada,
        font=("Courier New", 18, "bold"),
        width=10,
        justify="center",
        bd=2,
        relief="solid",
    )
    entrada.pack(ipady=6)
    entrada.focus()

    # ── Resultado ─────────────────────────────────────────────────────────────
    marco_resultado = tk.Frame(ventana, bg="#1A3A2F")
    marco_resultado.pack(pady=18)

    tk.Label(
        marco_resultado,
        text="Número original:",
        font=("Arial", 12),
        bg="#1A3A2F",
        fg="#00C853",
    ).pack()

    var_resultado = tk.StringVar(value="------")
    lbl_resultado = tk.Label(
        marco_resultado,
        textvariable=var_resultado,
        font=("Courier New", 28, "bold"),
        bg="#1A3A2F",
        fg="#FFD600",
    )
    lbl_resultado.pack(pady=4)

    # ── Botones ───────────────────────────────────────────────────────────────
    marco_botones = tk.Frame(ventana, bg="#1A3A2F")
    marco_botones.pack(pady=10)

    def _descifrar() -> None:
        """Valida entrada y muestra el número original."""
        texto = var_entrada.get().strip()
        if not validar_entrada(texto):
            messagebox.showerror(
                "Entrada inválida",
                "Por favor ingrese exactamente 6 dígitos numéricos.",
                parent=ventana,
            )
            return
        resultado = descifrar_numero(texto)
        var_resultado.set(resultado)

    def _limpiar() -> None:
        var_entrada.set("")
        var_resultado.set("------")
        entrada.focus()

    tk.Button(
        marco_botones,
        text="  Descifrar  ",
        command=_descifrar,
        font=("Arial", 12, "bold"),
        bg="#00C853",
        fg="#1A3A2F",
        relief="flat",
        cursor="hand2",
        padx=12,
        pady=6,
    ).grid(row=0, column=0, padx=8)

    tk.Button(
        marco_botones,
        text="  Limpiar  ",
        command=_limpiar,
        font=("Arial", 12, "bold"),
        bg="#607D8B",
        fg="white",
        relief="flat",
        cursor="hand2",
        padx=12,
        pady=6,
    ).grid(row=0, column=1, padx=8)

    tk.Button(
        marco_botones,
        text="  Cerrar  ",
        command=ventana.destroy,
        font=("Arial", 12, "bold"),
        bg="#C62828",
        fg="white",
        relief="flat",
        cursor="hand2",
        padx=12,
        pady=6,
    ).grid(row=0, column=2, padx=8)

    ventana.bind("<Return>", lambda e: _descifrar())
