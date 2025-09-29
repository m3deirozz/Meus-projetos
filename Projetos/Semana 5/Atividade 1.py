<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mercadão Medieval</title>
  <link href="https://fonts.googleapis.com/css2?family=Uncial+Antiqua&display=swap" rel="stylesheet">
  <style>
    /* ===================== Estilos Gerais ===================== */
    body {
      font-family: 'Uncial Antiqua', cursive;
      margin: 0;
      padding: 0;
      background: #f9f4e7;
      color: #2c1a0c;
      text-align: center;
    }








    a { text-decoration: none; color: inherit; }








    /* ===================== Header ===================== */
    header {
      position: relative;
      height: 400px;
      overflow: hidden;
      text-align: center;
      color: white;
    }








    header .banner {
      background-image: url('https://thumbs.dreamstime.com/b/arte-de-d-pixel-do-mercado-medieval-jogos-no-c%C3%A9u-azul-ai-gerou-da-cidade-322131946.jpg');
      background-size: cover;
      background-position: center;
      width: 100%;
      height: 100%;
      position: absolute;
      top: 0;
      left: 0;
      z-index: 0;
      filter: brightness(0.6);
    }








    header h1, header p {
      position: relative;
      z-index: 1;
      margin: 0;
      padding-top: 50px;
      text-shadow: 2px 2px 5px #00000088;
    }








    header h1 { font-size: 3rem; }
    header p { font-size: 1.2rem; }








    /* ===================== Nav ===================== */
    nav {
      background:#5a3d1e;
      padding: 12px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.3);
    }








    nav a {
      color: white;
      margin: 0 15px;
      font-weight: bold;
      font-size: 1.1em;
      transition: color 0.3s;
    }








    nav a:hover { color: #f9f4e7; }








    /* ===================== Main ===================== */
    main { max-width: 1200px; margin: 20px auto; padding: 0 15px; }
    section { margin-bottom: 40px; }
    section h2 { font-size: 2em; margin-bottom: 10px; color: #4e2a09; }








    /* ===================== Mercado ===================== */
    .imagens-mercado {
      display: flex;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 10px;
      margin-top: 20px;
    }
    .imagens-mercado img {
      width: 32%;
      border-radius: 8px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.2);
      transition: transform 0.2s;
    }
    .imagens-mercado img:hover { transform: scale(1.05); }








    /* ===================== Tabela ===================== */
    table { width: 100%; border-collapse: collapse; margin-top: 20px; }
    table, th, td { border: 1px solid #5a3d1e; }
    th, td { padding: 10px; text-align: center; }
    th { background: #5a3d1e; color: #fff9e6; }








    /* ===================== Card Leilão ===================== */
    .card {
      background: #fff9e6;
      padding: 20px;
      border-radius: 12px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.2);
      margin-top: 20px;
    }








    .lance-btn {
      background: linear-gradient(#8b5a2b, #5a3d1e);
      color: #fff9e6;
      border: none;
      padding: 12px 24px;
      border-radius: 6px;
      cursor: pointer;
      margin-top: 10px;
      transition: background 0.3s;
    }








    .lance-btn:hover {
      background: linear-gradient(#a86d34, #6e4821);
    }








    /* ===================== Sala de Troca ===================== */
    .container { display: flex; justify-content: space-around; flex-wrap: wrap; padding: 20px; }
    .player {
      width: 40%;
      min-width: 300px;
      padding: 20px;
      border: 4px solid #5a3d1e;
      border-radius: 12px;
      background: #fff9e6;
      box-shadow: 0 4px 10px rgba(0,0,0,0.3);
      margin-bottom: 20px;
    }
    .player h3 { color: #4e2a09; margin-bottom: 10px; }
    .inventory { display: none; list-style-type: none; padding: 0; margin-top: 10px; background: #f4ebd0; border-radius: 8px; border: 2px solid #5a3d1e; }
    .inventory li {
      padding: 8px;
      border-bottom: 1px solid #a38356;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.1em;
      transition: background 0.2s;
    }
    .inventory li:hover { background-color: #e8dab0; }
    .inventory li.selected { background-color: #d1ffd1; font-weight: bold; border-left: 6px solid #2f6b2f; }
    .button {
      margin-top: 15px;
      padding: 12px 24px;
      background: linear-gradient(#8b5a2b, #5a3d1e);
      color: #f9f4e7;
      border: 2px solid #3e2610;
      cursor: pointer;
      border-radius: 6px;
      font-size: 1.1em;
      box-shadow: 0 2px 6px rgba(0,0,0,0.6);
      transition: transform 0.2s;
    }
    .button:hover { transform: scale(1.05); background: linear-gradient(#a86d34, #6e4821); }
    .status { margin-top: 20px; font-weight: bold; font-size: 1.2em; color: #c49b3f; text-shadow: 1px 1px 2px #00000033; }
    .item-image { width: 40px; height: 40px; object-fit: contain; margin-right: 10px; }








    /* ===================== Footer ===================== */
    footer { background: #5a3d1e; color: #fff; padding: 15px; margin-top: 40px; }
  </style>
</head>
<body>








  <!-- Header -->
  <header>
    <div class="banner"></div>
    <h1>⚔️ Mercadão 🛡️</h1>
    <p>Tudo o que você procura, está aqui!</p>
  </header>








  <!-- Nav -->
  <nav>
    <a href="#mercado">🏪 Mercado</a>
    <a href="#tabela">📊 Tabela</a>
    <a href="#leilao">🔨 Leilão</a>
    <a href="#troca">🤝 Sala de Troca</a>
    <a href="#contato">📩 Contato</a>
  </nav>








  <!-- Main -->
  <main>
    <!-- Mercado -->
    <section id="mercado">
      <h2>Mercado</h2>
      <p>Confira alguns produtos do nosso mercado virtual:</p>
      <div class="imagens-mercado">
        <img src="https://img.freepik.com/vetores-premium/ilustracao-vetorial-de-desenho-animado-de-uma-espada-empunhada-por-um-cavaleiro-corajoso_1263357-8310.jpg" alt="Espada">
        <img src="https://img.freepik.com/vetores-gratis/cavaleiro-medieval-em-armadura_1308-174955.jpg" alt="Armadura">
        <img src="https://img.freepik.com/vetores-premium/frasco-redondo-com-cortica-com-desenho-linear-de-rabiscos-de-pocao-magica_253359-1956.jpg" alt="Poção">
      </div>
    </section>








    <!-- Tabela -->
    <section id="tabela">
      <h2>Tabela de Produtos</h2>
      <table>
        <tr><th>Produto</th><th>Preço</th><th>Estoque</th></tr>
        <tr><td>Espada Lendária</td><td>R$ 500</td><td>10</td></tr>
        <tr><td>Armadura Épica</td><td>R$ 750</td><td>5</td></tr>
        <tr><td>Poção de Cura</td><td>R$ 50</td><td>50</td></tr>
      </table>
    </section>








    <!-- Leilão -->
  <!-- Leilão -->
<section id="leilao">
  <h2>Leilão ao Vivo</h2>
  <div class="card">
    <h3>🔧 Configurar Novo Leilão</h3>
    <input type="text" id="itemLeilao" placeholder="Nome do item">
    <input type="number" id="lanceMinimo" placeholder="Valor mínimo">
    <button class="lance-btn" onclick="iniciarLeilao()">🎬 Iniciar Leilão</button>
  </div>
  <div class="card" style="margin-top: 20px;">
    <h3>Item em Leilão: <span id="itemAtual">Escudo Raro</span></h3>
    <p><strong>Tempo restante:</strong> <span id="timer">60</span> segundos</p>
    <p><strong>Lance atual:</strong> R$ <span id="lanceAtual">100</span></p>
    <p><strong>Usuário atual:</strong> <span id="usuarioAtual">Nenhum</span></p>
    <input type="text" id="usuario" placeholder="Seu nome">
    <input type="number" id="lance" placeholder="Digite seu lance">
    <button class="lance-btn" onclick="darLance()">Dar Lance</button>
  </div>
</section>












    <!-- Sala de Troca -->
    <section id="troca">
      <h2>🤝 Sala de Troca Medieval</h2>
      <div class="container">
        <div class="player" id="player1">
          <h3>Jogador 1</h3>
          <button class="button" onclick="toggleInventory('player1')">📜 Abrir Inventário</button>
          <ul class="inventory" id="inventory-player1"></ul>
          <button class="button" onclick="approveTrade('player1')">✅ Aprovar Troca</button>
        </div>
        <div class="player" id="player2">
          <h3>Jogador 2</h3>
          <button class="button" onclick="toggleInventory('player2')">📜 Abrir Inventário</button>
          <ul class="inventory" id="inventory-player2"></ul>
          <button class="button" onclick="approveTrade('player2')">✅ Aprovar Troca</button>
        </div>
      </div>
      <div class="status" id="status"></div>
    </section>








    <!-- Contato -->
    <section id="contato">
      <h2>Contato</h2>
      <p>📩 Envie-nos um e-mail: <strong>contato@mercadaomedieval.com</strong></p>
    </section>
  </main>








  <!-- Footer -->
  <footer>
    <p>&copy; 2025 Mercadão Medieval</p>
  </footer>








  <!-- Scripts -->
  <script>
    /* ===================== Leilão ===================== */
   /* ===================== Leilão ===================== */
let tempoRestante = 60;
let lanceAtual = 100;
let usuarioAtual = "Nenhum";
let itemAtual = "Escudo Raro";
let timerInterval;




function atualizarTela() {
  document.getElementById("timer").textContent = tempoRestante;
  document.getElementById("lanceAtual").textContent = lanceAtual;
  document.getElementById("usuarioAtual").textContent = usuarioAtual;
  document.getElementById("itemAtual").textContent = itemAtual;
}




function iniciarTimer() {
  clearInterval(timerInterval);
  tempoRestante = 300;
  timerInterval = setInterval(() => {
    if (tempoRestante > 0) {
      tempoRestante--;
      atualizarTela();
    } else {
      clearInterval(timerInterval);
      alert(`⏰ Leilão encerrado!\n🏆 Vencedor: ${usuarioAtual}\n💰 Lance: R$${lanceAtual}\n📦 Item: ${itemAtual}`);
    }
  }, 1000);
}




function iniciarLeilao() {
  const novoItem = document.getElementById("itemLeilao").value.trim();
  const valorMinimo = parseFloat(document.getElementById("lanceMinimo").value);
 
  if (!novoItem) {
    alert("Informe o nome do item.");
    return;
  }




  if (isNaN(valorMinimo) || valorMinimo <= 0) {
    alert("Informe um valor mínimo válido.");
    return;
  }




  itemAtual = novoItem;
  lanceAtual = valorMinimo;
  usuarioAtual = "Nenhum";
  tempoRestante = 300;
  atualizarTela();
  iniciarTimer();
}




function darLance() {
  const usuario = document.getElementById("usuario").value.trim();
  const novoLance = parseFloat(document.getElementById("lance").value);




  if (!usuario) {
    alert("Digite seu nome!");
    return;
  }




  if (isNaN(novoLance) || novoLance <= lanceAtual) {
    alert("O lance deve ser maior que o atual!");
    return;
  }




  lanceAtual = novoLance;
  usuarioAtual = usuario;
  tempoRestante += 20;
  atualizarTela();
}








    /* ===================== Sala de Troca ===================== */
    let selectedItems = { player1: { name: null, image: null }, player2: { name: null, image: null } };
    let inventories = {
      player1: ['Espada Longa', 'Escudo de Ferro', 'Poção de Cura'],
      player2: ['Armadura de Ferro', 'Machado de Guerra', 'Poção de Força']
    };
    let approved = { player1: false, player2: false };








    function getItemImage(item) {
      const images = {
        'Espada Longa': 'https://cdn-icons-png.flaticon.com/512/616/616554.png',
        'Escudo de Ferro': 'https://cdn-icons-png.flaticon.com/512/616/616554.png',
        'Poção de Cura': 'https://cdn-icons-png.flaticon.com/512/590/590685.png',
        'Armadura de Ferro': 'https://cdn-icons-png.flaticon.com/512/616/616430.png',
        'Machado de Guerra': 'https://cdn-icons-png.flaticon.com/512/616/616554.png',
        'Poção de Força': 'https://cdn-icons-png.flaticon.com/512/590/590681.png'
      };
      return images[item] || "https://via.placeholder.com/40";
    }








    function updateInventory(player) {
      const inv = document.getElementById(`inventory-${player}`);
      inv.innerHTML = '';
      inventories[player].forEach(item => {
        const li = document.createElement('li');
        li.innerHTML = `<img src="${getItemImage(item)}" class="item-image">${item}`;
        li.onclick = (event) => selectItem(player, item, getItemImage(item), event);
        inv.appendChild(li);
      });
    }








    function toggleInventory(player) {
      const inv = document.getElementById(`inventory-${player}`);
      inv.style.display = inv.style.display === 'block' ? 'none' : 'block';
    }








    function selectItem(player, item, image, event) {
      const items = document.getElementById(`inventory-${player}`).getElementsByTagName('li');
      for (let li of items) li.classList.remove('selected');
      selectedItems[player] = { name: item, image: image };
      event.currentTarget.classList.add('selected');
      document.getElementById('status').textContent = `${player === 'player1' ? 'Jogador 1' : 'Jogador 2'} escolheu ${item} para a troca.`;
    }








    function approveTrade(player) {
      if (!selectedItems[player].name) { alert(`Escolha um item primeiro, ${player}`); return; }
      approved[player] = true;
      document.getElementById('status').textContent = `${player} aprovou a troca.`;
      if (approved.player1 && approved.player2) {
        // Troca os itens
        const temp = selectedItems.player1;
        selectedItems.player1 = selectedItems.player2;
        selectedItems.player2 = temp;
        // Atualiza inventários
        inventories.player1 = inventories.player1.map(i => i === selectedItems.player2.name ? selectedItems.player1.name : i);
        inventories.player2 = inventories.player2.map(i => i === selectedItems.player1.name ? selectedItems.player2.name : i);
        updateInventory('player1'); updateInventory('player2');
        approved = { player1: false, player2: false };
        selectedItems = { player1: { name: null, image: null }, player2: { name: null, image: null } };
        document.getElementById('status').textContent = "✅ Troca concluída!";
      }
    }








    document.addEventListener("DOMContentLoaded", () => {
      atualizarTela();
      iniciarTimer();
      updateInventory('player1');
      updateInventory('player2');
    });
  </script>








</body>
</html>






