# Inteligência de Mercado e Geomarketing - Otimização de Last-Mile

Este projeto é um dashboard interativo construído com **Streamlit** para análise estratégica de mercado e logística urbana. O sistema simula um cenário de consumo na Ilha de Vitória, Espírito Santo, utilizando ciência de dados para otimizar operações de entrega e entender o comportamento de faturamento por região.

---

## Objetivos do Projeto
O objetivo deste portfólio é demonstrar proficiência técnica em:

* **Inteligência Espacial & Geomarketing:** Identificação de polos de consumo e análise de densidade demográfica de pedidos em perímetros urbanos reais.
* **Machine Learning Aplicado:** Implementação do algoritmo **K-Means** para clusterização espacial, permitindo a segmentação de áreas de atuação e descoberta de zonas de sombra.
* **Business Intelligence (BI):** Transformação de dados brutos em KPIs estratégicos (Faturamento, Ticket Médio, Lead Time) e diagnósticos de negócios.
* **Data Storytelling:** Visualização avançada com **Plotly** e mapas interativos com **Folium** para facilitar a tomada de decisão gerencial.

---

## Funcionalidades do Dashboard
O painel oferece uma visão 360º da operação logística e comercial:

* **Mapa de Calor de Consumo:** Visualização geográfica de pedidos onde o tamanho e a cor dos pontos indicam o volume financeiro e o cluster pertencente.
* **Análise de Eficiência Operacional:** Gráficos de distribuição de Lead Time (prazos) e dispersão de valores por categoria.
* **Diagnóstico Estratégico:** Seção de insights "caprichada" que separa forças (pontos positivos), gargalos (pontos negativos) e recomendações de ação.
* **Perfil do Consultor:** UI Card integrado com a trajetória profissional, destacando o diferencial de transição de carreira e visão multidisciplinar.

---

## Tecnologias Utilizadas
* **Linguagem:** Python 3.10+
* **Interface:** Streamlit
* **Análise de Dados:** Pandas, Numpy
* **Machine Learning:** Scikit-Learn (StandardScaler, KMeans)
* **Mapas:** Folium, Streamlit-Folium
* **Gráficos:** Plotly Express

---

## Como Executar o Projeto

**1. Clone o repositório:**

    git clone https://github.com/raphx3/ANALISTA-DE-DADOS-JUNIOR.git

**2. Navegue até o repositório:**
    
    cd nome-do-repositorio

**3. Crie o ambiente virtual:**

    python -m venv .venv

**4. Ative o ambiente virtual:**

    Windows: .\.venv\Scripts\activate

**5. Instale as dependências:**

    pip install -r requirements.txt
    
**6. Execução do Aplicativo**

    streamlit run app.py
