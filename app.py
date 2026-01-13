import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import st_folium
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import plotly.express as px

# 1. Configurações da Página
st.set_page_config(page_title="Geomarketing & Business Intelligence", layout="centered")

# 2. Simulação de Dados Estruturada (Cenário de Mercado)
@st.cache_data
def load_geo_business_data():
    np.random.seed(42)
    n_pedidos = 50
    
    centro_lat, centro_lon = -20.3000, -40.2990
    latitudes = np.random.normal(centro_lat, 0.004, n_pedidos)
    longitudes = np.random.normal(centro_lon, 0.004, n_pedidos)  
    
    categorias_biz = [
        'Supermercado & Bebidas', 
        'Farmácia & Saúde', 
        'Restaurantes (Gourmet)', 
        'Eletro & Tech', 
        'Pet Shop'
    ]
    
    data = {
        'ID_Pedido': range(1, n_pedidos + 1),
        'latitude': latitudes,
        'longitude': longitudes,
        'Categoria': np.random.choice(categorias_biz, n_pedidos),
        'Prazo_Entrega_Dias': np.random.randint(1, 10, n_pedidos)
    }
    
    df_temp = pd.DataFrame(data)
    
    weights = {
        'Eletro & Tech': 1200, 
        'Restaurantes (Gourmet)': 150, 
        'Supermercado & Bebidas': 350, 
        'Farmácia & Saúde': 120, 
        'Pet Shop': 200
    }
    df_temp['Valor_Venda'] = df_temp['Categoria'].map(weights) * np.random.uniform(0.8, 1.5, n_pedidos)
    
    return df_temp

df = load_geo_business_data()

# 3. Inteligência de Dados: Clusterização Espacial
X = df[['latitude', 'longitude', 'Valor_Venda']]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
df['Regiao_Cluster'] = kmeans.fit_predict(X_scaled)

# 4. Header Estratégico
st.title("Inteligência de Mercado e Geomarketing")
st.markdown(f"**Analista Responsável:** Raphael Alvarenga da Silva | Case: Otimização de Last-Mile")

# Proposta de Layout Harmônico (Cards de Metodologia)
st.divider()
meta_col1, meta_col2, meta_col3 = st.columns(3)

with meta_col1:
    st.markdown("### :material/visibility: Transparência")
    st.caption("""
    Dados gerados via código para demonstrar proficiência em 
    **Python, Estatística e Machine Learning**.
    """)

with meta_col2:
    st.markdown("### :material/map: Realismo Geográfico")
    st.caption("""
    Distribuição baseada em coordenadas reais de **Vitória-ES**, 
    respeitando perímetros urbanos.
    """)

with meta_col3:
    st.markdown("### :material/analytics: Lógica de Negócio")
    st.caption("""
    Dataset modelado com pesos de ticket médio e 
    clusterização **K-Means** para análise de Last-Mile.
    """)

# 5. Dashboard de Performance
st.divider()
c1, c2, c3, c4 = st.columns(4)
c1.metric("Faturamento Total", f"R$ {df['Valor_Venda'].sum():,.2f}")
c2.metric("Ticket Médio", f"R$ {df['Valor_Venda'].mean():,.2f}")
c3.metric("Lead Time Médio", f"{df['Prazo_Entrega_Dias'].mean():.1f} dias")
c4.metric("Qtd. Pedidos", len(df))

# 6. Mapa Interativo
st.subheader(":material/location_on: Polos de Consumo por Cluster")
m = folium.Map(location=[-20.300, -40.299], zoom_start=14, tiles='CartoDB dark_matter')

colors = ['#FF4B4B', '#1C83E1', '#00C781', '#FFBD45']
for i, row in df.iterrows():
    folium.CircleMarker(
        location=[row['latitude'], row['longitude']],
        radius=row['Valor_Venda']/400 if row['Valor_Venda'] < 2000 else 10,
        color=colors[int(row['Regiao_Cluster'])],
        fill=True,
        fill_opacity=0.7,
        tooltip=f"{row['Categoria']} - R${row['Valor_Venda']:.2f}"
    ).add_to(m)

