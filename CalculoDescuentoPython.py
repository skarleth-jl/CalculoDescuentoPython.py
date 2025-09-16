# Función para calcular el descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento y el monto final a pagar.

    Parámetros:
        monto_total (float): Monto total de la compra.
        porcentaje_descuento (float, opcional): Porcentaje de descuento (por defecto 10%).

    Retorna:
        tuple: (descuento, monto_final)
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    monto_final = monto_total - descuento
    return descuento, monto_final


# Programa principal
if __name__ == "__main__":
    # Primera llamada: solo con el monto (usa 10% por defecto)
    monto1 = 200
    descuento1, final1 = calcular_descuento(monto1)
    print(f"Compra: ${monto1} - Descuento: ${descuento1:.2f} - Total a pagar: ${final1:.2f}")

    # Segunda llamada: con monto y porcentaje personalizado
    monto2 = 500
    descuento2, final2 = calcular_descuento(monto2, 20)  # 20% de descuento
    print(f"Compra: ${monto2} - Descuento: ${descuento2:.2f} - Total a pagar: ${final2:.2f}")
