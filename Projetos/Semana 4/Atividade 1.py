<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bazar Arcano - Itens Mágicos e RPG</title>
    <style>
        /* Reset e Estilos Globais */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Times New Roman', Times, serif;
        }
       
        body {
            background: url('https://storage.googleapis.com/workspace-0f70711f-8b4e-4d94-86f1-2a93ccde5887/image/08151728-b87d-4968-aabb-816a89aa9326.png') repeat;
            color: #333;
            padding: 20px;
        }
       
        /* Header */
        header {
            text-align: center;
            margin-bottom: 30px;
            padding: 20px;
            background-color: rgba(139, 69, 19, 0.8);
            border: 3px double #8B4513;
            border-radius: 5px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
        }
       
        h1 {
            font-size: 2.5rem;
            color: #FFD700;
            text-shadow: 2px 2px 4px #000;
            letter-spacing: 2px;
        }
       
        .subtitle {
            font-style: italic;
            color: #FFF;
            margin-top: 10px;
        }
       
        /* Navegação */
        nav {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 10px;
            margin-bottom: 30px;
        }
       
        .category-btn {
            padding: 10px 20px;
            background-color: #5E3023;
            color: #FFD700;
            border: 1px solid #8B4513;
            border-radius: 20px;
            cursor: pointer;
            transition: all 0.3s;
            font-weight: bold;
        }
       
        .category-btn:hover {
            background-color: #8B4513;
            transform: translateY(-3px);
            box-shadow: 0 5px 10px rgba(0, 0, 0, 0.3);
        }
       
        /* Main Content */
        .container {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
            padding: 20px;
        }
       
        /* Cards de Itens */
        .item-card {
            background-color: rgba(255, 255, 255, 0.9);
            border: 2px solid #8B4513;
            border-radius: 10px;
            overflow: hidden;
            transition: transform 0.3s, box-shadow 0.3s;
            position: relative;
        }
       
        .item-card:hover {
            transform: scale(1.05);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3);
        }
       
        .item-image {
            width: 100%;
            height: 200px;
            object-fit: cover;
            border-bottom: 2px solid #8B4513;
        }
       
        .item-info {
            padding: 15px;
        }
       
        .item-name {
            font-size: 1.3rem;
            color: #5E3023;
            margin-bottom: 10px;
            font-weight: bold;
        }
       
        .item-desc {
            font-size: 0.9rem;
            margin-bottom: 15px;
            line-height: 1.4;
        }
       
        .item-price {
            font-size: 1.2rem;
            color: #5E3023;
            font-weight: bold;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
       
        .add-to-cart {
            padding: 8px 15px;
            background-color: #5E3023;
            color: #FFD700;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
       
        .add-to-cart:hover {
            background-color: #8B4513;
        }
       
        /* Carrinho */
        .cart-container {
            position: fixed;
            top: 20px;
            right: 20px;
            background-color: rgba(139, 69, 19, 0.9);
            border: 2px solid #FFD700;
            border-radius: 10px;
            padding: 15px;
            width: 300px;
            max-height: 80vh;
            overflow-y: auto;
            z-index: 100;
            color: #FFF;
            display: none;
        }
       
        .cart-header {
            display: flex;
            justify-content: space-between;
            margin-bottom: 15px;
            border-bottom: 1px solid #FFD700;
            padding-bottom: 10px;
        }
       
        .close-cart {
            background: none;
            border: none;
            color: #FFD700;
            cursor: pointer;
            font-size: 1.2rem;
        }
       
        .cart-items {
            margin-bottom: 15px;
        }
       
        .cart-item {
            display: flex;
            justify-content: space-between;
            margin-bottom: 10px;
            padding-bottom: 10px;
            border-bottom: 1px dashed #FFD700;
        }
       
        .cart-total {
            font-weight: bold;
            text-align: right;
            margin-top: 10px;
            font-size: 1.2rem;
        }
       
        .checkout-btn {
            width: 100%;
            padding: 10px;
            background-color: #FFD700;
            color: #5E3023;
            border: none;
            border-radius: 5px;
            font-weight: bold;
            cursor: pointer;
            transition: background-color 0.3s;
        }
       
        .checkout-btn:hover {
            background-color: #FFC000;
        }
       
        /* Botão do Carrinho */
        .cart-btn {
            position: fixed;
            bottom: 30px;
            right: 30px;
            background-color: #5E3023;
            color: #FFD700;
            border: 2px solid #FFD700;
            border-radius: 50%;
            width: 60px;
            height: 60px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            font-size: 1.5rem;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
            z-index: 99;
        }
       
        .cart-count {
            position: absolute;
            top: -10px;
            right: -10px;
            background-color: #FF0000;
            color: #FFF;
            border-radius: 50%;
            width: 25px;
            height: 25px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.8rem;
        }
       
        /* Responsividade */
        @media (max-width: 768px) {
            .container {
                grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            }
           
            .cart-container {
                width: 90%;
                left: 5%;
                right: 5%;
            }
        }
       
        /* Efeitos especiais */
        .rare {
            border: 2px solid #FFD700;
            box-shadow: 0 0 10px #FFD700;
            position: relative;
        }
       
        .rare::after {
            content: "RARO";
            position: absolute;
            top: 10px;
            right: 10px;
            background-color: #FFD700;
            color: #5E3023;
            padding: 3px 8px;
            border-radius: 5px;
            font-weight: bold;
            font-size: 0.8rem;
        }
       
        .legendary {
            border: 2px solid #9370DB;
            box-shadow: 0 0 15px #9370DB;
            position: relative;
        }
       
        .legendary::after {
            content: "LENDÁRIO";
            position: absolute;
            top: 10px;
            right: 10px;
            background-color: #9370DB;
            color: #FFF;
            padding: 3px 8px;
            border-radius: 5px;
            font-weight: bold;
            font-size: 0.8rem;
        }
    </style>
</head>
<body>
    <header>
        <h1>BAZAR ARCANO</h1>
        <p class="subtitle">Itens Mágicos e Equipamentos para Aventureiros</p>
    </header>
   
    <nav>
        <button class="category-btn" onclick="filterItems('all')">Todos</button>
        <button class="category-btn" onclick="filterItems('armas')">Armas</button>
        <button class="category-btn" onclick="filterItems('armaduras')">Armaduras</button>
        <button class="category-btn" onclick="filterItems('poções')">Poções</button>
        <button class="category-btn" onclick="filterItems('itens')">Itens Mágicos</button>
    </nav>
   
    <div class="container" id="items-container">
        <!-- Itens serão inseridos via JavaScript -->
    </div>
   
    <!-- Carrinho de Compras -->
    <div class="cart-container" id="cart">
        <div class="cart-header">
            <h2>Seu Carrinho</h2>
            <button class="close-cart" onclick="toggleCart()">&times;</button>
        </div>
        <div class="cart-items" id="cart-items">
            <!-- Itens do carrinho serão inseridos aqui -->
        </div>
        <div class="cart-total" id="cart-total">
            Total: 0 peças de ouro
        </div>
        <button class="checkout-btn" onclick="checkout()">Finalizar Compra</button>
    </div>
   
    <!-- Botão do Carrinho -->
    <div class="cart-btn" onclick="toggleCart()">
        🛒
        <div class="cart-count" id="cart-count">0</div>
    </div>
   
    <script>
        // Dados dos Itens
        const items = [
            {
                id: 1,
                name: "Espada Flamejante",
                category: "armas",
                price: 350,
                description: "Uma espada que emana chamas, causando dano adicional de fogo.",
                image: "https://storage.googleapis.com/workspace-0f70711f-8b4e-4d94-86f1-2a93ccde5887/image/29ca4156-6db7-41ee-9e2f-e9fa34d0f718.png",
                rarity: "rare"
            },
            {
                id: 2,
                name: "Cajado do Arcanista",
                category: "armas",
                price: 500,
                description: "Amplifica poderes mágicos, aumentando o dano de feitiços em 20%.",
                image: "https://storage.googleapis.com/workspace-0f70711f-8b4e-4d94-86f1-2a93ccde5887/image/6f5f2dec-410a-42ee-b58b-e05266240129.png",
                rarity: "legendary"
            },
            {
                id: 3,
                name: "Armadura de Placas Élfica",
                category: "armaduras",
                price: 800,
                description: "Leve como pena e forte como aço, proteção máxima com mínima restrição de movimento.",
                image: "https://storage.googleapis.com/workspace-0f70711f-8b4e-4d94-86f1-2a93ccde5887/image/10c98538-8ec7-48c0-bd2f-47f94ab7c4f1.png",
                rarity: "rare"
            },
            {
                id: 4,
                name: "Escudo do Dragão",
                category: "armaduras",
                price: 450,
                description: "Escudo resistente que concede 20% de resistência a dano elemental.",
                image: "https://storage.googleapis.com/workspace-0f70711f-8b4e-4d94-86f1-2a93ccde5887/image/61660f7e-0d58-4a5d-860e-42f5ec00177c.png",
                rarity: ""
            },
            {
                id: 5,
                name: "Poção de Cura Maior",
                category: "poções",
                price: 150,
                description: "Restaura 50 pontos de vida instantaneamente.",
                image: "https://storage.googleapis.com/workspace-0f70711f-8b4e-4d94-86f1-2a93ccde5887/image/f91f415b-27a4-4045-9551-765cb1d5b56a.png",
                rarity: ""
            },
            {
                id: 6,
                name: "Poção de Invisibilidade",
                category: "poções",
                price: 250,
                description: "Torna o consumidor invisível por 5 minutos ou até atacar.",
                image: "https://storage.googleapis.com/workspace-0f70711f-8b4e-4d94-86f1-2a93ccde5887/image/8a656ddc-77b6-4d58-b196-0aaf8c999e19.png",
                rarity: ""
            },
            {
                id: 7,
                name: "Anel da Ressurreição",
                category: "itens",
                price: 1500,
                description: "Revive o portador uma vez quando morre, com 50% da vida máxima.",
                image: "https://storage.googleapis.com/workspace-0f70711f-8b4e-4d94-86f1-2a93ccde5887/image/85b6fc12-fa2e-4057-a1b4-dd297f206280.png",
                rarity: "legendary"
            },
            {
                id: 8,
                name: "Cinto da Força do Gigante",
                category: "itens",
                price: 600,
                description: "Concede +4 de força enquanto equipado.",
                image: "https://storage.googleapis.com/workspace-0f70711f-8b4e-4d94-86f1-2a93ccde5887/image/0cf491ee-ca1f-41cf-b77f-b82484112aed.png",
                rarity: "rare"
            }
        ];
       
        // Carrinho de Compras
        let cart = [];
       
        // Função para exibir os itens
        function displayItems(itemsToShow = items) {
            const container = document.getElementById('items-container');
            container.innerHTML = '';
           
            itemsToShow.forEach(item => {
                const itemCard = document.createElement('div');
                itemCard.className = `item-card ${item.rarity}`;
                itemCard.innerHTML = `
                    <img src="${item.image}" alt="${item.name}" class="item-image" />
                    <div class="item-info">
                        <h3 class="item-name">${item.name}</h3>
                        <p class="item-desc">${item.description}</p>
                        <div class="item-price">
                            ${item.price} peças de ouro
                            <button class="add-to-cart" onclick="addToCart(${item.id})">Adicionar</button>
                        </div>
                    </div>
                `;
                container.appendChild(itemCard);
            });
        }
       
        // Função para filtrar itens por categoria
        function filterItems(category) {
            if (category === 'all') {
                displayItems();
                return;
            }
           
            const filteredItems = items.filter(item => item.category === category);
            displayItems(filteredItems);
        }
       
        // Funções do Carrinho
        function addToCart(itemId) {
            const item = items.find(i => i.id === itemId);
            const existingItem = cart.find(i => i.id === itemId);
           
            if (existingItem) {
                existingItem.quantity += 1;
            } else {
                cart.push({
                    ...item,
                    quantity: 1
                });
            }
           
            updateCart();
           
            // Efeito visual de confirmação
            const cartCount = document.getElementById('cart-count');
            cartCount.style.transform = 'scale(1.5)';
            setTimeout(() => {
                cartCount.style.transform = 'scale(1)';
            }, 300);
        }
       
        function updateCart() {
            const cartItemsContainer = document.getElementById('cart-items');
            const cartCount = document.getElementById('cart-count');
            const cartTotal = document.getElementById('cart-total');
           
            // Atualizar itens do carrinho
            cartItemsContainer.innerHTML = '';
            let total = 0;
           
            cart.forEach(item => {
                const cartItem = document.createElement('div');
                cartItem.className = 'cart-item';
                cartItem.innerHTML = `
                    <div>
                        <strong>${item.name}</strong><br>
                        ${item.price} peças x ${item.quantity}
                    </div>
                    <div>
                        <strong>${item.price * item.quantity} peças</strong>
                    </div>
                `;
                cartItemsContainer.appendChild(cartItem);
               
                total += item.price * item.quantity;
            });
           
            // Atualizar contador e total
            cartCount.textContent = cart.reduce((sum, item) => sum + item.quantity, 0);
            cartTotal.textContent = `Total: ${total} peças de ouro`;
        }
       
        function toggleCart() {
            const cart = document.getElementById('cart');
            cart.style.display = cart.style.display === 'block' ? 'none' : 'block';
        }
       
        function checkout() {
            if (cart.length === 0) {
                alert('Seu carrinho está vazio!');
                return;
            }
           
            const total = cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);
            alert(`Compra finalizada!\nTotal: ${total} peças de ouro\nObrigado por comprar no Bazar Arcano!`);
            cart = [];
            updateCart();
            toggleCart();
        }
       
        // Inicializar a página
        window.onload = function() {
            displayItems();
        };
    </script>
</body>
</html>