st_folium(m, width=1400, height=500)

# 7. Análise de Negócio e Tabela
st.divider()
col_a, col_b = st.columns([2, 1])

with col_a:
    st.subheader(":material/shopping_cart: Faturamento por Categoria")
    df_agrupado = df.groupby('Categoria')['Valor_Venda'].sum().sort_values().reset_index()
    
    fig_cat = px.bar(df_agrupado, 
                     y='Categoria', 
                     x='Valor_Venda', 
                     orientation='h',
                     color='Categoria', 
                     color_discrete_sequence=px.colors.qualitative.Prism,
                     template="plotly_dark")
    
    fig_cat.update_layout(showlegend=False)
    st.plotly_chart(fig_cat, use_container_width=True)

with col_b:
    st.subheader(":material/table_chart: Performance por Região")
    cluster_metrics = df.groupby('Regiao_Cluster').agg({
        'ID_Pedido': 'count',
        'Valor_Venda': 'sum'
    }).rename(columns={'ID_Pedido': 'Pedidos', 'Valor_Venda': 'Total_R$'})
    
    st.dataframe(cluster_metrics.style.highlight_max(axis=0), width='stretch')

# 7.1. Análises de Distribuição e Eficiência
st.divider()
st.subheader(":material/monitoring: Distribuição e Eficiência Operacional")
col_c, col_d, col_e = st.columns(3)

with col_c:
    st.write("**Frequência de Prazos (Lead Time)**")
    fig_hist = px.histogram(df, x="Prazo_Entrega_Dias", 
                            nbins=10, 
                            color_discrete_sequence=['#00C781'],
                            template="plotly_dark")
    fig_hist.update_layout(showlegend=False, yaxis_title="Qtd. Pedidos")
    st.plotly_chart(fig_hist, use_container_width=True)

with col_d:
    st.write("**Dispersão de Valores por Categoria**")
    fig_box = px.box(df, x="Categoria", y="Valor_Venda", 
                     color="Categoria",
                     template="plotly_dark")
    fig_box.update_layout(showlegend=False)
    st.plotly_chart(fig_box, use_container_width=True)

with col_e:
    st.write("**Ticket Médio vs. Prazo de Entrega**")
    fig_scatter = px.scatter(df, x="Valor_Venda", y="Prazo_Entrega_Dias",
                             color="Categoria",
                             size="Valor_Venda",
                             template="plotly_dark")
    st.plotly_chart(fig_scatter, use_container_width=True)

# 8. SEÇÃO DE INSIGHTS E AÇÃO
st.divider()
st.subheader(":material/psychology: Diagnóstico Estratégico e Recomendações")

ins1, ins2, ins3 = st.columns(3)

with ins1:
    st.markdown("#### :material/local_shipping: Eficiência Logística")
    st.markdown(":green[**Fortaleza:**] Alta densidade de pedidos identificada no Cluster principal, permitindo ganho de escala.")
    st.markdown(f":red[**Gargalo:**] Lead Time médio de {df['Prazo_Entrega_Dias'].mean():.1f} dias é elevado para operações urbanas.")
    st.info(f"**Ação:** Instalar *centro de distribuição* no centro do cluster de {cluster_metrics['Pedidos'].max()} pedidos para reduzir entregas para < 24h.")

with ins2:
    st.markdown("#### :material/payments: Performance de Vendas")
    categoria_top = df.groupby('Categoria')['Valor_Venda'].sum().idxmax()
    st.markdown(f":green[**Fortaleza:**] Categoria **{categoria_top}** possui excelente tração e ticket médio saudável.")
    st.markdown(":red[**Risco:**] Dependência excessiva de uma única categoria para bater as metas de faturamento.")
    st.info("**Ação:** Implementar estratégias de *Cross-selling* (venda cruzada) para tracionar categorias subutilizadas.")

