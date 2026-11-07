# 🌱 Minha Jornada · Clube do Segredo (Segredo da Insulina)

Site pessoal e painel interativo completo com todos os conteúdos da Jornada de 21 Dias, lista de compras inteligente, e-books em PDF e protocolos de emergência. Pronto para publicação no **GitHub Pages**!

---

## 🌟 O que está incluído no site

1. **📅 Jornada Completa (21 Dias)**:
   - Divisão pelas 3 fases: *Semana 1 (Reset)*, *Semana 2 (Aceleração)* e *Semana 3 (Consolidação)*.
   - Versões padrão e versão **Premium** de cada dia.
   - Leitor embutido para navegar nas receitas dos 3 Segredos, shots matinais e rotina noturna sem sair da página.
   - Checklist interativo que calcula sua evolução percentual em tempo real (salvo no navegador).

2. **🛒 Lista de Compras Inteligente**:
   - Dividida por seções: *Essenciais*, *Especiarias Secas*, *Frutas e Frescos*, *Chás e Ervas*, *Laticínios* e *Proteínas*.
   - Checkboxes interativos com contador automático para levar no celular ao supermercado.
   - Link para a versão original completa da lista.

3. **🎁 Livro de Receitas & E-books (PDF)**:
   - 🥤 *Shakes Emagrecedores* (Substitutos práticos e saborosos).
   - 🥒 *Receitas Detox* (Sucos e caldos para desinchar rápido).
   - 🍓 *Sobremesas para o Metabolismo* (Doces funcionais de baixo índice glicêmico).
   - 🍵 *Soro da Magreza & Chás* (Infusões anti-inflamatórias).
   - ⚡ *10 Dicas para Acelerar o Resultado*.

4. **🛡️ 10 Protocolos de Emergência**:
   - Manhã Turbo, Noite Reparadora, Festas & Eventos, Viagens & Férias, Recebendo Visitas, Preguiça & Cansaço, Marmitas da Semana, Fim de Semana, TPM & Ciclo, Estresse & Ansiedade.

5. **📊 Painel de Evolução**:
   - Acompanhamento de medidas e fotos de evolução.

---

## 🚀 Como Publicar no GitHub Pages (Passo a Passo)

### 1. Criar um repositório no GitHub
1. Acesse [github.com/new](https://github.com/new).
2. Dê um nome ao seu repositório (ex.: `clube-do-segredo` ou `minha-jornada`).
3. Escolha **Public** (Público) ou **Private** (se você tiver conta GitHub Pro/Team com Pages liberado).
4. **Não marque** as opções de adicionar README ou .gitignore (já criamos tudo pronto aqui).
5. Clique em **Create repository**.

### 2. Enviar os arquivos para o GitHub
Abra o terminal na pasta `d:\ANDREIA` (ou PowerShell) e execute os comandos:

```bash
# Vincular o repositório remoto (substitua SEU-USUARIO e NOME-REPO pelo seu GitHub)
git remote add origin https://github.com/SEU-USUARIO/NOME-REPO.git

# Enviar os arquivos
git push -u origin main
```

*(Se ainda não fez o commit inicial, basta rodar: `git add .` e `git commit -m "Meu portal pessoal"` antes do push)*

### 3. Ativar o GitHub Pages
1. No seu repositório no GitHub, clique na aba **Settings** (Configurações).
2. No menu lateral esquerdo, clique em **Pages**.
3. Em **Build and deployment** > **Source**, selecione **Deploy from a branch**.
4. Abaixo, em **Branch**, escolha `main` e a pasta `/(root)`.
5. Clique em **Save**.

🎉 **Pronto!** Em 1 a 2 minutos, o GitHub disponibilizará o link do seu site público:
`https://SEU-USUARIO.github.io/NOME-REPO/`

---

## 🔒 Privacidade e Segurança
O arquivo `.gitignore` já está configurado para **não enviar** suas credenciais ou perfis de sessão (`chrome_profile/` e `auth_state.json`) para o repositório público. Apenas os conteúdos estáticos, páginas, estilos e PDFs serão publicados.
