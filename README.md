
# Ingestão de Dados – Arquitetura Medalhão

## Ricardo Marques



## 🚀 Visão Geral
Este projeto demonstra uma implementação de pipeline de ingestão de dados seguindo o padrão de **Arquitetura Medalhão** (camadas Bronze → Silver → Gold). O objetivo é transportar dados de fontes variadas até um estado refinado e pronto para análise, garantindo governança, rastreabilidade e evolução incremental da qualidade dos dados.

## 🧩 Componentes Principais
- **Camada Bronze**: captura e armazena os dados em seu estado bruto, sem ou com mínima transformação.  
- **Camada Silver**: aplica limpeza, normalização e validação, elevando a qualidade dos dados.  
- **Camada Gold**: transforma os dados em artefatos modelados, agregados ou prontos para consumo analítico ou BI.  
- Scripts e orquestrações que suportam essas camadas estão dispostos na pasta `scripts/` do projeto.

## 🎯 Propósito do Projeto
- Prover um pipeline estruturado para ingestão, tratamento e disponibilização de dados em diferentes estágios de maturidade.  
- Permitir rastreabilidade da linhagem dos dados e facilitar reprocessamentos, auditoria e governança.  
- Atender à necessidade de transformar dados brutos em informações de alto valor, alinhadas a demandas de negócio, análise ou machine learning.

## 🔧 Tecnologias e Abordagem
- Implementação em **Python**, com uso de bibliotecas padrão para ingestão e transformação de dados.  
- Estrutura modular que facilita extensões ou adaptações para diferentes fontes de dados ou formatos.  
- Arquitetura baseada em camadas claramente definidas, o que favorece clareza, escalabilidade e manutenção.

## 📝 Como usar
1. Clone o repositório.  
2. Ative o ambiente Python (por exemplo via Poetry ou virtualenv).  
3. Execute os scripts seguindo a sequência: ingestão → limpeza/validação → modelagem/agregação.  
4. Verifique os artefatos produzidos em cada camada para garantir a qualidade e a conformidade com os requisitos de negócio.

## ✅ Benefícios
- Dados assegurados desde o estado bruto até o uso final, com qualidade crescente.  
- Facilidade para auditoria, linhagem e governança dos dados.  
- Capacidade de adaptação a novos casos de uso e fontes de dados.

