# OverlayPrompt

Aplicativo criado como um aviso, sempre no topo da tela, sobrepondo qualquer aplicação aberta.  
A mensagem funciona como um lembrete visual rápido e pode ser fechada com um único clique.

A janela usa transparência por cor e permanece sempre em primeiro plano, funcionando como um overlay leve, direto e portátil.

---

## 📸 **Preview**
_(adicione um screenshot ou GIF no futuro)_

## ✨ **Funcionalidades**
- Janela sempre no topo (**always-on-top**)  
- Transparência com cor-chave  
- Fechamento com clique  
- Overlay que não bloqueia apps ao fundo  
- Leve, rápido e com zero dependências externas  
- Portátil (executável único via PyInstaller)

---

## 🚀 **Como usar**
Após gerar o executável:

1. Baixe o arquivo `.exe`
2. Execute diretamente (não requer Python instalado)
3. A mensagem será exibida no canto configurado
4. Clique para fechar

---

## 🔧 **Como buildar (PyInstaller)**

Este projeto foi empacotado como standalone usando:

```bash
python -m PyInstaller --onefile --windowed separa_badge.py
```

Isso gera um binário único, similar a um flatpak portátil, que dispensa instalação e qualquer dependência adicional.

📁 Estrutura do projeto:
OverlayPrompt/
└── dist/
    └── separa_badge.exe   (gerado automaticamente)

📦 Requisitos
Nenhum e sem necessidade de dependências externas.
O executável gerado funciona sem Python e sem bibliotecas adicionais.

👤 Autor
Code Tangent
