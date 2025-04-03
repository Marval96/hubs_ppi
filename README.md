# **Hubs_PPI**
**Identificación de genes centrales (Hubs) en Redes de Interacción Proteína-Proteína (PPI)**

Esta herramienta busca identificar genes centrales (*hubs*). Se toma como entrada un listado de nodos con distintas métricas de centralidad generadas por Cytohubba en formato *'csv'*. Normaliza cada una de esas métricas para poderlas comparar entre si y las promedia para obtener un *score* de centralidad para cada uno de los nodos. Esta salida se guarda como 'hubs__$$$_scores.csv'. Además, también genera un gráfico 'hubs__$$$_scores.png' sobre la distribución de los *scores* de los nodos. **Esto puede ser útil para determinar que nodos abordar como genes centrales.**

Para ejecutar el la herramienta siga la siguente estructura después de importar la librería:

    analizar_hubs('network_file_hubs_cytohubba.csv', percentil)

Por ejemplo: 

    analizar_hubs('network_macs_ha_cytohubba.csv', 90)

La herramineta producirá un archivo con los puntajes de centralidad por nodo ya normalizados ('hubs_network_macs_ha_cytohubba_scores.csv') y el gráfico ('hubs_network_macs_ha_cytohubba_scores.png) de la distribución de los puntajes, considerándo el percentil 90, es decir, nos indicará el TOP 10% de los genes centrales o *hubs*.

### **Instalación:** 
1. Instala el ambiente Conda **desde tu terminal** con todas las dependencias de la herramineta con el archivo: hubs_ppi.yml  
---
    conda env create -f hubs_ppi.yml

2. Activa el ambiente Conda:
---
    conda activate hubs_ppi.yml


