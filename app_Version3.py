import streamlit as st
import pandas as pd

# Tabela de itens e preços extraída do cardápio
cardapio = [
    # Tradicionais
    {"categoria": "Tradicionais", "item": "Feijoada (500g)", "preco": 40.00},
    {"categoria": "Tradicionais", "item": "Dobradinha (500g)", "preco": 40.00},
    {"categoria": "Tradicionais", "item": "Sarapatel (500g)", "preco": 40.00},
    {"categoria": "Tradicionais", "item": "Prato Individual Tradicional", "preco": 20.00},
    {"categoria": "Tradicionais", "item": "Tradicional (1kg)", "preco": 75.00},

    # Especiais
    {"categoria": "Especiais", "item": "Bobó de Camarão (500g)", "preco": 50.00},
    {"categoria": "Especiais", "item": "Caldeirada (500g)", "preco": 50.00},
    {"categoria": "Especiais", "item": "Bacalhau de Côco (500g)", "preco": 50.00},
    {"categoria": "Especiais", "item": "Prato Individual Especial", "preco": 25.00},
    {"categoria": "Especiais", "item": "Especial (1kg)", "preco": 95.00},

    # Caldinho
    {"categoria": "Caldinhos", "item": "Caldinho de Feijoada", "preco": 14.00},
    {"categoria": "Caldinhos", "item": "Caldinho de Sarapatel", "preco": 14.00},
    {"categoria": "Caldinhos", "item": "Caldinho de Dobradinha", "preco": 14.00},
    {"categoria": "Caldinhos", "item": "Caldinho de Bobó de Camarão", "preco": 16.00},
    {"categoria": "Caldinhos", "item": "Caldinho de Caldeirada", "preco": 16.00},
    {"categoria": "Caldinhos", "item": "Caldinho de Bacalhau de Côco", "preco": 16.00},

    # Bebidas
    {"categoria": "Bebidas", "item": "Água Mineral", "preco": 3.00},
    {"categoria": "Bebidas", "item": "Água com Gás", "preco": 3.50},
    {"categoria": "Bebidas", "item": "Água de Coco", "preco": 10.00},
    {"categoria": "Bebidas", "item": "Suco Del Vale", "preco": 6.00},
    {"categoria": "Bebidas", "item": "H2O", "preco": 6.00},
    {"categoria": "Bebidas", "item": "Cachaça Dose", "preco": 6.00},
    {"categoria": "Bebidas", "item": "Refrigerante Lata", "preco": 6.00},
    {"categoria": "Bebidas", "item": "Heineken Zero", "preco": 12.00},
    {"categoria": "Bebidas", "item": "Cerveja Long Neck", "preco": 10.00},
    {"categoria": "Bebidas", "item": "Suco da Fruta", "preco": 10.00},
    {"categoria": "Bebidas", "item": "Whisky Dose", "preco": 10.00},

    # Doces
    {"categoria": "Doces", "item": "Brigadeiro", "preco": 3.00},
    {"categoria": "Doces", "item": "Beijinho de Côco", "preco": 3.00},
    {"categoria": "Doces", "item": "Bem Casado", "preco": 3.00},
    {"categoria": "Doces", "item": "Surpresa de Uva", "preco": 3.00},
]

st.title("🍽️ Controle de Pedidos - Sabor na Praça")

quantidades = {}
total_geral = 0

for categoria in sorted(set(item["categoria"] for item in cardapio)):
    st.header(f"📌 {categoria}")
    for item in [i for i in cardapio if i["categoria"] == categoria]:
        col1, col2, col3 = st.columns([3, 1, 2])
        with col1:
            st.markdown(f"**{item['item']}**")
        with col2:
            quantidade = st.number_input("Qtd", min_value=0, step=1, key=item["item"])
            quantidades[item["item"]] = quantidade
        with col3:
            preco_total = quantidade * item["preco"]
            st.markdown(f"R$ {preco_total:.2f}")
            total_geral += preco_total

st.markdown("---")
st.subheader(f"💰 Total a pagar: R$ {total_geral:.2f}")

# Resumo dos itens pedidos
pedido = []
for item in cardapio:
    qtd = quantidades.get(item["item"], 0)
    if qtd > 0:
        pedido.append({
            "Categoria": item["categoria"],
            "Item": item["item"],
            "Quantidade": qtd,
            "Valor Unitário": item["preco"],
            "Total Item": qtd * item["preco"]
        })

if pedido:
    st.markdown("### 📝 Resumo do Pedido")
    df_pedido = pd.DataFrame(pedido)
    st.dataframe(df_pedido, hide_index=True)
    
    # Botão para baixar resumo do pedido em CSV
    csv = df_pedido.to_csv(index=False, sep=';')
    st.download_button(
        label="⬇️ Baixar Resumo do Pedido (CSV)",
        data=csv,
        file_name="pedido.csv",
        mime="text/csv"
    )

# Botão Finalizar Pedido
if st.button("✅ Finalizar Pedido"):
    if not pedido:
        st.warning("Selecione pelo menos um item para finalizar o pedido!")
    else:
        st.success("Pedido finalizado com sucesso!")
        st.info(f"Total a pagar: R$ {total_geral:.2f}")