with ins3:
    st.markdown("#### :material/explore: Cobertura de Mercado")
    st.markdown(":green[**Fortaleza:**] Domínio consolidado nas áreas centrais de Vitória com clusters bem definidos.")
    st.markdown(":red[**Gargalo:**] Zonas de 'sombra' identificadas nas periferias dos clusters, onde a concorrência pode atuar.")
    st.info("**Ação:** Expansão da malha de parceiros logísticos nessas bordas para capturar 20% de demanda reprimida.")

# 9. SOBRE O AUTOR E MOTIVAÇÃO
st.divider()

with st.container():
    # Usamos gap="small" para minimizar o espaço padrão entre as colunas
    col_img, col_title = st.columns([0.5, 4], gap="small")
    
    with col_img:
        st.markdown("""
            <style>
            [data-testid="stImage"] img {
                border-radius: 15px; 
                border: 2px solid #00C781;
                object-fit: cover;
            }
            /* Remove paddings das colunas para permitir a aproximação total */
            [data-testid="column"] {
                padding-left: 0rem !important;
                padding-right: 0rem !important;
            }
            </style>
            """, unsafe_allow_html=True)
        st.image("foto_perfil.png", width=110)
        
    with col_title:
        # Aumentamos o margin-left negativo para eliminar o vácuo horizontal
        # margin-top 5px no cargo para a distância que você gostou anteriormente
        st.markdown("""
            <div style='margin-left: -0px; margin-top: -6px;'>
                <h2 style='margin-bottom: 0px; line-height: 1.1;'>Raphael Alvarenga</h2>
                <p style='color: #00C781; font-weight: bold; margin-top: 5px;'>Analista de Dados | Business Intelligence</p>
            </div>
            """, unsafe_allow_html=True)

    # Texto de Motivação Justificado
    st.markdown("""
<div style="text-align: justify;">
<b>Por quê?</b><br>
Este projeto nasceu da minha paixão por transformar dados complexos em decisões estratégicas. 
Embora minha base venha de análise de dados socioambientais da Oceanografia, encontrei no 
<b>Geomarketing, Séries Temporais e na Análise de Dados de Negócios</b> o ambiente ideal para 
aplicar meus conhecimentos em desafios reais de mercado.<br><br>
<b>Meu Diferencial</b><br>
Acredito que o fato de vir de uma área científica distinta me confere um diferencial competitivo: 
a capacidade de <b>pensar fora da caixa</b>. Minha formação me ensinou a observar fenômenos complexos 
por diferentes ângulos, uma habilidade que agora transponho para encontrar padrões de mercado que 
outros poderiam ignorar. Por estar iniciando minha jornada nesta área, possuo a mente aberta e o 
desejo de ser <b>moldado pela cultura e metodologias da empresa</b>, adaptando-me rapidamente aos 
padrões de excelência da equipe.<br><br>
<b>Meu Objetivo Profissional</b><br>
Estou em busca de oportunidades onde eu possa aplicar minhas habilidades em 
<b>Python, SQL, Data Storytelling e Dataviz</b>, com o foco em construir uma 
<b>atuação de longo prazo</b>. Meu objetivo é aprender continuamente, me especializar e crescer 
junto à empresa, contribuindo para que a cultura de dados seja um diferencial competitivo.<br><br>
<b>Cultura e Colaboração</b><br>
Sou uma pessoa que <b>gosta de pessoas e de trabalhar em equipe</b>. Acredito que a tecnologia só faz 
sentido quando compartilhada e construída coletivamente. Tenho prazer em me relacionar, trocar 
conhecimentos e, acima de tudo, em <b>colocar a minha cara nos projetos</b> — trazendo um toque 
pessoal de dedicação, senso de dono e criatividade em cada solução que entrego.
</div>
""", unsafe_allow_html=True)

    # Botão de Ação Alinhado à Direita
    st.markdown("<br>", unsafe_allow_html=True)
    col_vazia, col_btn = st.columns([2, 1])
    with col_btn:
        st.link_button("🔗 Conectar no LinkedIn", "https://www.linkedin.com/in/raphaelalvarengadasilva/", use_container_width=True)
