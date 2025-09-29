<!DOCTYPE html><html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Placar Campeonato de Luta - 24 Lutadores</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #111;
      color: #eee;
      text-align: center;
    }
    .bracket {
      display: flex;
      justify-content: center;
      flex-wrap: wrap;
      gap: 20px;
    }
    .round {
      display: flex;
      flex-direction: column;
      gap: 15px;
    }
    .match {
      border: 1px solid #444;
      border-radius: 8px;
      padding: 8px;
      background: #222;
      min-width: 120px;
    }
    .title {
      font-weight: bold;
      margin-bottom: 5px;
      color: #ffcc00;
    }
  </style>
</head>
<body>
  <h1>🏆 Campeonato de Luta - 24 Lutadores</h1>
  <div class="bracket">
    <!-- Pré-Oitavas -->
    <div class="round">
      <div class="title">Pré-Oitavas</div>
      <div class="match">9 vs 24</div>
      <div class="match">10 vs 23</div>
      <div class="match">11 vs 22</div>
      <div class="match">12 vs 21</div>
      <div class="match">13 vs 20</div>
      <div class="match">14 vs 19</div>
      <div class="match">15 vs 18</div>
      <div class="match">16 vs 17</div>
    </div><!-- Oitavas -->
<div class="round">
  <div class="title">Oitavas</div>
  <div class="match">1 vs Venc.1</div>
  <div class="match">2 vs Venc.2</div>
  <div class="match">3 vs Venc.3</div>
  <div class="match">4 vs Venc.4</div>
  <div class="match">5 vs Venc.5</div>
  <div class="match">6 vs Venc.6</div>
  <div class="match">7 vs Venc.7</div>
  <div class="match">8 vs Venc.8</div>
</div>

<!-- Quartas -->
<div class="round">
  <div class="title">Quartas</div>
  <div class="match">Venc.9 vs Venc.10</div>
  <div class="match">Venc.11 vs Venc.12</div>
  <div class="match">Venc.13 vs Venc.14</div>
  <div class="match">Venc.15 vs Venc.16</div>
</div>

<!-- Semifinais -->
<div class="round">
  <div class="title">Semifinais</div>
  <div class="match">Venc.17 vs Venc.18</div>
  <div class="match">Venc.19 vs Venc.20</div>
</div>

<!-- Final -->
<div class="round">
  <div class="title">Final</div>
  <div class="match">Venc.21 vs Venc.22</div>
</div>

  </div>
</body>
</html>
