# Space Cargo Tracker

## Descrição da Solução

O Space Cargo Tracker é uma aplicação desenvolvida em Python utilizando OpenCV para realizar a identificação de cargas espaciais por meio da leitura de QR Codes em tempo real.

A solução utiliza a webcam do computador para capturar vídeo continuamente, detectar QR Codes presentes na imagem e exibir automaticamente o identificador da carga detectada.

O projeto simula um sistema de rastreamento de equipamentos, módulos e suprimentos em operações espaciais, contribuindo para processos de logística, monitoramento e automação dentro do contexto da economia espacial.

---

## Funcionalidades

* Captura de vídeo em tempo real utilizando webcam;
* Detecção automática de QR Codes;
* Identificação de cargas e equipamentos;
* Exibição visual dos dados detectados;
* Monitoramento em tempo real.

---

## Bibliotecas Utilizadas

* Python 3.11
* OpenCV
* NumPy

---

## Vídeo

Link YOUTUBE:

```bash
git clone https://github.com/lzFelipee/GS1_Physical-Computing
```

## Instalação

Clone o repositório:

```bash
git clone https://github.com/lzFelipee/GS1_Physical-Computing
```

Acesse a pasta do projeto:

```bash
cd SpaceCargoTracker
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## Execução

Execute o sistema com:

```bash
python main.py
```

Após iniciar, a webcam será aberta e o sistema realizará a leitura automática dos QR Codes apresentados à câmera.

Pressione a tecla ESC para encerrar a aplicação.

---

## Exemplo de Uso

QR Code:

```text
SAT-001
```

Resultado exibido:

```text
CARGA IDENTIFICADA
ID: SAT-001
```

---

## Integrantes

* Luiz Felipe Motta da Silva — RM 559126
* Pedro Henrique Faim dos Santos — RM 557440
* Nicolas Lorenzo Ferreira da Silva — RM 557962

---

## Repositório

Projeto desenvolvido para a Global Solution FIAP – Space Connect.
